# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class IdentityGovernanceEntitlementManagementAccessPackageCatalogsAccessPackagesAccessPackageResourceRoleScopesAccessPackageResourceScopeOperations:
    """IdentityGovernanceEntitlementManagementAccessPackageCatalogsAccessPackagesAccessPackageResourceRoleScopesAccessPackageResourceScopeOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_governance.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get_access_package_resource(
        self,
        access_package_catalog_id: str,
        access_package_id: str,
        access_package_resource_role_scope_id: str,
        select: Optional[List[Union[str, "models.Enum1139"]]] = None,
        expand: Optional[List[Union[str, "models.Enum1140"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphAccessPackageResource":
        """Get accessPackageResource from identityGovernance.

        Get accessPackageResource from identityGovernance.

        :param access_package_catalog_id: key: id of accessPackageCatalog.
        :type access_package_catalog_id: str
        :param access_package_id: key: id of accessPackage.
        :type access_package_id: str
        :param access_package_resource_role_scope_id: key: id of accessPackageResourceRoleScope.
        :type access_package_resource_role_scope_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum1139]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_governance.models.Enum1140]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphAccessPackageResource, or the result of cls(response)
        :rtype: ~identity_governance.models.MicrosoftGraphAccessPackageResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphAccessPackageResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_access_package_resource.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageCatalog-id': self._serialize.url("access_package_catalog_id", access_package_catalog_id, 'str'),
            'accessPackage-id': self._serialize.url("access_package_id", access_package_id, 'str'),
            'accessPackageResourceRoleScope-id': self._serialize.url("access_package_resource_role_scope_id", access_package_resource_role_scope_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphAccessPackageResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_access_package_resource.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageCatalogs/{accessPackageCatalog-id}/accessPackages/{accessPackage-id}/accessPackageResourceRoleScopes/{accessPackageResourceRoleScope-id}/accessPackageResourceScope/accessPackageResource'}  # type: ignore

    async def update_access_package_resource(
        self,
        access_package_catalog_id: str,
        access_package_id: str,
        access_package_resource_role_scope_id: str,
        body: "models.MicrosoftGraphAccessPackageResource",
        **kwargs
    ) -> None:
        """Update the navigation property accessPackageResource in identityGovernance.

        Update the navigation property accessPackageResource in identityGovernance.

        :param access_package_catalog_id: key: id of accessPackageCatalog.
        :type access_package_catalog_id: str
        :param access_package_id: key: id of accessPackage.
        :type access_package_id: str
        :param access_package_resource_role_scope_id: key: id of accessPackageResourceRoleScope.
        :type access_package_resource_role_scope_id: str
        :param body: New navigation property values.
        :type body: ~identity_governance.models.MicrosoftGraphAccessPackageResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_access_package_resource.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageCatalog-id': self._serialize.url("access_package_catalog_id", access_package_catalog_id, 'str'),
            'accessPackage-id': self._serialize.url("access_package_id", access_package_id, 'str'),
            'accessPackageResourceRoleScope-id': self._serialize.url("access_package_resource_role_scope_id", access_package_resource_role_scope_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphAccessPackageResource')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_access_package_resource.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageCatalogs/{accessPackageCatalog-id}/accessPackages/{accessPackage-id}/accessPackageResourceRoleScopes/{accessPackageResourceRoleScope-id}/accessPackageResourceScope/accessPackageResource'}  # type: ignore

    async def delete_access_package_resource(
        self,
        access_package_catalog_id: str,
        access_package_id: str,
        access_package_resource_role_scope_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property accessPackageResource for identityGovernance.

        Delete navigation property accessPackageResource for identityGovernance.

        :param access_package_catalog_id: key: id of accessPackageCatalog.
        :type access_package_catalog_id: str
        :param access_package_id: key: id of accessPackage.
        :type access_package_id: str
        :param access_package_resource_role_scope_id: key: id of accessPackageResourceRoleScope.
        :type access_package_resource_role_scope_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_access_package_resource.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageCatalog-id': self._serialize.url("access_package_catalog_id", access_package_catalog_id, 'str'),
            'accessPackage-id': self._serialize.url("access_package_id", access_package_id, 'str'),
            'accessPackageResourceRoleScope-id': self._serialize.url("access_package_resource_role_scope_id", access_package_resource_role_scope_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_access_package_resource.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageCatalogs/{accessPackageCatalog-id}/accessPackages/{accessPackage-id}/accessPackageResourceRoleScopes/{accessPackageResourceRoleScope-id}/accessPackageResourceScope/accessPackageResource'}  # type: ignore
