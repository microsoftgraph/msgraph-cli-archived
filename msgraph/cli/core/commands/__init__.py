# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.cli import logger
from knack.commands import CommandGroup, CLICommand
from knack.util import CLIError

from msgraph.cli.core.commands._util import get_command_type_kwarg
from msgraph.cli.core.constants import CLI_COMMAND_KWARGS
from ._util import _merge_kwargs


class CliCommandType(object):
    def __init__(self, overrides=None, **kwargs):
        if isinstance(overrides, str):
            raise ValueError("Overrides has to be a {} (cannot be a string)".format(
                CliCommandType.__name__))
        self.settings = {}
        self.update(overrides, **kwargs)

    def __repr__(self):
        return str(vars(self))

    def update(self, other=None, **kwargs):
        if other:
            self.settings.update(**other.settings)
        self.settings.update(**kwargs)


class GraphCommandGroup(CommandGroup):
    def __init__(self, command_loader, group_name, **kwargs):
        merged_kwargs = self._merge_kwargs(kwargs, base_kwargs=command_loader.module_kwargs)
        operations_tmpl = merged_kwargs.pop('operations_tmpl', None)
        super(GraphCommandGroup, self).__init__(command_loader, group_name, operations_tmpl,
                                                **merged_kwargs)

        self.group_kwargs = merged_kwargs
        if operations_tmpl:
            self.group_kwargs['operations_tmpl'] = operations_tmpl
        self.is_stale = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_stale = True

    def _check_stale(self):
        if self.is_stale:
            message = "command authoring error: command group '{}' is stale! " \
                      "Check that the subsequent block for has a corresponding `as` statement.".format(
                          self.group_name)
            logger.error(message)
            raise CLIError(message)

    def _merge_kwargs(self, kwargs, base_kwargs=None):
        base = base_kwargs if base_kwargs is not None else getattr(self, 'group_kwargs')
        return _merge_kwargs(kwargs, base, CLI_COMMAND_KWARGS)

    def _flatten_kwargs(self, kwargs, default_source_name):
        merged_kwargs = self._merge_kwargs(kwargs)
        default_source = merged_kwargs.get(default_source_name, None)
        if default_source:
            arg_source_copy = default_source.settings.copy()
            arg_source_copy.update(merged_kwargs)
            return arg_source_copy
        return merged_kwargs

    def command(self, name, method_name=None, **kwargs):
        """
        Register a CLI command.
        :param name: Name of the command as it will be called on the command line
        :type name: str
        :param method_name: Name of the method the command maps to
        :type method_name: str
        :param kwargs: Keyword arguments. Supported keyword arguments include:
            - client_factory: Callable which returns a client needed to access the underlying command method. (function)
            - confirmation: Prompt prior to the action being executed. This is useful if the action
                            would cause a loss of data. (bool)
            - exception_handler: Exception handler for handling non-standard exceptions (function)
            - supports_no_wait: The command supports no wait. (bool)
            - no_wait_param: [deprecated] The name of a boolean parameter that will be exposed as `--no-wait`
              to skip long running operation polling. (string)
            - transform: Transform function for transforming the output of the command (function)
            - table_transformer: Transform function or JMESPath query to be applied to table output to create a
                                 better output format for tables. (function or string)
            - resource_type: The ResourceType enum value to use with min or max API. (ResourceType)
            - min_api: Minimum API version required for commands within the group (string)
            - max_api: Maximum API version required for commands within the group (string)
        :rtype: None
        """
        return self._command(name, method_name=method_name, **kwargs)

    def custom_command(self, name, method_name=None, **kwargs):
        """
        Register a CLI command.
        :param name: Name of the command as it will be called on the command line
        :type name: str
        :param method_name: Name of the method the command maps to
        :type method_name: str
        :param kwargs: Keyword arguments. Supported keyword arguments include:
            - client_factory: Callable which returns a client needed to access the underlying command method. (function)
            - confirmation: Prompt prior to the action being executed. This is useful if the action
                            would cause a loss of data. (bool)
            - exception_handler: Exception handler for handling non-standard exceptions (function)
            - supports_no_wait: The command supports no wait. (bool)
            - no_wait_param: [deprecated] The name of a boolean parameter that will be exposed as `--no-wait`
              to skip long running operation polling. (string)
            - transform: Transform function for transforming the output of the command (function)
            - table_transformer: Transform function or JMESPath query to be applied to table output to create a
                                 better output format for tables. (function or string)
            - resource_type: The ResourceType enum value to use with min or max API. (ResourceType)
            - min_api: Minimum API version required for commands within the group (string)
            - max_api: Maximum API version required for commands within the group (string)
        :rtype: None
        """
        return self._command(name, method_name=method_name, custom_command=True, **kwargs)

    def _command(self, name, method_name, custom_command=False, **kwargs):
        self._check_stale()
        merged_kwargs = self._flatten_kwargs(kwargs, get_command_type_kwarg(custom_command))

        operations_tmpl = merged_kwargs['operations_tmpl']
        command_name = '{} {}'.format(self.group_name, name) if self.group_name else name
        self.command_loader._cli_command(
            command_name,  # pylint: disable=protected-access
            operation=operations_tmpl.format(method_name),
            **merged_kwargs)
        return command_name

    # pylint: disable=no-self-use
    def _resolve_operation(self, kwargs, name, command_type=None, custom_command=False):
        source_kwarg = get_command_type_kwarg(custom_command)

        operations_tmpl = None
        if command_type:
            # Top priority: specified command_type for the parameter
            operations_tmpl = command_type.settings.get('operations_tmpl', None)

        if not operations_tmpl:
            # Second source: general operations_tmpl set for the command kwargs
            operations_tmpl = kwargs.get('operations_tmpl', None)

        if not operations_tmpl:
            # Final source: retrieve the operations_tmpl from the relevant 'command_type' or 'custom_command_type'
            command_type = kwargs.get(source_kwarg, None)
            operations_tmpl = command_type.settings.get('operations_tmpl', None)

        if not operations_tmpl:
            raise ValueError("command authoring error: unable to resolve 'operations_tmpl'")

        return operations_tmpl.format(name)

    def generic_update_command(self,
                               name,
                               getter_name='get',
                               getter_type=None,
                               setter_name='create_or_update',
                               setter_type=None,
                               setter_arg_name='parameters',
                               child_collection_prop_name=None,
                               child_collection_key='name',
                               child_arg_name='item_name',
                               custom_func_name=None,
                               custom_func_type=None,
                               **kwargs):
        from msgraph.cli.core.commands.arm import _cli_generic_update_command
        self._check_stale()
        merged_kwargs = self._flatten_kwargs(kwargs, get_command_type_kwarg())
        merged_kwargs_custom = self._flatten_kwargs(kwargs,
                                                    get_command_type_kwarg(custom_command=True))
        self._apply_tags(merged_kwargs, kwargs, name)

        getter_op = self._resolve_operation(merged_kwargs, getter_name, getter_type)
        setter_op = self._resolve_operation(merged_kwargs, setter_name, setter_type)
        custom_func_op = self._resolve_operation(
            merged_kwargs_custom, custom_func_name, custom_func_type,
            custom_command=True) if custom_func_name else None
        _cli_generic_update_command(self.command_loader,
                                    '{} {}'.format(self.group_name, name),
                                    getter_op=getter_op,
                                    setter_op=setter_op,
                                    setter_arg_name=setter_arg_name,
                                    custom_function_op=custom_func_op,
                                    child_collection_prop_name=child_collection_prop_name,
                                    child_collection_key=child_collection_key,
                                    child_arg_name=child_arg_name,
                                    **merged_kwargs)

    def wait_command(self, name, getter_name='get', **kwargs):
        self._wait_command(name, getter_name=getter_name, custom_command=False, **kwargs)

    def custom_wait_command(self, name, getter_name='get', **kwargs):
        self._wait_command(name, getter_name=getter_name, custom_command=True, **kwargs)

    def generic_wait_command(self, name, getter_name='get', getter_type=None, **kwargs):
        self._wait_command(name, getter_name=getter_name, getter_type=getter_type, **kwargs)

    def _wait_command(self,
                      name,
                      getter_name='get',
                      getter_type=None,
                      custom_command=False,
                      **kwargs):
        from azure.cli.core.commands.arm import _cli_wait_command
        self._check_stale()
        merged_kwargs = self._flatten_kwargs(kwargs, get_command_type_kwarg(custom_command))
        self._apply_tags(merged_kwargs, kwargs, name)

        if getter_type:
            merged_kwargs = _merge_kwargs(getter_type.settings, merged_kwargs, CLI_COMMAND_KWARGS)
        getter_op = self._resolve_operation(merged_kwargs,
                                            getter_name,
                                            getter_type,
                                            custom_command=custom_command)
        _cli_wait_command(self.command_loader,
                          '{} {}'.format(self.group_name, name),
                          getter_op=getter_op,
                          custom_command=custom_command,
                          **merged_kwargs)

    def show_command(self, name, getter_name='get', **kwargs):
        self._show_command(name, getter_name=getter_name, custom_command=False, **kwargs)

    def custom_show_command(self, name, getter_name='get', **kwargs):
        self._show_command(name, getter_name=getter_name, custom_command=True, **kwargs)

    def _show_command(self,
                      name,
                      getter_name='get',
                      getter_type=None,
                      custom_command=False,
                      **kwargs):
        from azure.cli.core.commands.arm import _cli_show_command
        self._check_stale()
        merged_kwargs = self._flatten_kwargs(kwargs, get_command_type_kwarg(custom_command))
        self._apply_tags(merged_kwargs, kwargs, name)

        if getter_type:
            merged_kwargs = _merge_kwargs(getter_type.settings, merged_kwargs, CLI_COMMAND_KWARGS)
        getter_op = self._resolve_operation(merged_kwargs,
                                            getter_name,
                                            getter_type,
                                            custom_command=custom_command)
        _cli_show_command(self.command_loader,
                          '{} {}'.format(self.group_name, name),
                          getter_op=getter_op,
                          custom_command=custom_command,
                          **merged_kwargs)

    def _apply_tags(self, merged_kwargs, kwargs, command_name):
        # don't inherit deprecation or preview info from command group
        merged_kwargs['deprecate_info'] = kwargs.get('deprecate_info', None)

        # transform is_preview and is_experimental to StatusTags
        merged_kwargs['preview_info'] = None
        merged_kwargs['experimental_info'] = None
        is_preview = kwargs.get('is_preview', False)
        is_experimental = kwargs.get('is_experimental', False)
        if is_preview and is_experimental:
            raise CLIError(
                PREVIEW_EXPERIMENTAL_CONFLICT_ERROR.format("command",
                                                           self.group_name + " " + command_name))
        if is_preview:
            merged_kwargs['preview_info'] = PreviewItem(self.command_loader.cli_ctx,
                                                        object_type='command')
        if is_experimental:
            merged_kwargs['experimental_info'] = ExperimentalItem(self.command_loader.cli_ctx,
                                                                  object_type='command')


class GraphCliCommand(CLICommand):
    def __init__(self,
                 loader,
                 name,
                 handler,
                 description=None,
                 table_transformer=None,
                 arguments_loader=None,
                 description_loader=None,
                 formatter_class=None,
                 deprecate_info=None,
                 validator=None,
                 **kwargs):
        super(GraphCliCommand, self).__init__(loader.cli_ctx,
                                              name,
                                              handler,
                                              description=description,
                                              table_transformer=table_transformer,
                                              arguments_loader=arguments_loader,
                                              description_loader=description_loader,
                                              formatter_class=formatter_class,
                                              deprecate_info=deprecate_info,
                                              validator=validator,
                                              **kwargs)
        self.loader = loader
        self.command_source = None
        self.no_wait_param = kwargs.get('no_wait_param', None)
        self.supports_no_wait = kwargs.get('supports_no_wait', False)
        self.exception_handler = kwargs.get('exception_handler', None)
        self.confirmation = kwargs.get('confirmation', False)
        self.command_kwargs = kwargs

    def __call__(self, *args, **kwargs):
        return self.handler(*args, **kwargs)


class ExtensionCommandSource:
    '''Class for commands contributed by an extension'''
    def __init__(self,
                 overrides_command=False,
                 extension_name=None,
                 preview=False,
                 experimental=False):
        super(ExtensionCommandSource, self).__init__()
        # True if the command overrides a CLI command
        self.overrides_command = overrides_command
        self.extension_name = extension_name
        self.preview = preview
        self.experimental = experimental

    def get_command_warn_msg(self):
        if self.overrides_command:
            if self.extension_name:
                return 'The behavior of this command has been altered by the following extension: '\
                    '{}'.format(self.extension_name)
            return 'The behavior of this command has been altered by an extension'
        if self.extension_name:
            return 'This command is from the following extension: {}'.format(self.extension_name)
        return 'This command is from an extension.'

    def get_preview_warn_msg(self):
        if self.preview:
            return 'The extension is in preview'
        return None

    def get_experimental_warn_msg(self):
        if self.experimental:
            return 'The extension is experimental and not covered by customer support. '\
                'Please use with discretion'
