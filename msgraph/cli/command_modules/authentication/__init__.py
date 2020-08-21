# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from msgraph.cli.core import AzCommandsLoader
from msgraph.cli.core.commands import CliCommandType
import msgraph.cli.command_modules.authentication._help

from ._exception_handler import auth_exception_handler


class AuthenticationCommandsLoader(AzCommandsLoader):
    """Provides authentication commands to msgraph-cli
    """

    def __init__(self, cli_ctx, **kwargs):
        super().__init__(cli_ctx, **kwargs)

    def load_command_table(self, args):
        # operations_tmpl is the file that contains the implementation of the command
        command_type = CliCommandType(
            operations_tmpl='msgraph.cli.command_modules.authentication.custom#{}',
            exception_handler=auth_exception_handler)
        with self.command_group('', command_type) as group:
            group.command('login', 'login')
            group.command('logout', 'logout')

        return self.command_table


COMMAND_LOADER_CLS = AuthenticationCommandsLoader
