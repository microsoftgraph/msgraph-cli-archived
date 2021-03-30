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

class InformationProtectionThreatAssessmentRequestOperations(object):
    """InformationProtectionThreatAssessmentRequestOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_sign_ins.models
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

    def list_result(
        self,
        threat_assessment_request_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum71"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum72"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfThreatAssessmentResult"]
        """Get results from informationProtection.

        Get results from informationProtection.

        :param threat_assessment_request_id: key: id of threatAssessmentRequest.
        :type threat_assessment_request_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_sign_ins.models.Enum71]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum72]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfThreatAssessmentResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~identity_sign_ins.models.CollectionOfThreatAssessmentResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfThreatAssessmentResult"]
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
                url = self.list_result.metadata['url']  # type: ignore
                path_format_arguments = {
                    'threatAssessmentRequest-id': self._serialize.url("threat_assessment_request_id", threat_assessment_request_id, 'str'),
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfThreatAssessmentResult', pipeline_response)
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
    list_result.metadata = {'url': '/informationProtection/threatAssessmentRequests/{threatAssessmentRequest-id}/results'}  # type: ignore

    def create_result(
        self,
        threat_assessment_request_id,  # type: str
        id=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        message=None,  # type: Optional[str]
        result_type=None,  # type: Optional[Union[str, "models.MicrosoftGraphThreatAssessmentResultType"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphThreatAssessmentResult"
        """Create new navigation property to results for informationProtection.

        Create new navigation property to results for informationProtection.

        :param threat_assessment_request_id: key: id of threatAssessmentRequest.
        :type threat_assessment_request_id: str
        :param id: Read-only.
        :type id: str
        :param created_date_time: The Timestamp type represents date and time information using ISO
         8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like
         this: '2014-01-01T00:00:00Z'.
        :type created_date_time: ~datetime.datetime
        :param message: The result message for each threat assessment.
        :type message: str
        :param result_type:
        :type result_type: str or ~identity_sign_ins.models.MicrosoftGraphThreatAssessmentResultType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphThreatAssessmentResult, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphThreatAssessmentResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphThreatAssessmentResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.MicrosoftGraphThreatAssessmentResult(id=id, created_date_time=created_date_time, message=message, result_type=result_type)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_result.metadata['url']  # type: ignore
        path_format_arguments = {
            'threatAssessmentRequest-id': self._serialize.url("threat_assessment_request_id", threat_assessment_request_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphThreatAssessmentResult')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphThreatAssessmentResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_result.metadata = {'url': '/informationProtection/threatAssessmentRequests/{threatAssessmentRequest-id}/results'}  # type: ignore

    def get_result(
        self,
        threat_assessment_request_id,  # type: str
        threat_assessment_result_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum73"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphThreatAssessmentResult"
        """Get results from informationProtection.

        Get results from informationProtection.

        :param threat_assessment_request_id: key: id of threatAssessmentRequest.
        :type threat_assessment_request_id: str
        :param threat_assessment_result_id: key: id of threatAssessmentResult.
        :type threat_assessment_result_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum73]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphThreatAssessmentResult, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphThreatAssessmentResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphThreatAssessmentResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_result.metadata['url']  # type: ignore
        path_format_arguments = {
            'threatAssessmentRequest-id': self._serialize.url("threat_assessment_request_id", threat_assessment_request_id, 'str'),
            'threatAssessmentResult-id': self._serialize.url("threat_assessment_result_id", threat_assessment_result_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphThreatAssessmentResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_result.metadata = {'url': '/informationProtection/threatAssessmentRequests/{threatAssessmentRequest-id}/results/{threatAssessmentResult-id}'}  # type: ignore

    def update_result(
        self,
        threat_assessment_request_id,  # type: str
        threat_assessment_result_id,  # type: str
        id=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        message=None,  # type: Optional[str]
        result_type=None,  # type: Optional[Union[str, "models.MicrosoftGraphThreatAssessmentResultType"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property results in informationProtection.

        Update the navigation property results in informationProtection.

        :param threat_assessment_request_id: key: id of threatAssessmentRequest.
        :type threat_assessment_request_id: str
        :param threat_assessment_result_id: key: id of threatAssessmentResult.
        :type threat_assessment_result_id: str
        :param id: Read-only.
        :type id: str
        :param created_date_time: The Timestamp type represents date and time information using ISO
         8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like
         this: '2014-01-01T00:00:00Z'.
        :type created_date_time: ~datetime.datetime
        :param message: The result message for each threat assessment.
        :type message: str
        :param result_type:
        :type result_type: str or ~identity_sign_ins.models.MicrosoftGraphThreatAssessmentResultType
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

        body = models.MicrosoftGraphThreatAssessmentResult(id=id, created_date_time=created_date_time, message=message, result_type=result_type)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_result.metadata['url']  # type: ignore
        path_format_arguments = {
            'threatAssessmentRequest-id': self._serialize.url("threat_assessment_request_id", threat_assessment_request_id, 'str'),
            'threatAssessmentResult-id': self._serialize.url("threat_assessment_result_id", threat_assessment_result_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphThreatAssessmentResult')
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

    update_result.metadata = {'url': '/informationProtection/threatAssessmentRequests/{threatAssessmentRequest-id}/results/{threatAssessmentResult-id}'}  # type: ignore

    def delete_result(
        self,
        threat_assessment_request_id,  # type: str
        threat_assessment_result_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property results for informationProtection.

        Delete navigation property results for informationProtection.

        :param threat_assessment_request_id: key: id of threatAssessmentRequest.
        :type threat_assessment_request_id: str
        :param threat_assessment_result_id: key: id of threatAssessmentResult.
        :type threat_assessment_result_id: str
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
        url = self.delete_result.metadata['url']  # type: ignore
        path_format_arguments = {
            'threatAssessmentRequest-id': self._serialize.url("threat_assessment_request_id", threat_assessment_request_id, 'str'),
            'threatAssessmentResult-id': self._serialize.url("threat_assessment_result_id", threat_assessment_result_id, 'str'),
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

    delete_result.metadata = {'url': '/informationProtection/threatAssessmentRequests/{threatAssessmentRequest-id}/results/{threatAssessmentResult-id}'}  # type: ignore