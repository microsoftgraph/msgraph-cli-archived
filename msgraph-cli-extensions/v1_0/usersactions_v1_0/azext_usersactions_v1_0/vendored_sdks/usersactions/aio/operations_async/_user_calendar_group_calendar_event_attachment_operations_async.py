# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class UserCalendarGroupCalendarEventAttachmentOperations:
    """UserCalendarGroupCalendarEventAttachmentOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_actions.models
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

    async def create_upload_session(
        self,
        user_id: str,
        calendar_group_id: str,
        calendar_id: str,
        event_id: str,
        attachment_item: Optional["models.MicrosoftGraphAttachmentItem"] = None,
        **kwargs
    ) -> "models.MicrosoftGraphUploadSession":
        """Invoke action createUploadSession.

        Invoke action createUploadSession.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param calendar_id: key: id of calendar.
        :type calendar_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param attachment_item: attachmentItem.
        :type attachment_item: ~users_actions.models.MicrosoftGraphAttachmentItem
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphUploadSession, or the result of cls(response)
        :rtype: ~users_actions.models.MicrosoftGraphUploadSession
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphUploadSession"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths15UmoapUsersUserIdCalendargroupsCalendargroupIdCalendarsCalendarIdEventsEventIdAttachmentsMicrosoftGraphCreateuploadsessionPostRequestbodyContentApplicationJsonSchema(attachment_item=attachment_item)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_upload_session.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
            'calendar-id': self._serialize.url("calendar_id", calendar_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths15UmoapUsersUserIdCalendargroupsCalendargroupIdCalendarsCalendarIdEventsEventIdAttachmentsMicrosoftGraphCreateuploadsessionPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphUploadSession', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_upload_session.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars/{calendar-id}/events/{event-id}/attachments/microsoft.graph.createUploadSession'}  # type: ignore
