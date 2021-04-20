# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, IO, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class shareslistactivitiesOperations:
    """shareslistactivitiesOperations async operations.

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

    async def get_drive_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        select: Optional[List[Union[str, "models.Enum259"]]] = None,
        expand: Optional[List[Union[str, "models.Enum260"]]] = None,
        **kwargs
    ) -> "models.microsoftgraphdriveitem":
        """Get driveItem from shares.

        Get driveItem from shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~files.models.Enum259]
        :param expand: Expand related entities.
        :type expand: list[str or ~files.models.Enum260]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphdriveitem, or the result of cls(response)
        :rtype: ~files.models.microsoftgraphdriveitem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphdriveitem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_drive_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
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

        deserialized = self._deserialize('microsoftgraphdriveitem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_drive_item.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/driveItem'}  # type: ignore

    async def update_drive_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        body: "models.microsoftgraphdriveitem",
        **kwargs
    ) -> None:
        """Update the navigation property driveItem in shares.

        Update the navigation property driveItem in shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param body: New navigation property values.
        :type body: ~files.models.microsoftgraphdriveitem
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
        url = self.update_drive_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphdriveitem')
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

    update_drive_item.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/driveItem'}  # type: ignore

    async def delete_drive_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property driveItem for shares.

        Delete navigation property driveItem for shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
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
        url = self.delete_drive_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
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

    delete_drive_item.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/driveItem'}  # type: ignore

    async def get_drive_item_content(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        **kwargs
    ) -> IO:
        """Get media content for the navigation property driveItem from shares.

        Get media content for the navigation property driveItem from shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/octet-stream, application/json"

        # Construct URL
        url = self.get_drive_item_content.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_drive_item_content.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/driveItem/content'}  # type: ignore

    async def set_drive_item_content(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        data: IO,
        **kwargs
    ) -> None:
        """Update media content for the navigation property driveItem in shares.

        Update media content for the navigation property driveItem in shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param data: New media content.
        :type data: IO
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
        content_type = kwargs.pop("content_type", "application/octet-stream")
        accept = "application/json"

        # Construct URL
        url = self.set_drive_item_content.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs['stream_content'] = data
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    set_drive_item_content.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/driveItem/content'}  # type: ignore

    async def get_list_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        select: Optional[List[Union[str, "models.Enum261"]]] = None,
        expand: Optional[List[Union[str, "models.Enum262"]]] = None,
        **kwargs
    ) -> "models.microsoftgraphlistitem":
        """Get listItem from shares.

        Get listItem from shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~files.models.Enum261]
        :param expand: Expand related entities.
        :type expand: list[str or ~files.models.Enum262]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphlistitem, or the result of cls(response)
        :rtype: ~files.models.microsoftgraphlistitem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphlistitem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_list_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
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

        deserialized = self._deserialize('microsoftgraphlistitem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_list_item.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/listItem'}  # type: ignore

    async def update_list_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        body: "models.microsoftgraphlistitem",
        **kwargs
    ) -> None:
        """Update the navigation property listItem in shares.

        Update the navigation property listItem in shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param body: New navigation property values.
        :type body: ~files.models.microsoftgraphlistitem
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
        url = self.update_list_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphlistitem')
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

    update_list_item.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/listItem'}  # type: ignore

    async def delete_list_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property listItem for shares.

        Delete navigation property listItem for shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
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
        url = self.delete_list_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
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

    delete_list_item.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/listItem'}  # type: ignore
