# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# This file is extracted from azure-cli
# --------------------------------------------------------------------------------------------

import argparse
import platform

from knack.util import CLIError
from knack import ArgumentsContext
from knack.arguments import (CLIArgumentType, CaseInsensitiveList)

from msgraph.cli.core.commands.validators import validate_tags
from msgraph.cli.core.local_context import LocalContextAction, LocalContextAttribute, ALL
from msgraph.cli.core.decorators import Completer

quotes = '""' if platform.system() == 'Windows' else "''"
quote_text = 'Use {} to clear existing tags.'.format(quotes)


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


tags_type = CLIArgumentType(
    validator=validate_tags,
    help="space-separated tags: key[=value] [key[=value] ...]. {}".format(quote_text),
    nargs='*')


def get_subscription_locations(cli_ctx):
    '''Not implemented because msgraph-cli doesn't support subscriptions'''
    # from msgraph.cli.core.commands.client_factory import get_subscription_service_client
    # subscription_client, subscription_id = get_subscription_service_client(cli_ctx)
    # return list(subscription_client.subscriptions.list_locations(subscription_id))
    pass


@Completer
def get_location_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    '''Not implemented because it depends on get_subscription_list'''
    # result = get_subscription_locations(cmd.cli_ctx)
    # return [item.name for item in result]
    pass


def get_location_name_type(cli_ctx):
    def location_name_type(name):
        if ' ' in name:
            # if display name is provided, attempt to convert to short form name
            name = next((location.name for location in get_subscription_locations(cli_ctx)
                         if location.display_name.lower() == name.lower()), name)
        return name

    return location_name_type


def get_location_type(cli_ctx):
    location_type = CLIArgumentType(
        options_list=['--location', '-l'],
        completer=get_location_completion_list,
        type=get_location_name_type(cli_ctx),
        help="Location. Values from: `az account list-locations`. "
        "You can configure the default location using `az configure --defaults location=<location>`.",
        metavar='LOCATION',
        configured_default='location',
        local_context_attribute=LocalContextAttribute(
            name='location', actions=[LocalContextAction.SET,
                                      LocalContextAction.GET], scopes=[ALL]))
    return location_type
