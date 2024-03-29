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


class Get1itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPLICATIONID = "applicationId"
    CHANGETYPE = "changeType"
    CLIENTSTATE = "clientState"
    CREATORID = "creatorId"
    ENCRYPTIONCERTIFICATE = "encryptionCertificate"
    ENCRYPTIONCERTIFICATEID = "encryptionCertificateId"
    EXPIRATIONDATETIME = "expirationDateTime"
    INCLUDERESOURCEDATA = "includeResourceData"
    LATESTSUPPORTEDTLSVERSION = "latestSupportedTlsVersion"
    LIFECYCLENOTIFICATIONURL = "lifecycleNotificationUrl"
    NOTIFICATIONURL = "notificationUrl"
    RESOURCE = "resource"

class Get5itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    APPLICATIONID = "applicationId"
    APPLICATIONIDDESC = "applicationId desc"
    CHANGETYPE = "changeType"
    CHANGETYPEDESC = "changeType desc"
    CLIENTSTATE = "clientState"
    CLIENTSTATEDESC = "clientState desc"
    CREATORID = "creatorId"
    CREATORIDDESC = "creatorId desc"
    ENCRYPTIONCERTIFICATE = "encryptionCertificate"
    ENCRYPTIONCERTIFICATEDESC = "encryptionCertificate desc"
    ENCRYPTIONCERTIFICATEID = "encryptionCertificateId"
    ENCRYPTIONCERTIFICATEIDDESC = "encryptionCertificateId desc"
    EXPIRATIONDATETIME = "expirationDateTime"
    EXPIRATIONDATETIMEDESC = "expirationDateTime desc"
    INCLUDERESOURCEDATA = "includeResourceData"
    INCLUDERESOURCEDATADESC = "includeResourceData desc"
    LATESTSUPPORTEDTLSVERSION = "latestSupportedTlsVersion"
    LATESTSUPPORTEDTLSVERSIONDESC = "latestSupportedTlsVersion desc"
    LIFECYCLENOTIFICATIONURL = "lifecycleNotificationUrl"
    LIFECYCLENOTIFICATIONURLDESC = "lifecycleNotificationUrl desc"
    NOTIFICATIONURL = "notificationUrl"
    NOTIFICATIONURLDESC = "notificationUrl desc"
    RESOURCE = "resource"
    RESOURCEDESC = "resource desc"

class Get6itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPLICATIONID = "applicationId"
    CHANGETYPE = "changeType"
    CLIENTSTATE = "clientState"
    CREATORID = "creatorId"
    ENCRYPTIONCERTIFICATE = "encryptionCertificate"
    ENCRYPTIONCERTIFICATEID = "encryptionCertificateId"
    EXPIRATIONDATETIME = "expirationDateTime"
    INCLUDERESOURCEDATA = "includeResourceData"
    LATESTSUPPORTEDTLSVERSION = "latestSupportedTlsVersion"
    LIFECYCLENOTIFICATIONURL = "lifecycleNotificationUrl"
    NOTIFICATIONURL = "notificationUrl"
    RESOURCE = "resource"
