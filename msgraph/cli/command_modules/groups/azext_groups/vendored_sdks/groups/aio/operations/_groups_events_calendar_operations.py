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

class GroupsEventsCalendarOperations:
    """GroupsEventsCalendarOperations async operations.

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

    async def allowed_calendar_sharing_roles(
        self,
        group_id: str,
        event_id: str,
        user: str,
        **kwargs
    ) -> List[Union[str, "models.MicrosoftGraphCalendarRoleType"]]:
        """Invoke function allowedCalendarSharingRoles.

        Invoke function allowedCalendarSharingRoles.

        :param group_id: key: id of group.
        :type group_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param user: Usage: User={User}.
        :type user: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphCalendarRoleType, or the result of cls(response)
        :rtype: list[str or ~groups.models.MicrosoftGraphCalendarRoleType]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[Union[str, "models.MicrosoftGraphCalendarRoleType"]]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.allowed_calendar_sharing_roles.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'User': self._serialize.url("user", user, 'str'),
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

        deserialized = self._deserialize('[str]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    allowed_calendar_sharing_roles.metadata = {'url': '/groups/{group-id}/events/{event-id}/calendar/microsoft.graph.allowedCalendarSharingRoles(User=\'{User}\')'}  # type: ignore

    async def get_schedule(
        self,
        group_id: str,
        event_id: str,
        body: "models.Paths1Kab48VGroupsGroupIdEventsEventIdCalendarMicrosoftGraphGetschedulePostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> List["models.MicrosoftGraphScheduleInformation"]:
        """Invoke action getSchedule.

        Invoke action getSchedule.

        :param group_id: key: id of group.
        :type group_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param body: Action parameters.
        :type body: ~groups.models.Paths1Kab48VGroupsGroupIdEventsEventIdCalendarMicrosoftGraphGetschedulePostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphScheduleInformation, or the result of cls(response)
        :rtype: list[~groups.models.MicrosoftGraphScheduleInformation]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphScheduleInformation"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.get_schedule.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1Kab48VGroupsGroupIdEventsEventIdCalendarMicrosoftGraphGetschedulePostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphScheduleInformation]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_schedule.metadata = {'url': '/groups/{group-id}/events/{event-id}/calendar/microsoft.graph.getSchedule'}  # type: ignore
