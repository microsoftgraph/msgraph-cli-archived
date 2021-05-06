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
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class RiskyUsersOperations(object):
    """RiskyUsersOperations operations.

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

    def list_history(
        self,
        risky_user_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum266"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum267"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum268"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfRiskyUserHistoryItem"]
        """Get history from riskyUsers.

        Get history from riskyUsers.

        :param risky_user_id: key: id of riskyUser.
        :type risky_user_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_sign_ins.models.Enum266]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum267]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_sign_ins.models.Enum268]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfRiskyUserHistoryItem or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~identity_sign_ins.models.CollectionOfRiskyUserHistoryItem]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfRiskyUserHistoryItem"]
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
                url = self.list_history.metadata['url']  # type: ignore
                path_format_arguments = {
                    'riskyUser-id': self._serialize.url("risky_user_id", risky_user_id, 'str'),
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
            deserialized = self._deserialize('CollectionOfRiskyUserHistoryItem', pipeline_response)
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
    list_history.metadata = {'url': '/riskyUsers/{riskyUser-id}/history'}  # type: ignore

    def create_history(
        self,
        risky_user_id,  # type: str
        body,  # type: "models.MicrosoftGraphRiskyUserHistoryItem"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphRiskyUserHistoryItem"
        """Create new navigation property to history for riskyUsers.

        Create new navigation property to history for riskyUsers.

        :param risky_user_id: key: id of riskyUser.
        :type risky_user_id: str
        :param body: New navigation property.
        :type body: ~identity_sign_ins.models.MicrosoftGraphRiskyUserHistoryItem
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphRiskyUserHistoryItem, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphRiskyUserHistoryItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphRiskyUserHistoryItem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_history.metadata['url']  # type: ignore
        path_format_arguments = {
            'riskyUser-id': self._serialize.url("risky_user_id", risky_user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphRiskyUserHistoryItem')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphRiskyUserHistoryItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_history.metadata = {'url': '/riskyUsers/{riskyUser-id}/history'}  # type: ignore

    def get_history(
        self,
        risky_user_id,  # type: str
        risky_user_history_item_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum269"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum270"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphRiskyUserHistoryItem"
        """Get history from riskyUsers.

        Get history from riskyUsers.

        :param risky_user_id: key: id of riskyUser.
        :type risky_user_id: str
        :param risky_user_history_item_id: key: id of riskyUserHistoryItem.
        :type risky_user_history_item_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum269]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_sign_ins.models.Enum270]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphRiskyUserHistoryItem, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphRiskyUserHistoryItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphRiskyUserHistoryItem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_history.metadata['url']  # type: ignore
        path_format_arguments = {
            'riskyUser-id': self._serialize.url("risky_user_id", risky_user_id, 'str'),
            'riskyUserHistoryItem-id': self._serialize.url("risky_user_history_item_id", risky_user_history_item_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphRiskyUserHistoryItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_history.metadata = {'url': '/riskyUsers/{riskyUser-id}/history/{riskyUserHistoryItem-id}'}  # type: ignore

    def update_history(
        self,
        risky_user_id,  # type: str
        risky_user_history_item_id,  # type: str
        body,  # type: "models.MicrosoftGraphRiskyUserHistoryItem"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property history in riskyUsers.

        Update the navigation property history in riskyUsers.

        :param risky_user_id: key: id of riskyUser.
        :type risky_user_id: str
        :param risky_user_history_item_id: key: id of riskyUserHistoryItem.
        :type risky_user_history_item_id: str
        :param body: New navigation property values.
        :type body: ~identity_sign_ins.models.MicrosoftGraphRiskyUserHistoryItem
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
        url = self.update_history.metadata['url']  # type: ignore
        path_format_arguments = {
            'riskyUser-id': self._serialize.url("risky_user_id", risky_user_id, 'str'),
            'riskyUserHistoryItem-id': self._serialize.url("risky_user_history_item_id", risky_user_history_item_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphRiskyUserHistoryItem')
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

    update_history.metadata = {'url': '/riskyUsers/{riskyUser-id}/history/{riskyUserHistoryItem-id}'}  # type: ignore

    def delete_history(
        self,
        risky_user_id,  # type: str
        risky_user_history_item_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property history for riskyUsers.

        Delete navigation property history for riskyUsers.

        :param risky_user_id: key: id of riskyUser.
        :type risky_user_id: str
        :param risky_user_history_item_id: key: id of riskyUserHistoryItem.
        :type risky_user_history_item_id: str
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
        url = self.delete_history.metadata['url']  # type: ignore
        path_format_arguments = {
            'riskyUser-id': self._serialize.url("risky_user_id", risky_user_id, 'str'),
            'riskyUserHistoryItem-id': self._serialize.url("risky_user_history_item_id", risky_user_history_item_id, 'str'),
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

    delete_history.metadata = {'url': '/riskyUsers/{riskyUser-id}/history/{riskyUserHistoryItem-id}'}  # type: ignore

    def confirm_compromised(
        self,
        body,  # type: "models.PathsL8Oa4IRiskyusersMicrosoftGraphConfirmcompromisedPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action confirmCompromised.

        Invoke action confirmCompromised.

        :param body: Action parameters.
        :type body: ~identity_sign_ins.models.PathsL8Oa4IRiskyusersMicrosoftGraphConfirmcompromisedPostRequestbodyContentApplicationJsonSchema
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
        url = self.confirm_compromised.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsL8Oa4IRiskyusersMicrosoftGraphConfirmcompromisedPostRequestbodyContentApplicationJsonSchema')
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

    confirm_compromised.metadata = {'url': '/riskyUsers/microsoft.graph.confirmCompromised'}  # type: ignore

    def dismiss(
        self,
        body,  # type: "models.PathsTai6NqRiskyusersMicrosoftGraphDismissPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action dismiss.

        Invoke action dismiss.

        :param body: Action parameters.
        :type body: ~identity_sign_ins.models.PathsTai6NqRiskyusersMicrosoftGraphDismissPostRequestbodyContentApplicationJsonSchema
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
        url = self.dismiss.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsTai6NqRiskyusersMicrosoftGraphDismissPostRequestbodyContentApplicationJsonSchema')
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

    dismiss.metadata = {'url': '/riskyUsers/microsoft.graph.dismiss'}  # type: ignore
