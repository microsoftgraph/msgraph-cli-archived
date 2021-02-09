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

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FinancialCompanyCustomerPaymentJournalCustomerPaymentOperations:
    """FinancialCompanyCustomerPaymentJournalCustomerPaymentOperations async operations.

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

    async def get_customer(
        self,
        company_id: str,
        customer_payment_journal_id: str,
        customer_payment_id: str,
        select: Optional[List[Union[str, "models.Enum35"]]] = None,
        expand: Optional[List[Union[str, "models.Enum36"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphCustomer":
        """Get customer from financials.

        Get customer from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param customer_payment_journal_id: key: id of customerPaymentJournal.
        :type customer_payment_journal_id: str
        :param customer_payment_id: key: id of customerPayment.
        :type customer_payment_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum35]
        :param expand: Expand related entities.
        :type expand: list[str or ~financials.models.Enum36]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphCustomer, or the result of cls(response)
        :rtype: ~financials.models.MicrosoftGraphCustomer
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphCustomer"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_customer.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'customerPaymentJournal-id': self._serialize.url("customer_payment_journal_id", customer_payment_journal_id, 'str'),
            'customerPayment-id': self._serialize.url("customer_payment_id", customer_payment_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphCustomer', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_customer.metadata = {'url': '/financials/companies/{company-id}/customerPaymentJournals/{customerPaymentJournal-id}/customerPayments/{customerPayment-id}/customer'}  # type: ignore

    async def update_customer(
        self,
        company_id: str,
        customer_payment_journal_id: str,
        customer_payment_id: str,
        id: Optional[str] = None,
        address: Optional["models.MicrosoftGraphPostalAddressType"] = None,
        blocked: Optional[str] = None,
        currency_code: Optional[str] = None,
        currency_id: Optional[str] = None,
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        number: Optional[str] = None,
        payment_method_id: Optional[str] = None,
        payment_terms_id: Optional[str] = None,
        phone_number: Optional[str] = None,
        shipment_method_id: Optional[str] = None,
        tax_area_display_name: Optional[str] = None,
        tax_area_id: Optional[str] = None,
        tax_liable: Optional[bool] = None,
        tax_registration_number: Optional[str] = None,
        type: Optional[str] = None,
        website: Optional[str] = None,
        currency: Optional["models.MicrosoftGraphCurrency"] = None,
        payment_method: Optional["models.MicrosoftGraphPaymentMethod"] = None,
        payment_term: Optional["models.MicrosoftGraphPaymentTerm"] = None,
        picture: Optional[List["models.MicrosoftGraphPicture"]] = None,
        shipment_method: Optional["models.MicrosoftGraphShipmentMethod"] = None,
        **kwargs
    ) -> None:
        """Update the navigation property customer in financials.

        Update the navigation property customer in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param customer_payment_journal_id: key: id of customerPaymentJournal.
        :type customer_payment_journal_id: str
        :param customer_payment_id: key: id of customerPayment.
        :type customer_payment_id: str
        :param id: Read-only.
        :type id: str
        :param address: postalAddressType.
        :type address: ~financials.models.MicrosoftGraphPostalAddressType
        :param blocked:
        :type blocked: str
        :param currency_code:
        :type currency_code: str
        :param currency_id:
        :type currency_id: str
        :param display_name:
        :type display_name: str
        :param email:
        :type email: str
        :param last_modified_date_time:
        :type last_modified_date_time: ~datetime.datetime
        :param number:
        :type number: str
        :param payment_method_id:
        :type payment_method_id: str
        :param payment_terms_id:
        :type payment_terms_id: str
        :param phone_number:
        :type phone_number: str
        :param shipment_method_id:
        :type shipment_method_id: str
        :param tax_area_display_name:
        :type tax_area_display_name: str
        :param tax_area_id:
        :type tax_area_id: str
        :param tax_liable:
        :type tax_liable: bool
        :param tax_registration_number:
        :type tax_registration_number: str
        :param type:
        :type type: str
        :param website:
        :type website: str
        :param currency: currency.
        :type currency: ~financials.models.MicrosoftGraphCurrency
        :param payment_method: paymentMethod.
        :type payment_method: ~financials.models.MicrosoftGraphPaymentMethod
        :param payment_term: paymentTerm.
        :type payment_term: ~financials.models.MicrosoftGraphPaymentTerm
        :param picture:
        :type picture: list[~financials.models.MicrosoftGraphPicture]
        :param shipment_method: shipmentMethod.
        :type shipment_method: ~financials.models.MicrosoftGraphShipmentMethod
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphCustomer(id=id, address=address, blocked=blocked, currency_code=currency_code, currency_id=currency_id, display_name=display_name, email=email, last_modified_date_time=last_modified_date_time, number=number, payment_method_id=payment_method_id, payment_terms_id=payment_terms_id, phone_number=phone_number, shipment_method_id=shipment_method_id, tax_area_display_name=tax_area_display_name, tax_area_id=tax_area_id, tax_liable=tax_liable, tax_registration_number=tax_registration_number, type=type, website=website, currency=currency, payment_method=payment_method, payment_term=payment_term, picture=picture, shipment_method=shipment_method)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_customer.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'customerPaymentJournal-id': self._serialize.url("customer_payment_journal_id", customer_payment_journal_id, 'str'),
            'customerPayment-id': self._serialize.url("customer_payment_id", customer_payment_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphCustomer')
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

    update_customer.metadata = {'url': '/financials/companies/{company-id}/customerPaymentJournals/{customerPaymentJournal-id}/customerPayments/{customerPayment-id}/customer'}  # type: ignore

    async def delete_customer(
        self,
        company_id: str,
        customer_payment_journal_id: str,
        customer_payment_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property customer for financials.

        Delete navigation property customer for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param customer_payment_journal_id: key: id of customerPaymentJournal.
        :type customer_payment_journal_id: str
        :param customer_payment_id: key: id of customerPayment.
        :type customer_payment_id: str
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
        url = self.delete_customer.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'customerPaymentJournal-id': self._serialize.url("customer_payment_journal_id", customer_payment_journal_id, 'str'),
            'customerPayment-id': self._serialize.url("customer_payment_id", customer_payment_id, 'str'),
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

    delete_customer.metadata = {'url': '/financials/companies/{company-id}/customerPaymentJournals/{customerPaymentJournal-id}/customerPayments/{customerPayment-id}/customer'}  # type: ignore