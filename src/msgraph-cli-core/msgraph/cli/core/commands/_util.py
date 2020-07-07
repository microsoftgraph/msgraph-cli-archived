import argparse
import base64
import inspect
from importlib import import_module
from knack.cli import logger
from knack.util import CLIError
from msgraph.cli.core.commands.validators import IterateValue
from msgraph.cli.core.commands.constants import CLI_COMMON_KWARGS


def _load_command_loader(loader, args, name=None, prefix=None, extension=None):
    module = None
    loader_cls = None

    if (extension):
        module = import_module(extension)
        loader_cls = getattr(module, 'COMMAND_LOADER_CLS', None)
    if (name is not None):
        module = import_module(prefix+name)
        loader_cls = getattr(module, 'COMMAND_LOADER_CLS', None)

    command_table = {}

    if loader_cls:
        command_loader = loader_cls(cli_ctx=loader.cli_ctx)
        # This will be used by interactive
        loader.loaders.append(command_loader)
        command_table = command_loader.load_command_table(args)
        if command_table:
            for cmd in list(command_table.keys()):
                # TODO: If desired to for extension to patch module, this can be uncommented
                # if loader.cmd_to_loader_map.get(cmd):
                #    loader.cmd_to_loader_map[cmd].append(command_loader)
                # else:
                loader.cmd_to_loader_map[cmd] = [command_loader]
    else:
        logger.debug(
            "Module '%s' is missing `COMMAND_LOADER_CLS` entry.", name)
    return command_table, command_loader.command_group_table


def _load_module_command_loader(loader, args, mod):
    return _load_command_loader(loader, args, name=mod, prefix='msgraph.cli.command_modules.')


def _load_extension_command_loader(loader, args, extension):
    return _load_command_loader(loader, args, extension=extension)


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


def read_file_content(file_path, allow_binary=False):
    from codecs import open as codecs_open
    # Note, always put 'utf-8-sig' first, so that BOM in WinOS won't cause trouble.
    for encoding in ['utf-8-sig', 'utf-8', 'utf-16', 'utf-16le', 'utf-16be']:
        try:
            with codecs_open(file_path, encoding=encoding) as f:
                logger.debug("attempting to read file %s as %s",
                             file_path, encoding)
                return f.read()
        except (UnicodeError, UnicodeDecodeError):
            pass

    if allow_binary:
        try:
            with open(file_path, 'rb') as input_file:
                logger.debug("attempting to read file %s as binary", file_path)
                return base64.b64encode(input_file.read()).decode("utf-8")
        except Exception:  # pylint: disable=broad-except
            pass
    raise CLIError(
        'Failed to decode file {} - unknown decoding'.format(file_path))


def _explode_list_args(args):
    """Iterate through each attribute member of args and create a copy with
    the IterateValues 'flattened' to only contain a single value

    Ex.
        { a1:'x', a2:IterateValue(['y', 'z']) } => [{ a1:'x', a2:'y'),{ a1:'x', a2:'z'}]
    """
    list_args = {argname: argvalue for argname, argvalue in vars(args).items()
                 if isinstance(argvalue, IterateValue)}
    if not list_args:
        yield args
    else:
        values = list(zip(*list_args.values()))
        for key in list_args:
            delattr(args, key)

        for value in values:
            new_ns = argparse.Namespace(**vars(args))
            for key_index, key in enumerate(list_args.keys()):
                setattr(new_ns, key, value[key_index])
            yield new_ns


def _merge_kwargs(patch_kwargs, base_kwargs, supported_kwargs=None):
    merged_kwargs = base_kwargs.copy()
    merged_kwargs.update(patch_kwargs)
    unrecognized_kwargs = [x for x in merged_kwargs if x not in (
        supported_kwargs or CLI_COMMON_KWARGS)]
    if unrecognized_kwargs:
        raise TypeError('unrecognized kwargs: {}'.format(unrecognized_kwargs))
    return merged_kwargs
