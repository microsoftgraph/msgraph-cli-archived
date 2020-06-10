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