# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FinancialCompanyGeneralLedgerEntryOperations:
    """FinancialCompanyGeneralLedgerEntryOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~financials.models
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

    async def get_account(
        self,
        company_id: str,
        general_ledger_entry_id: str,
        select: Optional[List[Union[str, "models.Enum94"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphAccount":
        """Get account from financials.

        Get account from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param general_ledger_entry_id: key: id of generalLedgerEntry.
        :type general_ledger_entry_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum94]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphAccount, or the result of cls(response)
        :rtype: ~financials.models.MicrosoftGraphAccount
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphAccount"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_account.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'generalLedgerEntry-id': self._serialize.url("general_ledger_entry_id", general_ledger_entry_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphAccount', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_account.metadata = {'url': '/financials/companies/{company-id}/generalLedgerEntries/{generalLedgerEntry-id}/account'}  # type: ignore

    async def update_account(
        self,
        company_id: str,
        general_ledger_entry_id: str,
        id: Optional[str] = None,
        blocked: Optional[bool] = None,
        category: Optional[str] = None,
        display_name: Optional[str] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        number: Optional[str] = None,
        sub_category: Optional[str] = None,
        **kwargs
    ) -> None:
        """Update the navigation property account in financials.

        Update the navigation property account in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param general_ledger_entry_id: key: id of generalLedgerEntry.
        :type general_ledger_entry_id: str
        :param id: Read-only.
        :type id: str
        :param blocked:
        :type blocked: bool
        :param category:
        :type category: str
        :param display_name:
        :type display_name: str
        :param last_modified_date_time:
        :type last_modified_date_time: ~datetime.datetime
        :param number:
        :type number: str
        :param sub_category:
        :type sub_category: str
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

        body = models.MicrosoftGraphAccount(id=id, blocked=blocked, category=category, display_name=display_name, last_modified_date_time=last_modified_date_time, number=number, sub_category=sub_category)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_account.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'generalLedgerEntry-id': self._serialize.url("general_ledger_entry_id", general_ledger_entry_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphAccount')
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

    update_account.metadata = {'url': '/financials/companies/{company-id}/generalLedgerEntries/{generalLedgerEntry-id}/account'}  # type: ignore

    async def delete_account(
        self,
        company_id: str,
        general_ledger_entry_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property account for financials.

        Delete navigation property account for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param general_ledger_entry_id: key: id of generalLedgerEntry.
        :type general_ledger_entry_id: str
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
        url = self.delete_account.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'generalLedgerEntry-id': self._serialize.url("general_ledger_entry_id", general_ledger_entry_id, 'str'),
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

    delete_account.metadata = {'url': '/financials/companies/{company-id}/generalLedgerEntries/{generalLedgerEntry-id}/account'}  # type: ignore