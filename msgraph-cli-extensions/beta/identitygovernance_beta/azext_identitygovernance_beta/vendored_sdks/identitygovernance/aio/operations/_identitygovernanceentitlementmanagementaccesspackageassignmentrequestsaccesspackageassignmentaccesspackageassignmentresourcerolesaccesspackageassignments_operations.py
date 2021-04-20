# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class identitygovernanceentitlementmanagementaccesspackageassignmentrequestsaccesspackageassignmentaccesspackageassignmentresourcerolesaccesspackageassignmentsOperations:
    """identitygovernanceentitlementmanagementaccesspackageassignmentrequestsaccesspackageassignmentaccesspackageassignmentresourcerolesaccesspackageassignmentsOperations async operations.

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

    async def my(
        self,
        access_package_assignment_request_id: str,
        access_package_assignment_resource_role_id: str,
        **kwargs
    ) -> List["models.microsoftgraphaccesspackageassignment"]:
        """Invoke function My.

        Invoke function My.

        :param access_package_assignment_request_id: key: id of accessPackageAssignmentRequest.
        :type access_package_assignment_request_id: str
        :param access_package_assignment_resource_role_id: key: id of
         accessPackageAssignmentResourceRole.
        :type access_package_assignment_resource_role_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of microsoftgraphaccesspackageassignment, or the result of cls(response)
        :rtype: list[~identity_governance.models.microsoftgraphaccesspackageassignment]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.microsoftgraphaccesspackageassignment"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.my.metadata['url']  # type: ignore
        path_format_arguments = {
            'accessPackageAssignmentRequest-id': self._serialize.url("access_package_assignment_request_id", access_package_assignment_request_id, 'str'),
            'accessPackageAssignmentResourceRole-id': self._serialize.url("access_package_assignment_resource_role_id", access_package_assignment_resource_role_id, 'str'),
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

        deserialized = self._deserialize('[microsoftgraphaccesspackageassignment]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    my.metadata = {'url': '/identityGovernance/entitlementManagement/accessPackageAssignmentRequests/{accessPackageAssignmentRequest-id}/accessPackageAssignment/accessPackageAssignmentResourceRoles/{accessPackageAssignmentResourceRole-id}/accessPackageAssignments/microsoft.graph.My()'}  # type: ignore