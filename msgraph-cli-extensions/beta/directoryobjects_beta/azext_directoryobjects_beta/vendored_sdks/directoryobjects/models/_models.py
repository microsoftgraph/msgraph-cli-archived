# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

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
        **kwargs
    ):
        super(CollectionOfDirectoryObject, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


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
        **kwargs
    ):
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.id = kwargs.get('id', None)


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
        **kwargs
    ):
        super(MicrosoftGraphDirectoryObject, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.deleted_date_time = kwargs.get('deleted_date_time', None)


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
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.error = kwargs['error']


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
        **kwargs
    ):
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)


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
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.innererror = kwargs.get('innererror', None)


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
        **kwargs
    ):
        super(Paths15Et6VvDirectoryobjectsDirectoryobjectIdMicrosoftGraphGetmembergroupsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.security_enabled_only = kwargs.get('security_enabled_only', False)


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
        **kwargs
    ):
        super(Paths16Hhl7EDirectoryobjectsDirectoryobjectIdMicrosoftGraphGetmemberobjectsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.security_enabled_only = kwargs.get('security_enabled_only', False)


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
        **kwargs
    ):
        super(Paths1B1K3OoDirectoryobjectsDirectoryobjectIdMicrosoftGraphCheckmemberobjectsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.ids = kwargs.get('ids', None)


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
        **kwargs
    ):
        super(Paths1Ffes6MDirectoryobjectsDirectoryobjectIdMicrosoftGraphCheckmembergroupsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.group_ids = kwargs.get('group_ids', None)


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
        **kwargs
    ):
        super(Paths1Re7RfDirectoryobjectsMicrosoftGraphValidatepropertiesPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.entity_type = kwargs.get('entity_type', None)
        self.display_name = kwargs.get('display_name', None)
        self.mail_nickname = kwargs.get('mail_nickname', None)
        self.on_behalf_of_user_id = kwargs.get('on_behalf_of_user_id', None)


class Paths50Tm3XDirectoryobjectsMicrosoftGraphGetuserownedobjectsPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model):
    """Paths50Tm3XDirectoryobjectsMicrosoftGraphGetuserownedobjectsPostRequestbodyContentApplicationJsonSchema.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param user_id:
    :type user_id: str
    :param type:
    :type type: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Paths50Tm3XDirectoryobjectsMicrosoftGraphGetuserownedobjectsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.user_id = kwargs.get('user_id', None)
        self.type = kwargs.get('type', None)


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
        **kwargs
    ):
        super(PathsG5Xp0HDirectoryobjectsMicrosoftGraphGetbyidsPostRequestbodyContentApplicationJsonSchema, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.ids = kwargs.get('ids', None)
        self.types = kwargs.get('types', None)