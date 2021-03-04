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

class FinancialOperations(object):
    """FinancialOperations operations.

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

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_company(
        self,
        orderby=None,  # type: Optional[List[Union[str, "models.Get5ItemsItem"]]]
        select=None,  # type: Optional[List[Union[str, "models.Get6ItemsItem"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get7ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfCompany"]
        """Get companies from financials.

        Get companies from financials.

        :param orderby: Order items by property values.
        :type orderby: list[str or ~financials.models.Get5ItemsItem]
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Get6ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~financials.models.Get7ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfCompany or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~financials.models.CollectionOfCompany]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfCompany"]
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
                url = self.list_company.metadata['url']  # type: ignore
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
            deserialized = self._deserialize('CollectionOfCompany', pipeline_response)
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
    list_company.metadata = {'url': '/financials/companies'}  # type: ignore

    def create_company(
        self,
        id=None,  # type: Optional[str]
        business_profile_id=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        name=None,  # type: Optional[str]
        system_version=None,  # type: Optional[str]
        accounts=None,  # type: Optional[List["models.MicrosoftGraphAccount"]]
        aged_accounts_payable=None,  # type: Optional[List["models.MicrosoftGraphAgedAccountsPayable"]]
        aged_accounts_receivable=None,  # type: Optional[List["models.MicrosoftGraphAgedAccountsReceivable"]]
        company_information=None,  # type: Optional[List["models.MicrosoftGraphCompanyInformation"]]
        countries_regions=None,  # type: Optional[List["models.MicrosoftGraphCountryRegion"]]
        currencies=None,  # type: Optional[List["models.MicrosoftGraphCurrency"]]
        customer_payment_journals=None,  # type: Optional[List["models.MicrosoftGraphCustomerPaymentJournal"]]
        customer_payments=None,  # type: Optional[List["models.MicrosoftGraphCustomerPayment"]]
        customers=None,  # type: Optional[List["models.MicrosoftGraphCustomer"]]
        dimensions=None,  # type: Optional[List["models.MicrosoftGraphDimension"]]
        dimension_values=None,  # type: Optional[List["models.MicrosoftGraphDimensionValue"]]
        employees=None,  # type: Optional[List["models.MicrosoftGraphEmployee"]]
        general_ledger_entries=None,  # type: Optional[List["models.MicrosoftGraphGeneralLedgerEntry"]]
        item_categories=None,  # type: Optional[List["models.MicrosoftGraphItemCategory"]]
        items=None,  # type: Optional[List["models.MicrosoftGraphItem"]]
        journal_lines=None,  # type: Optional[List["models.MicrosoftGraphJournalLine"]]
        journals=None,  # type: Optional[List["models.MicrosoftGraphJournal"]]
        payment_methods=None,  # type: Optional[List["models.MicrosoftGraphPaymentMethod"]]
        payment_terms=None,  # type: Optional[List["models.MicrosoftGraphPaymentTerm"]]
        picture=None,  # type: Optional[List["models.MicrosoftGraphPicture"]]
        purchase_invoice_lines=None,  # type: Optional[List["models.MicrosoftGraphPurchaseInvoiceLine"]]
        purchase_invoices=None,  # type: Optional[List["models.MicrosoftGraphPurchaseInvoice"]]
        sales_credit_memo_lines=None,  # type: Optional[List["models.MicrosoftGraphSalesCreditMemoLine"]]
        sales_credit_memos=None,  # type: Optional[List["models.MicrosoftGraphSalesCreditMemo"]]
        sales_invoice_lines=None,  # type: Optional[List["models.MicrosoftGraphSalesInvoiceLine"]]
        sales_invoices=None,  # type: Optional[List["models.MicrosoftGraphSalesInvoice"]]
        sales_order_lines=None,  # type: Optional[List["models.MicrosoftGraphSalesOrderLine"]]
        sales_orders=None,  # type: Optional[List["models.MicrosoftGraphSalesOrder"]]
        sales_quote_lines=None,  # type: Optional[List["models.MicrosoftGraphSalesQuoteLine"]]
        sales_quotes=None,  # type: Optional[List["models.MicrosoftGraphSalesQuote"]]
        shipment_methods=None,  # type: Optional[List["models.MicrosoftGraphShipmentMethod"]]
        tax_areas=None,  # type: Optional[List["models.MicrosoftGraphTaxArea"]]
        tax_groups=None,  # type: Optional[List["models.MicrosoftGraphTaxGroup"]]
        units_of_measure=None,  # type: Optional[List["models.MicrosoftGraphUnitOfMeasure"]]
        vendors=None,  # type: Optional[List["models.MicrosoftGraphVendor"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphCompany"
        """Create new navigation property to companies for financials.

        Create new navigation property to companies for financials.

        :param id: Read-only.
        :type id: str
        :param business_profile_id:
        :type business_profile_id: str
        :param display_name:
        :type display_name: str
        :param name:
        :type name: str
        :param system_version:
        :type system_version: str
        :param accounts:
        :type accounts: list[~financials.models.MicrosoftGraphAccount]
        :param aged_accounts_payable:
        :type aged_accounts_payable: list[~financials.models.MicrosoftGraphAgedAccountsPayable]
        :param aged_accounts_receivable:
        :type aged_accounts_receivable: list[~financials.models.MicrosoftGraphAgedAccountsReceivable]
        :param company_information:
        :type company_information: list[~financials.models.MicrosoftGraphCompanyInformation]
        :param countries_regions:
        :type countries_regions: list[~financials.models.MicrosoftGraphCountryRegion]
        :param currencies:
        :type currencies: list[~financials.models.MicrosoftGraphCurrency]
        :param customer_payment_journals:
        :type customer_payment_journals: list[~financials.models.MicrosoftGraphCustomerPaymentJournal]
        :param customer_payments:
        :type customer_payments: list[~financials.models.MicrosoftGraphCustomerPayment]
        :param customers:
        :type customers: list[~financials.models.MicrosoftGraphCustomer]
        :param dimensions:
        :type dimensions: list[~financials.models.MicrosoftGraphDimension]
        :param dimension_values:
        :type dimension_values: list[~financials.models.MicrosoftGraphDimensionValue]
        :param employees:
        :type employees: list[~financials.models.MicrosoftGraphEmployee]
        :param general_ledger_entries:
        :type general_ledger_entries: list[~financials.models.MicrosoftGraphGeneralLedgerEntry]
        :param item_categories:
        :type item_categories: list[~financials.models.MicrosoftGraphItemCategory]
        :param items:
        :type items: list[~financials.models.MicrosoftGraphItem]
        :param journal_lines:
        :type journal_lines: list[~financials.models.MicrosoftGraphJournalLine]
        :param journals:
        :type journals: list[~financials.models.MicrosoftGraphJournal]
        :param payment_methods:
        :type payment_methods: list[~financials.models.MicrosoftGraphPaymentMethod]
        :param payment_terms:
        :type payment_terms: list[~financials.models.MicrosoftGraphPaymentTerm]
        :param picture:
        :type picture: list[~financials.models.MicrosoftGraphPicture]
        :param purchase_invoice_lines:
        :type purchase_invoice_lines: list[~financials.models.MicrosoftGraphPurchaseInvoiceLine]
        :param purchase_invoices:
        :type purchase_invoices: list[~financials.models.MicrosoftGraphPurchaseInvoice]
        :param sales_credit_memo_lines:
        :type sales_credit_memo_lines: list[~financials.models.MicrosoftGraphSalesCreditMemoLine]
        :param sales_credit_memos:
        :type sales_credit_memos: list[~financials.models.MicrosoftGraphSalesCreditMemo]
        :param sales_invoice_lines:
        :type sales_invoice_lines: list[~financials.models.MicrosoftGraphSalesInvoiceLine]
        :param sales_invoices:
        :type sales_invoices: list[~financials.models.MicrosoftGraphSalesInvoice]
        :param sales_order_lines:
        :type sales_order_lines: list[~financials.models.MicrosoftGraphSalesOrderLine]
        :param sales_orders:
        :type sales_orders: list[~financials.models.MicrosoftGraphSalesOrder]
        :param sales_quote_lines:
        :type sales_quote_lines: list[~financials.models.MicrosoftGraphSalesQuoteLine]
        :param sales_quotes:
        :type sales_quotes: list[~financials.models.MicrosoftGraphSalesQuote]
        :param shipment_methods:
        :type shipment_methods: list[~financials.models.MicrosoftGraphShipmentMethod]
        :param tax_areas:
        :type tax_areas: list[~financials.models.MicrosoftGraphTaxArea]
        :param tax_groups:
        :type tax_groups: list[~financials.models.MicrosoftGraphTaxGroup]
        :param units_of_measure:
        :type units_of_measure: list[~financials.models.MicrosoftGraphUnitOfMeasure]
        :param vendors:
        :type vendors: list[~financials.models.MicrosoftGraphVendor]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphCompany, or the result of cls(response)
        :rtype: ~financials.models.MicrosoftGraphCompany
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphCompany"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.MicrosoftGraphCompany(id=id, business_profile_id=business_profile_id, display_name=display_name, name=name, system_version=system_version, accounts=accounts, aged_accounts_payable=aged_accounts_payable, aged_accounts_receivable=aged_accounts_receivable, company_information=company_information, countries_regions=countries_regions, currencies=currencies, customer_payment_journals=customer_payment_journals, customer_payments=customer_payments, customers=customers, dimensions=dimensions, dimension_values=dimension_values, employees=employees, general_ledger_entries=general_ledger_entries, item_categories=item_categories, items=items, journal_lines=journal_lines, journals=journals, payment_methods=payment_methods, payment_terms=payment_terms, picture=picture, purchase_invoice_lines=purchase_invoice_lines, purchase_invoices=purchase_invoices, sales_credit_memo_lines=sales_credit_memo_lines, sales_credit_memos=sales_credit_memos, sales_invoice_lines=sales_invoice_lines, sales_invoices=sales_invoices, sales_order_lines=sales_order_lines, sales_orders=sales_orders, sales_quote_lines=sales_quote_lines, sales_quotes=sales_quotes, shipment_methods=shipment_methods, tax_areas=tax_areas, tax_groups=tax_groups, units_of_measure=units_of_measure, vendors=vendors)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_company.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphCompany')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphCompany', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_company.metadata = {'url': '/financials/companies'}  # type: ignore

    def get_company(
        self,
        company_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum4"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get2ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphCompany"
        """Get companies from financials.

        Get companies from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum4]
        :param expand: Expand related entities.
        :type expand: list[str or ~financials.models.Get2ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphCompany, or the result of cls(response)
        :rtype: ~financials.models.MicrosoftGraphCompany
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphCompany"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_company.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphCompany', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_company.metadata = {'url': '/financials/companies/{company-id}'}  # type: ignore

    def update_company(
        self,
        company_id,  # type: str
        id=None,  # type: Optional[str]
        business_profile_id=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        name=None,  # type: Optional[str]
        system_version=None,  # type: Optional[str]
        accounts=None,  # type: Optional[List["models.MicrosoftGraphAccount"]]
        aged_accounts_payable=None,  # type: Optional[List["models.MicrosoftGraphAgedAccountsPayable"]]
        aged_accounts_receivable=None,  # type: Optional[List["models.MicrosoftGraphAgedAccountsReceivable"]]
        company_information=None,  # type: Optional[List["models.MicrosoftGraphCompanyInformation"]]
        countries_regions=None,  # type: Optional[List["models.MicrosoftGraphCountryRegion"]]
        currencies=None,  # type: Optional[List["models.MicrosoftGraphCurrency"]]
        customer_payment_journals=None,  # type: Optional[List["models.MicrosoftGraphCustomerPaymentJournal"]]
        customer_payments=None,  # type: Optional[List["models.MicrosoftGraphCustomerPayment"]]
        customers=None,  # type: Optional[List["models.MicrosoftGraphCustomer"]]
        dimensions=None,  # type: Optional[List["models.MicrosoftGraphDimension"]]
        dimension_values=None,  # type: Optional[List["models.MicrosoftGraphDimensionValue"]]
        employees=None,  # type: Optional[List["models.MicrosoftGraphEmployee"]]
        general_ledger_entries=None,  # type: Optional[List["models.MicrosoftGraphGeneralLedgerEntry"]]
        item_categories=None,  # type: Optional[List["models.MicrosoftGraphItemCategory"]]
        items=None,  # type: Optional[List["models.MicrosoftGraphItem"]]
        journal_lines=None,  # type: Optional[List["models.MicrosoftGraphJournalLine"]]
        journals=None,  # type: Optional[List["models.MicrosoftGraphJournal"]]
        payment_methods=None,  # type: Optional[List["models.MicrosoftGraphPaymentMethod"]]
        payment_terms=None,  # type: Optional[List["models.MicrosoftGraphPaymentTerm"]]
        picture=None,  # type: Optional[List["models.MicrosoftGraphPicture"]]
        purchase_invoice_lines=None,  # type: Optional[List["models.MicrosoftGraphPurchaseInvoiceLine"]]
        purchase_invoices=None,  # type: Optional[List["models.MicrosoftGraphPurchaseInvoice"]]
        sales_credit_memo_lines=None,  # type: Optional[List["models.MicrosoftGraphSalesCreditMemoLine"]]
        sales_credit_memos=None,  # type: Optional[List["models.MicrosoftGraphSalesCreditMemo"]]
        sales_invoice_lines=None,  # type: Optional[List["models.MicrosoftGraphSalesInvoiceLine"]]
        sales_invoices=None,  # type: Optional[List["models.MicrosoftGraphSalesInvoice"]]
        sales_order_lines=None,  # type: Optional[List["models.MicrosoftGraphSalesOrderLine"]]
        sales_orders=None,  # type: Optional[List["models.MicrosoftGraphSalesOrder"]]
        sales_quote_lines=None,  # type: Optional[List["models.MicrosoftGraphSalesQuoteLine"]]
        sales_quotes=None,  # type: Optional[List["models.MicrosoftGraphSalesQuote"]]
        shipment_methods=None,  # type: Optional[List["models.MicrosoftGraphShipmentMethod"]]
        tax_areas=None,  # type: Optional[List["models.MicrosoftGraphTaxArea"]]
        tax_groups=None,  # type: Optional[List["models.MicrosoftGraphTaxGroup"]]
        units_of_measure=None,  # type: Optional[List["models.MicrosoftGraphUnitOfMeasure"]]
        vendors=None,  # type: Optional[List["models.MicrosoftGraphVendor"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property companies in financials.

        Update the navigation property companies in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param id: Read-only.
        :type id: str
        :param business_profile_id:
        :type business_profile_id: str
        :param display_name:
        :type display_name: str
        :param name:
        :type name: str
        :param system_version:
        :type system_version: str
        :param accounts:
        :type accounts: list[~financials.models.MicrosoftGraphAccount]
        :param aged_accounts_payable:
        :type aged_accounts_payable: list[~financials.models.MicrosoftGraphAgedAccountsPayable]
        :param aged_accounts_receivable:
        :type aged_accounts_receivable: list[~financials.models.MicrosoftGraphAgedAccountsReceivable]
        :param company_information:
        :type company_information: list[~financials.models.MicrosoftGraphCompanyInformation]
        :param countries_regions:
        :type countries_regions: list[~financials.models.MicrosoftGraphCountryRegion]
        :param currencies:
        :type currencies: list[~financials.models.MicrosoftGraphCurrency]
        :param customer_payment_journals:
        :type customer_payment_journals: list[~financials.models.MicrosoftGraphCustomerPaymentJournal]
        :param customer_payments:
        :type customer_payments: list[~financials.models.MicrosoftGraphCustomerPayment]
        :param customers:
        :type customers: list[~financials.models.MicrosoftGraphCustomer]
        :param dimensions:
        :type dimensions: list[~financials.models.MicrosoftGraphDimension]
        :param dimension_values:
        :type dimension_values: list[~financials.models.MicrosoftGraphDimensionValue]
        :param employees:
        :type employees: list[~financials.models.MicrosoftGraphEmployee]
        :param general_ledger_entries:
        :type general_ledger_entries: list[~financials.models.MicrosoftGraphGeneralLedgerEntry]
        :param item_categories:
        :type item_categories: list[~financials.models.MicrosoftGraphItemCategory]
        :param items:
        :type items: list[~financials.models.MicrosoftGraphItem]
        :param journal_lines:
        :type journal_lines: list[~financials.models.MicrosoftGraphJournalLine]
        :param journals:
        :type journals: list[~financials.models.MicrosoftGraphJournal]
        :param payment_methods:
        :type payment_methods: list[~financials.models.MicrosoftGraphPaymentMethod]
        :param payment_terms:
        :type payment_terms: list[~financials.models.MicrosoftGraphPaymentTerm]
        :param picture:
        :type picture: list[~financials.models.MicrosoftGraphPicture]
        :param purchase_invoice_lines:
        :type purchase_invoice_lines: list[~financials.models.MicrosoftGraphPurchaseInvoiceLine]
        :param purchase_invoices:
        :type purchase_invoices: list[~financials.models.MicrosoftGraphPurchaseInvoice]
        :param sales_credit_memo_lines:
        :type sales_credit_memo_lines: list[~financials.models.MicrosoftGraphSalesCreditMemoLine]
        :param sales_credit_memos:
        :type sales_credit_memos: list[~financials.models.MicrosoftGraphSalesCreditMemo]
        :param sales_invoice_lines:
        :type sales_invoice_lines: list[~financials.models.MicrosoftGraphSalesInvoiceLine]
        :param sales_invoices:
        :type sales_invoices: list[~financials.models.MicrosoftGraphSalesInvoice]
        :param sales_order_lines:
        :type sales_order_lines: list[~financials.models.MicrosoftGraphSalesOrderLine]
        :param sales_orders:
        :type sales_orders: list[~financials.models.MicrosoftGraphSalesOrder]
        :param sales_quote_lines:
        :type sales_quote_lines: list[~financials.models.MicrosoftGraphSalesQuoteLine]
        :param sales_quotes:
        :type sales_quotes: list[~financials.models.MicrosoftGraphSalesQuote]
        :param shipment_methods:
        :type shipment_methods: list[~financials.models.MicrosoftGraphShipmentMethod]
        :param tax_areas:
        :type tax_areas: list[~financials.models.MicrosoftGraphTaxArea]
        :param tax_groups:
        :type tax_groups: list[~financials.models.MicrosoftGraphTaxGroup]
        :param units_of_measure:
        :type units_of_measure: list[~financials.models.MicrosoftGraphUnitOfMeasure]
        :param vendors:
        :type vendors: list[~financials.models.MicrosoftGraphVendor]
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

        body = models.MicrosoftGraphCompany(id=id, business_profile_id=business_profile_id, display_name=display_name, name=name, system_version=system_version, accounts=accounts, aged_accounts_payable=aged_accounts_payable, aged_accounts_receivable=aged_accounts_receivable, company_information=company_information, countries_regions=countries_regions, currencies=currencies, customer_payment_journals=customer_payment_journals, customer_payments=customer_payments, customers=customers, dimensions=dimensions, dimension_values=dimension_values, employees=employees, general_ledger_entries=general_ledger_entries, item_categories=item_categories, items=items, journal_lines=journal_lines, journals=journals, payment_methods=payment_methods, payment_terms=payment_terms, picture=picture, purchase_invoice_lines=purchase_invoice_lines, purchase_invoices=purchase_invoices, sales_credit_memo_lines=sales_credit_memo_lines, sales_credit_memos=sales_credit_memos, sales_invoice_lines=sales_invoice_lines, sales_invoices=sales_invoices, sales_order_lines=sales_order_lines, sales_orders=sales_orders, sales_quote_lines=sales_quote_lines, sales_quotes=sales_quotes, shipment_methods=shipment_methods, tax_areas=tax_areas, tax_groups=tax_groups, units_of_measure=units_of_measure, vendors=vendors)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_company.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphCompany')
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

    update_company.metadata = {'url': '/financials/companies/{company-id}'}  # type: ignore

    def delete_company(
        self,
        company_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property companies for financials.

        Delete navigation property companies for financials.

        :param company_id: key: id of company.
        :type company_id: str
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
        url = self.delete_company.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
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

    delete_company.metadata = {'url': '/financials/companies/{company-id}'}  # type: ignore