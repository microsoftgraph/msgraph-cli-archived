# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import six
import types
from importlib import import_module
from knack.deprecation import Deprecated
from knack import CLICommandsLoader, ArgumentsContext
from knack.introspection import extract_args_from_signature, extract_full_summary_from_signature

from msgraph.cli.core.commands import GraphCommandGroup, GraphCliCommand
from msgraph.cli.core.commands._util import get_arg_list
from msgraph.cli.core.commands.client_factory import resolve_client_arg_name
from msgraph.cli.core.constants import EXCLUDED_PARAMS


class ExtensionCommandsLoader(CLICommandsLoader):
    '''Load extensions command table
    '''
    def __init__(self, cli_ctx=None, command_group_cls=None, argument_context_cls=None, **kwargs):
        super().__init__(cli_ctx=cli_ctx,
                         command_cls=GraphCliCommand,
                         excluded_command_handler_args=EXCLUDED_PARAMS)
        self.module_kwargs = kwargs
        self._command_group_cls = command_group_cls or GraphCommandGroup
        self._argument_context_cls = ArgumentsContext

    def command_group(self, group_name, command_type=None, **kwargs):
        '''Used by extensions to add commands into the command_table

        :param group_name:   group_name of the set of commands. ie users
        :param command_type: Cli command_type
        '''
        if command_type:
            kwargs['command_type'] = command_type
        return self._command_group_cls(self, group_name, **kwargs)

    def _cli_command(self,
                     name,
                     operation=None,
                     handler=None,
                     argument_loader=None,
                     description_loader=None,
                     **kwargs):
        '''Adds a command to the command table
        :param name: command name
        '''
        kwargs['deprecate_info'] = Deprecated.ensure_new_style_deprecation(
            self.cli_ctx, kwargs, 'command')

        if operation and not isinstance(operation, six.string_types):
            raise TypeError("Operation must be a string. Got '{}'".format(operation))
        if handler and not callable(handler):
            raise TypeError("Handler must be a callable. Got '{}'".format(operation))
        if bool(operation) == bool(handler):
            raise TypeError("Must specify exactly one of either 'operation' or 'handler'")

        name = ' '.join(name.split())

        client_factory = kwargs.get('client_factory', None)

        def default_command_handler(command_args):
            ''' Handler function for user commands.

            :param command_args: list of commandline arguments
            '''

            # Gets the handler function from  the specified operation template
            op = handler or self.get_op_handler(operation,
                                                operation_group=kwargs.get('operation_group'))
            op_args = get_arg_list(op)

            # Removes cmd from list of command_args. This is because the handler function
            # doesn't expect cmd as an argument.
            cmd = command_args.get('cmd') if 'cmd' in op_args else command_args.pop('cmd')

            # Gets the http client. In our case, the client is a GraphSession object.
            client = client_factory(cmd.cli_ctx, command_args) if client_factory else None

            # If a client exists, add it to the list of arguments passed to a handler function.
            if client:
                client_arg_name = resolve_client_arg_name(operation, kwargs)
                if client_arg_name in op_args:
                    command_args[client_arg_name] = client
            return op(**command_args)

        def default_arguments_loader():
            '''Loads handler function's arguments from operation_template
            '''
            # Get the handler function for the specified operation template
            op = handler or self.get_op_handler(operation,
                                                operation_group=kwargs.get('operation_group'))

            # Extract command args from the handler function signature
            cmd_args = list(
                extract_args_from_signature(op, excluded_params=self.excluded_command_handler_args))
            return cmd_args

        def default_description_loader():
            '''Loads handler function's description.
            '''
            op = handler or self.get_op_handler(operation,
                                                operation_group=kwargs.get('operation_group'))
            return extract_full_summary_from_signature(op)

        kwargs['arguments_loader'] = argument_loader or default_arguments_loader
        kwargs['description_loader'] = description_loader or default_description_loader

        # Adds command to command_table with it's associated command handler and loaders.
        self.command_table[name] = self.command_cls(self, name, handler or default_command_handler,
                                                    **kwargs)

    def argument_context(self, scope, **kwargs):
        '''Gets an instance of the ArgumentContext class.
        '''
        return self._argument_context_cls(self, scope, **kwargs)

    def _update_command_definitions(self):
        '''Updates command definition with arguments.
        '''
        master_arg_registry = self.cli_ctx.invocation.commands_loader.argument_registry
        master_extra_arg_registry = self.cli_ctx.invocation.commands_loader.extra_argument_registry

        for command_name, command in self.command_table.items():
            # Add any arguments explicitly registered for this command
            for argument_name, argument_definition in master_extra_arg_registry[command_name].items(
            ):
                command.arguments[argument_name] = argument_definition

            for argument_name in command.arguments:
                overrides = master_arg_registry.get_cli_argument(command_name, argument_name)
                command.update_argument(argument_name, overrides)

    def get_op_handler(self, operation, operation_group=None):
        '''Import and load the operation handler
         An operation handle is the function called when a user runs a command.

        :param operation: operation template
        '''
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
