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

from ._configuration_async import IdentityDirectoryManagementConfiguration
from .operations_async import ContactOrgContactOperations
from .operations_async import ContactOperations
from .operations_async import ContractContractOperations
from .operations_async import ContractOperations
from .operations_async import DeviceDeviceOperations
from .operations_async import DeviceOperations
from .operations_async import DirectoryDirectoryOperations
from .operations_async import DirectoryOperations
from .operations_async import DirectoryAdministrativeUnitOperations
from .operations_async import DirectoryRoleDirectoryRoleOperations
from .operations_async import DirectoryRoleOperations
from .operations_async import DirectoryRoleTemplateDirectoryRoleTemplateOperations
from .operations_async import DirectoryRoleTemplateOperations
from .operations_async import DomainDomainOperations
from .operations_async import DomainOperations
from .operations_async import OrganizationOrganizationOperations
from .operations_async import OrganizationOperations
from .operations_async import SubscribedSkuSubscribedSkuOperations
from .operations_async import UserOperations
from .. import models


class IdentityDirectoryManagement(object):
    """IdentityDirectoryManagement.

    :ivar contact_org_contact: ContactOrgContactOperations operations
    :vartype contact_org_contact: identity_directory_management.aio.operations_async.ContactOrgContactOperations
    :ivar contact: ContactOperations operations
    :vartype contact: identity_directory_management.aio.operations_async.ContactOperations
    :ivar contract_contract: ContractContractOperations operations
    :vartype contract_contract: identity_directory_management.aio.operations_async.ContractContractOperations
    :ivar contract: ContractOperations operations
    :vartype contract: identity_directory_management.aio.operations_async.ContractOperations
    :ivar device_device: DeviceDeviceOperations operations
    :vartype device_device: identity_directory_management.aio.operations_async.DeviceDeviceOperations
    :ivar device: DeviceOperations operations
    :vartype device: identity_directory_management.aio.operations_async.DeviceOperations
    :ivar directory_directory: DirectoryDirectoryOperations operations
    :vartype directory_directory: identity_directory_management.aio.operations_async.DirectoryDirectoryOperations
    :ivar directory: DirectoryOperations operations
    :vartype directory: identity_directory_management.aio.operations_async.DirectoryOperations
    :ivar directory_administrative_unit: DirectoryAdministrativeUnitOperations operations
    :vartype directory_administrative_unit: identity_directory_management.aio.operations_async.DirectoryAdministrativeUnitOperations
    :ivar directory_role_directory_role: DirectoryRoleDirectoryRoleOperations operations
    :vartype directory_role_directory_role: identity_directory_management.aio.operations_async.DirectoryRoleDirectoryRoleOperations
    :ivar directory_role: DirectoryRoleOperations operations
    :vartype directory_role: identity_directory_management.aio.operations_async.DirectoryRoleOperations
    :ivar directory_role_template_directory_role_template: DirectoryRoleTemplateDirectoryRoleTemplateOperations operations
    :vartype directory_role_template_directory_role_template: identity_directory_management.aio.operations_async.DirectoryRoleTemplateDirectoryRoleTemplateOperations
    :ivar directory_role_template: DirectoryRoleTemplateOperations operations
    :vartype directory_role_template: identity_directory_management.aio.operations_async.DirectoryRoleTemplateOperations
    :ivar domain_domain: DomainDomainOperations operations
    :vartype domain_domain: identity_directory_management.aio.operations_async.DomainDomainOperations
    :ivar domain: DomainOperations operations
    :vartype domain: identity_directory_management.aio.operations_async.DomainOperations
    :ivar organization_organization: OrganizationOrganizationOperations operations
    :vartype organization_organization: identity_directory_management.aio.operations_async.OrganizationOrganizationOperations
    :ivar organization: OrganizationOperations operations
    :vartype organization: identity_directory_management.aio.operations_async.OrganizationOperations
    :ivar subscribed_sku_subscribed_sku: SubscribedSkuSubscribedSkuOperations operations
    :vartype subscribed_sku_subscribed_sku: identity_directory_management.aio.operations_async.SubscribedSkuSubscribedSkuOperations
    :ivar user: UserOperations operations
    :vartype user: identity_directory_management.aio.operations_async.UserOperations
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
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
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
        self._config = IdentityDirectoryManagementConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.contact_org_contact = ContactOrgContactOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.contact = ContactOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.contract_contract = ContractContractOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.contract = ContractOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_device = DeviceDeviceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device = DeviceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.directory_directory = DirectoryDirectoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.directory = DirectoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.directory_administrative_unit = DirectoryAdministrativeUnitOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.directory_role_directory_role = DirectoryRoleDirectoryRoleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.directory_role = DirectoryRoleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.directory_role_template_directory_role_template = DirectoryRoleTemplateDirectoryRoleTemplateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.directory_role_template = DirectoryRoleTemplateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.domain_domain = DomainDomainOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.domain = DomainOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.organization_organization = OrganizationOrganizationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.organization = OrganizationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscribed_sku_subscribed_sku = SubscribedSkuSubscribedSkuOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "IdentityDirectoryManagement":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)