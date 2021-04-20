# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class teamsprimarychannelmessagesrepliesOperations(object):
    """teamsprimarychannelmessagesrepliesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~teams.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def delta(
        self,
        team_id,  # type: str
        chat_message_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.microsoftgraphchatmessage"]
        """Invoke function delta.

        Invoke function delta.

        :param team_id: key: id of team.
        :type team_id: str
        :param chat_message_id: key: id of chatMessage.
        :type chat_message_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of microsoftgraphchatmessage, or the result of cls(response)
        :rtype: list[~teams.models.microsoftgraphchatmessage]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.microsoftgraphchatmessage"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delta.metadata['url']  # type: ignore
        path_format_arguments = {
            'team-id': self._serialize.url("team_id", team_id, 'str'),
            'chatMessage-id': self._serialize.url("chat_message_id", chat_message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('[microsoftgraphchatmessage]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delta.metadata = {'url': '/teams/{team-id}/primaryChannel/messages/{chatMessage-id}/replies/microsoft.graph.delta()'}  # type: ignore
