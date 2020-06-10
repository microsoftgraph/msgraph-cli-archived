import inspect
from importlib import import_module

from knack.cli import logger


def _load_command_loader(loader, args, name, prefix):
    module = import_module(prefix + name)
    loader_cls = getattr(module, 'COMMAND_LOADER_CLS', None)
    command_table = {}

    if loader_cls:
        command_loader = loader_cls(cli_ctx=loader.cli_ctx)
        loader.loaders.append(command_loader)  # This will be used by interactive
        command_table = command_loader.load_command_table(args)
        if command_table:
            for cmd in list(command_table.keys()):
                # TODO: If desired to for extension to patch module, this can be uncommented
                # if loader.cmd_to_loader_map.get(cmd):
                #    loader.cmd_to_loader_map[cmd].append(command_loader)
                # else:
                loader.cmd_to_loader_map[cmd] = [command_loader]
    else:
        logger.debug("Module '%s' is missing `COMMAND_LOADER_CLS` entry.", name)
    return command_table, command_loader.command_group_table


def _load_module_command_loader(loader, args, mod):
    return _load_command_loader(loader, args, mod, 'command_modules.')


def get_command_type_kwarg(custom_command=False):
    return 'custom_command_type' if custom_command else 'command_type'


def get_arg_list(op):
    try:
        # only supported in python3 - falling back to argspec if not available
        sig = inspect.signature(op)
        return sig.parameters
    except AttributeError:
        sig = inspect.getargspec(op)  # pylint: disable=deprecated-method
        return sig.args

def augment_no_wait_handler_args(no_wait_enabled, handler, handler_args):
    """ Populates handler_args with the appropriate args for no wait """
    h_args = get_arg_list(handler)
    if 'no_wait' in h_args:
        handler_args['no_wait'] = no_wait_enabled
    if 'raw' in h_args and no_wait_enabled:
        # support autorest 2
        handler_args['raw'] = True
    if 'polling' in h_args and no_wait_enabled:
        # support autorest 3
        handler_args['polling'] = False