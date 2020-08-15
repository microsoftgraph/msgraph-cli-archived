# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from msgraph.cli.core import AzCommandsLoader
from msgraph.cli.core.commands import CliCommandType
import msgraph.cli.command_modules.authentication._help


class AuthenticationCommandsLoader(AzCommandsLoader):
    """Provides authentication commands to msgraph-cli
    """
    def __init__(self, cli_ctx, **kwargs):
        super().__init__(cli_ctx, **kwargs)

    def load_command_table(self, args):
        # operations_tmpl is the file that contains the implementation of the command
        template = CliCommandType(operations_tmpl='msgraph.cli.command_modules.authentication.custom#{}')

        with self.command_group('', template) as g:
            g.command('login', 'login')

        return self.command_table


COMMAND_LOADER_CLS = AuthenticationCommandsLoader
