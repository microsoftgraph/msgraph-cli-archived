import types
from importlib import import_module

import six
from knack import CLICommandsLoader, CLICommand, ArgumentsContext
from knack.deprecation import Deprecated
from knack.introspection import extract_args_from_signature, extract_full_summary_from_signature
from knack.util import CLIError
from knack import CLI
from knack import CLICommandsLoader
from knack.cli import logger
from knack.arguments import ignore_type

from msgraph.cli.core.commands import GraphCommandGroup, GraphCliCommand
from msgraph.cli.core.commands._util import get_arg_list
from msgraph.cli.core.commands.client_factory import resolve_client_arg_name
from msgraph.cli.core.commands.parameters import GraphArgumentContext
from .commands.constants import EXCLUDED_PARAMS


import pkgutil
from importlib import import_module
import sys
from collections import OrderedDict


from msgraph.cli.core.commands._util import _load_module_command_loader
from msgraph.cli.core.invocation import GraphCliCommandInvoker


__version__ = '1.0.0'


class MainCommandsLoader(CLICommandsLoader):
    def __init__(self, cli_ctx=None):
        super(MainCommandsLoader, self).__init__(cli_ctx)
        self.cmd_to_loader_map = {}
        self.loaders = []
        self.command_table = dict()

    # pylint: disable=too-many-statements
    def load_command_table(self, args):
        """ Load commands into the command table

        :params args: List of the arguments from the commandline
        :type args: list
        :return: The ordered command table
        :rtype: collections.dict
        """
        self._update_command_table_from_modules(args)
        return OrderedDict(self.command_table)

    def load_arguments(self, command=None):
        """ Load arguments for the specified command

        :param command: The command to load arguments for
        :type command: str
        """
        if command is None:
            command_loaders = set()
            for loaders in self.cmd_to_loader_map.values():
                command_loaders = command_loaders.union(set(loaders))
            logger.info('Applying %s command loaders...', len(command_loaders))
        else:
            command_loaders = self.cmd_to_loader_map.get(command, None)

        if command_loaders:
            for loader in command_loaders:

                # register global args
                with loader.argument_context('') as c:
                    c.argument('cmd', ignore_type)

                if command is None:
                    # load all arguments via reflection
                    for cmd in loader.command_table.values():
                        cmd.load_arguments()  # this loads the arguments via reflection
                    loader.skip_applicability = True
                    # this adds entries to the argument registries
                    loader.load_arguments('')
                else:
                    loader.command_name = command
                    # this loads the arguments via reflection
                    self.command_table[command].load_arguments()
                    # this adds entries to the argument registries
                    loader.load_arguments(command)
                self.argument_registry.arguments.update(
                    loader.argument_registry.arguments)
                self.extra_argument_registry.update(
                    loader.extra_argument_registry)
                loader._update_command_definitions()  # pylint: disable=protected-access

    def _update_command_table_from_modules(self, args):
        installed_command_modules = []
        BLACKLISTED_MODS = ['context', 'shell', 'documentdb', 'component']

        try:
            modules = import_module('msgraph.cli.command_modules')
            installed_command_modules = [modname for _, modname, _ in
                                         pkgutil.iter_modules(modules.__path__)
                                         if modname not in BLACKLISTED_MODS]
            print(installed_command_modules)
            for module in installed_command_modules:
                command_table, group_table = _load_module_command_loader(
                    self, args, module)
                self.command_table.update(command_table)
                self.command_group_table.update(group_table)
        except ImportError as e:
            logger.warning(e)


def get_default_cli():

    return CLI(
        cli_name='mg',
        commands_loader_cls=MainCommandsLoader,
        invocation_cls=GraphCliCommandInvoker
    )


class GraphCommandsLoader(CLICommandsLoader):
    def __init__(self, cli_ctx=None, command_group_cls=None, argument_context_cls=None, **kwargs):
        super(GraphCommandsLoader, self).__init__(
            cli_ctx=cli_ctx, command_cls=GraphCliCommand, excluded_command_handler_args=EXCLUDED_PARAMS)
        self.module_kwargs = kwargs
        self._command_group_cls = command_group_cls or GraphCommandGroup
        self._argument_context_cls = ArgumentsContext

    def command_group(self, group_name, command_type=None, **kwargs):
        if command_type:
            kwargs['command_type'] = command_type
        return self._command_group_cls(self, group_name, **kwargs)

    def _cli_command(self, name, operation=None, handler=None, argument_loader=None, description_loader=None, **kwargs):
        kwargs['deprecate_info'] = Deprecated.ensure_new_style_deprecation(
            self.cli_ctx, kwargs, 'command')

        if operation and not isinstance(operation, six.string_types):
            raise TypeError(
                "Operation must be a string. Got '{}'".format(operation))
        if handler and not callable(handler):
            raise TypeError(
                "Handler must be a callable. Got '{}'".format(operation))
        if bool(operation) == bool(handler):
            raise TypeError(
                "Must specify exactly one of either 'operation' or 'handler'")

        name = ' '.join(name.split())

        client_factory = kwargs.get('client_factory', None)

        def default_command_handler(command_args):
            op = handler or self.get_op_handler(
                operation, operation_group=kwargs.get('operation_group'))
            op_args = get_arg_list(op)
            cmd = command_args.get(
                'cmd') if 'cmd' in op_args else command_args.pop('cmd')
            client = client_factory(
                cmd.cli_ctx, command_args) if client_factory else None

            if client:
                client_arg_name = resolve_client_arg_name(operation, kwargs)
                if client_arg_name in op_args:
                    command_args[client_arg_name] = client
            return op(**command_args)

        def default_arguments_loader():
            op = handler or self.get_op_handler(
                operation, operation_group=kwargs.get('operation_group'))
            cmd_args = list(extract_args_from_signature(
                op, excluded_params=self.excluded_command_handler_args))
            return cmd_args

        def default_description_loader():
            op = handler or self.get_op_handler(
                operation, operation_group=kwargs.get('operation_group'))
            return extract_full_summary_from_signature(op)

        kwargs['arguments_loader'] = argument_loader or default_arguments_loader
        kwargs['description_loader'] = description_loader or default_description_loader

        self.command_table[name] = self.command_cls(
            self, name, handler or default_command_handler, **kwargs)

    def argument_context(self, scope, **kwargs):
        return self._argument_context_cls(self, scope, **kwargs)

    def _update_command_definitions(self):
        master_arg_registry = self.cli_ctx.invocation.commands_loader.argument_registry
        master_extra_arg_registry = self.cli_ctx.invocation.commands_loader.extra_argument_registry

        for command_name, command in self.command_table.items():
            # Add any arguments explicitly registered for this command
            for argument_name, argument_definition in master_extra_arg_registry[command_name].items():
                command.arguments[argument_name] = argument_definition

            for argument_name in command.arguments:
                overrides = master_arg_registry.get_cli_argument(
                    command_name, argument_name)
                command.update_argument(argument_name, overrides)

    def get_op_handler(self, operation, operation_group=None):
        """Import and load the operation handler"""
        try:
            mod_to_import, attr_path = operation.split('#')
            op = import_module(mod_to_import)
            for part in attr_path.split('.'):
                op = getattr(op, part)
            if isinstance(op, types.FunctionType):
                return op
            return six.get_method_function(op)
        except (ValueError, AttributeError):
            raise ValueError("The operation '{}' is invalid".format(operation))
