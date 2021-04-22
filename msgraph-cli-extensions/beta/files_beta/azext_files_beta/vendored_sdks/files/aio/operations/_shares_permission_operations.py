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
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class SharesPermissionOperations:
    """SharesPermissionOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~files.models
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

    async def grant(
        self,
        shared_drive_item_id: str,
        body: "models.Paths1Mcxy93SharesShareddriveitemIdPermissionMicrosoftGraphGrantPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> List["models.MicrosoftGraphPermission"]:
        """Invoke action grant.

        Invoke action grant.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param body: Action parameters.
        :type body: ~files.models.Paths1Mcxy93SharesShareddriveitemIdPermissionMicrosoftGraphGrantPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphPermission, or the result of cls(response)
        :rtype: list[~files.models.MicrosoftGraphPermission]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphPermission"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.grant.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1Mcxy93SharesShareddriveitemIdPermissionMicrosoftGraphGrantPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphPermission]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    grant.metadata = {'url': '/shares/{sharedDriveItem-id}/permission/microsoft.graph.grant'}  # type: ignore

    async def revoke_grants(
        self,
        shared_drive_item_id: str,
        body: "models.Paths50Xy75SharesShareddriveitemIdPermissionMicrosoftGraphRevokegrantsPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> "models.MicrosoftGraphPermission":
        """Invoke action revokeGrants.

        Invoke action revokeGrants.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param body: Action parameters.
        :type body: ~files.models.Paths50Xy75SharesShareddriveitemIdPermissionMicrosoftGraphRevokegrantsPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPermission, or the result of cls(response)
        :rtype: ~files.models.MicrosoftGraphPermission
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPermission"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.revoke_grants.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths50Xy75SharesShareddriveitemIdPermissionMicrosoftGraphRevokegrantsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPermission', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    revoke_grants.metadata = {'url': '/shares/{sharedDriveItem-id}/permission/microsoft.graph.revokeGrants'}  # type: ignore
