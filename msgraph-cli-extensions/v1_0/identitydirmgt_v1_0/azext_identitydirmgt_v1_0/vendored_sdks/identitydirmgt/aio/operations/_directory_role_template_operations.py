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

class DirectoryRoleTemplateOperations:
    """DirectoryRoleTemplateOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_directory_management.models
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

    async def check_member_group(
        self,
        directory_role_template_id: str,
        group_ids: Optional[List[str]] = None,
        **kwargs
    ) -> List[str]:
        """Invoke action checkMemberGroups.

        Invoke action checkMemberGroups.

        :param directory_role_template_id: key: id of directoryRoleTemplate.
        :type directory_role_template_id: str
        :param group_ids:
        :type group_ids: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.PathsMwgbeoDirectoryroletemplatesDirectoryroletemplateIdMicrosoftGraphCheckmembergroupsPostRequestbodyContentApplicationJsonSchema(group_ids=group_ids)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.check_member_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'directoryRoleTemplate-id': self._serialize.url("directory_role_template_id", directory_role_template_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsMwgbeoDirectoryroletemplatesDirectoryroletemplateIdMicrosoftGraphCheckmembergroupsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
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
    check_member_group.metadata = {'url': '/directoryRoleTemplates/{directoryRoleTemplate-id}/microsoft.graph.checkMemberGroups'}  # type: ignore

    async def check_member_object(
        self,
        directory_role_template_id: str,
        ids: Optional[List[str]] = None,
        **kwargs
    ) -> List[str]:
        """Invoke action checkMemberObjects.

        Invoke action checkMemberObjects.

        :param directory_role_template_id: key: id of directoryRoleTemplate.
        :type directory_role_template_id: str
        :param ids:
        :type ids: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.PathsYkfgk1DirectoryroletemplatesDirectoryroletemplateIdMicrosoftGraphCheckmemberobjectsPostRequestbodyContentApplicationJsonSchema(ids=ids)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.check_member_object.metadata['url']  # type: ignore
        path_format_arguments = {
            'directoryRoleTemplate-id': self._serialize.url("directory_role_template_id", directory_role_template_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsYkfgk1DirectoryroletemplatesDirectoryroletemplateIdMicrosoftGraphCheckmemberobjectsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
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
    check_member_object.metadata = {'url': '/directoryRoleTemplates/{directoryRoleTemplate-id}/microsoft.graph.checkMemberObjects'}  # type: ignore

    async def get_member_group(
        self,
        directory_role_template_id: str,
        security_enabled_only: Optional[bool] = False,
        **kwargs
    ) -> List[str]:
        """Invoke action getMemberGroups.

        Invoke action getMemberGroups.

        :param directory_role_template_id: key: id of directoryRoleTemplate.
        :type directory_role_template_id: str
        :param security_enabled_only:
        :type security_enabled_only: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.PathsU5PhcgDirectoryroletemplatesDirectoryroletemplateIdMicrosoftGraphGetmembergroupsPostRequestbodyContentApplicationJsonSchema(security_enabled_only=security_enabled_only)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.get_member_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'directoryRoleTemplate-id': self._serialize.url("directory_role_template_id", directory_role_template_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsU5PhcgDirectoryroletemplatesDirectoryroletemplateIdMicrosoftGraphGetmembergroupsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
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
    get_member_group.metadata = {'url': '/directoryRoleTemplates/{directoryRoleTemplate-id}/microsoft.graph.getMemberGroups'}  # type: ignore

    async def get_member_object(
        self,
        directory_role_template_id: str,
        security_enabled_only: Optional[bool] = False,
        **kwargs
    ) -> List[str]:
        """Invoke action getMemberObjects.

        Invoke action getMemberObjects.

        :param directory_role_template_id: key: id of directoryRoleTemplate.
        :type directory_role_template_id: str
        :param security_enabled_only:
        :type security_enabled_only: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.Paths116Bv3CDirectoryroletemplatesDirectoryroletemplateIdMicrosoftGraphGetmemberobjectsPostRequestbodyContentApplicationJsonSchema(security_enabled_only=security_enabled_only)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.get_member_object.metadata['url']  # type: ignore
        path_format_arguments = {
            'directoryRoleTemplate-id': self._serialize.url("directory_role_template_id", directory_role_template_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths116Bv3CDirectoryroletemplatesDirectoryroletemplateIdMicrosoftGraphGetmemberobjectsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
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
    get_member_object.metadata = {'url': '/directoryRoleTemplates/{directoryRoleTemplate-id}/microsoft.graph.getMemberObjects'}  # type: ignore

    async def restore(
        self,
        directory_role_template_id: str,
        **kwargs
    ) -> "models.MicrosoftGraphDirectoryObject":
        """Invoke action restore.

        Invoke action restore.

        :param directory_role_template_id: key: id of directoryRoleTemplate.
        :type directory_role_template_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphDirectoryObject, or the result of cls(response)
        :rtype: ~identity_directory_management.models.MicrosoftGraphDirectoryObject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphDirectoryObject"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.restore.metadata['url']  # type: ignore
        path_format_arguments = {
            'directoryRoleTemplate-id': self._serialize.url("directory_role_template_id", directory_role_template_id, 'str'),
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

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphDirectoryObject', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    restore.metadata = {'url': '/directoryRoleTemplates/{directoryRoleTemplate-id}/microsoft.graph.restore'}  # type: ignore

    async def get_available_extension_property(
        self,
        is_synced_from_on_premises: Optional[bool] = False,
        **kwargs
    ) -> List["models.MicrosoftGraphExtensionProperty"]:
        """Invoke action getAvailableExtensionProperties.

        Invoke action getAvailableExtensionProperties.

        :param is_synced_from_on_premises:
        :type is_synced_from_on_premises: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphExtensionProperty, or the result of cls(response)
        :rtype: list[~identity_directory_management.models.MicrosoftGraphExtensionProperty]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphExtensionProperty"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.PathsGlwoxyDirectoryroletemplatesMicrosoftGraphGetavailableextensionpropertiesPostRequestbodyContentApplicationJsonSchema(is_synced_from_on_premises=is_synced_from_on_premises)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.get_available_extension_property.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsGlwoxyDirectoryroletemplatesMicrosoftGraphGetavailableextensionpropertiesPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphExtensionProperty]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_available_extension_property.metadata = {'url': '/directoryRoleTemplates/microsoft.graph.getAvailableExtensionProperties'}  # type: ignore

    async def get_by_id(
        self,
        ids: Optional[List[str]] = None,
        types: Optional[List[str]] = None,
        **kwargs
    ) -> List["models.MicrosoftGraphDirectoryObject"]:
        """Invoke action getByIds.

        Invoke action getByIds.

        :param ids:
        :type ids: list[str]
        :param types:
        :type types: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphDirectoryObject, or the result of cls(response)
        :rtype: list[~identity_directory_management.models.MicrosoftGraphDirectoryObject]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphDirectoryObject"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.Paths6Ovq2LDirectoryroletemplatesMicrosoftGraphGetbyidsPostRequestbodyContentApplicationJsonSchema(ids=ids, types=types)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.get_by_id.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths6Ovq2LDirectoryroletemplatesMicrosoftGraphGetbyidsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphDirectoryObject]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_by_id.metadata = {'url': '/directoryRoleTemplates/microsoft.graph.getByIds'}  # type: ignore

    async def validate_property(
        self,
        entity_type: Optional[str] = None,
        display_name: Optional[str] = None,
        mail_nickname: Optional[str] = None,
        on_behalf_of_user_id: Optional[str] = None,
        **kwargs
    ) -> None:
        """Invoke action validateProperties.

        Invoke action validateProperties.

        :param entity_type:
        :type entity_type: str
        :param display_name:
        :type display_name: str
        :param mail_nickname:
        :type mail_nickname: str
        :param on_behalf_of_user_id:
        :type on_behalf_of_user_id: str
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

        body = models.Paths1Binbx4DirectoryroletemplatesMicrosoftGraphValidatepropertiesPostRequestbodyContentApplicationJsonSchema(entity_type=entity_type, display_name=display_name, mail_nickname=mail_nickname, on_behalf_of_user_id=on_behalf_of_user_id)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.validate_property.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1Binbx4DirectoryroletemplatesMicrosoftGraphValidatepropertiesPostRequestbodyContentApplicationJsonSchema')
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

    validate_property.metadata = {'url': '/directoryRoleTemplates/microsoft.graph.validateProperties'}  # type: ignore