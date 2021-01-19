from knack.log import get_logger
from knack.util import CLIError

from msgraph.cli.core.help._help import CliCommandHelpFile, CliGroupHelpFile

logger = get_logger(__name__)


def get_all_help(cli_ctx, skip=True):
    invoker = cli_ctx.invocation
    help_ctx = cli_ctx.help_cls(cli_ctx)
    if not invoker:
        raise CLIError('CLI context does not contain invocation.')

    parser_keys = []
    parser_values = []
    sub_parser_keys = []
    sub_parser_values = []
    _store_parsers(invoker.parser, parser_keys, parser_values, sub_parser_keys, sub_parser_values)
    for cmd, parser in zip(parser_keys, parser_values):
        if cmd not in sub_parser_keys:
            sub_parser_keys.append(cmd)
            sub_parser_values.append(parser)
    help_files = []
    help_errors = {}
    for cmd, parser in zip(sub_parser_keys, sub_parser_values):
        try:
            help_ctx.update_loaders_with_help_file_contents(cmd.split())
            help_file = CliGroupHelpFile(help_ctx, cmd, parser) if _is_group(parser) \
                else CliCommandHelpFile(help_ctx, cmd, parser)
            help_file.load(parser)
            help_files.append(help_file)
        except Exception as ex:  # pylint: disable=broad-except
            if skip:
                logger.warning("Skipping '%s': %s", cmd, ex)
            else:
                help_errors[cmd] = "Error '{}': {}".format(cmd, ex)
    if help_errors:
        raise CLIError(help_errors)
    help_files = sorted(help_files, key=lambda x: x.command)
    return help_files


def _store_parsers(parser, parser_keys, parser_values, sub_parser_keys, sub_parser_values):
    for s in parser.subparsers.values():
        parser_keys.append(_get_parser_name(s))
        parser_values.append(s)
        if _is_group(s):
            for c in s.choices.values():
                sub_parser_keys.append(_get_parser_name(c))
                sub_parser_values.append(c)
                _store_parsers(c, parser_keys, parser_values, sub_parser_keys, sub_parser_values)


def _get_parser_name(s):
    return (s._prog_prefix if hasattr(s, '_prog_prefix') else s.prog)[3:]  # pylint: disable=protected-access


def _is_group(parser):
    return getattr(parser, '_subparsers', None) is not None \
        or getattr(parser, 'choices', None) is not None