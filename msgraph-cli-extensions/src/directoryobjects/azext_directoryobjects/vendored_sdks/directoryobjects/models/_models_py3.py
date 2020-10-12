# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CollectionOfDirectoryObject(msrest.serialization.Model):
    """Collection of directoryObject.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param value:
    :type value: list[~directory_objects.models.MicrosoftGraphDirectoryObject]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'value': {'key': 'value', 'type': '[MicrosoftGraphDirectoryObject]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        value: Optional[List["MicrosoftGraphDirectoryObject"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfDirectoryObject, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.value = value
        self.odata_next_link = odata_next_link


class MicrosoftGraphEntity(msrest.serialization.Model):
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
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id


class MicrosoftGraphDirectoryObject(MicrosoftGraphEntity):
    """Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.

    :param id: Read-only.
    :type id: str
    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param deleted_date_time:
    :type deleted_date_time: ~datetime.datetime
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'deleted_date_time': {'key': 'deletedDateTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        additional_properties: Optional[Dict[str, object]] = None,
        deleted_date_time: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(MicrosoftGraphDirectoryObject, self).__init__(id=id, **kwargs)
        self.additional_properties = additional_properties
        self.deleted_date_time = deleted_date_time


class MicrosoftGraphExtensionProperty(MicrosoftGraphDirectoryObject):
    """Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param id: Read-only.
    :type id: str
    :param deleted_date_time:
    :type deleted_date_time: ~datetime.datetime
    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param app_display_name: Display name of the application object on which this extension
     property is defined. Read-only.
    :type app_display_name: str
    :param data_type: Specifies the data type of the value the extension property can hold.
     Following values are supported. Not nullable. Binary - 256 bytes maximumBooleanDateTime - Must
     be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger -
     64-bit value.String - 256 characters maximum.
    :type data_type: str
    :param is_synced_from_on_premises: Indicates if this extension property was sycned from
     onpremises directory using Azure AD Connect. Read-only.
    :type is_synced_from_on_premises: bool
    :param name: Name of the extension property. Not nullable.
    :type name: str
    :param target_objects: Following values are supported. Not nullable.
     UserGroupOrganizationDeviceApplication.
    :type target_objects: list[str]
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'str'},
        'deleted_date_time': {'key': 'deletedDateTime', 'type': 'iso-8601'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'app_display_name': {'key': 'appDisplayName', 'type': 'str'},
        'data_type': {'key': 'dataType', 'type': 'str'},
        'is_synced_from_on_premises': {'key': 'isSyncedFromOnPremises', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'target_objects': {'key': 'targetObjects', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        id: Optional[str] = None,
        deleted_date_time: Optional[datetime.datetime] = None,
        additional_properties: Optional[Dict[str, object]] = None,
        app_display_name: Optional[str] = None,
        data_type: Optional[str] = None,
        is_synced_from_on_premises: Optional[bool] = None,
        name: Optional[str] = None,
        target_objects: Optional[List[str]] = None,
        **kwargs
    ):
        super(MicrosoftGraphExtensionProperty, self).__init__(id=id, deleted_date_time=deleted_date_time, **kwargs)
        self.additional_properties = additional_properties
        self.additional_properties = additional_properties
        self.app_display_name = app_display_name
        self.data_type = data_type
        self.is_synced_from_on_premises = is_synced_from_on_premises
        self.name = name
        self.target_objects = target_objects


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param error: Required.
    :type error: ~directory_objects.models.OdataErrorMain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'error': {'key': 'error', 'type': 'OdataErrorMain'},
    }

    def __init__(
        self,
        *,
        error: "OdataErrorMain",
        additional_properties: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.error = error


class OdataErrorDetail(msrest.serialization.Model):
    """OdataErrorDetail.

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
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message
        self.target = target


class OdataErrorMain(msrest.serialization.Model):
    """OdataErrorMain.

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
    :type details: list[~directory_objects.models.OdataErrorDetail]
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
        'details': {'key': 'details', 'type': '[OdataErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': '{object}'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        additional_properties: Optional[Dict[str, object]] = None,
        target: Optional[str] = None,
        details: Optional[List["OdataErrorDetail"]] = None,
        innererror: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror


class Paths15Et6VvDirectoryobjectsDirectoryobjectIdMicrosoftGraphGetmembergroupsPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model):
    """Paths15Et6VvDirectoryobjectsDirectoryobjectIdMicrosoftGraphGetmembergroupsPostRequestbodyContentApplicationJsonSchema.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param security_enabled_only:
    :type security_enabled_only: bool
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'security_enabled_only': {'key': 'securityEnabledOnly', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        security_enabled_only: Optional[bool] = False,
        **kwargs
    ):
        super(Paths15Et6VvDirectoryobjectsDirectoryobjectIdMicrosoftGraphGetmembergroupsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.security_enabled_only = security_enabled_only


class Paths16Hhl7EDirectoryobjectsDirectoryobjectIdMicrosoftGraphGetmemberobjectsPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model):
    """Paths16Hhl7EDirectoryobjectsDirectoryobjectIdMicrosoftGraphGetmemberobjectsPostRequestbodyContentApplicationJsonSchema.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param security_enabled_only:
    :type security_enabled_only: bool
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'security_enabled_only': {'key': 'securityEnabledOnly', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        security_enabled_only: Optional[bool] = False,
        **kwargs
    ):
        super(Paths16Hhl7EDirectoryobjectsDirectoryobjectIdMicrosoftGraphGetmemberobjectsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.security_enabled_only = security_enabled_only


class Paths1B1K3OoDirectoryobjectsDirectoryobjectIdMicrosoftGraphCheckmemberobjectsPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model):
    """Paths1B1K3OoDirectoryobjectsDirectoryobjectIdMicrosoftGraphCheckmemberobjectsPostRequestbodyContentApplicationJsonSchema.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param ids:
    :type ids: list[str]
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'ids': {'key': 'ids', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        ids: Optional[List[str]] = None,
        **kwargs
    ):
        super(Paths1B1K3OoDirectoryobjectsDirectoryobjectIdMicrosoftGraphCheckmemberobjectsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.ids = ids


class Paths1Ffes6MDirectoryobjectsDirectoryobjectIdMicrosoftGraphCheckmembergroupsPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model):
    """Paths1Ffes6MDirectoryobjectsDirectoryobjectIdMicrosoftGraphCheckmembergroupsPostRequestbodyContentApplicationJsonSchema.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param group_ids:
    :type group_ids: list[str]
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'group_ids': {'key': 'groupIds', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        group_ids: Optional[List[str]] = None,
        **kwargs
    ):
        super(Paths1Ffes6MDirectoryobjectsDirectoryobjectIdMicrosoftGraphCheckmembergroupsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.group_ids = group_ids


class Paths1Izu2OlDirectoryobjectsMicrosoftGraphGetavailableextensionpropertiesPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model):
    """Paths1Izu2OlDirectoryobjectsMicrosoftGraphGetavailableextensionpropertiesPostRequestbodyContentApplicationJsonSchema.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param is_synced_from_on_premises:
    :type is_synced_from_on_premises: bool
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'is_synced_from_on_premises': {'key': 'isSyncedFromOnPremises', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        is_synced_from_on_premises: Optional[bool] = False,
        **kwargs
    ):
        super(Paths1Izu2OlDirectoryobjectsMicrosoftGraphGetavailableextensionpropertiesPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.is_synced_from_on_premises = is_synced_from_on_premises


class Paths1Re7RfDirectoryobjectsMicrosoftGraphValidatepropertiesPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model):
    """Paths1Re7RfDirectoryobjectsMicrosoftGraphValidatepropertiesPostRequestbodyContentApplicationJsonSchema.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param entity_type:
    :type entity_type: str
    :param display_name:
    :type display_name: str
    :param mail_nickname:
    :type mail_nickname: str
    :param on_behalf_of_user_id:
    :type on_behalf_of_user_id: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'entity_type': {'key': 'entityType', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'mail_nickname': {'key': 'mailNickname', 'type': 'str'},
        'on_behalf_of_user_id': {'key': 'onBehalfOfUserId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        entity_type: Optional[str] = None,
        display_name: Optional[str] = None,
        mail_nickname: Optional[str] = None,
        on_behalf_of_user_id: Optional[str] = None,
        **kwargs
    ):
        super(Paths1Re7RfDirectoryobjectsMicrosoftGraphValidatepropertiesPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.entity_type = entity_type
        self.display_name = display_name
        self.mail_nickname = mail_nickname
        self.on_behalf_of_user_id = on_behalf_of_user_id


class PathsG5Xp0HDirectoryobjectsMicrosoftGraphGetbyidsPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model):
    """PathsG5Xp0HDirectoryobjectsMicrosoftGraphGetbyidsPostRequestbodyContentApplicationJsonSchema.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param ids:
    :type ids: list[str]
    :param types:
    :type types: list[str]
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'ids': {'key': 'ids', 'type': '[str]'},
        'types': {'key': 'types', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        ids: Optional[List[str]] = None,
        types: Optional[List[str]] = None,
        **kwargs
    ):
        super(PathsG5Xp0HDirectoryobjectsMicrosoftGraphGetbyidsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.ids = ids
        self.types = types
