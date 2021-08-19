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

class GroupsEventsCalendarEventsOperations:
    """GroupsEventsCalendarEventsOperations async operations.

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

    async def accept(
        self,
        group_id: str,
        event_id: str,
        event_id1: str,
        body: "models.Paths1Mk1Xt2GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphAcceptPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> None:
        """Invoke action accept.

        Invoke action accept.

        :param group_id: key: id of group.
        :type group_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param body: Action parameters.
        :type body: ~groups.models.Paths1Mk1Xt2GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphAcceptPostRequestbodyContentApplicationJsonSchema
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
        url = self.accept.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1Mk1Xt2GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphAcceptPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    accept.metadata = {'url': '/groups/{group-id}/events/{event-id}/calendar/events/{event-id1}/microsoft.graph.accept'}  # type: ignore

    async def cancel(
        self,
        group_id: str,
        event_id: str,
        event_id1: str,
        body: "models.PathsQmqltlGroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphCancelPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> None:
        """Invoke action cancel.

        Invoke action cancel.

        :param group_id: key: id of group.
        :type group_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param body: Action parameters.
        :type body: ~groups.models.PathsQmqltlGroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphCancelPostRequestbodyContentApplicationJsonSchema
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
        url = self.cancel.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsQmqltlGroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphCancelPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    cancel.metadata = {'url': '/groups/{group-id}/events/{event-id}/calendar/events/{event-id1}/microsoft.graph.cancel'}  # type: ignore

    async def decline(
        self,
        group_id: str,
        event_id: str,
        event_id1: str,
        body: "models.Paths12Xjrs6GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphDeclinePostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> None:
        """Invoke action decline.

        Invoke action decline.

        :param group_id: key: id of group.
        :type group_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param body: Action parameters.
        :type body: ~groups.models.Paths12Xjrs6GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphDeclinePostRequestbodyContentApplicationJsonSchema
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
        url = self.decline.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths12Xjrs6GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphDeclinePostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    decline.metadata = {'url': '/groups/{group-id}/events/{event-id}/calendar/events/{event-id1}/microsoft.graph.decline'}  # type: ignore

    async def dismiss_reminder(
        self,
        group_id: str,
        event_id: str,
        event_id1: str,
        **kwargs
    ) -> None:
        """Invoke action dismissReminder.

        Invoke action dismissReminder.

        :param group_id: key: id of group.
        :type group_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
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
        url = self.dismiss_reminder.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
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

    dismiss_reminder.metadata = {'url': '/groups/{group-id}/events/{event-id}/calendar/events/{event-id1}/microsoft.graph.dismissReminder'}  # type: ignore

    async def forward(
        self,
        group_id: str,
        event_id: str,
        event_id1: str,
        body: "models.PathsOltky4GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphForwardPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> None:
        """Invoke action forward.

        Invoke action forward.

        :param group_id: key: id of group.
        :type group_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param body: Action parameters.
        :type body: ~groups.models.PathsOltky4GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphForwardPostRequestbodyContentApplicationJsonSchema
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
        url = self.forward.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsOltky4GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphForwardPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    forward.metadata = {'url': '/groups/{group-id}/events/{event-id}/calendar/events/{event-id1}/microsoft.graph.forward'}  # type: ignore

    async def snooze_reminder(
        self,
        group_id: str,
        event_id: str,
        event_id1: str,
        body: "models.Paths1Wci047GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphSnoozereminderPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> None:
        """Invoke action snoozeReminder.

        Invoke action snoozeReminder.

        :param group_id: key: id of group.
        :type group_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param body: Action parameters.
        :type body: ~groups.models.Paths1Wci047GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphSnoozereminderPostRequestbodyContentApplicationJsonSchema
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
        url = self.snooze_reminder.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1Wci047GroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphSnoozereminderPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    snooze_reminder.metadata = {'url': '/groups/{group-id}/events/{event-id}/calendar/events/{event-id1}/microsoft.graph.snoozeReminder'}  # type: ignore

    async def tentatively_accept(
        self,
        group_id: str,
        event_id: str,
        event_id1: str,
        body: "models.Paths1J1NfgGroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphTentativelyacceptPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> None:
        """Invoke action tentativelyAccept.

        Invoke action tentativelyAccept.

        :param group_id: key: id of group.
        :type group_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param body: Action parameters.
        :type body: ~groups.models.Paths1J1NfgGroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphTentativelyacceptPostRequestbodyContentApplicationJsonSchema
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
        url = self.tentatively_accept.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1J1NfgGroupsGroupIdEventsEventIdCalendarEventsEventId1MicrosoftGraphTentativelyacceptPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    tentatively_accept.metadata = {'url': '/groups/{group-id}/events/{event-id}/calendar/events/{event-id1}/microsoft.graph.tentativelyAccept'}  # type: ignore

    async def delta(
        self,
        group_id: str,
        event_id: str,
        **kwargs
    ) -> List["models.MicrosoftGraphEvent"]:
        """Invoke function delta.

        Invoke function delta.

        :param group_id: key: id of group.
        :type group_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphEvent, or the result of cls(response)
        :rtype: list[~groups.models.MicrosoftGraphEvent]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphEvent"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delta.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
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

        deserialized = self._deserialize('[MicrosoftGraphEvent]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delta.metadata = {'url': '/groups/{group-id}/events/{event-id}/calendar/events/microsoft.graph.delta()'}  # type: ignore
