# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import DevicesCorporateManagementConfiguration
from .operations import DeviceAppManagementDeviceAppManagementOperations
from .operations import DeviceAppManagementOperations
from .operations import DeviceAppManagementAndroidManagedAppProtectionsOperations
from .operations import DeviceAppManagementDefaultManagedAppProtectionsOperations
from .operations import DeviceAppManagementIosManagedAppProtectionsOperations
from .operations import DeviceAppManagementManagedAppPoliciesOperations
from .operations import DeviceAppManagementManagedAppRegistrationsOperations
from .operations import DeviceAppManagementManagedAppRegistrationsAppliedPoliciesOperations
from .operations import DeviceAppManagementManagedAppRegistrationsIntendedPoliciesOperations
from .operations import DeviceAppManagementManagedEBooksOperations
from .operations import DeviceAppManagementManagedEBooksUserStateSummaryOperations
from .operations import DeviceAppManagementMobileAppConfigurationsOperations
from .operations import DeviceAppManagementMobileAppsOperations
from .operations import DeviceAppManagementTargetedManagedAppConfigurationsOperations
from .operations import DeviceAppManagementVppTokensOperations
from .operations import UsersOperations
from .operations import UsersManagedDevicesOperations
from .. import models


class DevicesCorporateManagement(object):
    """DevicesCorporateManagement.

    :ivar device_app_management_device_app_management: DeviceAppManagementDeviceAppManagementOperations operations
    :vartype device_app_management_device_app_management: devices_corporate_management.aio.operations.DeviceAppManagementDeviceAppManagementOperations
    :ivar device_app_management: DeviceAppManagementOperations operations
    :vartype device_app_management: devices_corporate_management.aio.operations.DeviceAppManagementOperations
    :ivar device_app_management_android_managed_app_protections: DeviceAppManagementAndroidManagedAppProtectionsOperations operations
    :vartype device_app_management_android_managed_app_protections: devices_corporate_management.aio.operations.DeviceAppManagementAndroidManagedAppProtectionsOperations
    :ivar device_app_management_default_managed_app_protections: DeviceAppManagementDefaultManagedAppProtectionsOperations operations
    :vartype device_app_management_default_managed_app_protections: devices_corporate_management.aio.operations.DeviceAppManagementDefaultManagedAppProtectionsOperations
    :ivar device_app_management_ios_managed_app_protections: DeviceAppManagementIosManagedAppProtectionsOperations operations
    :vartype device_app_management_ios_managed_app_protections: devices_corporate_management.aio.operations.DeviceAppManagementIosManagedAppProtectionsOperations
    :ivar device_app_management_managed_app_policies: DeviceAppManagementManagedAppPoliciesOperations operations
    :vartype device_app_management_managed_app_policies: devices_corporate_management.aio.operations.DeviceAppManagementManagedAppPoliciesOperations
    :ivar device_app_management_managed_app_registrations: DeviceAppManagementManagedAppRegistrationsOperations operations
    :vartype device_app_management_managed_app_registrations: devices_corporate_management.aio.operations.DeviceAppManagementManagedAppRegistrationsOperations
    :ivar device_app_management_managed_app_registrations_applied_policies: DeviceAppManagementManagedAppRegistrationsAppliedPoliciesOperations operations
    :vartype device_app_management_managed_app_registrations_applied_policies: devices_corporate_management.aio.operations.DeviceAppManagementManagedAppRegistrationsAppliedPoliciesOperations
    :ivar device_app_management_managed_app_registrations_intended_policies: DeviceAppManagementManagedAppRegistrationsIntendedPoliciesOperations operations
    :vartype device_app_management_managed_app_registrations_intended_policies: devices_corporate_management.aio.operations.DeviceAppManagementManagedAppRegistrationsIntendedPoliciesOperations
    :ivar device_app_management_managed_ebooks: DeviceAppManagementManagedEBooksOperations operations
    :vartype device_app_management_managed_ebooks: devices_corporate_management.aio.operations.DeviceAppManagementManagedEBooksOperations
    :ivar device_app_management_managed_ebooks_user_state_summary: DeviceAppManagementManagedEBooksUserStateSummaryOperations operations
    :vartype device_app_management_managed_ebooks_user_state_summary: devices_corporate_management.aio.operations.DeviceAppManagementManagedEBooksUserStateSummaryOperations
    :ivar device_app_management_mobile_app_configurations: DeviceAppManagementMobileAppConfigurationsOperations operations
    :vartype device_app_management_mobile_app_configurations: devices_corporate_management.aio.operations.DeviceAppManagementMobileAppConfigurationsOperations
    :ivar device_app_management_mobile_apps: DeviceAppManagementMobileAppsOperations operations
    :vartype device_app_management_mobile_apps: devices_corporate_management.aio.operations.DeviceAppManagementMobileAppsOperations
    :ivar device_app_management_targeted_managed_app_configurations: DeviceAppManagementTargetedManagedAppConfigurationsOperations operations
    :vartype device_app_management_targeted_managed_app_configurations: devices_corporate_management.aio.operations.DeviceAppManagementTargetedManagedAppConfigurationsOperations
    :ivar device_app_management_vpp_tokens: DeviceAppManagementVppTokensOperations operations
    :vartype device_app_management_vpp_tokens: devices_corporate_management.aio.operations.DeviceAppManagementVppTokensOperations
    :ivar users: UsersOperations operations
    :vartype users: devices_corporate_management.aio.operations.UsersOperations
    :ivar users_managed_devices: UsersManagedDevicesOperations operations
    :vartype users_managed_devices: devices_corporate_management.aio.operations.UsersManagedDevicesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param top: Show only the first n items.
    :type top: int
    :param skip: Skip the first n items.
    :type skip: int
    :param search: Search items by search phrases.
    :type search: str
    :param filter: Filter items by property values.
    :type filter: str
    :param count: Include count of items.
    :type count: bool
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = DevicesCorporateManagementConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.device_app_management_device_app_management = DeviceAppManagementDeviceAppManagementOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management = DeviceAppManagementOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_android_managed_app_protections = DeviceAppManagementAndroidManagedAppProtectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_default_managed_app_protections = DeviceAppManagementDefaultManagedAppProtectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_ios_managed_app_protections = DeviceAppManagementIosManagedAppProtectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_policies = DeviceAppManagementManagedAppPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_registrations = DeviceAppManagementManagedAppRegistrationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_registrations_applied_policies = DeviceAppManagementManagedAppRegistrationsAppliedPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_registrations_intended_policies = DeviceAppManagementManagedAppRegistrationsIntendedPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_ebooks = DeviceAppManagementManagedEBooksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_ebooks_user_state_summary = DeviceAppManagementManagedEBooksUserStateSummaryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_mobile_app_configurations = DeviceAppManagementMobileAppConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_mobile_apps = DeviceAppManagementMobileAppsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_targeted_managed_app_configurations = DeviceAppManagementTargetedManagedAppConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_vpp_tokens = DeviceAppManagementVppTokensOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users = UsersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_managed_devices = UsersManagedDevicesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DevicesCorporateManagement":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)