import argparse
from collections import OrderedDict
import copy
import json
import re
from six import string_types

from msgraph.cli.core import EXCLUDED_PARAMS
from msgraph.cli.core.command_loaders import ExtensionCommandsLoader as AzCommandsLoader

from knack.introspection import extract_args_from_signature, extract_full_summary_from_signature


# pylint: disable=too-many-statements
def _cli_generic_update_command(context,
                                name,
                                getter_op,
                                setter_op,
                                setter_arg_name='parameters',
                                child_collection_prop_name=None,
                                child_collection_key='name',
                                child_arg_name='item_name',
                                custom_function_op=None,
                                **kwargs):
    if not isinstance(context, AzCommandsLoader):
        raise TypeError("'context' expected type '{}'. Got: '{}'".format(
            AzCommandsLoader.__name__, type(context)))
    if not isinstance(getter_op, string_types):
        raise TypeError("Getter operation must be a string. Got '{}'".format(getter_op))
    if not isinstance(setter_op, string_types):
        raise TypeError("Setter operation must be a string. Got '{}'".format(setter_op))
    if custom_function_op and not isinstance(custom_function_op, string_types):
        raise TypeError(
            "Custom function operation must be a string. Got '{}'".format(custom_function_op))

    def set_arguments_loader():
        return dict(
            extract_args_from_signature(context.get_op_handler(
                setter_op, operation_group=kwargs.get('operation_group')),
                                        excluded_params=EXCLUDED_PARAMS))

    def function_arguments_loader():
        if not custom_function_op:
            return {}

        custom_op = context.get_op_handler(custom_function_op)
        context._apply_doc_string(custom_op, kwargs)  # pylint: disable=protected-access
        return dict(extract_args_from_signature(custom_op, excluded_params=EXCLUDED_PARAMS))

    def generic_update_arguments_loader():
        arguments = get_arguments_loader(context,
                                         getter_op,
                                         operation_group=kwargs.get('operation_group'))
        arguments.update(set_arguments_loader())
        arguments.update(function_arguments_loader())
        arguments.pop('instance', None)  # inherited from custom_function(instance, ...)
        arguments.pop('parent', None)
        arguments.pop('expand', None)  # possibly inherited from the getter
        arguments.pop(setter_arg_name, None)

        # Add the generic update parameters
        class OrderedArgsAction(argparse.Action):  # pylint:disable=too-few-public-methods
            def __call__(self, parser, namespace, values, option_string=None):
                if not getattr(namespace, 'ordered_arguments', None):
                    setattr(namespace, 'ordered_arguments', [])
                namespace.ordered_arguments.append((option_string, values))

        group_name = 'Generic Update'
        arguments['properties_to_set'] = CLICommandArgument(
            'properties_to_set',
            options_list=['--set'],
            nargs='+',
            action=OrderedArgsAction,
            default=[],
            help='Update an object by specifying a property path and value to set.  Example: {}'.
            format(set_usage),
            metavar='KEY=VALUE',
            arg_group=group_name)
        arguments['properties_to_add'] = CLICommandArgument(
            'properties_to_add',
            options_list=['--add'],
            nargs='+',
            action=OrderedArgsAction,
            default=[],
            help='Add an object to a list of objects by specifying a path and '
            'key value pairs.  Example: {}'.format(add_usage),
            metavar='LIST KEY=VALUE',
            arg_group=group_name)
        arguments['properties_to_remove'] = CLICommandArgument(
            'properties_to_remove',
            options_list=['--remove'],
            nargs='+',
            action=OrderedArgsAction,
            default=[],
            help='Remove a property or an element from a list.  Example: {}'.format(remove_usage),
            metavar='LIST INDEX',
            arg_group=group_name)
        arguments['force_string'] = CLICommandArgument(
            'force_string',
            action='store_true',
            arg_group=group_name,
            help=
            "When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON."
        )
        return [(k, v) for k, v in arguments.items()]

    def _extract_handler_and_args(args, commmand_kwargs, op, context):
        from azure.cli.core.commands.client_factory import resolve_client_arg_name
        factory = _get_client_factory(name, **commmand_kwargs)
        client = None
        if factory:
            try:
                client = factory(context.cli_ctx)
            except TypeError:
                client = factory(context.cli_ctx, args)

        client_arg_name = resolve_client_arg_name(op, kwargs)
        op_handler = context.get_op_handler(op, operation_group=kwargs.get('operation_group'))
        raw_args = dict(
            extract_args_from_signature(op_handler, excluded_params=EXCLUDED_NON_CLIENT_PARAMS))
        op_args = {key: val for key, val in args.items() if key in raw_args}
        if client_arg_name in raw_args:
            op_args[client_arg_name] = client
        return op_handler, op_args

    def handler(args):  # pylint: disable=too-many-branches,too-many-statements
        cmd = args.get('cmd')
        context_copy = copy.copy(context)
        context_copy.cli_ctx = cmd.cli_ctx
        force_string = args.get('force_string', False)
        ordered_arguments = args.pop('ordered_arguments', [])
        dest_names = child_arg_name.split('.')
        child_names = [args.get(key, None) for key in dest_names]
        for item in ['properties_to_add', 'properties_to_set', 'properties_to_remove']:
            if args[item]:
                raise CLIError("Unexpected '{}' was not empty.".format(item))
            del args[item]

        getter, getterargs = _extract_handler_and_args(args, cmd.command_kwargs, getter_op,
                                                       context_copy)

        if child_collection_prop_name:
            parent = cached_get(cmd, getter, **getterargs)
            instance = find_child_item(parent,
                                       *child_names,
                                       path=child_collection_prop_name,
                                       key_path=child_collection_key)
        else:
            parent = None
            instance = cached_get(cmd, getter, **getterargs)

        # pass instance to the custom_function, if provided
        if custom_function_op:
            custom_function, custom_func_args = _extract_handler_and_args(
                args, cmd.command_kwargs, custom_function_op, context_copy)
            if child_collection_prop_name:
                parent = custom_function(instance=instance, parent=parent, **custom_func_args)
            else:
                instance = custom_function(instance=instance, **custom_func_args)

        # apply generic updates after custom updates
        setter, setterargs = _extract_handler_and_args(args, cmd.command_kwargs, setter_op,
                                                       context_copy)

        for arg in ordered_arguments:
            arg_type, arg_values = arg
            if arg_type == '--set':
                try:
                    for expression in arg_values:
                        set_properties(instance, expression, force_string)
                except ValueError:
                    raise CLIError('invalid syntax: {}'.format(set_usage))
            elif arg_type == '--add':
                try:
                    add_properties(instance, arg_values, force_string)
                except ValueError:
                    raise CLIError('invalid syntax: {}'.format(add_usage))
            elif arg_type == '--remove':
                try:
                    remove_properties(instance, arg_values)
                except ValueError:
                    raise CLIError('invalid syntax: {}'.format(remove_usage))

        # Done... update the instance!
        setterargs[setter_arg_name] = parent if child_collection_prop_name else instance

        # Handle no-wait
        supports_no_wait = cmd.command_kwargs.get('supports_no_wait', None)
        if supports_no_wait:
            no_wait_enabled = args.get('no_wait', False)
            augment_no_wait_handler_args(no_wait_enabled, setter, setterargs)
        else:
            no_wait_param = cmd.command_kwargs.get('no_wait_param', None)
            if no_wait_param:
                setterargs[no_wait_param] = args[no_wait_param]

        if setter_arg_name == 'parameters':
            result = cached_put(cmd, setter, **setterargs)
        else:
            result = cached_put(cmd,
                                setter,
                                setterargs[setter_arg_name],
                                setter_arg_name=setter_arg_name,
                                **setterargs)

        if supports_no_wait and no_wait_enabled:
            return None

        no_wait_param = cmd.command_kwargs.get('no_wait_param', None)
        if no_wait_param and setterargs.get(no_wait_param, None):
            return None

        if _is_poller(result):
            result = result.result()

        if child_collection_prop_name:
            result = find_child_item(result,
                                     *child_names,
                                     path=child_collection_prop_name,
                                     key_path=child_collection_key)
        return result

    context._cli_command(name,
                         handler=handler,
                         argument_loader=generic_update_arguments_loader,
                         **kwargs)  # pylint: disable=protected-access


def _cli_show_command(context, name, getter_op, custom_command=False, **kwargs):

    if not isinstance(getter_op, string_types):
        raise ValueError("Getter operation must be a string. Got '{}'".format(type(getter_op)))

    factory = _get_client_factory(name, custom_command=custom_command, **kwargs)

    def generic_show_arguments_loader():
        cmd_args = get_arguments_loader(context,
                                        getter_op,
                                        operation_group=kwargs.get('operation_group'))
        return [(k, v) for k, v in cmd_args.items()]

    def description_loader():
        return extract_full_summary_from_signature(
            context.get_op_handler(getter_op, operation_group=kwargs.get('operation_group')))

    def handler(args):
        from azure.cli.core.commands.client_factory import resolve_client_arg_name
        context_copy = copy.copy(context)
        getter_args = dict(
            extract_args_from_signature(context_copy.get_op_handler(
                getter_op, operation_group=kwargs.get('operation_group')),
                                        excluded_params=EXCLUDED_NON_CLIENT_PARAMS))
        cmd = args.get('cmd') if 'cmd' in getter_args else args.pop('cmd')
        context_copy.cli_ctx = cmd.cli_ctx
        operations_tmpl = _get_operations_tmpl(cmd, custom_command=custom_command)
        client_arg_name = resolve_client_arg_name(operations_tmpl, kwargs)
        try:
            client = factory(context_copy.cli_ctx) if factory else None
        except TypeError:
            client = factory(context_copy.cli_ctx, args) if factory else None

        if client and (client_arg_name in getter_args):
            args[client_arg_name] = client

        getter = context_copy.get_op_handler(getter_op,
                                             operation_group=kwargs.get('operation_group'))
        try:
            return getter(**args)
        except Exception as ex:  # pylint: disable=broad-except
            show_exception_handler(ex)

    context._cli_command(
        name,
        handler=handler,
        argument_loader=generic_show_arguments_loader,  # pylint: disable=protected-access
        description_loader=description_loader,
        **kwargs)
