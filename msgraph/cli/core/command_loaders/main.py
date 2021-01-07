# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import pkgutil
from knack.cli import logger
from importlib import import_module
from collections import OrderedDict
from knack.arguments import ignore_type
from knack import CLICommandsLoader

from msgraph.cli.core.commands._util import _load_module_command_loader, _load_extension_command_loader
from msgraph.cli.core.profile import read_profile

version = read_profile().get('version', 'v1.0')

if version == 'v1.0':
    from msgraph.cli.core.v1_0_installed_extensions import installed_extensions
else:
    from msgraph.cli.core.beta_installed_extensions import installed_extensions


class MainCommandsLoader(CLICommandsLoader):
    """
    Loads command_tables from command_modules.
    """
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
        self._update_command_table_from_extensions(args)
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
                self.argument_registry.arguments.update(loader.argument_registry.arguments)
                self.extra_argument_registry.update(loader.extra_argument_registry)
                loader._update_command_definitions()  # pylint: disable=protected-access

    def _update_command_table_from_modules(self, args):
        """Loads command_table from msgraph.command_modules

        :params args: List of the arguments from the commandline
        """
        installed_command_modules = []
        BLACKLISTED_MODS = ['context', 'shell', 'documentdb', 'component']

        try:
            modules = import_module('msgraph.command_modules')
            installed_command_modules = [
                modname for _, modname, _ in pkgutil.iter_modules(modules.__path__)
                if modname not in BLACKLISTED_MODS
            ]
            for module in installed_command_modules:
                command_table, group_table = _load_module_command_loader(self, args, module)
                self.command_table.update(command_table)
                self.command_group_table.update(group_table)
        except ImportError as e:
            logger.warning(e)

    def _update_command_table_from_extensions(self, args):
        """Loads command_table from installed extensions

        :params args: List of the arguments from the commandline
        """
        try:
            for extension in installed_extensions:
                command_table, group_table = _load_extension_command_loader(self, args, extension)
                self.command_table.update(command_table)
                self.command_group_table.update(group_table)
        except ImportError as e:
            logger.warning(e)
