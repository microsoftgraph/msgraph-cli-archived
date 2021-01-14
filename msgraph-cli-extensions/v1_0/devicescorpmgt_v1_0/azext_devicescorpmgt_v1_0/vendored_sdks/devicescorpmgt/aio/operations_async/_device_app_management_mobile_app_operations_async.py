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
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DeviceAppManagementMobileAppOperations:
    """DeviceAppManagementMobileAppOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~devices_corporate_management.models
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

    def list_assignment(
        self,
        mobile_app_id: str,
        orderby: Optional[List[Union[str, "models.Enum114"]]] = None,
        select: Optional[List[Union[str, "models.Enum115"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfMobileAppAssignment"]:
        """Get assignments from deviceAppManagement.

        Get assignments from deviceAppManagement.

        :param mobile_app_id: key: id of mobileApp.
        :type mobile_app_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~devices_corporate_management.models.Enum114]
        :param select: Select properties to be returned.
        :type select: list[str or ~devices_corporate_management.models.Enum115]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfMobileAppAssignment or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~devices_corporate_management.models.CollectionOfMobileAppAssignment]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfMobileAppAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_assignment.metadata['url']  # type: ignore
                path_format_arguments = {
                    'mobileApp-id': self._serialize.url("mobile_app_id", mobile_app_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
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
            deserialized = self._deserialize('CollectionOfMobileAppAssignment', pipeline_response)
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
    list_assignment.metadata = {'url': '/deviceAppManagement/mobileApps/{mobileApp-id}/assignments'}  # type: ignore

    async def create_assignment(
        self,
        mobile_app_id: str,
        id: Optional[str] = None,
        intent: Optional[Union[str, "models.MicrosoftGraphInstallIntent"]] = None,
        settings: Optional[Dict[str, object]] = None,
        target: Optional[Dict[str, object]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphMobileAppAssignment":
        """Create new navigation property to assignments for deviceAppManagement.

        Create new navigation property to assignments for deviceAppManagement.

        :param mobile_app_id: key: id of mobileApp.
        :type mobile_app_id: str
        :param id: Read-only.
        :type id: str
        :param intent:
        :type intent: str or ~devices_corporate_management.models.MicrosoftGraphInstallIntent
        :param settings: Abstract class to contain properties used to assign a mobile app to a group.
        :type settings: dict[str, object]
        :param target: Base type for assignment targets.
        :type target: dict[str, object]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphMobileAppAssignment, or the result of cls(response)
        :rtype: ~devices_corporate_management.models.MicrosoftGraphMobileAppAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphMobileAppAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphMobileAppAssignment(id=id, intent=intent, settings=settings, target=target)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'mobileApp-id': self._serialize.url("mobile_app_id", mobile_app_id, 'str'),
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
        body_content = self._serialize.body(_body, 'MicrosoftGraphMobileAppAssignment')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphMobileAppAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_assignment.metadata = {'url': '/deviceAppManagement/mobileApps/{mobileApp-id}/assignments'}  # type: ignore

    async def get_assignment(
        self,
        mobile_app_id: str,
        mobile_app_assignment_id: str,
        select: Optional[List[Union[str, "models.Enum116"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphMobileAppAssignment":
        """Get assignments from deviceAppManagement.

        Get assignments from deviceAppManagement.

        :param mobile_app_id: key: id of mobileApp.
        :type mobile_app_id: str
        :param mobile_app_assignment_id: key: id of mobileAppAssignment.
        :type mobile_app_assignment_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~devices_corporate_management.models.Enum116]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphMobileAppAssignment, or the result of cls(response)
        :rtype: ~devices_corporate_management.models.MicrosoftGraphMobileAppAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphMobileAppAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'mobileApp-id': self._serialize.url("mobile_app_id", mobile_app_id, 'str'),
            'mobileAppAssignment-id': self._serialize.url("mobile_app_assignment_id", mobile_app_assignment_id, 'str'),
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
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphMobileAppAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_assignment.metadata = {'url': '/deviceAppManagement/mobileApps/{mobileApp-id}/assignments/{mobileAppAssignment-id}'}  # type: ignore

    async def update_assignment(
        self,
        mobile_app_id: str,
        mobile_app_assignment_id: str,
        id: Optional[str] = None,
        intent: Optional[Union[str, "models.MicrosoftGraphInstallIntent"]] = None,
        settings: Optional[Dict[str, object]] = None,
        target: Optional[Dict[str, object]] = None,
        **kwargs
    ) -> None:
        """Update the navigation property assignments in deviceAppManagement.

        Update the navigation property assignments in deviceAppManagement.

        :param mobile_app_id: key: id of mobileApp.
        :type mobile_app_id: str
        :param mobile_app_assignment_id: key: id of mobileAppAssignment.
        :type mobile_app_assignment_id: str
        :param id: Read-only.
        :type id: str
        :param intent:
        :type intent: str or ~devices_corporate_management.models.MicrosoftGraphInstallIntent
        :param settings: Abstract class to contain properties used to assign a mobile app to a group.
        :type settings: dict[str, object]
        :param target: Base type for assignment targets.
        :type target: dict[str, object]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphMobileAppAssignment(id=id, intent=intent, settings=settings, target=target)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'mobileApp-id': self._serialize.url("mobile_app_id", mobile_app_id, 'str'),
            'mobileAppAssignment-id': self._serialize.url("mobile_app_assignment_id", mobile_app_assignment_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphMobileAppAssignment')
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

    update_assignment.metadata = {'url': '/deviceAppManagement/mobileApps/{mobileApp-id}/assignments/{mobileAppAssignment-id}'}  # type: ignore

    async def delete_assignment(
        self,
        mobile_app_id: str,
        mobile_app_assignment_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property assignments for deviceAppManagement.

        Delete navigation property assignments for deviceAppManagement.

        :param mobile_app_id: key: id of mobileApp.
        :type mobile_app_id: str
        :param mobile_app_assignment_id: key: id of mobileAppAssignment.
        :type mobile_app_assignment_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'mobileApp-id': self._serialize.url("mobile_app_id", mobile_app_id, 'str'),
            'mobileAppAssignment-id': self._serialize.url("mobile_app_assignment_id", mobile_app_assignment_id, 'str'),
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

    delete_assignment.metadata = {'url': '/deviceAppManagement/mobileApps/{mobileApp-id}/assignments/{mobileAppAssignment-id}'}  # type: ignore

    def list_category(
        self,
        mobile_app_id: str,
        orderby: Optional[List[Union[str, "models.Enum117"]]] = None,
        select: Optional[List[Union[str, "models.Enum118"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfMobileAppCategory0"]:
        """Get categories from deviceAppManagement.

        Get categories from deviceAppManagement.

        :param mobile_app_id: key: id of mobileApp.
        :type mobile_app_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~devices_corporate_management.models.Enum117]
        :param select: Select properties to be returned.
        :type select: list[str or ~devices_corporate_management.models.Enum118]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfMobileAppCategory0 or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~devices_corporate_management.models.CollectionOfMobileAppCategory0]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfMobileAppCategory0"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_category.metadata['url']  # type: ignore
                path_format_arguments = {
                    'mobileApp-id': self._serialize.url("mobile_app_id", mobile_app_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
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
            deserialized = self._deserialize('CollectionOfMobileAppCategory0', pipeline_response)
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
    list_category.metadata = {'url': '/deviceAppManagement/mobileApps/{mobileApp-id}/categories'}  # type: ignore

    def list_ref_category(
        self,
        mobile_app_id: str,
        orderby: Optional[List[Union[str, "models.Enum119"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfLinksOfMobileAppCategory"]:
        """Get ref of categories from deviceAppManagement.

        Get ref of categories from deviceAppManagement.

        :param mobile_app_id: key: id of mobileApp.
        :type mobile_app_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~devices_corporate_management.models.Enum119]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfLinksOfMobileAppCategory or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~devices_corporate_management.models.CollectionOfLinksOfMobileAppCategory]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfLinksOfMobileAppCategory"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_ref_category.metadata['url']  # type: ignore
                path_format_arguments = {
                    'mobileApp-id': self._serialize.url("mobile_app_id", mobile_app_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
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

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfLinksOfMobileAppCategory', pipeline_response)
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
    list_ref_category.metadata = {'url': '/deviceAppManagement/mobileApps/{mobileApp-id}/categories/$ref'}  # type: ignore

    async def create_ref_category(
        self,
        mobile_app_id: str,
        body: Dict[str, object],
        **kwargs
    ) -> Dict[str, object]:
        """Create new navigation property ref to categories for deviceAppManagement.

        Create new navigation property ref to categories for deviceAppManagement.

        :param mobile_app_id: key: id of mobileApp.
        :type mobile_app_id: str
        :param body: New navigation property ref value.
        :type body: dict[str, object]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: dict mapping str to object, or the result of cls(response)
        :rtype: dict[str, object]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Dict[str, object]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_ref_category.metadata['url']  # type: ignore
        path_format_arguments = {
            'mobileApp-id': self._serialize.url("mobile_app_id", mobile_app_id, 'str'),
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
        body_content = self._serialize.body(body, '{object}')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('{object}', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_ref_category.metadata = {'url': '/deviceAppManagement/mobileApps/{mobileApp-id}/categories/$ref'}  # type: ignore

    async def assign(
        self,
        mobile_app_id: str,
        mobile_app_assignments: Optional[List["models.MicrosoftGraphMobileAppAssignment"]] = None,
        **kwargs
    ) -> None:
        """Invoke action assign.

        Invoke action assign.

        :param mobile_app_id: key: id of mobileApp.
        :type mobile_app_id: str
        :param mobile_app_assignments:
        :type mobile_app_assignments: list[~devices_corporate_management.models.MicrosoftGraphMobileAppAssignment]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths12NzrcrDeviceappmanagementMobileappsMobileappIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema(mobile_app_assignments=mobile_app_assignments)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.assign.metadata['url']  # type: ignore
        path_format_arguments = {
            'mobileApp-id': self._serialize.url("mobile_app_id", mobile_app_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths12NzrcrDeviceappmanagementMobileappsMobileappIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema')
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

    assign.metadata = {'url': '/deviceAppManagement/mobileApps/{mobileApp-id}/microsoft.graph.assign'}  # type: ignore