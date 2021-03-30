# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class PrivilegedRoleAssignmentRequestPrivilegedRoleAssignmentRequestOperations(object):
    """PrivilegedRoleAssignmentRequestPrivilegedRoleAssignmentRequestOperations operations.

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

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_privileged_role_assignment_request(
        self,
        orderby=None,  # type: Optional[List[Union[str, "models.Enum1391"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum1392"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum1393"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfPrivilegedRoleAssignmentRequest"]
        """Get entities from privilegedRoleAssignmentRequests.

        Get entities from privilegedRoleAssignmentRequests.

        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_governance.models.Enum1391]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum1392]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_governance.models.Enum1393]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfPrivilegedRoleAssignmentRequest or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~identity_governance.models.CollectionOfPrivilegedRoleAssignmentRequest]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfPrivilegedRoleAssignmentRequest"]
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
                url = self.list_privileged_role_assignment_request.metadata['url']  # type: ignore
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfPrivilegedRoleAssignmentRequest', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_privileged_role_assignment_request.metadata = {'url': '/privilegedRoleAssignmentRequests'}  # type: ignore

    def create_privileged_role_assignment_request(
        self,
        id=None,  # type: Optional[str]
        assignment_state=None,  # type: Optional[str]
        duration=None,  # type: Optional[str]
        reason=None,  # type: Optional[str]
        requested_date_time=None,  # type: Optional[datetime.datetime]
        role_id=None,  # type: Optional[str]
        schedule=None,  # type: Optional["models.MicrosoftGraphGovernanceSchedule"]
        status=None,  # type: Optional[str]
        ticket_number=None,  # type: Optional[str]
        ticket_system=None,  # type: Optional[str]
        type=None,  # type: Optional[str]
        user_id=None,  # type: Optional[str]
        role_info=None,  # type: Optional["models.MicrosoftGraphPrivilegedRole"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPrivilegedRoleAssignmentRequest"
        """Add new entity to privilegedRoleAssignmentRequests.

        Add new entity to privilegedRoleAssignmentRequests.

        :param id: Read-only.
        :type id: str
        :param assignment_state:
        :type assignment_state: str
        :param duration:
        :type duration: str
        :param reason:
        :type reason: str
        :param requested_date_time:
        :type requested_date_time: ~datetime.datetime
        :param role_id:
        :type role_id: str
        :param schedule: governanceSchedule.
        :type schedule: ~identity_governance.models.MicrosoftGraphGovernanceSchedule
        :param status:
        :type status: str
        :param ticket_number:
        :type ticket_number: str
        :param ticket_system:
        :type ticket_system: str
        :param type:
        :type type: str
        :param user_id:
        :type user_id: str
        :param role_info: privilegedRole.
        :type role_info: ~identity_governance.models.MicrosoftGraphPrivilegedRole
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPrivilegedRoleAssignmentRequest, or the result of cls(response)
        :rtype: ~identity_governance.models.MicrosoftGraphPrivilegedRoleAssignmentRequest
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPrivilegedRoleAssignmentRequest"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.MicrosoftGraphPrivilegedRoleAssignmentRequest(id=id, assignment_state=assignment_state, duration=duration, reason=reason, requested_date_time=requested_date_time, role_id=role_id, schedule=schedule, status=status, ticket_number=ticket_number, ticket_system=ticket_system, type=type, user_id=user_id, role_info=role_info)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_privileged_role_assignment_request.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphPrivilegedRoleAssignmentRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPrivilegedRoleAssignmentRequest', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_privileged_role_assignment_request.metadata = {'url': '/privilegedRoleAssignmentRequests'}  # type: ignore

    def get_privileged_role_assignment_request(
        self,
        privileged_role_assignment_request_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum1394"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum1395"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPrivilegedRoleAssignmentRequest"
        """Get entity from privilegedRoleAssignmentRequests by key.

        Get entity from privilegedRoleAssignmentRequests by key.

        :param privileged_role_assignment_request_id: key: id of privilegedRoleAssignmentRequest.
        :type privileged_role_assignment_request_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum1394]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_governance.models.Enum1395]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPrivilegedRoleAssignmentRequest, or the result of cls(response)
        :rtype: ~identity_governance.models.MicrosoftGraphPrivilegedRoleAssignmentRequest
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPrivilegedRoleAssignmentRequest"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_privileged_role_assignment_request.metadata['url']  # type: ignore
        path_format_arguments = {
            'privilegedRoleAssignmentRequest-id': self._serialize.url("privileged_role_assignment_request_id", privileged_role_assignment_request_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPrivilegedRoleAssignmentRequest', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_privileged_role_assignment_request.metadata = {'url': '/privilegedRoleAssignmentRequests/{privilegedRoleAssignmentRequest-id}'}  # type: ignore

    def update_privileged_role_assignment_request(
        self,
        privileged_role_assignment_request_id,  # type: str
        id=None,  # type: Optional[str]
        assignment_state=None,  # type: Optional[str]
        duration=None,  # type: Optional[str]
        reason=None,  # type: Optional[str]
        requested_date_time=None,  # type: Optional[datetime.datetime]
        role_id=None,  # type: Optional[str]
        schedule=None,  # type: Optional["models.MicrosoftGraphGovernanceSchedule"]
        status=None,  # type: Optional[str]
        ticket_number=None,  # type: Optional[str]
        ticket_system=None,  # type: Optional[str]
        type=None,  # type: Optional[str]
        user_id=None,  # type: Optional[str]
        role_info=None,  # type: Optional["models.MicrosoftGraphPrivilegedRole"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update entity in privilegedRoleAssignmentRequests.

        Update entity in privilegedRoleAssignmentRequests.

        :param privileged_role_assignment_request_id: key: id of privilegedRoleAssignmentRequest.
        :type privileged_role_assignment_request_id: str
        :param id: Read-only.
        :type id: str
        :param assignment_state:
        :type assignment_state: str
        :param duration:
        :type duration: str
        :param reason:
        :type reason: str
        :param requested_date_time:
        :type requested_date_time: ~datetime.datetime
        :param role_id:
        :type role_id: str
        :param schedule: governanceSchedule.
        :type schedule: ~identity_governance.models.MicrosoftGraphGovernanceSchedule
        :param status:
        :type status: str
        :param ticket_number:
        :type ticket_number: str
        :param ticket_system:
        :type ticket_system: str
        :param type:
        :type type: str
        :param user_id:
        :type user_id: str
        :param role_info: privilegedRole.
        :type role_info: ~identity_governance.models.MicrosoftGraphPrivilegedRole
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

        body = models.MicrosoftGraphPrivilegedRoleAssignmentRequest(id=id, assignment_state=assignment_state, duration=duration, reason=reason, requested_date_time=requested_date_time, role_id=role_id, schedule=schedule, status=status, ticket_number=ticket_number, ticket_system=ticket_system, type=type, user_id=user_id, role_info=role_info)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_privileged_role_assignment_request.metadata['url']  # type: ignore
        path_format_arguments = {
            'privilegedRoleAssignmentRequest-id': self._serialize.url("privileged_role_assignment_request_id", privileged_role_assignment_request_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphPrivilegedRoleAssignmentRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_privileged_role_assignment_request.metadata = {'url': '/privilegedRoleAssignmentRequests/{privilegedRoleAssignmentRequest-id}'}  # type: ignore

    def delete_privileged_role_assignment_request(
        self,
        privileged_role_assignment_request_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete entity from privilegedRoleAssignmentRequests.

        Delete entity from privilegedRoleAssignmentRequests.

        :param privileged_role_assignment_request_id: key: id of privilegedRoleAssignmentRequest.
        :type privileged_role_assignment_request_id: str
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
        url = self.delete_privileged_role_assignment_request.metadata['url']  # type: ignore
        path_format_arguments = {
            'privilegedRoleAssignmentRequest-id': self._serialize.url("privileged_role_assignment_request_id", privileged_role_assignment_request_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_privileged_role_assignment_request.metadata = {'url': '/privilegedRoleAssignmentRequests/{privilegedRoleAssignmentRequest-id}'}  # type: ignore