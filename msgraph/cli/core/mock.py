# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msgraph.cli.core import MgCLI


class DummyCli(MgCLI):
    """A dummy CLI instance can be used to facilitate automation"""
    def __init__(self, commands_loader_cls=None, **kwargs):
        import os

        from msgraph.cli.core.command_loaders import MainCommandsLoader
        from msgraph.cli.core.invocation import CommandInvoker
        from msgraph.cli.core.help._help import GraphCliHelp

        from knack.completion import ARGCOMPLETE_ENV_NAME

        super(DummyCli, self).__init__(cli_name='mg',
                                       commands_loader_cls=commands_loader_cls
                                       or MainCommandsLoader,
                                       help_cls=GraphCliHelp,
                                       invocation_cls=CommandInvoker)

        self.data['headers'] = {
        }  # the x-ms-client-request-id is generated before a command is to execute
        self.data['command'] = 'unknown'
        self.data['completer_active'] = ARGCOMPLETE_ENV_NAME in os.environ
        self.data['query_active'] = False

        loader = self.commands_loader_cls(self)
        setattr(self, 'commands_loader', loader)

    def get_cli_version(self):
        from msgraph.cli.core import __version__ as cli_version
        return cli_version