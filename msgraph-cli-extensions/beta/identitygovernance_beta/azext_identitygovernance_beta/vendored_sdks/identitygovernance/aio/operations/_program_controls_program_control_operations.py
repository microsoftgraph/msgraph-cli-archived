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

class ProgramControlsProgramControlOperations:
    """ProgramControlsProgramControlOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_governance.models
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

    def list_program_control(
        self,
        orderby: Optional[List[Union[str, "models.Enum1416"]]] = None,
        select: Optional[List[Union[str, "models.Enum1417"]]] = None,
        expand: Optional[List[Union[str, "models.Enum1418"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfProgramControl"]:
        """Get entities from programControls.

        Get entities from programControls.

        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_governance.models.Enum1416]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum1417]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_governance.models.Enum1418]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfProgramControl or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~identity_governance.models.CollectionOfProgramControl]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfProgramControl"]
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
                url = self.list_program_control.metadata['url']  # type: ignore
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
            deserialized = self._deserialize('CollectionOfProgramControl', pipeline_response)
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
    list_program_control.metadata = {'url': '/programControls'}  # type: ignore

    async def create_program_control(
        self,
        body: "models.MicrosoftGraphProgramControl",
        **kwargs
    ) -> "models.MicrosoftGraphProgramControl":
        """Add new entity to programControls.

        Add new entity to programControls.

        :param body: New entity.
        :type body: ~identity_governance.models.MicrosoftGraphProgramControl
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphProgramControl, or the result of cls(response)
        :rtype: ~identity_governance.models.MicrosoftGraphProgramControl
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphProgramControl"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_program_control.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphProgramControl')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphProgramControl', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_program_control.metadata = {'url': '/programControls'}  # type: ignore

    async def get_program_control(
        self,
        program_control_id: str,
        select: Optional[List[Union[str, "models.Enum1419"]]] = None,
        expand: Optional[List[Union[str, "models.Enum1420"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphProgramControl":
        """Get entity from programControls by key.

        Get entity from programControls by key.

        :param program_control_id: key: id of programControl.
        :type program_control_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum1419]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_governance.models.Enum1420]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphProgramControl, or the result of cls(response)
        :rtype: ~identity_governance.models.MicrosoftGraphProgramControl
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphProgramControl"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_program_control.metadata['url']  # type: ignore
        path_format_arguments = {
            'programControl-id': self._serialize.url("program_control_id", program_control_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphProgramControl', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_program_control.metadata = {'url': '/programControls/{programControl-id}'}  # type: ignore

    async def update_program_control(
        self,
        program_control_id: str,
        body: "models.MicrosoftGraphProgramControl",
        **kwargs
    ) -> None:
        """Update entity in programControls.

        Update entity in programControls.

        :param program_control_id: key: id of programControl.
        :type program_control_id: str
        :param body: New property values.
        :type body: ~identity_governance.models.MicrosoftGraphProgramControl
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
        url = self.update_program_control.metadata['url']  # type: ignore
        path_format_arguments = {
            'programControl-id': self._serialize.url("program_control_id", program_control_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphProgramControl')
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

    update_program_control.metadata = {'url': '/programControls/{programControl-id}'}  # type: ignore

    async def delete_program_control(
        self,
        program_control_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete entity from programControls.

        Delete entity from programControls.

        :param program_control_id: key: id of programControl.
        :type program_control_id: str
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
        url = self.delete_program_control.metadata['url']  # type: ignore
        path_format_arguments = {
            'programControl-id': self._serialize.url("program_control_id", program_control_id, 'str'),
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

    delete_program_control.metadata = {'url': '/programControls/{programControl-id}'}  # type: ignore
