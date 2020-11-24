import argparse
import platform
from knack.util import CLIError
from knack import ArgumentsContext
from knack.arguments import (CLIArgumentType, CaseInsensitiveList)

from msgraph.cli.core.commands.validators import validate_tag, validate_tags


class GraphArgumentContext(ArgumentsContext):
    pass


def get_three_state_flag(positive_label='true',
                         negative_label='false',
                         invert=False,
                         return_label=False):
    """ Creates a flag-like argument that can also accept positive/negative values. This allows
    consistency between create commands that typically use flags and update commands that require
    positive/negative values without introducing breaking changes. Flag-like behavior always
    implies the affirmative unless invert=True then invert the logic.
    - positive_label: label for the positive value (ex: 'enabled')
    - negative_label: label for the negative value (ex: 'disabled')
    - invert: invert the boolean logic for the flag
    - return_label: if true, return the corresponding label. Otherwise, return a boolean value
    """
    choices = [positive_label, negative_label]

    # pylint: disable=too-few-public-methods
    class ThreeStateAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            values = values or positive_label
            is_positive = values.lower() == positive_label.lower()
            is_positive = not is_positive if invert else is_positive
            set_val = None
            if return_label:
                set_val = positive_label if is_positive else negative_label
            else:
                set_val = is_positive
            setattr(namespace, self.dest, set_val)

    params = {'choices': CaseInsensitiveList(choices), 'nargs': '?', 'action': ThreeStateAction}
    return CLIArgumentType(**params)


def get_enum_type(data, default=None):
    """ Creates the argparse choices and type kwargs for a supplied enum type or list of strings. """
    if not data:
        return None

    # transform enum types, otherwise assume list of string choices
    try:
        choices = [x.value for x in data]
    except AttributeError:
        choices = data

    # pylint: disable=too-few-public-methods
    class DefaultAction(argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            def _get_value(val):
                return next((x for x in self.choices if x.lower() == val.lower()), val)

            if isinstance(values, list):
                values = [_get_value(v) for v in values]
            else:
                values = _get_value(values)
            setattr(args, self.dest, values)

    def _type(value):
        return next((x for x in choices if x.lower() == value.lower()), value) if value else value

    default_value = None
    if default:
        default_value = next((x for x in choices if x.lower() == default.lower()), None)
        if not default_value:
            raise CLIError(
                "Command authoring exception: unrecognized default '{}' from choices '{}'".format(
                    default, choices))
        arg_type = CLIArgumentType(choices=CaseInsensitiveList(choices),
                                   action=DefaultAction,
                                   default=default_value)
    else:
        arg_type = CLIArgumentType(choices=CaseInsensitiveList(choices), action=DefaultAction)
    return arg_type


quotes = '""' if platform.system() == 'Windows' else "''"
quote_text = 'Use {} to clear existing tags.'.format(quotes)

tags_type = CLIArgumentType(
    validator=validate_tags,
    help="space-separated tags: key[=value] [key[=value] ...]. {}".format(quote_text),
    nargs='*')

tag_type = CLIArgumentType(type=validate_tag,
                           help="a single tag in 'key[=value]' format. {}".format(quote_text),
                           nargs='?',
                           const='')
