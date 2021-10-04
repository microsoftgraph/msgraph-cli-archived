# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Get2itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    AUDIOCONFERENCING = "audioConferencing"
    CHATINFO = "chatInfo"
    CREATIONDATETIME = "creationDateTime"
    ENDDATETIME = "endDateTime"
    EXTERNALID = "externalId"
    JOININFORMATION = "joinInformation"
    JOINWEBURL = "joinWebUrl"
    PARTICIPANTS = "participants"
    STARTDATETIME = "startDateTime"
    SUBJECT = "subject"
    VIDEOTELECONFERENCEID = "videoTeleconferenceId"

class Get6itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    AUDIOCONFERENCING = "audioConferencing"
    AUDIOCONFERENCINGDESC = "audioConferencing desc"
    CHATINFO = "chatInfo"
    CHATINFODESC = "chatInfo desc"
    CREATIONDATETIME = "creationDateTime"
    CREATIONDATETIMEDESC = "creationDateTime desc"
    ENDDATETIME = "endDateTime"
    ENDDATETIMEDESC = "endDateTime desc"
    EXTERNALID = "externalId"
    EXTERNALIDDESC = "externalId desc"
    JOININFORMATION = "joinInformation"
    JOININFORMATIONDESC = "joinInformation desc"
    JOINWEBURL = "joinWebUrl"
    JOINWEBURLDESC = "joinWebUrl desc"
    PARTICIPANTS = "participants"
    PARTICIPANTSDESC = "participants desc"
    STARTDATETIME = "startDateTime"
    STARTDATETIMEDESC = "startDateTime desc"
    SUBJECT = "subject"
    SUBJECTDESC = "subject desc"
    VIDEOTELECONFERENCEID = "videoTeleconferenceId"
    VIDEOTELECONFERENCEIDDESC = "videoTeleconferenceId desc"

class Get7itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    AUDIOCONFERENCING = "audioConferencing"
    CHATINFO = "chatInfo"
    CREATIONDATETIME = "creationDateTime"
    ENDDATETIME = "endDateTime"
    EXTERNALID = "externalId"
    JOININFORMATION = "joinInformation"
    JOINWEBURL = "joinWebUrl"
    PARTICIPANTS = "participants"
    STARTDATETIME = "startDateTime"
    SUBJECT = "subject"
    VIDEOTELECONFERENCEID = "videoTeleconferenceId"

class Microsoftgraphbodytype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TEXT = "text"
    HTML = "html"