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

from azure.cli.core.commands.validators import validate_file_or_dict
from azext_cloudcommunications.action import (
    AddAudioConferencing,
    AddChatInfo,
    AddJoinInformation
)


def load_arguments(self, _):

    with self.argument_context('cloudcommunications user create-online-meeting') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('audio_conferencing', action=AddAudioConferencing, nargs='+', help='audioConferencing')
        c.argument('chat_info', action=AddChatInfo, nargs='+', help='chatInfo')
        c.argument('creation_date_time', help='The meeting creation time in UTC. Read-only.')
        c.argument('end_date_time', help='The meeting end time in UTC.')
        c.argument('external_id', type=str, help='')
        c.argument('join_information', action=AddJoinInformation, nargs='+', help='itemBody')
        c.argument('join_web_url', type=str, help='The join URL of the online meeting. Read-only.')
        c.argument('start_date_time', help='The meeting start time in UTC.')
        c.argument('subject', type=str, help='The subject of the online meeting.')
        c.argument('video_teleconference_id', type=str, help='The video teleconferencing ID. Read-only.')
        c.argument('attendees', type=validate_file_or_dict, help=' Expected value: json-string/json-file/@json-file.',
                   arg_group='Participants')
        c.argument('organizer', type=validate_file_or_dict, help='meetingParticipantInfo Expected value: '
                   'json-string/json-file/@json-file.', arg_group='Participants')

    with self.argument_context('cloudcommunications user delete-online-meeting') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('online_meeting_id', type=str, help='key: id of onlineMeeting')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('cloudcommunications user list-online-meeting') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('cloudcommunications user show-online-meeting') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('online_meeting_id', type=str, help='key: id of onlineMeeting')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('cloudcommunications user update-online-meeting') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('online_meeting_id', type=str, help='key: id of onlineMeeting')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('audio_conferencing', action=AddAudioConferencing, nargs='+', help='audioConferencing')
        c.argument('chat_info', action=AddChatInfo, nargs='+', help='chatInfo')
        c.argument('creation_date_time', help='The meeting creation time in UTC. Read-only.')
        c.argument('end_date_time', help='The meeting end time in UTC.')
        c.argument('external_id', type=str, help='')
        c.argument('join_information', action=AddJoinInformation, nargs='+', help='itemBody')
        c.argument('join_web_url', type=str, help='The join URL of the online meeting. Read-only.')
        c.argument('start_date_time', help='The meeting start time in UTC.')
        c.argument('subject', type=str, help='The subject of the online meeting.')
        c.argument('video_teleconference_id', type=str, help='The video teleconferencing ID. Read-only.')
        c.argument('attendees', type=validate_file_or_dict, help=' Expected value: json-string/json-file/@json-file.',
                   arg_group='Participants')
        c.argument('organizer', type=validate_file_or_dict, help='meetingParticipantInfo Expected value: '
                   'json-string/json-file/@json-file.', arg_group='Participants')
