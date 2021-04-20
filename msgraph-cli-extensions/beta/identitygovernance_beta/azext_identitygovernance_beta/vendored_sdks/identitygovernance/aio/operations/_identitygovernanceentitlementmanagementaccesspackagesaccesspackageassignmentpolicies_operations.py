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

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class identitygovernanceentitlementmanagementaccesspackagesaccesspackageassignmentpoliciesOperations:
    """identitygovernanceentitlementmanagementaccesspackagesaccesspackageassignmentpoliciesOperations async operations.

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

    async def get_access_package(
        self,
        access_package_id: str,
        access_package_assignment_policy_id: str,
        select: Optional[List[Union[str, "models.Enum1230"]]] = None,
        expand: Optional[List[Union[str, "models.Enum1231"]]] = None,
        **kwargs
    ) -> "models.microsoftgraphaccesspackage":
        """Get accessPackage from identityGovernance.

        Get accessPackage from identityGovernance.

        :param access_package_id: key: id of accessPackage.
        :type access_package_id: str
        :param access_package_assignment_policy_id: key: id of accessPackageAssignmentPolicy.
        :type access_package_assignment_policy_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum1230]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_governance.models.Enum1231]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphaccesspackage, or the result of cls(response)
        :rtype: ~identity_governance.models.microsoftgraphaccesspackage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphaccesspackage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_access_package.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackage-id': self._serialize.url("access_package_id", access_package_id, 'str'),
            'accessPackageAssignmentPolicy-id': self._serialize.url("access_package_assignment_policy_id", access_package_assignment_policy_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphaccesspackage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_access_package.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackages/{accessPackage-id}/accessPackageAssignmentPolicies/{accessPackageAssignmentPolicy-id}/accessPackage'}  # type: ignore

    async def get_ref_access_package(
        self,
        access_package_id: str,
        access_package_assignment_policy_id: str,
        **kwargs
    ) -> str:
        """Get ref of accessPackage from identityGovernance.

        Get ref of accessPackage from identityGovernance.

        :param access_package_id: key: id of accessPackage.
        :type access_package_id: str
        :param access_package_assignment_policy_id: key: id of accessPackageAssignmentPolicy.
        :type access_package_assignment_policy_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[str]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_ref_access_package.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackage-id': self._serialize.url("access_package_id", access_package_id, 'str'),
            'accessPackageAssignmentPolicy-id': self._serialize.url("access_package_assignment_policy_id", access_package_assignment_policy_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_ref_access_package.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackages/{accessPackage-id}/accessPackageAssignmentPolicies/{accessPackageAssignmentPolicy-id}/accessPackage/$ref'}  # type: ignore

    async def set_ref_access_package(
        self,
        access_package_id: str,
        access_package_assignment_policy_id: str,
        body: Dict[str, object],
        **kwargs
    ) -> None:
        """Update the ref of navigation property accessPackage in identityGovernance.

        Update the ref of navigation property accessPackage in identityGovernance.

        :param access_package_id: key: id of accessPackage.
        :type access_package_id: str
        :param access_package_assignment_policy_id: key: id of accessPackageAssignmentPolicy.
        :type access_package_assignment_policy_id: str
        :param body: New navigation property ref values.
        :type body: dict[str, object]
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
        url = self.set_ref_access_package.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackage-id': self._serialize.url("access_package_id", access_package_id, 'str'),
            'accessPackageAssignmentPolicy-id': self._serialize.url("access_package_assignment_policy_id", access_package_assignment_policy_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, '{object}')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    set_ref_access_package.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackages/{accessPackage-id}/accessPackageAssignmentPolicies/{accessPackageAssignmentPolicy-id}/accessPackage/$ref'}  # type: ignore

    async def delete_ref_access_package(
        self,
        access_package_id: str,
        access_package_assignment_policy_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete ref of navigation property accessPackage for identityGovernance.

        Delete ref of navigation property accessPackage for identityGovernance.

        :param access_package_id: key: id of accessPackage.
        :type access_package_id: str
        :param access_package_assignment_policy_id: key: id of accessPackageAssignmentPolicy.
        :type access_package_assignment_policy_id: str
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
        url = self.delete_ref_access_package.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackage-id': self._serialize.url("access_package_id", access_package_id, 'str'),
            'accessPackageAssignmentPolicy-id': self._serialize.url("access_package_assignment_policy_id", access_package_assignment_policy_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_ref_access_package.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackages/{accessPackage-id}/accessPackageAssignmentPolicies/{accessPackageAssignmentPolicy-id}/accessPackage/$ref'}  # type: ignore

    async def get_access_package_catalog(
        self,
        access_package_id: str,
        access_package_assignment_policy_id: str,
        select: Optional[List[Union[str, "models.Enum1232"]]] = None,
        expand: Optional[List[Union[str, "models.Enum1233"]]] = None,
        **kwargs
    ) -> "models.microsoftgraphaccesspackagecatalog":
        """Get accessPackageCatalog from identityGovernance.

        Get accessPackageCatalog from identityGovernance.

        :param access_package_id: key: id of accessPackage.
        :type access_package_id: str
        :param access_package_assignment_policy_id: key: id of accessPackageAssignmentPolicy.
        :type access_package_assignment_policy_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum1232]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_governance.models.Enum1233]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphaccesspackagecatalog, or the result of cls(response)
        :rtype: ~identity_governance.models.microsoftgraphaccesspackagecatalog
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphaccesspackagecatalog"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_access_package_catalog.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackage-id': self._serialize.url("access_package_id", access_package_id, 'str'),
            'accessPackageAssignmentPolicy-id': self._serialize.url("access_package_assignment_policy_id", access_package_assignment_policy_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphaccesspackagecatalog', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_access_package_catalog.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackages/{accessPackage-id}/accessPackageAssignmentPolicies/{accessPackageAssignmentPolicy-id}/accessPackageCatalog'}  # type: ignore

    async def update_access_package_catalog(
        self,
        access_package_id: str,
        access_package_assignment_policy_id: str,
        body: "models.microsoftgraphaccesspackagecatalog",
        **kwargs
    ) -> None:
        """Update the navigation property accessPackageCatalog in identityGovernance.

        Update the navigation property accessPackageCatalog in identityGovernance.

        :param access_package_id: key: id of accessPackage.
        :type access_package_id: str
        :param access_package_assignment_policy_id: key: id of accessPackageAssignmentPolicy.
        :type access_package_assignment_policy_id: str
        :param body: New navigation property values.
        :type body: ~identity_governance.models.microsoftgraphaccesspackagecatalog
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
        url = self.update_access_package_catalog.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackage-id': self._serialize.url("access_package_id", access_package_id, 'str'),
            'accessPackageAssignmentPolicy-id': self._serialize.url("access_package_assignment_policy_id", access_package_assignment_policy_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphaccesspackagecatalog')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_access_package_catalog.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackages/{accessPackage-id}/accessPackageAssignmentPolicies/{accessPackageAssignmentPolicy-id}/accessPackageCatalog'}  # type: ignore

    async def delete_access_package_catalog(
        self,
        access_package_id: str,
        access_package_assignment_policy_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property accessPackageCatalog for identityGovernance.

        Delete navigation property accessPackageCatalog for identityGovernance.

        :param access_package_id: key: id of accessPackage.
        :type access_package_id: str
        :param access_package_assignment_policy_id: key: id of accessPackageAssignmentPolicy.
        :type access_package_assignment_policy_id: str
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
        url = self.delete_access_package_catalog.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackage-id': self._serialize.url("access_package_id", access_package_id, 'str'),
            'accessPackageAssignmentPolicy-id': self._serialize.url("access_package_assignment_policy_id", access_package_assignment_policy_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_access_package_catalog.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackages/{accessPackage-id}/accessPackageAssignmentPolicies/{accessPackageAssignmentPolicy-id}/accessPackageCatalog'}  # type: ignore
