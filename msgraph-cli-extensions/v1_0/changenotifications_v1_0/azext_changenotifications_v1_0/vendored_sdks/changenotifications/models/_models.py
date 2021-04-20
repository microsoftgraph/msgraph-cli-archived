# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class collectionofsubscription(msrest.serialization.Model):
    """Collection of subscription.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param value:
    :type value: list[~change_notifications.models.microsoftgraphsubscription]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'value': {'key': 'value', 'type': '[microsoftgraphsubscription]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(collectionofsubscription, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


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
        **kwargs
    ):
        super(microsoftgraphentity, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.id = kwargs.get('id', None)


class microsoftgraphsubscription(microsoftgraphentity):
    """subscription.

    :param id: Read-only.
    :type id: str
    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param application_id: Identifier of the application used to create the subscription. Read-
     only.
    :type application_id: str
    :param change_type: Required. Indicates the type of change in the subscribed resource that will
     raise a change notification. The supported values are: created, updated, deleted. Multiple
     values can be combined using a comma-separated list.Note: Drive root item and list change
     notifications support only the updated changeType. User and group change notifications support
     updated and deleted changeType.
    :type change_type: str
    :param client_state: Optional. Specifies the value of the clientState property sent by the
     service in each change notification. The maximum length is 128 characters. The client can check
     that the change notification came from the service by comparing the value of the clientState
     property sent with the subscription with the value of the clientState property received with
     each change notification.
    :type client_state: str
    :param creator_id: Identifier of the user or service principal that created the subscription.
     If the app used delegated permissions to create the subscription, this field contains the id of
     the signed-in user the app called on behalf of. If the app used application permissions, this
     field contains the id of the service principal corresponding to the app. Read-only.
    :type creator_id: str
    :param encryption_certificate: A base64-encoded representation of a certificate with a public
     key used to encrypt resource data in change notifications. Optional. Required when
     includeResourceData is true.
    :type encryption_certificate: str
    :param encryption_certificate_id: A custom app-provided identifier to help identify the
     certificate needed to decrypt resource data. Optional.
    :type encryption_certificate_id: str
    :param expiration_date_time: Required. Specifies the date and time when the webhook
     subscription expires. The time is in UTC, and can be an amount of time from subscription
     creation that varies for the resource subscribed to.  See the table below for maximum supported
     subscription length of time.
    :type expiration_date_time: ~datetime.datetime
    :param include_resource_data: When set to true, change notifications include resource data
     (such as content of a chat message). Optional.
    :type include_resource_data: bool
    :param latest_supported_tls_version:
    :type latest_supported_tls_version: str
    :param lifecycle_notification_url:
    :type lifecycle_notification_url: str
    :param notification_url: Required. The URL of the endpoint that will receive the change
     notifications. This URL must make use of the HTTPS protocol.
    :type notification_url: str
    :param resource: Required. Specifies the resource that will be monitored for changes. Do not
     include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values
     for each supported resource.
    :type resource: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'change_type': {'key': 'changeType', 'type': 'str'},
        'client_state': {'key': 'clientState', 'type': 'str'},
        'creator_id': {'key': 'creatorId', 'type': 'str'},
        'encryption_certificate': {'key': 'encryptionCertificate', 'type': 'str'},
        'encryption_certificate_id': {'key': 'encryptionCertificateId', 'type': 'str'},
        'expiration_date_time': {'key': 'expirationDateTime', 'type': 'iso-8601'},
        'include_resource_data': {'key': 'includeResourceData', 'type': 'bool'},
        'latest_supported_tls_version': {'key': 'latestSupportedTlsVersion', 'type': 'str'},
        'lifecycle_notification_url': {'key': 'lifecycleNotificationUrl', 'type': 'str'},
        'notification_url': {'key': 'notificationUrl', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(microsoftgraphsubscription, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.application_id = kwargs.get('application_id', None)
        self.change_type = kwargs.get('change_type', None)
        self.client_state = kwargs.get('client_state', None)
        self.creator_id = kwargs.get('creator_id', None)
        self.encryption_certificate = kwargs.get('encryption_certificate', None)
        self.encryption_certificate_id = kwargs.get('encryption_certificate_id', None)
        self.expiration_date_time = kwargs.get('expiration_date_time', None)
        self.include_resource_data = kwargs.get('include_resource_data', None)
        self.latest_supported_tls_version = kwargs.get('latest_supported_tls_version', None)
        self.lifecycle_notification_url = kwargs.get('lifecycle_notification_url', None)
        self.notification_url = kwargs.get('notification_url', None)
        self.resource = kwargs.get('resource', None)


class odataerror(msrest.serialization.Model):
    """odataerror.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param error: Required.
    :type error: ~change_notifications.models.odataerrormain
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
        **kwargs
    ):
        super(odataerror, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.error = kwargs['error']


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
        **kwargs
    ):
        super(odataerrordetail, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)


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
    :type details: list[~change_notifications.models.odataerrordetail]
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
        **kwargs
    ):
        super(odataerrormain, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.innererror = kwargs.get('innererror', None)
