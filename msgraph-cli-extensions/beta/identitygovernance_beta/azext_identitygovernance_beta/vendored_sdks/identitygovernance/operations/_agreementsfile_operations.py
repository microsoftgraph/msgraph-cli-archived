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
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class agreementsfileOperations(object):
    """agreementsfileOperations operations.

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

    def list_localizations(
        self,
        agreement_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum30"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum31"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.collectionofagreementfilelocalization"]
        """Get localizations from agreements.

        Get localizations from agreements.

        :param agreement_id: key: id of agreement.
        :type agreement_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_governance.models.Enum30]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum31]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either collectionofagreementfilelocalization or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~identity_governance.models.collectionofagreementfilelocalization]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.collectionofagreementfilelocalization"]
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
                url = self.list_localizations.metadata['url']  # type: ignore
                path_format_arguments = {
                    'agreement-id': self._serialize.url("agreement_id", agreement_id, 'str'),
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
            deserialized = self._deserialize('collectionofagreementfilelocalization', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.odataerror, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_localizations.metadata = {'url': '/agreements/{agreement-id}/file/localizations'}  # type: ignore

    def create_localizations(
        self,
        agreement_id,  # type: str
        body,  # type: "models.microsoftgraphagreementfilelocalization"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphagreementfilelocalization"
        """Create new navigation property to localizations for agreements.

        Create new navigation property to localizations for agreements.

        :param agreement_id: key: id of agreement.
        :type agreement_id: str
        :param body: New navigation property.
        :type body: ~identity_governance.models.microsoftgraphagreementfilelocalization
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphagreementfilelocalization, or the result of cls(response)
        :rtype: ~identity_governance.models.microsoftgraphagreementfilelocalization
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphagreementfilelocalization"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_localizations.metadata['url']  # type: ignore
        path_format_arguments = {
            'agreement-id': self._serialize.url("agreement_id", agreement_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphagreementfilelocalization')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphagreementfilelocalization', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_localizations.metadata = {'url': '/agreements/{agreement-id}/file/localizations'}  # type: ignore

    def get_localizations(
        self,
        agreement_id,  # type: str
        agreement_file_localization_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum32"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphagreementfilelocalization"
        """Get localizations from agreements.

        Get localizations from agreements.

        :param agreement_id: key: id of agreement.
        :type agreement_id: str
        :param agreement_file_localization_id: key: id of agreementFileLocalization.
        :type agreement_file_localization_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_governance.models.Enum32]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphagreementfilelocalization, or the result of cls(response)
        :rtype: ~identity_governance.models.microsoftgraphagreementfilelocalization
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphagreementfilelocalization"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_localizations.metadata['url']  # type: ignore
        path_format_arguments = {
            'agreement-id': self._serialize.url("agreement_id", agreement_id, 'str'),
            'agreementFileLocalization-id': self._serialize.url("agreement_file_localization_id", agreement_file_localization_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphagreementfilelocalization', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_localizations.metadata = {'url': '/agreements/{agreement-id}/file/localizations/{agreementFileLocalization-id}'}  # type: ignore

    def update_localizations(
        self,
        agreement_id,  # type: str
        agreement_file_localization_id,  # type: str
        body,  # type: "models.microsoftgraphagreementfilelocalization"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property localizations in agreements.

        Update the navigation property localizations in agreements.

        :param agreement_id: key: id of agreement.
        :type agreement_id: str
        :param agreement_file_localization_id: key: id of agreementFileLocalization.
        :type agreement_file_localization_id: str
        :param body: New navigation property values.
        :type body: ~identity_governance.models.microsoftgraphagreementfilelocalization
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
        url = self.update_localizations.metadata['url']  # type: ignore
        path_format_arguments = {
            'agreement-id': self._serialize.url("agreement_id", agreement_id, 'str'),
            'agreementFileLocalization-id': self._serialize.url("agreement_file_localization_id", agreement_file_localization_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphagreementfilelocalization')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_localizations.metadata = {'url': '/agreements/{agreement-id}/file/localizations/{agreementFileLocalization-id}'}  # type: ignore

    def delete_localizations(
        self,
        agreement_id,  # type: str
        agreement_file_localization_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property localizations for agreements.

        Delete navigation property localizations for agreements.

        :param agreement_id: key: id of agreement.
        :type agreement_id: str
        :param agreement_file_localization_id: key: id of agreementFileLocalization.
        :type agreement_file_localization_id: str
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
        url = self.delete_localizations.metadata['url']  # type: ignore
        path_format_arguments = {
            'agreement-id': self._serialize.url("agreement_id", agreement_id, 'str'),
            'agreementFileLocalization-id': self._serialize.url("agreement_file_localization_id", agreement_file_localization_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_localizations.metadata = {'url': '/agreements/{agreement-id}/file/localizations/{agreementFileLocalization-id}'}  # type: ignore
