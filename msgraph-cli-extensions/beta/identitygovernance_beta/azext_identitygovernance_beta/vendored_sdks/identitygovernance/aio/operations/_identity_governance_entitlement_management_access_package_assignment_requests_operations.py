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

class IdentityGovernanceEntitlementManagementAccessPackageAssignmentRequestsOperations:
    """IdentityGovernanceEntitlementManagementAccessPackageAssignmentRequestsOperations async operations.

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
        access_package_assignment_request_id: str,
        select: Optional[List[Union[str, "models.Enum167"]]] = None,
        expand: Optional[List[Union[str, "models.Enum168"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphAccessPackage":
        """Get accessPackage from identityGovernance.

        Get accessPackage from identityGovernance.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum167]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_governance.models.Enum168]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphAccessPackage, or the result of cls(response)
        :rtype: ~identity_governance.models.MicrosoftGraphAccessPackage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphAccessPackage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_access_package.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphAccessPackage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_access_package.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/accessPackage'}  # type: ignore

    async def get_ref_access_package(
        self,
        access_package_assignment_request_id: str,
        **kwargs
    ) -> str:
        """Get ref of accessPackage from identityGovernance.

        Get ref of accessPackage from identityGovernance.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
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
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
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
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_ref_access_package.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/accessPackage/$ref'}  # type: ignore

    async def set_ref_access_package(
        self,
        access_package_assignment_request_id: str,
        body: Dict[str, object],
        **kwargs
    ) -> None:
        """Update the ref of navigation property accessPackage in identityGovernance.

        Update the ref of navigation property accessPackage in identityGovernance.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
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
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
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
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    set_ref_access_package.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/accessPackage/$ref'}  # type: ignore

    async def delete_ref_access_package(
        self,
        access_package_assignment_request_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete ref of navigation property accessPackage for identityGovernance.

        Delete ref of navigation property accessPackage for identityGovernance.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
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
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
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

    delete_ref_access_package.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/accessPackage/$ref'}  # type: ignore

    async def get_access_package_assignment(
        self,
        access_package_assignment_request_id: str,
        select: Optional[List[Union[str, "models.Enum169"]]] = None,
        expand: Optional[List[Union[str, "models.Enum170"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphAccessPackageAssignment":
        """Get accessPackageAssignment from identityGovernance.

        Get accessPackageAssignment from identityGovernance.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum169]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_governance.models.Enum170]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphAccessPackageAssignment, or the result of cls(response)
        :rtype: ~identity_governance.models.MicrosoftGraphAccessPackageAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphAccessPackageAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_access_package_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphAccessPackageAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_access_package_assignment.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/accessPackageAssignment'}  # type: ignore

    async def update_access_package_assignment(
        self,
        access_package_assignment_request_id: str,
        body: "models.MicrosoftGraphAccessPackageAssignment",
        **kwargs
    ) -> None:
        """Update the navigation property accessPackageAssignment in identityGovernance.

        Update the navigation property accessPackageAssignment in identityGovernance.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
        :param body: New navigation property values.
        :type body: ~identity_governance.models.MicrosoftGraphAccessPackageAssignment
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
        url = self.update_access_package_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphAccessPackageAssignment')
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

    update_access_package_assignment.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/accessPackageAssignment'}  # type: ignore

    async def delete_access_package_assignment(
        self,
        access_package_assignment_request_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property accessPackageAssignment for identityGovernance.

        Delete navigation property accessPackageAssignment for identityGovernance.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
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
        url = self.delete_access_package_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
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

    delete_access_package_assignment.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/accessPackageAssignment'}  # type: ignore

    async def cancel(
        self,
        access_package_assignment_request_id: str,
        **kwargs
    ) -> None:
        """Invoke action Cancel.

        Invoke action Cancel.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
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
        url = self.cancel.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    cancel.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/microsoft.graph.Cancel'}  # type: ignore

    async def get_requestor(
        self,
        access_package_assignment_request_id: str,
        select: Optional[List[Union[str, "models.Enum450"]]] = None,
        expand: Optional[List[Union[str, "models.Enum451"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphAccessPackageSubject":
        """Get requestor from identityGovernance.

        Get requestor from identityGovernance.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum450]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_governance.models.Enum451]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphAccessPackageSubject, or the result of cls(response)
        :rtype: ~identity_governance.models.MicrosoftGraphAccessPackageSubject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphAccessPackageSubject"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_requestor.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphAccessPackageSubject', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_requestor.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/requestor'}  # type: ignore

    async def update_requestor(
        self,
        access_package_assignment_request_id: str,
        body: "models.MicrosoftGraphAccessPackageSubject",
        **kwargs
    ) -> None:
        """Update the navigation property requestor in identityGovernance.

        Update the navigation property requestor in identityGovernance.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
        :param body: New navigation property values.
        :type body: ~identity_governance.models.MicrosoftGraphAccessPackageSubject
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
        url = self.update_requestor.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphAccessPackageSubject')
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

    update_requestor.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/requestor'}  # type: ignore

    async def delete_requestor(
        self,
        access_package_assignment_request_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property requestor for identityGovernance.

        Delete navigation property requestor for identityGovernance.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
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
        url = self.delete_requestor.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
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

    delete_requestor.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/requestor'}  # type: ignore

    async def my(
        self,
        **kwargs
    ) -> List["models.MicrosoftGraphAccessPackageAssignmentRequest"]:
        """Invoke function My.

        Invoke function My.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphAccessPackageAssignmentRequest, or the result of cls(response)
        :rtype: list[~identity_governance.models.MicrosoftGraphAccessPackageAssignmentRequest]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphAccessPackageAssignmentRequest"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.my.metadata['url']  # type: ignore

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
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphAccessPackageAssignmentRequest]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    my.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/microsoft.graph.My()'}  # type: ignore
