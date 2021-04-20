# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class usersactivitiesOperations:
    """usersactivitiesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~cross_device_experiences.models
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

    def list_history_items(
        self,
        user_id: str,
        user_activity_id: str,
        orderby: Optional[List[Union[str, "models.Enum6"]]] = None,
        select: Optional[List[Union[str, "models.Enum7"]]] = None,
        expand: Optional[List[Union[str, "models.Get9itemsitem"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.collectionofactivityhistoryitem"]:
        """Get historyItems from users.

        Get historyItems from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_activity_id: key: id of userActivity.
        :type user_activity_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~cross_device_experiences.models.Enum6]
        :param select: Select properties to be returned.
        :type select: list[str or ~cross_device_experiences.models.Enum7]
        :param expand: Expand related entities.
        :type expand: list[str or ~cross_device_experiences.models.Get9itemsitem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either collectionofactivityhistoryitem or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~cross_device_experiences.models.collectionofactivityhistoryitem]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.collectionofactivityhistoryitem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_history_items.metadata['url']  # type: ignore
                path_format_arguments = {
                    'user-id': self._serialize.url("user_id", user_id, 'str'),
                    'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('collectionofactivityhistoryitem', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.odataerror, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_history_items.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems'}  # type: ignore

    async def create_history_items(
        self,
        user_id: str,
        user_activity_id: str,
        body: "models.microsoftgraphactivityhistoryitem",
        **kwargs
    ) -> "models.microsoftgraphactivityhistoryitem":
        """Create new navigation property to historyItems for users.

        Create new navigation property to historyItems for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_activity_id: key: id of userActivity.
        :type user_activity_id: str
        :param body: New navigation property.
        :type body: ~cross_device_experiences.models.microsoftgraphactivityhistoryitem
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphactivityhistoryitem, or the result of cls(response)
        :rtype: ~cross_device_experiences.models.microsoftgraphactivityhistoryitem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphactivityhistoryitem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_history_items.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphactivityhistoryitem')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphactivityhistoryitem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_history_items.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems'}  # type: ignore

    async def get_history_items(
        self,
        user_id: str,
        user_activity_id: str,
        activity_history_item_id: str,
        select: Optional[List[Union[str, "models.Enum9"]]] = None,
        expand: Optional[List[Union[str, "models.Get4itemsitem"]]] = None,
        **kwargs
    ) -> "models.microsoftgraphactivityhistoryitem":
        """Get historyItems from users.

        Get historyItems from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_activity_id: key: id of userActivity.
        :type user_activity_id: str
        :param activity_history_item_id: key: id of activityHistoryItem.
        :type activity_history_item_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~cross_device_experiences.models.Enum9]
        :param expand: Expand related entities.
        :type expand: list[str or ~cross_device_experiences.models.Get4itemsitem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphactivityhistoryitem, or the result of cls(response)
        :rtype: ~cross_device_experiences.models.microsoftgraphactivityhistoryitem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphactivityhistoryitem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_history_items.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
            'activityHistoryItem-id': self._serialize.url("activity_history_item_id", activity_history_item_id, 'str'),
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

        deserialized = self._deserialize('microsoftgraphactivityhistoryitem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_history_items.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems/{activityHistoryItem-id}'}  # type: ignore

    async def update_history_items(
        self,
        user_id: str,
        user_activity_id: str,
        activity_history_item_id: str,
        body: "models.microsoftgraphactivityhistoryitem",
        **kwargs
    ) -> None:
        """Update the navigation property historyItems in users.

        Update the navigation property historyItems in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_activity_id: key: id of userActivity.
        :type user_activity_id: str
        :param activity_history_item_id: key: id of activityHistoryItem.
        :type activity_history_item_id: str
        :param body: New navigation property values.
        :type body: ~cross_device_experiences.models.microsoftgraphactivityhistoryitem
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
        url = self.update_history_items.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
            'activityHistoryItem-id': self._serialize.url("activity_history_item_id", activity_history_item_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphactivityhistoryitem')
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

    update_history_items.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems/{activityHistoryItem-id}'}  # type: ignore

    async def delete_history_items(
        self,
        user_id: str,
        user_activity_id: str,
        activity_history_item_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property historyItems for users.

        Delete navigation property historyItems for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_activity_id: key: id of userActivity.
        :type user_activity_id: str
        :param activity_history_item_id: key: id of activityHistoryItem.
        :type activity_history_item_id: str
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
        url = self.delete_history_items.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
            'activityHistoryItem-id': self._serialize.url("activity_history_item_id", activity_history_item_id, 'str'),
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

    delete_history_items.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems/{activityHistoryItem-id}'}  # type: ignore
