import pkgutil
from importlib import import_module
import sys
from collections import OrderedDict
from knack import CLI
from knack import CLICommandsLoader
from knack.cli import logger
from knack.arguments import ignore_type

from msgraph.cli.core.commands._util import _load_module_command_loader
from msgraph.cli.core.invocation import GraphCliCommandInvoker


class MainCommandsLoader(CLICommandsLoader):
    def __init__(self, cli_ctx=None):
        super(MainCommandsLoader, self).__init__(cli_ctx)
        self.cmd_to_loader_map = {}
        self.loaders = []
        self.command_table=dict()

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
                    loader.load_arguments('')  # this adds entries to the argument registries
                else:
                    loader.command_name = command
                    self.command_table[command].load_arguments()  # this loads the arguments via reflection
                    loader.load_arguments(command)  # this adds entries to the argument registries
                self.argument_registry.arguments.update(loader.argument_registry.arguments)
                self.extra_argument_registry.update(loader.extra_argument_registry)
                loader._update_command_definitions()  # pylint: disable=protected-access

    def _update_command_table_from_modules(self, args):
        installed_command_modules = []
        BLACKLISTED_MODS = ['context', 'shell', 'documentdb', 'component']

        try:
            modules = import_module('command_modules')
            installed_command_modules = [modname for _, modname, _ in
                                             pkgutil.iter_modules(modules.__path__)
                                             if modname not in BLACKLISTED_MODS]
            for module in installed_command_modules:
                command_table, group_table = _load_module_command_loader(self, args, module)
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


mg_cli = get_default_cli()

exit_code = mg_cli.invoke(sys.argv[1:])
sys.exit(exit_code)