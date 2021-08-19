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
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class GroupsConversationsOperations:
    """GroupsConversationsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~groups.models
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

    def list_threads(
        self,
        group_id: str,
        conversation_id: str,
        orderby: Optional[List[Union[str, "models.Enum87"]]] = None,
        select: Optional[List[Union[str, "models.Enum88"]]] = None,
        expand: Optional[List[Union[str, "models.Get9ItemsItem"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfConversationThread"]:
        """Get threads from groups.

        A collection of all the conversation threads in the conversation. A navigation property. Read-
        only. Nullable.

        :param group_id: key: id of group.
        :type group_id: str
        :param conversation_id: key: id of conversation.
        :type conversation_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~groups.models.Enum87]
        :param select: Select properties to be returned.
        :type select: list[str or ~groups.models.Enum88]
        :param expand: Expand related entities.
        :type expand: list[str or ~groups.models.Get9ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfConversationThread or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~groups.models.CollectionOfConversationThread]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfConversationThread"]
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
                url = self.list_threads.metadata['url']  # type: ignore
                path_format_arguments = {
                    'group-id': self._serialize.url("group_id", group_id, 'str'),
                    'conversation-id': self._serialize.url("conversation_id", conversation_id, 'str'),
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
            deserialized = self._deserialize('CollectionOfConversationThread', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_threads.metadata = {'url': '/groups/{group-id}/conversations/{conversation-id}/threads'}  # type: ignore

    async def create_threads(
        self,
        group_id: str,
        conversation_id: str,
        body: "models.MicrosoftGraphConversationThread",
        **kwargs
    ) -> "models.MicrosoftGraphConversationThread":
        """Create new navigation property to threads for groups.

        A collection of all the conversation threads in the conversation. A navigation property. Read-
        only. Nullable.

        :param group_id: key: id of group.
        :type group_id: str
        :param conversation_id: key: id of conversation.
        :type conversation_id: str
        :param body: New navigation property.
        :type body: ~groups.models.MicrosoftGraphConversationThread
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphConversationThread, or the result of cls(response)
        :rtype: ~groups.models.MicrosoftGraphConversationThread
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphConversationThread"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_threads.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'conversation-id': self._serialize.url("conversation_id", conversation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphConversationThread')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphConversationThread', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_threads.metadata = {'url': '/groups/{group-id}/conversations/{conversation-id}/threads'}  # type: ignore

    async def get_threads(
        self,
        group_id: str,
        conversation_id: str,
        conversation_thread_id: str,
        select: Optional[List[Union[str, "models.Enum90"]]] = None,
        expand: Optional[List[Union[str, "models.Get4ItemsItem"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphConversationThread":
        """Get threads from groups.

        A collection of all the conversation threads in the conversation. A navigation property. Read-
        only. Nullable.

        :param group_id: key: id of group.
        :type group_id: str
        :param conversation_id: key: id of conversation.
        :type conversation_id: str
        :param conversation_thread_id: key: id of conversationThread.
        :type conversation_thread_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~groups.models.Enum90]
        :param expand: Expand related entities.
        :type expand: list[str or ~groups.models.Get4ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphConversationThread, or the result of cls(response)
        :rtype: ~groups.models.MicrosoftGraphConversationThread
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphConversationThread"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_threads.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'conversation-id': self._serialize.url("conversation_id", conversation_id, 'str'),
            'conversationThread-id': self._serialize.url("conversation_thread_id", conversation_thread_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphConversationThread', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_threads.metadata = {'url': '/groups/{group-id}/conversations/{conversation-id}/threads/{conversationThread-id}'}  # type: ignore

    async def update_threads(
        self,
        group_id: str,
        conversation_id: str,
        conversation_thread_id: str,
        body: "models.MicrosoftGraphConversationThread",
        **kwargs
    ) -> None:
        """Update the navigation property threads in groups.

        A collection of all the conversation threads in the conversation. A navigation property. Read-
        only. Nullable.

        :param group_id: key: id of group.
        :type group_id: str
        :param conversation_id: key: id of conversation.
        :type conversation_id: str
        :param conversation_thread_id: key: id of conversationThread.
        :type conversation_thread_id: str
        :param body: New navigation property values.
        :type body: ~groups.models.MicrosoftGraphConversationThread
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
        url = self.update_threads.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'conversation-id': self._serialize.url("conversation_id", conversation_id, 'str'),
            'conversationThread-id': self._serialize.url("conversation_thread_id", conversation_thread_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphConversationThread')
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

    update_threads.metadata = {'url': '/groups/{group-id}/conversations/{conversation-id}/threads/{conversationThread-id}'}  # type: ignore

    async def delete_threads(
        self,
        group_id: str,
        conversation_id: str,
        conversation_thread_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property threads for groups.

        A collection of all the conversation threads in the conversation. A navigation property. Read-
        only. Nullable.

        :param group_id: key: id of group.
        :type group_id: str
        :param conversation_id: key: id of conversation.
        :type conversation_id: str
        :param conversation_thread_id: key: id of conversationThread.
        :type conversation_thread_id: str
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
        url = self.delete_threads.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'conversation-id': self._serialize.url("conversation_id", conversation_id, 'str'),
            'conversationThread-id': self._serialize.url("conversation_thread_id", conversation_thread_id, 'str'),
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

    delete_threads.metadata = {'url': '/groups/{group-id}/conversations/{conversation-id}/threads/{conversationThread-id}'}  # type: ignore
