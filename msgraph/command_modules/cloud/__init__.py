# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from msgraph.cli.core import AzCommandsLoader
from msgraph.cli.core.commands import CliCommandType
from msgraph.command_modules.cloud._exception_handler import cloud_exception_handler
import msgraph.command_modules.cloud._help


class CloudCommandsLoader(AzCommandsLoader):
    """Provides cloud commands to msgraph-cli
    """
    def __init__(self, cli_ctx, **kwargs):
        super().__init__(cli_ctx, **kwargs)

    def load_command_table(self, args):
        # operations_tmpl is the file that contains the implementation of the command
        command_type = CliCommandType(operations_tmpl='msgraph.command_modules.cloud.custom#{}',
                                      exception_handler=cloud_exception_handler)
        with self.command_group('cloud', command_type) as group:
            group.command('set', 'set_cloud')
            group.command('list', 'show_clouds')
            group.command('register', 'add_cloud')
            group.command('update', 'update_cloud')
            group.command('unregister', 'delete_cloud')
            group.command('set-version', 'set_version')
            group.command('show', 'show_profile')

        return self.command_table


COMMAND_LOADER_CLS = CloudCommandsLoader
