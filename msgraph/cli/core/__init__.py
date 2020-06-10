import types
from importlib import import_module

import six
from knack import CLICommandsLoader, CLICommand
from knack.deprecation import Deprecated
from knack.introspection import extract_args_from_signature, extract_full_summary_from_signature
from knack.util import CLIError

from msgraph.cli.core.commands import GraphCommandGroup, GraphCliCommand
from msgraph.cli.core.commands._util import get_arg_list
from msgraph.cli.core.commands.client_factory import resolve_client_arg_name


class GraphCommandsLoader(CLICommandsLoader):
    def __init__(self, cli_ctx=None, **kwargs):
        super(GraphCommandsLoader, self).__init__(cli_ctx=cli_ctx, command_cls=GraphCliCommand)
        self.module_kwargs = kwargs
        self._command_group_cls = GraphCommandGroup

    def command_group(self, group_name, command_type=None, **kwargs):
        if command_type:
            kwargs['command_type'] = command_type
        return self._command_group_cls(self, group_name, **kwargs)

    def _cli_command(self, name, operation=None, handler=None, argument_loader=None, description_loader=None, **kwargs):
        kwargs['deprecate_info'] = Deprecated.ensure_new_style_deprecation(self.cli_ctx, kwargs, 'command')

        if operation and not isinstance(operation, six.string_types):
            raise TypeError("Operation must be a string. Got '{}'".format(operation))
        if handler and not callable(handler):
            raise TypeError("Handler must be callable. Got '{}'".format(operation))
        if bool(operation) == bool(handler):
            raise TypeError("Must specify exactly on of either 'operation' or 'handler'")

        name = ' '.join(name.split())
        client_factory = kwargs.get('client_factory', None)

        def default_command_handler(command_args):
            op = handler or self.get_op_handler(operation, operation_group=kwargs.get('operation_group'))
            op_args = get_arg_list(op)
            cmd = command_args.get('cmd') if 'cmd' in op_args else command_args.pop('cmd')

            client = client_factory(cmd.cli_ctx, command_args) if client_factory else None

            if client:
                client_arg_name = resolve_client_arg_name(operation, kwargs)
                if client_arg_name in op_args:
                    command_args[client_arg_name] = client
            return op(**command_args)

        def default_arguments_loader():
            op = handler or self.get_op_handler(operation, operation_group=kwargs.get('operation_group'))
            self._apply_doc_string(op, kwargs)
            cmd_args = list(extract_args_from_signature(op, excluded_params=self.excluded_command_handler_args))
            return cmd_args

        def default_description_loader():
            op = handler or self.get_op_handler(operation, operation_group=kwargs.get('operation_group'))
            self._apply_doc_string(op, kwargs)
            return extract_full_summary_from_signature(op)

        kwargs['arguments_loader'] = argument_loader or default_arguments_loader
        kwargs['description_loader'] = description_loader or default_description_loader

        self.command_table[name] = self.command_cls(self, name, handler or default_command_handler, **kwargs)

    def get_op_handler(self, operation, operation_group=None):
        try:
            mod_to_import, attr_path = operation.split('#')
            op = import_module(mod_to_import)
            for part in attr_path.split('.'):
                op = getattr(op, part)
            if isinstance(op, types.Function):
                return op
            return six.get_method_function(op)
        except (ValueError, AttributeError):
            raise ValueError("The operation '{}' is invalid".format(operation))

    def _apply_doc_string(self, dest, command_kwargs):
        doc_string_source = command_kwargs.get('doc_string_source', None)
        if not doc_string_source:
            return
        if not isinstance(doc_string_source, str):
            raise CLIError("command authoring error: applying doc_string_source '{}' directly will cause slowdown. "
                           'Import by string name instead.'.format(doc_string_source.__name__))
