from msgraph.cli.core import AzCommandsLoader
from msgraph.cli.core.commands import CliCommandType
import msgraph.cli.command_modules.authentication._help


class AuthenticationCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx, **kwargs):
        super().__init__(cli_ctx, **kwargs)

    def load_command_table(self, args):
        template = CliCommandType(operations_tmpl='msgraph.cli.command_modules.authentication.custom#{}')

        with self.command_group('', template) as g:
            g.command('login', 'login')

        return self.command_table


COMMAND_LOADER_CLS = AuthenticationCommandsLoader
