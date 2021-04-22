# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CollectionOfActivityHistoryItem(msrest.serialization.Model):
    """Collection of activityHistoryItem.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param value:
    :type value: list[~cross_device_experiences.models.MicrosoftGraphActivityHistoryItem]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'value': {'key': 'value', 'type': '[MicrosoftGraphActivityHistoryItem]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfActivityHistoryItem, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfUserActivity(msrest.serialization.Model):
    """Collection of userActivity.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param value:
    :type value: list[~cross_device_experiences.models.MicrosoftGraphUserActivity]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'value': {'key': 'value', 'type': '[MicrosoftGraphUserActivity]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfUserActivity, self).__init__(**kwargs)
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


class MicrosoftGraphActivityHistoryItem(MicrosoftGraphEntity):
    """activityHistoryItem.

    :param id: Read-only.
    :type id: str
    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param active_duration_seconds: Optional. The duration of active user engagement. if not
     supplied, this is calculated from the startedDateTime and lastActiveDateTime.
    :type active_duration_seconds: int
    :param created_date_time: Set by the server. DateTime in UTC when the object was created on the
     server.
    :type created_date_time: ~datetime.datetime
    :param expiration_date_time: Optional. UTC DateTime when the historyItem will undergo hard-
     delete. Can be set by the client.
    :type expiration_date_time: ~datetime.datetime
    :param last_active_date_time: Optional. UTC DateTime when the historyItem (activity session)
     was last understood as active or finished - if null, historyItem status should be Ongoing.
    :type last_active_date_time: ~datetime.datetime
    :param last_modified_date_time: Set by the server. DateTime in UTC when the object was modified
     on the server.
    :type last_modified_date_time: ~datetime.datetime
    :param started_date_time: Required. UTC DateTime when the historyItem (activity session) was
     started. Required for timeline history.
    :type started_date_time: ~datetime.datetime
    :param status:  Possible values include: "active", "updated", "deleted", "ignored",
     "unknownFutureValue".
    :type status: str or ~cross_device_experiences.models.MicrosoftGraphStatus
    :param user_timezone: Optional. The timezone in which the user's device used to generate the
     activity was located at activity creation time. Values supplied as Olson IDs in order to
     support cross-platform representation.
    :type user_timezone: str
    :param activity: userActivity.
    :type activity: ~cross_device_experiences.models.MicrosoftGraphUserActivity
    """

    _validation = {
        'active_duration_seconds': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'active_duration_seconds': {'key': 'activeDurationSeconds', 'type': 'int'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'expiration_date_time': {'key': 'expirationDateTime', 'type': 'iso-8601'},
        'last_active_date_time': {'key': 'lastActiveDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'started_date_time': {'key': 'startedDateTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'user_timezone': {'key': 'userTimezone', 'type': 'str'},
        'activity': {'key': 'activity', 'type': 'MicrosoftGraphUserActivity'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphActivityHistoryItem, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.active_duration_seconds = kwargs.get('active_duration_seconds', None)
        self.created_date_time = kwargs.get('created_date_time', None)
        self.expiration_date_time = kwargs.get('expiration_date_time', None)
        self.last_active_date_time = kwargs.get('last_active_date_time', None)
        self.last_modified_date_time = kwargs.get('last_modified_date_time', None)
        self.started_date_time = kwargs.get('started_date_time', None)
        self.status = kwargs.get('status', None)
        self.user_timezone = kwargs.get('user_timezone', None)
        self.activity = kwargs.get('activity', None)


class MicrosoftGraphImageInfo(msrest.serialization.Model):
    """imageInfo.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param add_image_query: Optional; parameter used to indicate the server is able to render image
     dynamically in response to parameterization. For example – a high contrast image.
    :type add_image_query: bool
    :param alternate_text: Optional; alt-text accessible content for the image.
    :type alternate_text: str
    :param alternative_text:
    :type alternative_text: str
    :param icon_url: Optional; URI that points to an icon which represents the application used to
     generate the activity.
    :type icon_url: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'add_image_query': {'key': 'addImageQuery', 'type': 'bool'},
        'alternate_text': {'key': 'alternateText', 'type': 'str'},
        'alternative_text': {'key': 'alternativeText', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphImageInfo, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.add_image_query = kwargs.get('add_image_query', None)
        self.alternate_text = kwargs.get('alternate_text', None)
        self.alternative_text = kwargs.get('alternative_text', None)
        self.icon_url = kwargs.get('icon_url', None)


class MicrosoftGraphUserActivity(MicrosoftGraphEntity):
    """userActivity.

    :param id: Read-only.
    :type id: str
    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param activation_url: Required. URL used to launch the activity in the best native experience
     represented by the appId. Might launch a web-based app if no native app exists.
    :type activation_url: str
    :param activity_source_host: Required. URL for the domain representing the cross-platform
     identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or
     configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and
     is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain.
     For example: https://contoso.com or https://myapp.contoso.com but NOT
     https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per
     cross-platform app identity. For example, a separate file and domain is needed for Word vs.
     PowerPoint.
    :type activity_source_host: str
    :param app_activity_id: Required. The unique activity ID in the context of the app - supplied
     by caller and immutable thereafter.
    :type app_activity_id: str
    :param app_display_name: Optional. Short text description of the app used to generate the
     activity for use in cases when the app is not installed on the user’s local device.
    :type app_display_name: str
    :param content_info: Json.
    :type content_info: dict[str, object]
    :param content_url: Optional. Used in the event the content can be rendered outside of a native
     or web-based app experience (for example, a pointer to an item in an RSS feed).
    :type content_url: str
    :param created_date_time: Set by the server. DateTime in UTC when the object was created on the
     server.
    :type created_date_time: ~datetime.datetime
    :param expiration_date_time: Set by the server. DateTime in UTC when the object expired on the
     server.
    :type expiration_date_time: ~datetime.datetime
    :param fallback_url: Optional. URL used to launch the activity in a web-based app, if
     available.
    :type fallback_url: str
    :param last_modified_date_time: Set by the server. DateTime in UTC when the object was modified
     on the server.
    :type last_modified_date_time: ~datetime.datetime
    :param status:  Possible values include: "active", "updated", "deleted", "ignored",
     "unknownFutureValue".
    :type status: str or ~cross_device_experiences.models.MicrosoftGraphStatus
    :param user_timezone: Optional. The timezone in which the user's device used to generate the
     activity was located at activity creation time; values supplied as Olson IDs in order to
     support cross-platform representation.
    :type user_timezone: str
    :param visual_elements: visualInfo.
    :type visual_elements: ~cross_device_experiences.models.MicrosoftGraphVisualInfo
    :param history_items: Optional. NavigationProperty/Containment; navigation property to the
     activity's historyItems.
    :type history_items: list[~cross_device_experiences.models.MicrosoftGraphActivityHistoryItem]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'activation_url': {'key': 'activationUrl', 'type': 'str'},
        'activity_source_host': {'key': 'activitySourceHost', 'type': 'str'},
        'app_activity_id': {'key': 'appActivityId', 'type': 'str'},
        'app_display_name': {'key': 'appDisplayName', 'type': 'str'},
        'content_info': {'key': 'contentInfo', 'type': '{object}'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'expiration_date_time': {'key': 'expirationDateTime', 'type': 'iso-8601'},
        'fallback_url': {'key': 'fallbackUrl', 'type': 'str'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'user_timezone': {'key': 'userTimezone', 'type': 'str'},
        'visual_elements': {'key': 'visualElements', 'type': 'MicrosoftGraphVisualInfo'},
        'history_items': {'key': 'historyItems', 'type': '[MicrosoftGraphActivityHistoryItem]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphUserActivity, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.activation_url = kwargs.get('activation_url', None)
        self.activity_source_host = kwargs.get('activity_source_host', None)
        self.app_activity_id = kwargs.get('app_activity_id', None)
        self.app_display_name = kwargs.get('app_display_name', None)
        self.content_info = kwargs.get('content_info', None)
        self.content_url = kwargs.get('content_url', None)
        self.created_date_time = kwargs.get('created_date_time', None)
        self.expiration_date_time = kwargs.get('expiration_date_time', None)
        self.fallback_url = kwargs.get('fallback_url', None)
        self.last_modified_date_time = kwargs.get('last_modified_date_time', None)
        self.status = kwargs.get('status', None)
        self.user_timezone = kwargs.get('user_timezone', None)
        self.visual_elements = kwargs.get('visual_elements', None)
        self.history_items = kwargs.get('history_items', None)


class MicrosoftGraphVisualInfo(msrest.serialization.Model):
    """visualInfo.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param attribution: imageInfo.
    :type attribution: ~cross_device_experiences.models.MicrosoftGraphImageInfo
    :param background_color: Optional. Background color used to render the activity in the UI -
     brand color for the application source of the activity. Must be a valid hex color.
    :type background_color: str
    :param content: Json.
    :type content: dict[str, object]
    :param description: Optional. Longer text description of the user's unique activity (example:
     document name, first sentence, and/or metadata).
    :type description: str
    :param display_text: Required. Short text description of the user's unique activity (for
     example, document name in cases where an activity refers to document creation).
    :type display_text: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'attribution': {'key': 'attribution', 'type': 'MicrosoftGraphImageInfo'},
        'background_color': {'key': 'backgroundColor', 'type': 'str'},
        'content': {'key': 'content', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'display_text': {'key': 'displayText', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphVisualInfo, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.attribution = kwargs.get('attribution', None)
        self.background_color = kwargs.get('background_color', None)
        self.content = kwargs.get('content', None)
        self.description = kwargs.get('description', None)
        self.display_text = kwargs.get('display_text', None)


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param error: Required.
    :type error: ~cross_device_experiences.models.OdataErrorMain
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
    :type details: list[~cross_device_experiences.models.OdataErrorDetail]
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
