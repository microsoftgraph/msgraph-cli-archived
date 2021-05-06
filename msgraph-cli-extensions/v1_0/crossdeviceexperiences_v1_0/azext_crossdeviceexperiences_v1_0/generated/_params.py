# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from msgraph.cli.core.commands.parameters import get_enum_type
from msgraph.cli.core.commands.validators import validate_file_or_dict
from azext_crossdeviceexperiences_v1_0.action import AddAttribution


def load_arguments(self, _):

    with self.argument_context('crossdeviceexperiences user create-activity') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('activation_url', type=str, help='Required. URL used to launch the activity in the best native '
                   'experience represented by the appId. Might launch a web-based app if no native app exists.')
        c.argument('activity_source_host', type=str, help='Required. URL for the domain representing the '
                   'cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the '
                   'domain or configurable via Windows Dev Center. The JSON file is named '
                   'cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level '
                   'domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but '
                   'NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per '
                   'cross-platform app identity. For example, a separate file and domain is needed for Word vs. '
                   'PowerPoint.')
        c.argument('app_activity_id', type=str, help='Required. The unique activity ID in the context of the app - '
                   'supplied by caller and immutable thereafter.')
        c.argument('app_display_name', type=str, help='Optional. Short text description of the app used to generate '
                   'the activity for use in cases when the app is not installed on the user’s local device.')
        c.argument('content_info', type=validate_file_or_dict, help='Json Expected value: json-string/@json-file.')
        c.argument('content_url', type=str, help='Optional. Used in the event the content can be rendered outside of a '
                   'native or web-based app experience (for example, a pointer to an item in an RSS feed).')
        c.argument('created_date_time', help='Set by the server. DateTime in UTC when the object was created on the '
                   'server.')
        c.argument('expiration_date_time', help='Set by the server. DateTime in UTC when the object expired on the '
                   'server.')
        c.argument('fallback_url', type=str, help='Optional. URL used to launch the activity in a web-based app, if '
                   'available.')
        c.argument('last_modified_date_time', help='Set by the server. DateTime in UTC when the object was modified on '
                   'the server.')
        c.argument('status', arg_type=get_enum_type(['active', 'updated', 'deleted', 'ignored', 'unknownFutureValue']),
                   help='')
        c.argument('user_timezone', type=str, help='Optional. The timezone in which the user\'s device used to '
                   'generate the activity was located at activity creation time; values supplied as Olson IDs in order '
                   'to support cross-platform representation.')
        c.argument('history_items', type=validate_file_or_dict, help='Optional. NavigationProperty/Containment; '
                   'navigation property to the activity\'s historyItems. Expected value: json-string/@json-file.')
        c.argument('attribution', action=AddAttribution, nargs='+', help='imageInfo', arg_group='Visual Elements')
        c.argument('background_color', type=str, help='Optional. Background color used to render the activity in the '
                   'UI - brand color for the application source of the activity. Must be a valid hex color',
                   arg_group='Visual Elements')
        c.argument('content', type=validate_file_or_dict, help='Json Expected value: json-string/@json-file.',
                   arg_group='Visual Elements')
        c.argument('description', type=str, help='Optional. Longer text description of the user\'s unique activity '
                   '(example: document name, first sentence, and/or metadata)', arg_group='Visual Elements')
        c.argument('display_text', type=str, help='Required. Short text description of the user\'s unique activity '
                   '(for example, document name in cases where an activity refers to document creation)',
                   arg_group='Visual Elements')

    with self.argument_context('crossdeviceexperiences user delete-activity') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('crossdeviceexperiences user list-activity') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('crossdeviceexperiences user show-activity') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('crossdeviceexperiences user update-activity') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('activation_url', type=str, help='Required. URL used to launch the activity in the best native '
                   'experience represented by the appId. Might launch a web-based app if no native app exists.')
        c.argument('activity_source_host', type=str, help='Required. URL for the domain representing the '
                   'cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the '
                   'domain or configurable via Windows Dev Center. The JSON file is named '
                   'cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level '
                   'domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but '
                   'NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per '
                   'cross-platform app identity. For example, a separate file and domain is needed for Word vs. '
                   'PowerPoint.')
        c.argument('app_activity_id', type=str, help='Required. The unique activity ID in the context of the app - '
                   'supplied by caller and immutable thereafter.')
        c.argument('app_display_name', type=str, help='Optional. Short text description of the app used to generate '
                   'the activity for use in cases when the app is not installed on the user’s local device.')
        c.argument('content_info', type=validate_file_or_dict, help='Json Expected value: json-string/@json-file.')
        c.argument('content_url', type=str, help='Optional. Used in the event the content can be rendered outside of a '
                   'native or web-based app experience (for example, a pointer to an item in an RSS feed).')
        c.argument('created_date_time', help='Set by the server. DateTime in UTC when the object was created on the '
                   'server.')
        c.argument('expiration_date_time', help='Set by the server. DateTime in UTC when the object expired on the '
                   'server.')
        c.argument('fallback_url', type=str, help='Optional. URL used to launch the activity in a web-based app, if '
                   'available.')
        c.argument('last_modified_date_time', help='Set by the server. DateTime in UTC when the object was modified on '
                   'the server.')
        c.argument('status', arg_type=get_enum_type(['active', 'updated', 'deleted', 'ignored', 'unknownFutureValue']),
                   help='')
        c.argument('user_timezone', type=str, help='Optional. The timezone in which the user\'s device used to '
                   'generate the activity was located at activity creation time; values supplied as Olson IDs in order '
                   'to support cross-platform representation.')
        c.argument('history_items', type=validate_file_or_dict, help='Optional. NavigationProperty/Containment; '
                   'navigation property to the activity\'s historyItems. Expected value: json-string/@json-file.')
        c.argument('attribution', action=AddAttribution, nargs='+', help='imageInfo', arg_group='Visual Elements')
        c.argument('background_color', type=str, help='Optional. Background color used to render the activity in the '
                   'UI - brand color for the application source of the activity. Must be a valid hex color',
                   arg_group='Visual Elements')
        c.argument('content', type=validate_file_or_dict, help='Json Expected value: json-string/@json-file.',
                   arg_group='Visual Elements')
        c.argument('description', type=str, help='Optional. Longer text description of the user\'s unique activity '
                   '(example: document name, first sentence, and/or metadata)', arg_group='Visual Elements')
        c.argument('display_text', type=str, help='Required. Short text description of the user\'s unique activity '
                   '(for example, document name in cases where an activity refers to document creation)',
                   arg_group='Visual Elements')

    with self.argument_context('crossdeviceexperiences user-activity create-history-item') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('active_duration_seconds', type=int, help='Optional. The duration of active user engagement. if not '
                   'supplied, this is calculated from the startedDateTime and lastActiveDateTime.')
        c.argument('created_date_time', help='Set by the server. DateTime in UTC when the object was created on the '
                   'server.')
        c.argument('expiration_date_time', help='Optional. UTC DateTime when the historyItem will undergo hard-delete. '
                   'Can be set by the client.')
        c.argument('last_active_date_time', help='Optional. UTC DateTime when the historyItem (activity session) was '
                   'last understood as active or finished - if null, historyItem status should be Ongoing.')
        c.argument('last_modified_date_time', help='Set by the server. DateTime in UTC when the object was modified on '
                   'the server.')
        c.argument('started_date_time', help='Required. UTC DateTime when the historyItem (activity session) was '
                   'started. Required for timeline history.')
        c.argument('status', arg_type=get_enum_type(['active', 'updated', 'deleted', 'ignored', 'unknownFutureValue']),
                   help='')
        c.argument('user_timezone', type=str, help='Optional. The timezone in which the user\'s device used to '
                   'generate the activity was located at activity creation time. Values supplied as Olson IDs in order '
                   'to support cross-platform representation.')
        c.argument('activity', type=validate_file_or_dict,
                   help='userActivity Expected value: json-string/@json-file.')

    with self.argument_context('crossdeviceexperiences user-activity delete-history-item') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('activity_history_item_id', type=str, help='key: id of activityHistoryItem')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('crossdeviceexperiences user-activity list-history-item') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('crossdeviceexperiences user-activity show-history-item') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('activity_history_item_id', type=str, help='key: id of activityHistoryItem')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('crossdeviceexperiences user-activity update-history-item') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('activity_history_item_id', type=str, help='key: id of activityHistoryItem')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('active_duration_seconds', type=int, help='Optional. The duration of active user engagement. if not '
                   'supplied, this is calculated from the startedDateTime and lastActiveDateTime.')
        c.argument('created_date_time', help='Set by the server. DateTime in UTC when the object was created on the '
                   'server.')
        c.argument('expiration_date_time', help='Optional. UTC DateTime when the historyItem will undergo hard-delete. '
                   'Can be set by the client.')
        c.argument('last_active_date_time', help='Optional. UTC DateTime when the historyItem (activity session) was '
                   'last understood as active or finished - if null, historyItem status should be Ongoing.')
        c.argument('last_modified_date_time', help='Set by the server. DateTime in UTC when the object was modified on '
                   'the server.')
        c.argument('started_date_time', help='Required. UTC DateTime when the historyItem (activity session) was '
                   'started. Required for timeline history.')
        c.argument('status', arg_type=get_enum_type(['active', 'updated', 'deleted', 'ignored', 'unknownFutureValue']),
                   help='')
        c.argument('user_timezone', type=str, help='Optional. The timezone in which the user\'s device used to '
                   'generate the activity was located at activity creation time. Values supplied as Olson IDs in order '
                   'to support cross-platform representation.')
        c.argument('activity', type=validate_file_or_dict,
                   help='userActivity Expected value: json-string/@json-file.')

    with self.argument_context('crossdeviceexperiences user-activity-history-item delete-ref-activity') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('activity_history_item_id', type=str, help='key: id of activityHistoryItem')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('crossdeviceexperiences user-activity-history-item set-ref-activity') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('activity_history_item_id', type=str, help='key: id of activityHistoryItem')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('crossdeviceexperiences user-activity-history-item show-activity') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('activity_history_item_id', type=str, help='key: id of activityHistoryItem')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('crossdeviceexperiences user-activity-history-item show-ref-activity') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user_activity_id', type=str, help='key: id of userActivity')
        c.argument('activity_history_item_id', type=str, help='key: id of activityHistoryItem')
