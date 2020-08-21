import copy
import os
import sys
import json
import six
from knack.cli import logger
from knack.invocation import CommandInvoker
from knack.events import (
    EVENT_INVOKER_PRE_CMD_TBL_CREATE, EVENT_INVOKER_POST_CMD_TBL_CREATE, EVENT_INVOKER_CMD_TBL_LOADED,
    EVENT_INVOKER_PRE_PARSE_ARGS, EVENT_INVOKER_POST_PARSE_ARGS, EVENT_INVOKER_FILTER_RESULT,
    EVENT_INVOKER_TRANSFORM_RESULT
)
from knack.util import CommandResultItem, todict, CLIError
from azure.core.exceptions import HttpResponseError, ClientAuthenticationError

from msgraph.cli.core.commands._util import read_file_content, _explode_list_args
from msgraph.cli.core.commands.events import EVENT_INVOKER_PRE_CMD_TBL_TRUNCATE, EVENT_INVOKER_PRE_LOAD_ARGUMENTS, \
    EVENT_INVOKER_POST_LOAD_ARGUMENTS


def _expand_file_prefixed_files(args):
    def _load_file(path):
        if path == '-':
            content = sys.stdin.read()
        else:
            content = read_file_content(
                os.path.expanduser(path), allow_binary=True)

        return content.rstrip(os.linesep)

    def _maybe_load_file(arg):
        ix = arg.find('@')
        if ix == -1:  # no @ found
            return arg

        poss_file = arg[ix + 1:]
        if not poss_file:  # if nothing after @ then it can't be a file
            return arg
        if ix == 0:
            try:
                return _load_file(poss_file)
            except IOError:
                logger.debug("Failed to load '%s', assume not a file", arg)
                return arg

        # if @ not at the start it can't be a file
        return arg

    def _expand_file_prefix(arg):
        arg_split = arg.split('=', 1)
        try:
            return '='.join([arg_split[0], _maybe_load_file(arg_split[1])])
        except IndexError:
            return _maybe_load_file(arg_split[0])

    return list([_expand_file_prefix(arg) for arg in args])


def _pre_command_table_create(cli_ctx, args):
    return _expand_file_prefixed_files(args)


def _is_paged(obj):
    # Since loading msrest is expensive, we avoid it until we have to
    import collections
    if isinstance(obj, collections.Iterable) \
            and not isinstance(obj, list) \
            and not isinstance(obj, dict):
        from msrest.paging import Paged
        from azure.core.paging import ItemPaged as AzureCorePaged
        return isinstance(obj, (AzureCorePaged, Paged))
    return False


class GraphCliCommandInvoker(CommandInvoker):
    def execute(self, args):
        self.cli_ctx.raise_event(EVENT_INVOKER_PRE_CMD_TBL_CREATE, args=args)
        self.commands_loader.load_command_table(args)
        self.cli_ctx.raise_event(EVENT_INVOKER_PRE_CMD_TBL_TRUNCATE,
                                 load_cmd_tbl_func=self.commands_loader.load_command_table, args=args)
        command = self._rudimentary_get_command(args)
        self.cli_ctx.invocation.data['command_string'] = command
        try:
            self.commands_loader.command_table = {
                command: self.commands_loader.command_table[command]}
        except KeyError:
            cmd_table = {}
            group_names = set()
            for cmd_name, cmd in self.commands_loader.command_table.items():
                if command and not cmd_name.startswith(command):
                    continue
                cmd_stub = cmd_name[len(command):].strip()
                group_name = cmd_stub.split(' ', 1)[0]
                if group_name:
                    cmd_table[cmd_name] = cmd
                    group_names.add(group_name)
                self.commands_loader.command_table = cmd_table

        # update with the truncated table
        self.commands_loader.command_table = self.commands_loader.command_table
        self.commands_loader.command_name = command
        self.cli_ctx.raise_event(
            EVENT_INVOKER_PRE_LOAD_ARGUMENTS, commands_loader=self.commands_loader)
        self.commands_loader.load_arguments(command)
        self.cli_ctx.raise_event(
            EVENT_INVOKER_POST_LOAD_ARGUMENTS, commands_loader=self.commands_loader)
        self.cli_ctx.raise_event(
            EVENT_INVOKER_POST_CMD_TBL_CREATE, commands_loader=self.commands_loader)
        self.parser.cli_ctx = self.cli_ctx
        self.parser.load_command_table(self.commands_loader)

        self.cli_ctx.raise_event(EVENT_INVOKER_CMD_TBL_LOADED, cmd_tbl=self.commands_loader.command_table,
                                 parser=self.parser)

        arg_check = [a for a in args if a not in ['--debug', '--verbose']]
        if not arg_check:
            # TODO: Enable autocomplete
            # self.parser.enable_autocomplete()
            subparser = self.parser.subparsers[tuple()]
            self.help.show_welcome(subparser)
            return CommandResultItem(None, exit_code=0)

        if args[0].lower() == 'help':
            args[0] = '--help'

        self.cli_ctx.raise_event(EVENT_INVOKER_PRE_PARSE_ARGS, args=args)
        parsed_args = self.parser.parse_args(args)
        self.cli_ctx.raise_event(
            EVENT_INVOKER_POST_PARSE_ARGS, command=parsed_args.command, args=parsed_args)

        cmd = parsed_args.func
        self.cli_ctx.data['command'] = parsed_args.command

        self.cli_ctx.data['safe_params'] = GraphCliCommandInvoker._extract_parameter_names(
            args)

        command_source = self.commands_loader.command_table[command].command_source

        jobs = []
        for expanded_arg in _explode_list_args(parsed_args):
            cmd_copy = copy.copy(cmd)
            cmd_copy.cli_ctx = copy.copy(cmd.cli_ctx)
            cmd_copy.cli_ctx.data = copy.deepcopy(cmd.cli_ctx.data)
            expanded_arg.cmd = expanded_arg._cmd = cmd_copy

            self._validation(expanded_arg)
            jobs.append((expanded_arg, cmd_copy))

        ids = getattr(parsed_args, '_ids', None) or [None] * len(jobs)

        results, exceptions = self._run_jobs_serially(jobs, ids)

        # handle exceptions
        if len(exceptions) == 1 and not results:
            ex, id_arg = exceptions[0]
            raise ex
        if exceptions:
            for exception, id_arg in exceptions:
                logger.warning('%s: "%s"', id_arg, str(exception))
            if not results:
                return CommandResultItem(None, exit_code=1, error=CLIError('Encountered more than one exception.'))
            logger.warning('Encountered more than one exception.')

        if results and len(results) == 1:
            results = results[0]

        event_data = {'result': results}
        self.cli_ctx.raise_event(
            EVENT_INVOKER_FILTER_RESULT, event_data=event_data)

        return CommandResultItem(
            event_data['result'],
            table_transformer=self.commands_loader.command_table[
                parsed_args.command].table_transformer,
            is_query_active=self.data['query_active'])

    def _run_jobs_serially(self, jobs, ids):
        results, exceptions = [], []
        for job, id_arg in zip(jobs, ids):
            expanded_arg, cmd_copy = job
            try:
                results.append(self._run_job(expanded_arg, cmd_copy))
            except(Exception, SystemExit) as ex:  # pylint: disable=broad-except
                exceptions.append((ex, id_arg))
        return results, exceptions

    def _run_jobs_concurrently(self, jobs, ids):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        tasks, results, exceptions = [], [], []
        with ThreadPoolExecutor(max_workers=10) as executor:
            for expanded_arg, cmd_copy in jobs:
                tasks.append(executor.submit(
                    self._run_job, expanded_arg, cmd_copy))
            for index, task in enumerate(as_completed(tasks)):
                try:
                    results.append(task.result())
                except (Exception, SystemExit) as ex:  # pylint: disable=broad-except
                    exceptions.append((ex, ids[index]))
        return results, exceptions

    def _run_job(self, expanded_arg, cmd_copy):
        params = self._filter_params(expanded_arg)
        try:
            result = cmd_copy(params)
            if cmd_copy.supports_no_wait and getattr(expanded_arg, 'no_wait', False):
                result = None
            elif cmd_copy.no_wait_param and getattr(expanded_arg, cmd_copy.no_wait_param, False):
                result = None

            transform_op = cmd_copy.command_kwargs.get('transform', None)
            if transform_op:
                result = transform_op(result)

            if _is_paged(result):
                result = list(result)

            result = todict(
                result, GraphCliCommandInvoker.remove_additional_prop_layer)

            # Formatting result so that non utf8 encoded characters are ignored.
            formatted_json = format_json({'result': result})
            result = json.loads(formatted_json)

            event_data = {'result': result}
            cmd_copy.cli_ctx.raise_event(
                EVENT_INVOKER_TRANSFORM_RESULT, event_data=event_data)
            return event_data['result']
        except Exception as ex:  # pylint: disable=broad-except
            if isinstance(ex, HttpResponseError):
                if ex.status_code == 403:  # pylint: disable=no-member
                    self.handle_403()
                    sys.exit(1)
            if isinstance(ex, ClientAuthenticationError):
                self.handle_auth_error(ex)
                sys.exit(1)
            if cmd_copy.exception_handler:
                cmd_copy.exception_handler(ex)
                return CommandResultItem(None, exit_code=1, error=ex)
            six.reraise(*sys.exc_info())

    @staticmethod
    def handle_403():
        raise CLIError(
            'You have insufficient privileges to complete the operation, login with required scopes')

    @staticmethod
    def handle_auth_error(ex):
        raise CLIError(ex.message)

    @staticmethod
    def _extract_parameter_names(args):
        # note: name start with more than 2 '-' will be treated as value e.g. certs in PEM format
        return [(p.split('=', 1)[0] if p.startswith('--') else p[:2]) for p in args if
                (p.startswith('-') and not p.startswith('---') and len(p) > 1)]

    @staticmethod
    def remove_additional_prop_layer(obj, converted_dic):
        from msrest.serialization import Model
        if isinstance(obj, Model):
            # let us make sure this is the additional properties auto-generated by SDK
            if ('additionalProperties' in converted_dic and isinstance(obj.additional_properties, dict)):
                converted_dic.update(converted_dic.pop('additionalProperties'))
        return converted_dic


class _ComplexEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=method-hidden
        if isinstance(o, bytes) and not isinstance(o, str):
            # Decode byte strings with utf-8, ignore if not possible.
            return o.decode('utf-8', 'ignore')
        return json.JSONEncoder.default(self, o)


def format_json(obj):
    result = obj['result']
    # OrderedDict.__dict__ is always '{}', to persist the data, convert to dict first.
    input_dict = dict(result) if hasattr(result, '__dict__') else result
    return json.dumps(input_dict, ensure_ascii=False, indent=2, sort_keys=True, cls=_ComplexEncoder,
                      separators=(',', ': ')) + '\n'
