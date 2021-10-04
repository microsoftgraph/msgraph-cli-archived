# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._cloud_communications_enums import *


class collectionofonlinemeeting(msrest.serialization.Model):
    """Collection of onlineMeeting.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param value:
    :type value: list[~cloud_communications.models.microsoftgraphonlinemeeting]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'value': {'key': 'value', 'type': '[microsoftgraphonlinemeeting]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        value: Optional[List["microsoftgraphonlinemeeting"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(collectionofonlinemeeting, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.value = value
        self.odata_next_link = odata_next_link


class microsoftgraphaudioconferencing(msrest.serialization.Model):
    """audioConferencing.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param conference_id:
    :type conference_id: str
    :param dialin_url: A URL to the externally-accessible web page that contains dial-in
     information.
    :type dialin_url: str
    :param toll_free_number: The toll-free number that connects to the Audio Conference Provider.
    :type toll_free_number: str
    :param toll_number: The toll number that connects to the Audio Conference Provider.
    :type toll_number: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'conference_id': {'key': 'conferenceId', 'type': 'str'},
        'dialin_url': {'key': 'dialinUrl', 'type': 'str'},
        'toll_free_number': {'key': 'tollFreeNumber', 'type': 'str'},
        'toll_number': {'key': 'tollNumber', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        conference_id: Optional[str] = None,
        dialin_url: Optional[str] = None,
        toll_free_number: Optional[str] = None,
        toll_number: Optional[str] = None,
        **kwargs
    ):
        super(microsoftgraphaudioconferencing, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.conference_id = conference_id
        self.dialin_url = dialin_url
        self.toll_free_number = toll_free_number
        self.toll_number = toll_number


class microsoftgraphchatinfo(msrest.serialization.Model):
    """chatInfo.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param message_id: The unique identifier of a message in a Microsoft Teams channel.
    :type message_id: str
    :param reply_chain_message_id: The ID of the reply message.
    :type reply_chain_message_id: str
    :param thread_id: The unique identifier for a thread in Microsoft Teams.
    :type thread_id: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'reply_chain_message_id': {'key': 'replyChainMessageId', 'type': 'str'},
        'thread_id': {'key': 'threadId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        message_id: Optional[str] = None,
        reply_chain_message_id: Optional[str] = None,
        thread_id: Optional[str] = None,
        **kwargs
    ):
        super(microsoftgraphchatinfo, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.message_id = message_id
        self.reply_chain_message_id = reply_chain_message_id
        self.thread_id = thread_id


class microsoftgraphentity(msrest.serialization.Model):
    """entity.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        super(microsoftgraphentity, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id


class microsoftgraphidentity(msrest.serialization.Model):
    """identity.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param display_name: The identity's display name. Note that this may not always be available or
     up to date. For example, if a user changes their display name, the API may show the new value
     in a future response, but the items associated with the user won't show up as having changed
     when using delta.
    :type display_name: str
    :param id: Unique identifier for the identity.
    :type id: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        super(microsoftgraphidentity, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.display_name = display_name
        self.id = id


class microsoftgraphidentityset(msrest.serialization.Model):
    """identitySet.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param application: identity.
    :type application: ~cloud_communications.models.microsoftgraphidentity
    :param device: identity.
    :type device: ~cloud_communications.models.microsoftgraphidentity
    :param user: identity.
    :type user: ~cloud_communications.models.microsoftgraphidentity
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'application': {'key': 'application', 'type': 'microsoftgraphidentity'},
        'device': {'key': 'device', 'type': 'microsoftgraphidentity'},
        'user': {'key': 'user', 'type': 'microsoftgraphidentity'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        application: Optional["microsoftgraphidentity"] = None,
        device: Optional["microsoftgraphidentity"] = None,
        user: Optional["microsoftgraphidentity"] = None,
        **kwargs
    ):
        super(microsoftgraphidentityset, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.application = application
        self.device = device
        self.user = user


class microsoftgraphitembody(msrest.serialization.Model):
    """itemBody.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param content: The content of the item.
    :type content: str
    :param content_type:  Possible values include: "text", "html".
    :type content_type: str or ~cloud_communications.models.Microsoftgraphbodytype
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'content': {'key': 'content', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        content: Optional[str] = None,
        content_type: Optional[Union[str, "Microsoftgraphbodytype"]] = None,
        **kwargs
    ):
        super(microsoftgraphitembody, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.content = content
        self.content_type = content_type


class microsoftgraphmeetingparticipantinfo(msrest.serialization.Model):
    """meetingParticipantInfo.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param identity: identitySet.
    :type identity: ~cloud_communications.models.microsoftgraphidentityset
    :param upn: User principal name of the participant.
    :type upn: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'identity': {'key': 'identity', 'type': 'microsoftgraphidentityset'},
        'upn': {'key': 'upn', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        identity: Optional["microsoftgraphidentityset"] = None,
        upn: Optional[str] = None,
        **kwargs
    ):
        super(microsoftgraphmeetingparticipantinfo, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.identity = identity
        self.upn = upn


class microsoftgraphmeetingparticipants(msrest.serialization.Model):
    """meetingParticipants.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param attendees:
    :type attendees: list[~cloud_communications.models.microsoftgraphmeetingparticipantinfo]
    :param organizer: meetingParticipantInfo.
    :type organizer: ~cloud_communications.models.microsoftgraphmeetingparticipantinfo
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'attendees': {'key': 'attendees', 'type': '[microsoftgraphmeetingparticipantinfo]'},
        'organizer': {'key': 'organizer', 'type': 'microsoftgraphmeetingparticipantinfo'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        attendees: Optional[List["microsoftgraphmeetingparticipantinfo"]] = None,
        organizer: Optional["microsoftgraphmeetingparticipantinfo"] = None,
        **kwargs
    ):
        super(microsoftgraphmeetingparticipants, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.attendees = attendees
        self.organizer = organizer


class microsoftgraphonlinemeeting(microsoftgraphentity):
    """onlineMeeting.

    :param id: Read-only.
    :type id: str
    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param audio_conferencing: audioConferencing.
    :type audio_conferencing: ~cloud_communications.models.microsoftgraphaudioconferencing
    :param chat_info: chatInfo.
    :type chat_info: ~cloud_communications.models.microsoftgraphchatinfo
    :param creation_date_time: The meeting creation time in UTC. Read-only.
    :type creation_date_time: ~datetime.datetime
    :param end_date_time: The meeting end time in UTC.
    :type end_date_time: ~datetime.datetime
    :param external_id:
    :type external_id: str
    :param join_information: itemBody.
    :type join_information: ~cloud_communications.models.microsoftgraphitembody
    :param join_web_url: The join URL of the online meeting. Read-only.
    :type join_web_url: str
    :param participants: meetingParticipants.
    :type participants: ~cloud_communications.models.microsoftgraphmeetingparticipants
    :param start_date_time: The meeting start time in UTC.
    :type start_date_time: ~datetime.datetime
    :param subject: The subject of the online meeting.
    :type subject: str
    :param video_teleconference_id: The video teleconferencing ID. Read-only.
    :type video_teleconference_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'audio_conferencing': {'key': 'audioConferencing', 'type': 'microsoftgraphaudioconferencing'},
        'chat_info': {'key': 'chatInfo', 'type': 'microsoftgraphchatinfo'},
        'creation_date_time': {'key': 'creationDateTime', 'type': 'iso-8601'},
        'end_date_time': {'key': 'endDateTime', 'type': 'iso-8601'},
        'external_id': {'key': 'externalId', 'type': 'str'},
        'join_information': {'key': 'joinInformation', 'type': 'microsoftgraphitembody'},
        'join_web_url': {'key': 'joinWebUrl', 'type': 'str'},
        'participants': {'key': 'participants', 'type': 'microsoftgraphmeetingparticipants'},
        'start_date_time': {'key': 'startDateTime', 'type': 'iso-8601'},
        'subject': {'key': 'subject', 'type': 'str'},
        'video_teleconference_id': {'key': 'videoTeleconferenceId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        additional_properties: Optional[Dict[str, object]] = None,
        audio_conferencing: Optional["microsoftgraphaudioconferencing"] = None,
        chat_info: Optional["microsoftgraphchatinfo"] = None,
        creation_date_time: Optional[datetime.datetime] = None,
        end_date_time: Optional[datetime.datetime] = None,
        external_id: Optional[str] = None,
        join_information: Optional["microsoftgraphitembody"] = None,
        join_web_url: Optional[str] = None,
        participants: Optional["microsoftgraphmeetingparticipants"] = None,
        start_date_time: Optional[datetime.datetime] = None,
        subject: Optional[str] = None,
        video_teleconference_id: Optional[str] = None,
        **kwargs
    ):
        super(microsoftgraphonlinemeeting, self).__init__(id=id, **kwargs)
        self.additional_properties = additional_properties
        self.audio_conferencing = audio_conferencing
        self.chat_info = chat_info
        self.creation_date_time = creation_date_time
        self.end_date_time = end_date_time
        self.external_id = external_id
        self.join_information = join_information
        self.join_web_url = join_web_url
        self.participants = participants
        self.start_date_time = start_date_time
        self.subject = subject
        self.video_teleconference_id = video_teleconference_id


class odataerror(msrest.serialization.Model):
    """odataerror.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param error: Required.
    :type error: ~cloud_communications.models.odataerrormain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'error': {'key': 'error', 'type': 'odataerrormain'},
    }

    def __init__(
        self,
        *,
        error: "odataerrormain",
        additional_properties: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(odataerror, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.error = error


class odataerrordetail(msrest.serialization.Model):
    """odataerrordetail.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        additional_properties: Optional[Dict[str, object]] = None,
        target: Optional[str] = None,
        **kwargs
    ):
        super(odataerrordetail, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message
        self.target = target


class odataerrormain(msrest.serialization.Model):
    """odataerrormain.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~cloud_communications.models.odataerrordetail]
    :param innererror: The structure of this object is service-specific.
    :type innererror: dict[str, object]
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[odataerrordetail]'},
        'innererror': {'key': 'innererror', 'type': '{object}'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        additional_properties: Optional[Dict[str, object]] = None,
        target: Optional[str] = None,
        details: Optional[List["odataerrordetail"]] = None,
        innererror: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(odataerrormain, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror