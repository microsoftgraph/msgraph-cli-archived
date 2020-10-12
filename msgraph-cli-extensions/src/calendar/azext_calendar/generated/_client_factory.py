# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_calendar_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.calendar import Calendar
    return get_mgmt_service_client(cli_ctx,
                                   Calendar,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_group(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).group


def cf_group_calendar(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).group_calendar


def cf_group_calendar_calendar_view(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).group_calendar_calendar_view


def cf_group_calendar_event(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).group_calendar_event


def cf_group_calendar_view(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).group_calendar_view


def cf_group_calendar_view_calendar(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).group_calendar_view_calendar


def cf_group_event(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).group_event


def cf_group_event_calendar(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).group_event_calendar


def cf_place_place(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).place_place


def cf_user(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user


def cf_user_calendar(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar


def cf_user_calendar_calendar_view(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar_calendar_view


def cf_user_calendar_event(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar_event


def cf_user_calendar_group(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar_group


def cf_user_calendar_group_calendar(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar_group_calendar


def cf_user_calendar_group_calendar_calendar_view(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar_group_calendar_calendar_view


def cf_user_calendar_group_calendar_event(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar_group_calendar_event


def cf_user_calendar(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar


def cf_user_calendar_calendar_view(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar_calendar_view


def cf_user_calendar_event(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar_event


def cf_user_calendar_view(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar_view


def cf_user_calendar_view_calendar(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_calendar_view_calendar


def cf_user_event(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_event


def cf_user_event_calendar(cli_ctx, *_):
    return cf_calendar_cl(cli_ctx).user_event_calendar
