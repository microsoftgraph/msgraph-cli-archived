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

class ChatsInstalledAppsOperations:
    """ChatsInstalledAppsOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def upgrade(
        self,
        chat_id: str,
        teams_app_installation_id: str,
        **kwargs
    ) -> None:
        """Invoke action upgrade.

        Invoke action upgrade.

        :param chat_id: key: id of chat.
        :type chat_id: str
        :param teams_app_installation_id: key: id of teamsAppInstallation.
        :type teams_app_installation_id: str
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
        url = self.upgrade.metadata['url']  # type: ignore
        path_format_arguments = {
            'chat-id': self._serialize.url("chat_id", chat_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
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

    upgrade.metadata = {'url': '/chats/{chat-id}/installedApps/{teamsAppInstallation-id}/microsoft.graph.upgrade'}  # type: ignore

    async def get_teams_app(
        self,
        chat_id: str,
        teams_app_installation_id: str,
        select: Optional[List[Union[str, "models.Enum26"]]] = None,
        expand: Optional[List[Union[str, "models.Enum27"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphTeamsApp":
        """Get teamsApp from chats.

        Get teamsApp from chats.

        :param chat_id: key: id of chat.
        :type chat_id: str
        :param teams_app_installation_id: key: id of teamsAppInstallation.
        :type teams_app_installation_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~teams.models.Enum26]
        :param expand: Expand related entities.
        :type expand: list[str or ~teams.models.Enum27]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTeamsApp, or the result of cls(response)
        :rtype: ~teams.models.MicrosoftGraphTeamsApp
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTeamsApp"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_teams_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'chat-id': self._serialize.url("chat_id", chat_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphTeamsApp', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_teams_app.metadata = {'url': '/chats/{chat-id}/installedApps/{teamsAppInstallation-id}/teamsApp'}  # type: ignore

    async def get_ref_teams_app(
        self,
        chat_id: str,
        teams_app_installation_id: str,
        **kwargs
    ) -> str:
        """Get ref of teamsApp from chats.

        Get ref of teamsApp from chats.

        :param chat_id: key: id of chat.
        :type chat_id: str
        :param teams_app_installation_id: key: id of teamsAppInstallation.
        :type teams_app_installation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[str]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_ref_teams_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'chat-id': self._serialize.url("chat_id", chat_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
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

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_ref_teams_app.metadata = {'url': '/chats/{chat-id}/installedApps/{teamsAppInstallation-id}/teamsApp/$ref'}  # type: ignore

    async def set_ref_teams_app(
        self,
        chat_id: str,
        teams_app_installation_id: str,
        body: Dict[str, object],
        **kwargs
    ) -> None:
        """Update the ref of navigation property teamsApp in chats.

        Update the ref of navigation property teamsApp in chats.

        :param chat_id: key: id of chat.
        :type chat_id: str
        :param teams_app_installation_id: key: id of teamsAppInstallation.
        :type teams_app_installation_id: str
        :param body: New navigation property ref values.
        :type body: dict[str, object]
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
        url = self.set_ref_teams_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'chat-id': self._serialize.url("chat_id", chat_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, '{object}')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    set_ref_teams_app.metadata = {'url': '/chats/{chat-id}/installedApps/{teamsAppInstallation-id}/teamsApp/$ref'}  # type: ignore

    async def delete_ref_teams_app(
        self,
        chat_id: str,
        teams_app_installation_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete ref of navigation property teamsApp for chats.

        Delete ref of navigation property teamsApp for chats.

        :param chat_id: key: id of chat.
        :type chat_id: str
        :param teams_app_installation_id: key: id of teamsAppInstallation.
        :type teams_app_installation_id: str
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
        url = self.delete_ref_teams_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'chat-id': self._serialize.url("chat_id", chat_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
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

    delete_ref_teams_app.metadata = {'url': '/chats/{chat-id}/installedApps/{teamsAppInstallation-id}/teamsApp/$ref'}  # type: ignore

    async def get_teams_app_definition(
        self,
        chat_id: str,
        teams_app_installation_id: str,
        select: Optional[List[Union[str, "models.Enum28"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphTeamsAppDefinition":
        """Get teamsAppDefinition from chats.

        Get teamsAppDefinition from chats.

        :param chat_id: key: id of chat.
        :type chat_id: str
        :param teams_app_installation_id: key: id of teamsAppInstallation.
        :type teams_app_installation_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~teams.models.Enum28]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTeamsAppDefinition, or the result of cls(response)
        :rtype: ~teams.models.MicrosoftGraphTeamsAppDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTeamsAppDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_teams_app_definition.metadata['url']  # type: ignore
        path_format_arguments = {
            'chat-id': self._serialize.url("chat_id", chat_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphTeamsAppDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_teams_app_definition.metadata = {'url': '/chats/{chat-id}/installedApps/{teamsAppInstallation-id}/teamsAppDefinition'}  # type: ignore

    async def get_ref_teams_app_definition(
        self,
        chat_id: str,
        teams_app_installation_id: str,
        **kwargs
    ) -> str:
        """Get ref of teamsAppDefinition from chats.

        Get ref of teamsAppDefinition from chats.

        :param chat_id: key: id of chat.
        :type chat_id: str
        :param teams_app_installation_id: key: id of teamsAppInstallation.
        :type teams_app_installation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[str]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_ref_teams_app_definition.metadata['url']  # type: ignore
        path_format_arguments = {
            'chat-id': self._serialize.url("chat_id", chat_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
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

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_ref_teams_app_definition.metadata = {'url': '/chats/{chat-id}/installedApps/{teamsAppInstallation-id}/teamsAppDefinition/$ref'}  # type: ignore

    async def set_ref_teams_app_definition(
        self,
        chat_id: str,
        teams_app_installation_id: str,
        body: Dict[str, object],
        **kwargs
    ) -> None:
        """Update the ref of navigation property teamsAppDefinition in chats.

        Update the ref of navigation property teamsAppDefinition in chats.

        :param chat_id: key: id of chat.
        :type chat_id: str
        :param teams_app_installation_id: key: id of teamsAppInstallation.
        :type teams_app_installation_id: str
        :param body: New navigation property ref values.
        :type body: dict[str, object]
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
        url = self.set_ref_teams_app_definition.metadata['url']  # type: ignore
        path_format_arguments = {
            'chat-id': self._serialize.url("chat_id", chat_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, '{object}')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    set_ref_teams_app_definition.metadata = {'url': '/chats/{chat-id}/installedApps/{teamsAppInstallation-id}/teamsAppDefinition/$ref'}  # type: ignore

    async def delete_ref_teams_app_definition(
        self,
        chat_id: str,
        teams_app_installation_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete ref of navigation property teamsAppDefinition for chats.

        Delete ref of navigation property teamsAppDefinition for chats.

        :param chat_id: key: id of chat.
        :type chat_id: str
        :param teams_app_installation_id: key: id of teamsAppInstallation.
        :type teams_app_installation_id: str
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
        url = self.delete_ref_teams_app_definition.metadata['url']  # type: ignore
        path_format_arguments = {
            'chat-id': self._serialize.url("chat_id", chat_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
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

    delete_ref_teams_app_definition.metadata = {'url': '/chats/{chat-id}/installedApps/{teamsAppInstallation-id}/teamsAppDefinition/$ref'}  # type: ignore
