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
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UsersMailFoldersMessagesOperations(object):
    """UsersMailFoldersMessagesOperations operations.

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
        message_id,  # type: str
        body,  # type: "models.PathsDy94GcUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCopyPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphMessage"
        """Invoke action copy.

        Invoke action copy.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.PathsDy94GcUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCopyPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphMessage, or the result of cls(response)
        :rtype: ~users_actions.models.MicrosoftGraphMessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphMessage"]
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
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsDy94GcUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCopyPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphMessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    copy.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.copy'}  # type: ignore

    def create_forward(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.Paths29L6IuUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCreateforwardPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphMessage"
        """Invoke action createForward.

        Invoke action createForward.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.Paths29L6IuUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCreateforwardPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphMessage, or the result of cls(response)
        :rtype: ~users_actions.models.MicrosoftGraphMessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphMessage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_forward.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths29L6IuUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCreateforwardPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphMessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_forward.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.createForward'}  # type: ignore

    def create_reply(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.PathsGpd5XxUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCreatereplyPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphMessage"
        """Invoke action createReply.

        Invoke action createReply.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.PathsGpd5XxUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCreatereplyPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphMessage, or the result of cls(response)
        :rtype: ~users_actions.models.MicrosoftGraphMessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphMessage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_reply.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsGpd5XxUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCreatereplyPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphMessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_reply.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.createReply'}  # type: ignore

    def create_reply_all(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.Paths3M6QbmUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCreatereplyallPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphMessage"
        """Invoke action createReplyAll.

        Invoke action createReplyAll.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.Paths3M6QbmUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCreatereplyallPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphMessage, or the result of cls(response)
        :rtype: ~users_actions.models.MicrosoftGraphMessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphMessage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_reply_all.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths3M6QbmUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphCreatereplyallPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphMessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_reply_all.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.createReplyAll'}  # type: ignore

    def forward(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.Paths1X7Dum0UsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphForwardPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action forward.

        Invoke action forward.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.Paths1X7Dum0UsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphForwardPostRequestbodyContentApplicationJsonSchema
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
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1X7Dum0UsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphForwardPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    forward.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.forward'}  # type: ignore

    def move(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.Paths1Ph8596UsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphMovePostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphMessage"
        """Invoke action move.

        Invoke action move.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.Paths1Ph8596UsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphMovePostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphMessage, or the result of cls(response)
        :rtype: ~users_actions.models.MicrosoftGraphMessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphMessage"]
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
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1Ph8596UsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphMovePostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphMessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    move.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.move'}  # type: ignore

    def reply(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.Paths6Zjq1HUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphReplyPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action reply.

        Invoke action reply.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.Paths6Zjq1HUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphReplyPostRequestbodyContentApplicationJsonSchema
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
        url = self.reply.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths6Zjq1HUsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphReplyPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    reply.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.reply'}  # type: ignore

    def reply_all(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        body,  # type: "models.Paths16Mdb34UsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphReplyallPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action replyAll.

        Invoke action replyAll.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.Paths16Mdb34UsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphReplyallPostRequestbodyContentApplicationJsonSchema
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
        url = self.reply_all.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths16Mdb34UsersUserIdMailfoldersMailfolderIdMessagesMessageIdMicrosoftGraphReplyallPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    reply_all.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.replyAll'}  # type: ignore

    def send(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action send.

        Invoke action send.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
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
        url = self.send.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    send.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.send'}  # type: ignore

    def unsubscribe(
        self,
        user_id,  # type: str
        mail_folder_id,  # type: str
        message_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action unsubscribe.

        Invoke action unsubscribe.

        :param user_id: key: id of user.
        :type user_id: str
        :param mail_folder_id: key: id of mailFolder.
        :type mail_folder_id: str
        :param message_id: key: id of message.
        :type message_id: str
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
        url = self.unsubscribe.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'mailFolder-id': self._serialize.url("mail_folder_id", mail_folder_id, 'str'),
            'message-id': self._serialize.url("message_id", message_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    unsubscribe.metadata = {'url': '/users/{user-id}/mailFolders/{mailFolder-id}/messages/{message-id}/microsoft.graph.unsubscribe'}  # type: ignore
