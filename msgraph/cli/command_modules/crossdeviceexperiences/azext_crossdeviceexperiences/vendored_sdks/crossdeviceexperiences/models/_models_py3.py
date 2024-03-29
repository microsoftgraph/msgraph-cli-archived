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

from ._cross_device_experiences_enums import *


class collectionofactivityhistoryitem(msrest.serialization.Model):
    """Collection of activityHistoryItem.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param value:
    :type value: list[~cross_device_experiences.models.microsoftgraphactivityhistoryitem]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'value': {'key': 'value', 'type': '[microsoftgraphactivityhistoryitem]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        value: Optional[List["microsoftgraphactivityhistoryitem"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(collectionofactivityhistoryitem, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.value = value
        self.odata_next_link = odata_next_link


class collectionofuseractivity(msrest.serialization.Model):
    """Collection of userActivity.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param value:
    :type value: list[~cross_device_experiences.models.microsoftgraphuseractivity]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'value': {'key': 'value', 'type': '[microsoftgraphuseractivity]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        value: Optional[List["microsoftgraphuseractivity"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(collectionofuseractivity, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.value = value
        self.odata_next_link = odata_next_link


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


class microsoftgraphactivityhistoryitem(microsoftgraphentity):
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
    :type status: str or ~cross_device_experiences.models.Microsoftgraphstatus
    :param user_timezone: Optional. The timezone in which the user's device used to generate the
     activity was located at activity creation time. Values supplied as Olson IDs in order to
     support cross-platform representation.
    :type user_timezone: str
    :param activity: userActivity.
    :type activity: ~cross_device_experiences.models.microsoftgraphuseractivity
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
        'activity': {'key': 'activity', 'type': 'microsoftgraphuseractivity'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        additional_properties: Optional[Dict[str, object]] = None,
        active_duration_seconds: Optional[int] = None,
        created_date_time: Optional[datetime.datetime] = None,
        expiration_date_time: Optional[datetime.datetime] = None,
        last_active_date_time: Optional[datetime.datetime] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        started_date_time: Optional[datetime.datetime] = None,
        status: Optional[Union[str, "Microsoftgraphstatus"]] = None,
        user_timezone: Optional[str] = None,
        activity: Optional["microsoftgraphuseractivity"] = None,
        **kwargs
    ):
        super(microsoftgraphactivityhistoryitem, self).__init__(id=id, **kwargs)
        self.additional_properties = additional_properties
        self.active_duration_seconds = active_duration_seconds
        self.created_date_time = created_date_time
        self.expiration_date_time = expiration_date_time
        self.last_active_date_time = last_active_date_time
        self.last_modified_date_time = last_modified_date_time
        self.started_date_time = started_date_time
        self.status = status
        self.user_timezone = user_timezone
        self.activity = activity


class microsoftgraphimageinfo(msrest.serialization.Model):
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
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        add_image_query: Optional[bool] = None,
        alternate_text: Optional[str] = None,
        alternative_text: Optional[str] = None,
        icon_url: Optional[str] = None,
        **kwargs
    ):
        super(microsoftgraphimageinfo, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.add_image_query = add_image_query
        self.alternate_text = alternate_text
        self.alternative_text = alternative_text
        self.icon_url = icon_url


class microsoftgraphuseractivity(microsoftgraphentity):
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
    :type status: str or ~cross_device_experiences.models.Microsoftgraphstatus
    :param user_timezone: Optional. The timezone in which the user's device used to generate the
     activity was located at activity creation time; values supplied as Olson IDs in order to
     support cross-platform representation.
    :type user_timezone: str
    :param visual_elements: visualInfo.
    :type visual_elements: ~cross_device_experiences.models.microsoftgraphvisualinfo
    :param history_items: Optional. NavigationProperty/Containment; navigation property to the
     activity's historyItems.
    :type history_items: list[~cross_device_experiences.models.microsoftgraphactivityhistoryitem]
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
        'visual_elements': {'key': 'visualElements', 'type': 'microsoftgraphvisualinfo'},
        'history_items': {'key': 'historyItems', 'type': '[microsoftgraphactivityhistoryitem]'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        additional_properties: Optional[Dict[str, object]] = None,
        activation_url: Optional[str] = None,
        activity_source_host: Optional[str] = None,
        app_activity_id: Optional[str] = None,
        app_display_name: Optional[str] = None,
        content_info: Optional[Dict[str, object]] = None,
        content_url: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
        expiration_date_time: Optional[datetime.datetime] = None,
        fallback_url: Optional[str] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        status: Optional[Union[str, "Microsoftgraphstatus"]] = None,
        user_timezone: Optional[str] = None,
        visual_elements: Optional["microsoftgraphvisualinfo"] = None,
        history_items: Optional[List["microsoftgraphactivityhistoryitem"]] = None,
        **kwargs
    ):
        super(microsoftgraphuseractivity, self).__init__(id=id, **kwargs)
        self.additional_properties = additional_properties
        self.activation_url = activation_url
        self.activity_source_host = activity_source_host
        self.app_activity_id = app_activity_id
        self.app_display_name = app_display_name
        self.content_info = content_info
        self.content_url = content_url
        self.created_date_time = created_date_time
        self.expiration_date_time = expiration_date_time
        self.fallback_url = fallback_url
        self.last_modified_date_time = last_modified_date_time
        self.status = status
        self.user_timezone = user_timezone
        self.visual_elements = visual_elements
        self.history_items = history_items


class microsoftgraphvisualinfo(msrest.serialization.Model):
    """visualInfo.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param attribution: imageInfo.
    :type attribution: ~cross_device_experiences.models.microsoftgraphimageinfo
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
        'attribution': {'key': 'attribution', 'type': 'microsoftgraphimageinfo'},
        'background_color': {'key': 'backgroundColor', 'type': 'str'},
        'content': {'key': 'content', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'display_text': {'key': 'displayText', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        attribution: Optional["microsoftgraphimageinfo"] = None,
        background_color: Optional[str] = None,
        content: Optional[Dict[str, object]] = None,
        description: Optional[str] = None,
        display_text: Optional[str] = None,
        **kwargs
    ):
        super(microsoftgraphvisualinfo, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.attribution = attribution
        self.background_color = background_color
        self.content = content
        self.description = description
        self.display_text = display_text


class odataerror(msrest.serialization.Model):
    """odataerror.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param error: Required.
    :type error: ~cross_device_experiences.models.odataerrormain
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
    :type details: list[~cross_device_experiences.models.odataerrordetail]
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
