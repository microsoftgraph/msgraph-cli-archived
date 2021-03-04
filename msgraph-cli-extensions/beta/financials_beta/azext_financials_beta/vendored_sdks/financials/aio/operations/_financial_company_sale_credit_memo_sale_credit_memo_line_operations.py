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

class FinancialCompanySaleCreditMemoSaleCreditMemoLineOperations:
    """FinancialCompanySaleCreditMemoSaleCreditMemoLineOperations async operations.

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
        sales_credit_memo_id: str,
        sales_credit_memo_line_id: str,
        select: Optional[List[Union[str, "models.Enum205"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphAccount":
        """Get account from financials.

        Get account from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_credit_memo_id: key: id of salesCreditMemo.
        :type sales_credit_memo_id: str
        :param sales_credit_memo_line_id: key: id of salesCreditMemoLine.
        :type sales_credit_memo_line_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum205]
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
            'salesCreditMemo-id': self._serialize.url("sales_credit_memo_id", sales_credit_memo_id, 'str'),
            'salesCreditMemoLine-id': self._serialize.url("sales_credit_memo_line_id", sales_credit_memo_line_id, 'str'),
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
    get_account.metadata = {'url': '/financials/companies/{company-id}/salesCreditMemos/{salesCreditMemo-id}/salesCreditMemoLines/{salesCreditMemoLine-id}/account'}  # type: ignore

    async def update_account(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        sales_credit_memo_line_id: str,
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
        :param sales_credit_memo_id: key: id of salesCreditMemo.
        :type sales_credit_memo_id: str
        :param sales_credit_memo_line_id: key: id of salesCreditMemoLine.
        :type sales_credit_memo_line_id: str
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
            'salesCreditMemo-id': self._serialize.url("sales_credit_memo_id", sales_credit_memo_id, 'str'),
            'salesCreditMemoLine-id': self._serialize.url("sales_credit_memo_line_id", sales_credit_memo_line_id, 'str'),
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

    update_account.metadata = {'url': '/financials/companies/{company-id}/salesCreditMemos/{salesCreditMemo-id}/salesCreditMemoLines/{salesCreditMemoLine-id}/account'}  # type: ignore

    async def delete_account(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        sales_credit_memo_line_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property account for financials.

        Delete navigation property account for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_credit_memo_id: key: id of salesCreditMemo.
        :type sales_credit_memo_id: str
        :param sales_credit_memo_line_id: key: id of salesCreditMemoLine.
        :type sales_credit_memo_line_id: str
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
            'salesCreditMemo-id': self._serialize.url("sales_credit_memo_id", sales_credit_memo_id, 'str'),
            'salesCreditMemoLine-id': self._serialize.url("sales_credit_memo_line_id", sales_credit_memo_line_id, 'str'),
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

    delete_account.metadata = {'url': '/financials/companies/{company-id}/salesCreditMemos/{salesCreditMemo-id}/salesCreditMemoLines/{salesCreditMemoLine-id}/account'}  # type: ignore

    async def get_item(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        sales_credit_memo_line_id: str,
        select: Optional[List[Union[str, "models.Enum206"]]] = None,
        expand: Optional[List[Union[str, "models.Enum207"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphItem":
        """Get item from financials.

        Get item from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_credit_memo_id: key: id of salesCreditMemo.
        :type sales_credit_memo_id: str
        :param sales_credit_memo_line_id: key: id of salesCreditMemoLine.
        :type sales_credit_memo_line_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum206]
        :param expand: Expand related entities.
        :type expand: list[str or ~financials.models.Enum207]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphItem, or the result of cls(response)
        :rtype: ~financials.models.MicrosoftGraphItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphItem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesCreditMemo-id': self._serialize.url("sales_credit_memo_id", sales_credit_memo_id, 'str'),
            'salesCreditMemoLine-id': self._serialize.url("sales_credit_memo_line_id", sales_credit_memo_line_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_item.metadata = {'url': '/financials/companies/{company-id}/salesCreditMemos/{salesCreditMemo-id}/salesCreditMemoLines/{salesCreditMemoLine-id}/item'}  # type: ignore

    async def update_item(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        sales_credit_memo_line_id: str,
        id: Optional[str] = None,
        base_unit_of_measure_id: Optional[str] = None,
        blocked: Optional[bool] = None,
        display_name: Optional[str] = None,
        gtin: Optional[str] = None,
        inventory: Optional[float] = None,
        item_category_code: Optional[str] = None,
        item_category_id: Optional[str] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        number: Optional[str] = None,
        price_includes_tax: Optional[bool] = None,
        tax_group_code: Optional[str] = None,
        tax_group_id: Optional[str] = None,
        type: Optional[str] = None,
        unit_cost: Optional[float] = None,
        unit_price: Optional[float] = None,
        item_category: Optional["models.MicrosoftGraphItemCategory"] = None,
        picture: Optional[List["models.MicrosoftGraphPicture"]] = None,
        **kwargs
    ) -> None:
        """Update the navigation property item in financials.

        Update the navigation property item in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_credit_memo_id: key: id of salesCreditMemo.
        :type sales_credit_memo_id: str
        :param sales_credit_memo_line_id: key: id of salesCreditMemoLine.
        :type sales_credit_memo_line_id: str
        :param id: Read-only.
        :type id: str
        :param base_unit_of_measure_id:
        :type base_unit_of_measure_id: str
        :param blocked:
        :type blocked: bool
        :param display_name:
        :type display_name: str
        :param gtin:
        :type gtin: str
        :param inventory:
        :type inventory: float
        :param item_category_code:
        :type item_category_code: str
        :param item_category_id:
        :type item_category_id: str
        :param last_modified_date_time:
        :type last_modified_date_time: ~datetime.datetime
        :param number:
        :type number: str
        :param price_includes_tax:
        :type price_includes_tax: bool
        :param tax_group_code:
        :type tax_group_code: str
        :param tax_group_id:
        :type tax_group_id: str
        :param type:
        :type type: str
        :param unit_cost:
        :type unit_cost: float
        :param unit_price:
        :type unit_price: float
        :param item_category: itemCategory.
        :type item_category: ~financials.models.MicrosoftGraphItemCategory
        :param picture:
        :type picture: list[~financials.models.MicrosoftGraphPicture]
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

        body = models.MicrosoftGraphItem(id=id, base_unit_of_measure_id=base_unit_of_measure_id, blocked=blocked, display_name=display_name, gtin=gtin, inventory=inventory, item_category_code=item_category_code, item_category_id=item_category_id, last_modified_date_time=last_modified_date_time, number=number, price_includes_tax=price_includes_tax, tax_group_code=tax_group_code, tax_group_id=tax_group_id, type=type, unit_cost=unit_cost, unit_price=unit_price, item_category=item_category, picture=picture)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesCreditMemo-id': self._serialize.url("sales_credit_memo_id", sales_credit_memo_id, 'str'),
            'salesCreditMemoLine-id': self._serialize.url("sales_credit_memo_line_id", sales_credit_memo_line_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphItem')
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

    update_item.metadata = {'url': '/financials/companies/{company-id}/salesCreditMemos/{salesCreditMemo-id}/salesCreditMemoLines/{salesCreditMemoLine-id}/item'}  # type: ignore

    async def delete_item(
        self,
        company_id: str,
        sales_credit_memo_id: str,
        sales_credit_memo_line_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property item for financials.

        Delete navigation property item for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_credit_memo_id: key: id of salesCreditMemo.
        :type sales_credit_memo_id: str
        :param sales_credit_memo_line_id: key: id of salesCreditMemoLine.
        :type sales_credit_memo_line_id: str
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
        url = self.delete_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesCreditMemo-id': self._serialize.url("sales_credit_memo_id", sales_credit_memo_id, 'str'),
            'salesCreditMemoLine-id': self._serialize.url("sales_credit_memo_line_id", sales_credit_memo_line_id, 'str'),
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

    delete_item.metadata = {'url': '/financials/companies/{company-id}/salesCreditMemos/{salesCreditMemo-id}/salesCreditMemoLines/{salesCreditMemoLine-id}/item'}  # type: ignore
