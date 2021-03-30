# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class UserOnlineMeetingOperations:
    """UserOnlineMeetingOperations async operations.

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

    async def create_or_get(
        self,
        user_id: str,
        chat_info: Optional["models.MicrosoftGraphChatInfo"] = None,
        end_date_time: Optional[datetime.datetime] = None,
        external_id: Optional[str] = None,
        start_date_time: Optional[datetime.datetime] = None,
        subject: Optional[str] = None,
        attendees: Optional[List["models.MicrosoftGraphMeetingParticipantInfo"]] = None,
        organizer: Optional["models.MicrosoftGraphMeetingParticipantInfo"] = None,
        **kwargs
    ) -> "models.MicrosoftGraphOnlineMeeting":
        """Invoke action createOrGet.

        Invoke action createOrGet.

        :param user_id: key: id of user.
        :type user_id: str
        :param chat_info: chatInfo.
        :type chat_info: ~users_actions.models.MicrosoftGraphChatInfo
        :param end_date_time:
        :type end_date_time: ~datetime.datetime
        :param external_id:
        :type external_id: str
        :param start_date_time:
        :type start_date_time: ~datetime.datetime
        :param subject:
        :type subject: str
        :param attendees:
        :type attendees: list[~users_actions.models.MicrosoftGraphMeetingParticipantInfo]
        :param organizer: meetingParticipantInfo.
        :type organizer: ~users_actions.models.MicrosoftGraphMeetingParticipantInfo
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnlineMeeting, or the result of cls(response)
        :rtype: ~users_actions.models.MicrosoftGraphOnlineMeeting
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnlineMeeting"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.Paths1H47062UsersUserIdOnlinemeetingsMicrosoftGraphCreateorgetPostRequestbodyContentApplicationJsonSchema(chat_info=chat_info, end_date_time=end_date_time, external_id=external_id, start_date_time=start_date_time, subject=subject, attendees=attendees, organizer=organizer)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_get.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1H47062UsersUserIdOnlinemeetingsMicrosoftGraphCreateorgetPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOnlineMeeting', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_get.metadata = {'url': '/users/{user-id}/onlineMeetings/microsoft.graph.createOrGet'}  # type: ignore