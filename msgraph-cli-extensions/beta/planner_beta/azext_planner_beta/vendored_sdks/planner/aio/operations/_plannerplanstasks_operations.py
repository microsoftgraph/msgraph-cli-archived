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

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class plannerplanstasksOperations:
    """plannerplanstasksOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~planner.models
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

    async def get_assigned_to_task_board_format(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        select: Optional[List[Union[str, "models.Enum73"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.microsoftgraphplannerassignedtotaskboardtaskformat":
        """Get assignedToTaskBoardFormat from planner.

        Get assignedToTaskBoardFormat from planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~planner.models.Enum73]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphplannerassignedtotaskboardtaskformat, or the result of cls(response)
        :rtype: ~planner.models.microsoftgraphplannerassignedtotaskboardtaskformat
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphplannerassignedtotaskboardtaskformat"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_assigned_to_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphplannerassignedtotaskboardtaskformat', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_assigned_to_task_board_format.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/assignedToTaskBoardFormat'}  # type: ignore

    async def update_assigned_to_task_board_format(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        body: "models.microsoftgraphplannerassignedtotaskboardtaskformat",
        **kwargs
    ) -> None:
        """Update the navigation property assignedToTaskBoardFormat in planner.

        Update the navigation property assignedToTaskBoardFormat in planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param body: New navigation property values.
        :type body: ~planner.models.microsoftgraphplannerassignedtotaskboardtaskformat
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
        url = self.update_assigned_to_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphplannerassignedtotaskboardtaskformat')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_assigned_to_task_board_format.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/assignedToTaskBoardFormat'}  # type: ignore

    async def delete_assigned_to_task_board_format(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property assignedToTaskBoardFormat for planner.

        Delete navigation property assignedToTaskBoardFormat for planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
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
        url = self.delete_assigned_to_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_assigned_to_task_board_format.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/assignedToTaskBoardFormat'}  # type: ignore

    async def get_bucket_task_board_format(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        select: Optional[List[Union[str, "models.Enum74"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.microsoftgraphplannerbuckettaskboardtaskformat":
        """Get bucketTaskBoardFormat from planner.

        Get bucketTaskBoardFormat from planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~planner.models.Enum74]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphplannerbuckettaskboardtaskformat, or the result of cls(response)
        :rtype: ~planner.models.microsoftgraphplannerbuckettaskboardtaskformat
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphplannerbuckettaskboardtaskformat"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_bucket_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphplannerbuckettaskboardtaskformat', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_bucket_task_board_format.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/bucketTaskBoardFormat'}  # type: ignore

    async def update_bucket_task_board_format(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        body: "models.microsoftgraphplannerbuckettaskboardtaskformat",
        **kwargs
    ) -> None:
        """Update the navigation property bucketTaskBoardFormat in planner.

        Update the navigation property bucketTaskBoardFormat in planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param body: New navigation property values.
        :type body: ~planner.models.microsoftgraphplannerbuckettaskboardtaskformat
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
        url = self.update_bucket_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphplannerbuckettaskboardtaskformat')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_bucket_task_board_format.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/bucketTaskBoardFormat'}  # type: ignore

    async def delete_bucket_task_board_format(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property bucketTaskBoardFormat for planner.

        Delete navigation property bucketTaskBoardFormat for planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
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
        url = self.delete_bucket_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_bucket_task_board_format.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/bucketTaskBoardFormat'}  # type: ignore

    async def get_details(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        select: Optional[List[Union[str, "models.Enum75"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.microsoftgraphplannertaskdetails":
        """Get details from planner.

        Get details from planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~planner.models.Enum75]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphplannertaskdetails, or the result of cls(response)
        :rtype: ~planner.models.microsoftgraphplannertaskdetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphplannertaskdetails"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_details.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphplannertaskdetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_details.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/details'}  # type: ignore

    async def update_details(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        body: "models.microsoftgraphplannertaskdetails",
        **kwargs
    ) -> None:
        """Update the navigation property details in planner.

        Update the navigation property details in planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param body: New navigation property values.
        :type body: ~planner.models.microsoftgraphplannertaskdetails
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
        url = self.update_details.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphplannertaskdetails')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_details.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/details'}  # type: ignore

    async def delete_details(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property details for planner.

        Delete navigation property details for planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
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
        url = self.delete_details.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_details.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/details'}  # type: ignore

    async def get_progress_task_board_format(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        select: Optional[List[Union[str, "models.Enum76"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.microsoftgraphplannerprogresstaskboardtaskformat":
        """Get progressTaskBoardFormat from planner.

        Get progressTaskBoardFormat from planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~planner.models.Enum76]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphplannerprogresstaskboardtaskformat, or the result of cls(response)
        :rtype: ~planner.models.microsoftgraphplannerprogresstaskboardtaskformat
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphplannerprogresstaskboardtaskformat"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_progress_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphplannerprogresstaskboardtaskformat', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_progress_task_board_format.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/progressTaskBoardFormat'}  # type: ignore

    async def update_progress_task_board_format(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        body: "models.microsoftgraphplannerprogresstaskboardtaskformat",
        **kwargs
    ) -> None:
        """Update the navigation property progressTaskBoardFormat in planner.

        Update the navigation property progressTaskBoardFormat in planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param body: New navigation property values.
        :type body: ~planner.models.microsoftgraphplannerprogresstaskboardtaskformat
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
        url = self.update_progress_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphplannerprogresstaskboardtaskformat')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_progress_task_board_format.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/progressTaskBoardFormat'}  # type: ignore

    async def delete_progress_task_board_format(
        self,
        planner_plan_id: str,
        planner_task_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property progressTaskBoardFormat for planner.

        Delete navigation property progressTaskBoardFormat for planner.

        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
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
        url = self.delete_progress_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_progress_task_board_format.metadata = {'url': '/planner/plans/{plannerPlan-id}/tasks/{plannerTask-id}/progressTaskBoardFormat'}  # type: ignore
