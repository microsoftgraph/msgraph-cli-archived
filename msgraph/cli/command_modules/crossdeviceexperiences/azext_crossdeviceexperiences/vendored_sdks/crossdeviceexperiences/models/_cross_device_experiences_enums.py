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


class Enum11(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVATIONURL = "activationUrl"
    ACTIVITYSOURCEHOST = "activitySourceHost"
    APPACTIVITYID = "appActivityId"
    APPDISPLAYNAME = "appDisplayName"
    CONTENTINFO = "contentInfo"
    CONTENTURL = "contentUrl"
    CREATEDDATETIME = "createdDateTime"
    EXPIRATIONDATETIME = "expirationDateTime"
    FALLBACKURL = "fallbackUrl"
    LASTMODIFIEDDATETIME = "lastModifiedDateTime"
    STATUS = "status"
    USERTIMEZONE = "userTimezone"
    VISUALELEMENTS = "visualElements"
    HISTORYITEMS = "historyItems"

class Enum12(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    HISTORYITEMS = "historyItems"

class Enum6(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    ACTIVEDURATIONSECONDS = "activeDurationSeconds"
    ACTIVEDURATIONSECONDSDESC = "activeDurationSeconds desc"
    CREATEDDATETIME = "createdDateTime"
    CREATEDDATETIMEDESC = "createdDateTime desc"
    EXPIRATIONDATETIME = "expirationDateTime"
    EXPIRATIONDATETIMEDESC = "expirationDateTime desc"
    LASTACTIVEDATETIME = "lastActiveDateTime"
    LASTACTIVEDATETIMEDESC = "lastActiveDateTime desc"
    LASTMODIFIEDDATETIME = "lastModifiedDateTime"
    LASTMODIFIEDDATETIMEDESC = "lastModifiedDateTime desc"
    STARTEDDATETIME = "startedDateTime"
    STARTEDDATETIMEDESC = "startedDateTime desc"
    STATUS = "status"
    STATUSDESC = "status desc"
    USERTIMEZONE = "userTimezone"
    USERTIMEZONEDESC = "userTimezone desc"

class Enum7(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVEDURATIONSECONDS = "activeDurationSeconds"
    CREATEDDATETIME = "createdDateTime"
    EXPIRATIONDATETIME = "expirationDateTime"
    LASTACTIVEDATETIME = "lastActiveDateTime"
    LASTMODIFIEDDATETIME = "lastModifiedDateTime"
    STARTEDDATETIME = "startedDateTime"
    STATUS = "status"
    USERTIMEZONE = "userTimezone"
    ACTIVITY = "activity"

class Enum9(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVEDURATIONSECONDS = "activeDurationSeconds"
    CREATEDDATETIME = "createdDateTime"
    EXPIRATIONDATETIME = "expirationDateTime"
    LASTACTIVEDATETIME = "lastActiveDateTime"
    LASTMODIFIEDDATETIME = "lastModifiedDateTime"
    STARTEDDATETIME = "startedDateTime"
    STATUS = "status"
    USERTIMEZONE = "userTimezone"
    ACTIVITY = "activity"

class Get2itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVATIONURL = "activationUrl"
    ACTIVITYSOURCEHOST = "activitySourceHost"
    APPACTIVITYID = "appActivityId"
    APPDISPLAYNAME = "appDisplayName"
    CONTENTINFO = "contentInfo"
    CONTENTURL = "contentUrl"
    CREATEDDATETIME = "createdDateTime"
    EXPIRATIONDATETIME = "expirationDateTime"
    FALLBACKURL = "fallbackUrl"
    LASTMODIFIEDDATETIME = "lastModifiedDateTime"
    STATUS = "status"
    USERTIMEZONE = "userTimezone"
    VISUALELEMENTS = "visualElements"
    HISTORYITEMS = "historyItems"

class Get3itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    HISTORYITEMS = "historyItems"

class Get4itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ACTIVITY = "activity"

class Get6itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    ACTIVATIONURL = "activationUrl"
    ACTIVATIONURLDESC = "activationUrl desc"
    ACTIVITYSOURCEHOST = "activitySourceHost"
    ACTIVITYSOURCEHOSTDESC = "activitySourceHost desc"
    APPACTIVITYID = "appActivityId"
    APPACTIVITYIDDESC = "appActivityId desc"
    APPDISPLAYNAME = "appDisplayName"
    APPDISPLAYNAMEDESC = "appDisplayName desc"
    CONTENTINFO = "contentInfo"
    CONTENTINFODESC = "contentInfo desc"
    CONTENTURL = "contentUrl"
    CONTENTURLDESC = "contentUrl desc"
    CREATEDDATETIME = "createdDateTime"
    CREATEDDATETIMEDESC = "createdDateTime desc"
    EXPIRATIONDATETIME = "expirationDateTime"
    EXPIRATIONDATETIMEDESC = "expirationDateTime desc"
    FALLBACKURL = "fallbackUrl"
    FALLBACKURLDESC = "fallbackUrl desc"
    LASTMODIFIEDDATETIME = "lastModifiedDateTime"
    LASTMODIFIEDDATETIMEDESC = "lastModifiedDateTime desc"
    STATUS = "status"
    STATUSDESC = "status desc"
    USERTIMEZONE = "userTimezone"
    USERTIMEZONEDESC = "userTimezone desc"
    VISUALELEMENTS = "visualElements"
    VISUALELEMENTSDESC = "visualElements desc"

class Get7itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVATIONURL = "activationUrl"
    ACTIVITYSOURCEHOST = "activitySourceHost"
    APPACTIVITYID = "appActivityId"
    APPDISPLAYNAME = "appDisplayName"
    CONTENTINFO = "contentInfo"
    CONTENTURL = "contentUrl"
    CREATEDDATETIME = "createdDateTime"
    EXPIRATIONDATETIME = "expirationDateTime"
    FALLBACKURL = "fallbackUrl"
    LASTMODIFIEDDATETIME = "lastModifiedDateTime"
    STATUS = "status"
    USERTIMEZONE = "userTimezone"
    VISUALELEMENTS = "visualElements"
    HISTORYITEMS = "historyItems"

class Get8itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    HISTORYITEMS = "historyItems"

class Get9itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ACTIVITY = "activity"

class Microsoftgraphstatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ACTIVE = "active"
    UPDATED = "updated"
    DELETED = "deleted"
    IGNORED = "ignored"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"
