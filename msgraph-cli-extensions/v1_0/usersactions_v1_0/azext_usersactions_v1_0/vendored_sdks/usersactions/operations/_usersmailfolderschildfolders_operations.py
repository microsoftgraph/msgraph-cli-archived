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
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class usersmailfolderschildfoldersOperations(object):
    """usersmailfolderschildfoldersOperations operations.

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

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def copy(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        mail_folder_id1,  # type: str
        body,  # type: "models.paths1e02jcusersuseridmailfoldersmailfolderidchildfoldersmailfolderid1microsoftgraphcopypostrequestbodycontentapplicationjsonschema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphmailfolder"
        """Invoke action copy.

        Invoke action copy.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param mail_folder_id1: key: id of mailFolder.
        :type mail_folder_id1: str
        :param body: Action parameters.
        :type body: ~users_actions.models.paths1e02jcusersuseridmailfoldersmailfolderidchildfoldersmailfolderid1microsoftgraphcopypostrequestbodycontentapplicationjsonschema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphmailfolder, or the result of cls(response)
        :rtype: ~users_actions.models.microsoftgraphmailfolder
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphmailfolder"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.copy.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'mailFolder-id1': self._serialize.url("mail_folder_id1", mail_folder_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'paths1e02jcusersuseridmailfoldersmailfolderidchildfoldersmailfolderid1microsoftgraphcopypostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphmailfolder', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    copy.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/childFolders/{mailFolder-id1}/microsoft.graph.copy'}  # type: ignore

    def move(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        mail_folder_id1,  # type: str
        body,  # type: "models.paths1ekxa5vusersuseridmailfoldersmailfolderidchildfoldersmailfolderid1microsoftgraphmovepostrequestbodycontentapplicationjsonschema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphmailfolder"
        """Invoke action move.

        Invoke action move.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param mail_folder_id1: key: id of mailFolder.
        :type mail_folder_id1: str
        :param body: Action parameters.
        :type body: ~users_actions.models.paths1ekxa5vusersuseridmailfoldersmailfolderidchildfoldersmailfolderid1microsoftgraphmovepostrequestbodycontentapplicationjsonschema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphmailfolder, or the result of cls(response)
        :rtype: ~users_actions.models.microsoftgraphmailfolder
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphmailfolder"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.move.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'mailFolder-id1': self._serialize.url("mail_folder_id1", mail_folder_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'paths1ekxa5vusersuseridmailfoldersmailfolderidchildfoldersmailfolderid1microsoftgraphmovepostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphmailfolder', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    move.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/childFolders/{mailFolder-id1}/microsoft.graph.move'}  # type: ignore
