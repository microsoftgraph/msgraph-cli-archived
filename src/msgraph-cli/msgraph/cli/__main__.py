import sys

from msgraph.cli.core import get_default_cli

mg_cli = get_default_cli()


def cli_main(cli, args):
    return cli.invoke(args)


exit_code = cli_main(mg_cli, sys.argv[1:])
sys.exit(exit_code)
