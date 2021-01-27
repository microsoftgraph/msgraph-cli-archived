# Azure CLI Module Creation Report

### financials financial create-company

create-company a financials financial.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial|financials|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-company|CreateCompanies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--business-profile-id**|string||business_profile_id|businessProfileId|
|**--display-name**|string||display_name|displayName|
|**--name**|string||name|name|
|**--system-version**|string||system_version|systemVersion|
|**--accounts**|array||accounts|accounts|
|**--aged-accounts-payable**|array||aged_accounts_payable|agedAccountsPayable|
|**--aged-accounts-receivable**|array||aged_accounts_receivable|agedAccountsReceivable|
|**--company-information**|array||company_information|companyInformation|
|**--countries-regions**|array||countries_regions|countriesRegions|
|**--currencies**|array||currencies|currencies|
|**--customer-payment-journals**|array||customer_payment_journals|customerPaymentJournals|
|**--customer-payments**|array||customer_payments|customerPayments|
|**--customers**|array||customers|customers|
|**--dimensions**|array||dimensions|dimensions|
|**--dimension-values**|array||dimension_values|dimensionValues|
|**--employees**|array||employees|employees|
|**--general-ledger-entries**|array||general_ledger_entries|generalLedgerEntries|
|**--item-categories**|array||item_categories|itemCategories|
|**--items**|array||items|items|
|**--journal-lines**|array||journal_lines|journalLines|
|**--journals**|array||journals|journals|
|**--payment-methods**|array||payment_methods|paymentMethods|
|**--payment-terms**|array||payment_terms|paymentTerms|
|**--picture**|array||picture|picture|
|**--purchase-invoice-lines**|array||purchase_invoice_lines|purchaseInvoiceLines|
|**--purchase-invoices**|array||purchase_invoices|purchaseInvoices|
|**--sales-credit-memo-lines**|array||sales_credit_memo_lines|salesCreditMemoLines|
|**--sales-credit-memos**|array||sales_credit_memos|salesCreditMemos|
|**--sales-invoice-lines**|array||sales_invoice_lines|salesInvoiceLines|
|**--sales-invoices**|array||sales_invoices|salesInvoices|
|**--sales-order-lines**|array||sales_order_lines|salesOrderLines|
|**--sales-orders**|array||sales_orders|salesOrders|
|**--sales-quote-lines**|array||sales_quote_lines|salesQuoteLines|
|**--sales-quotes**|array||sales_quotes|salesQuotes|
|**--shipment-methods**|array||shipment_methods|shipmentMethods|
|**--tax-areas**|array||tax_areas|taxAreas|
|**--tax-groups**|array||tax_groups|taxGroups|
|**--units-of-measure**|array||units_of_measure|unitsOfMeasure|
|**--vendors**|array||vendors|vendors|

### financials financial delete

delete a financials financial.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial|financials|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCompanies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial get-company

get-company a financials financial.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial|financials|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-company|GetCompanies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial list-company

list-company a financials financial.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial|financials|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-company|ListCompanies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial update-company

update-company a financials financial.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial|financials|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-company|UpdateCompanies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--business-profile-id**|string||business_profile_id|businessProfileId|
|**--display-name**|string||display_name|displayName|
|**--name**|string||name|name|
|**--system-version**|string||system_version|systemVersion|
|**--accounts**|array||accounts|accounts|
|**--aged-accounts-payable**|array||aged_accounts_payable|agedAccountsPayable|
|**--aged-accounts-receivable**|array||aged_accounts_receivable|agedAccountsReceivable|
|**--company-information**|array||company_information|companyInformation|
|**--countries-regions**|array||countries_regions|countriesRegions|
|**--currencies**|array||currencies|currencies|
|**--customer-payment-journals**|array||customer_payment_journals|customerPaymentJournals|
|**--customer-payments**|array||customer_payments|customerPayments|
|**--customers**|array||customers|customers|
|**--dimensions**|array||dimensions|dimensions|
|**--dimension-values**|array||dimension_values|dimensionValues|
|**--employees**|array||employees|employees|
|**--general-ledger-entries**|array||general_ledger_entries|generalLedgerEntries|
|**--item-categories**|array||item_categories|itemCategories|
|**--items**|array||items|items|
|**--journal-lines**|array||journal_lines|journalLines|
|**--journals**|array||journals|journals|
|**--payment-methods**|array||payment_methods|paymentMethods|
|**--payment-terms**|array||payment_terms|paymentTerms|
|**--picture**|array||picture|picture|
|**--purchase-invoice-lines**|array||purchase_invoice_lines|purchaseInvoiceLines|
|**--purchase-invoices**|array||purchase_invoices|purchaseInvoices|
|**--sales-credit-memo-lines**|array||sales_credit_memo_lines|salesCreditMemoLines|
|**--sales-credit-memos**|array||sales_credit_memos|salesCreditMemos|
|**--sales-invoice-lines**|array||sales_invoice_lines|salesInvoiceLines|
|**--sales-invoices**|array||sales_invoices|salesInvoices|
|**--sales-order-lines**|array||sales_order_lines|salesOrderLines|
|**--sales-orders**|array||sales_orders|salesOrders|
|**--sales-quote-lines**|array||sales_quote_lines|salesQuoteLines|
|**--sales-quotes**|array||sales_quotes|salesQuotes|
|**--shipment-methods**|array||shipment_methods|shipmentMethods|
|**--tax-areas**|array||tax_areas|taxAreas|
|**--tax-groups**|array||tax_groups|taxGroups|
|**--units-of-measure**|array||units_of_measure|unitsOfMeasure|
|**--vendors**|array||vendors|vendors|

### financials financial-company create-account

create-account a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-account|CreateAccounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company create-aged-account-payable

create-aged-account-payable a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-aged-account-payable|CreateAgedAccountsPayable|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--aged-as-of-date**|date||aged_as_of_date|agedAsOfDate|
|**--balance-due**|number||balance_due|balanceDue|
|**--currency-code**|string||currency_code|currencyCode|
|**--current-amount**|number||current_amount|currentAmount|
|**--name**|string||name|name|
|**--period1-amount**|number||period1_amount|period1Amount|
|**--period2-amount**|number||period2_amount|period2Amount|
|**--period3-amount**|number||period3_amount|period3Amount|
|**--period-length-filter**|string||period_length_filter|periodLengthFilter|
|**--vendor-number**|string||vendor_number|vendorNumber|

### financials financial-company create-aged-account-receivable

create-aged-account-receivable a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-aged-account-receivable|CreateAgedAccountsReceivable|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--aged-as-of-date**|date||aged_as_of_date|agedAsOfDate|
|**--balance-due**|number||balance_due|balanceDue|
|**--currency-code**|string||currency_code|currencyCode|
|**--current-amount**|number||current_amount|currentAmount|
|**--customer-number**|string||customer_number|customerNumber|
|**--name**|string||name|name|
|**--period1-amount**|number||period1_amount|period1Amount|
|**--period2-amount**|number||period2_amount|period2Amount|
|**--period3-amount**|number||period3_amount|period3Amount|
|**--period-length-filter**|string||period_length_filter|periodLengthFilter|

### financials financial-company create-company-information

create-company-information a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-company-information|CreateCompanyInformation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--currency-code**|string||currency_code|currencyCode|
|**--current-fiscal-year-start-date**|date||current_fiscal_year_start_date|currentFiscalYearStartDate|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--fax-number**|string||fax_number|faxNumber|
|**--industry**|string||industry|industry|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--phone-number**|string||phone_number|phoneNumber|
|**--picture**|byte-array||picture|picture|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--website**|string||website|website|

### financials financial-company create-country-region

create-country-region a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-country-region|CreateCountriesRegions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--address-format**|string||address_format|addressFormat|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company create-currency

create-currency a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-currency|CreateCurrencies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company create-customer

create-customer a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-customer|CreateCustomers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--type**|string||type|type|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company create-customer-payment

create-customer-payment a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-customer-payment|CreateCustomerPayments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--amount**|number||amount|amount|
|**--applies-to-invoice-id**|uuid||applies_to_invoice_id|appliesToInvoiceId|
|**--applies-to-invoice-number**|string||applies_to_invoice_number|appliesToInvoiceNumber|
|**--comment**|string||comment|comment|
|**--contact-id**|string||contact_id|contactId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-number**|string||customer_number|customerNumber|
|**--description**|string||description|description|
|**--document-number**|string||document_number|documentNumber|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--journal-display-name**|string||journal_display_name|journalDisplayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--line-number**|integer||line_number|lineNumber|
|**--posting-date**|date||posting_date|postingDate|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||currency_code|currencyCode|
|**--customer-currency-id**|uuid||currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company create-customer-payment-journal

create-customer-payment-journal a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-customer-payment-journal|CreateCustomerPaymentJournals|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--balancing-account-id**|uuid||balancing_account_id|balancingAccountId|
|**--balancing-account-number**|string||balancing_account_number|balancingAccountNumber|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--account**|object|account|account|account|
|**--customer-payments**|array||customer_payments|customerPayments|

### financials financial-company create-dimension

create-dimension a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-dimension|CreateDimensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--dimension-values**|array||dimension_values|dimensionValues|

### financials financial-company create-dimension-value

create-dimension-value a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-dimension-value|CreateDimensionValues|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company create-employee

create-employee a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-employee|CreateEmployees|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--birth-date**|date||birth_date|birthDate|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--employment-date**|date||employment_date|employmentDate|
|**--given-name**|string||given_name|givenName|
|**--job-title**|string||job_title|jobTitle|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--middle-name**|string||middle_name|middleName|
|**--mobile-phone**|string||mobile_phone|mobilePhone|
|**--number**|string||number|number|
|**--personal-email**|string||personal_email|personalEmail|
|**--phone-number**|string||phone_number|phoneNumber|
|**--statistics-group-code**|string||statistics_group_code|statisticsGroupCode|
|**--status**|string||status|status|
|**--surname**|string||surname|surname|
|**--termination-date**|date||termination_date|terminationDate|
|**--picture**|array||picture|picture|

### financials financial-company create-general-ledger-entry

create-general-ledger-entry a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-general-ledger-entry|CreateGeneralLedgerEntries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--account-number**|string||account_number|accountNumber|
|**--credit-amount**|number||credit_amount|creditAmount|
|**--debit-amount**|number||debit_amount|debitAmount|
|**--description**|string||description|description|
|**--document-number**|string||document_number|documentNumber|
|**--document-type**|string||document_type|documentType|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--posting-date**|date||posting_date|postingDate|
|**--account**|object|account|account|account|

### financials financial-company create-item

create-item a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-item|CreateItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company create-item-category

create-item-category a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-item-category|CreateItemCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company create-journal

create-journal a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-journal|CreateJournals|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--balancing-account-id**|uuid||balancing_account_id|balancingAccountId|
|**--balancing-account-number**|string||balancing_account_number|balancingAccountNumber|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--account**|object|account|account|account|
|**--journal-lines**|array||journal_lines|journalLines|

### financials financial-company create-journal-line

create-journal-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-journal-line|CreateJournalLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--account-number**|string||account_number|accountNumber|
|**--amount**|number||amount|amount|
|**--comment**|string||comment|comment|
|**--description**|string||description|description|
|**--document-number**|string||document_number|documentNumber|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--journal-display-name**|string||journal_display_name|journalDisplayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--line-number**|integer||line_number|lineNumber|
|**--posting-date**|date||posting_date|postingDate|
|**--account**|object|account|account|account|

### financials financial-company create-payment-method

create-payment-method a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-payment-method|CreatePaymentMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company create-payment-term

create-payment-term a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-payment-term|CreatePaymentTerms|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company create-picture

create-picture a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company create-purchase-invoice

create-purchase-invoice a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-purchase-invoice|CreatePurchaseInvoices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--buy-from-address**|object|postalAddressType|buy_from_address|buyFromAddress|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--due-date**|date||due_date|dueDate|
|**--invoice-date**|date||invoice_date|invoiceDate|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--pay-to-address**|object|postalAddressType|pay_to_address|payToAddress|
|**--pay-to-contact**|string||pay_to_contact|payToContact|
|**--pay-to-name**|string||pay_to_name|payToName|
|**--pay-to-vendor-id**|uuid||pay_to_vendor_id|payToVendorId|
|**--pay-to-vendor-number**|string||pay_to_vendor_number|payToVendorNumber|
|**--prices-include-tax**|boolean||prices_include_tax|pricesIncludeTax|
|**--ship-to-address**|object|postalAddressType|ship_to_address|shipToAddress|
|**--ship-to-contact**|string||ship_to_contact|shipToContact|
|**--ship-to-name**|string||ship_to_name|shipToName|
|**--status**|string||status|status|
|**--total-amount-excluding-tax**|number||total_amount_excluding_tax|totalAmountExcludingTax|
|**--total-amount-including-tax**|number||total_amount_including_tax|totalAmountIncludingTax|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--vendor-id**|uuid||vendor_id|vendorId|
|**--vendor-invoice-number**|string||vendor_invoice_number|vendorInvoiceNumber|
|**--vendor-name**|string||vendor_name|vendorName|
|**--vendor-number**|string||vendor_number|vendorNumber|
|**--currency**|object|currency|currency|currency|
|**--purchase-invoice-lines**|array||purchase_invoice_lines|purchaseInvoiceLines|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--vendor-address**|object|postalAddressType|address|address|
|**--vendor-balance**|number||balance|balance|
|**--vendor-blocked**|string||blocked|blocked|
|**--vendor-currency-code**|string||microsoft_graph_vendor_currency_code|currencyCode|
|**--vendor-currency-id**|uuid||microsoft_graph_vendor_currency_id|currencyId|
|**--vendor-display-name**|string||display_name|displayName|
|**--vendor-email**|string||email|email|
|**--vendor-last-modified-date-time**|date-time||microsoft_graph_vendor_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-vendor-number**|string||microsoft_graph_vendor_number|number|
|**--vendor-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--vendor-payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--vendor-phone-number**|string||phone_number|phoneNumber|
|**--vendor-tax-liable**|boolean||tax_liable|taxLiable|
|**--vendor-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--vendor-website**|string||website|website|
|**--vendor-currency**|object|currency|microsoft_graph_currency|currency|
|**--vendor-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--vendor-payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--vendor-picture**|array||picture|picture|

### financials financial-company create-purchase-invoice-line

create-purchase-invoice-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-purchase-invoice-line|CreatePurchaseInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--expected-receipt-date**|date||expected_receipt_date|expectedReceiptDate|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-cost**|number||unit_cost|unitCost|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||number_unit_cost|unitCost|
|**--item-unit-price**|number||unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company create-sale-credit-memo

create-sale-credit-memo a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-credit-memo|CreateSalesCreditMemos|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--billing-postal-address**|object|postalAddressType|billing_postal_address|billingPostalAddress|
|**--bill-to-customer-id**|uuid||bill_to_customer_id|billToCustomerId|
|**--bill-to-customer-number**|string||bill_to_customer_number|billToCustomerNumber|
|**--bill-to-name**|string||bill_to_name|billToName|
|**--credit-memo-date**|date||credit_memo_date|creditMemoDate|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-name**|string||customer_name|customerName|
|**--customer-number**|string||customer_number|customerNumber|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--due-date**|date||due_date|dueDate|
|**--email**|string||email|email|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--invoice-id**|uuid||invoice_id|invoiceId|
|**--invoice-number**|string||invoice_number|invoiceNumber|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--prices-include-tax**|boolean||prices_include_tax|pricesIncludeTax|
|**--salesperson**|string||salesperson|salesperson|
|**--selling-postal-address**|object|postalAddressType|selling_postal_address|sellingPostalAddress|
|**--status**|string||status|status|
|**--total-amount-excluding-tax**|number||total_amount_excluding_tax|totalAmountExcludingTax|
|**--total-amount-including-tax**|number||total_amount_including_tax|totalAmountIncludingTax|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--currency**|object|currency|currency|currency|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--sales-credit-memo-lines**|array||sales_credit_memo_lines|salesCreditMemoLines|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||microsoft_graph_customer_currency_code|currencyCode|
|**--customer-currency-id**|uuid||microsoft_graph_customer_currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||microsoft_graph_customer_email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-customer-number**|string||microsoft_graph_customer_number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||microsoft_graph_customer_payment_terms_id_payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||microsoft_graph_customer_phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|microsoft_graph_currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|microsoft_graph_payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company create-sale-credit-memo-line

create-sale-credit-memo-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-credit-memo-line|CreateSalesCreditMemoLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company create-sale-invoice

create-sale-invoice a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-invoice|CreateSalesInvoices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--billing-postal-address**|object|postalAddressType|billing_postal_address|billingPostalAddress|
|**--bill-to-customer-id**|uuid||bill_to_customer_id|billToCustomerId|
|**--bill-to-customer-number**|string||bill_to_customer_number|billToCustomerNumber|
|**--bill-to-name**|string||bill_to_name|billToName|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-name**|string||customer_name|customerName|
|**--customer-number**|string||customer_number|customerNumber|
|**--customer-purchase-order-reference**|string||customer_purchase_order_reference|customerPurchaseOrderReference|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--due-date**|date||due_date|dueDate|
|**--email**|string||email|email|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--invoice-date**|date||invoice_date|invoiceDate|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--order-id**|uuid||order_id|orderId|
|**--order-number**|string||order_number|orderNumber|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--prices-include-tax**|boolean||prices_include_tax|pricesIncludeTax|
|**--salesperson**|string||salesperson|salesperson|
|**--selling-postal-address**|object|postalAddressType|selling_postal_address|sellingPostalAddress|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--shipping-postal-address**|object|postalAddressType|shipping_postal_address|shippingPostalAddress|
|**--ship-to-contact**|string||ship_to_contact|shipToContact|
|**--ship-to-name**|string||ship_to_name|shipToName|
|**--status**|string||status|status|
|**--total-amount-excluding-tax**|number||total_amount_excluding_tax|totalAmountExcludingTax|
|**--total-amount-including-tax**|number||total_amount_including_tax|totalAmountIncludingTax|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--currency**|object|currency|currency|currency|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--sales-invoice-lines**|array||sales_invoice_lines|salesInvoiceLines|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||microsoft_graph_customer_currency_code|currencyCode|
|**--customer-currency-id**|uuid||microsoft_graph_customer_currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||microsoft_graph_customer_email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-customer-number**|string||microsoft_graph_customer_number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||microsoft_graph_customer_payment_terms_id_payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||microsoft_graph_customer_phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||microsoft_graph_customer_shipment_method_id_shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|microsoft_graph_currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|microsoft_graph_payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|microsoft_graph_shipment_method|shipmentMethod|

### financials financial-company create-sale-invoice-line

create-sale-invoice-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-invoice-line|CreateSalesInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company create-sale-order

create-sale-order a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-order|CreateSalesOrders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--billing-postal-address**|object|postalAddressType|billing_postal_address|billingPostalAddress|
|**--bill-to-customer-id**|uuid||bill_to_customer_id|billToCustomerId|
|**--bill-to-customer-number**|string||bill_to_customer_number|billToCustomerNumber|
|**--bill-to-name**|string||bill_to_name|billToName|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-name**|string||customer_name|customerName|
|**--customer-number**|string||customer_number|customerNumber|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--email**|string||email|email|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--fully-shipped**|boolean||fully_shipped|fullyShipped|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--order-date**|date||order_date|orderDate|
|**--partial-shipping**|boolean||partial_shipping|partialShipping|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--prices-include-tax**|boolean||prices_include_tax|pricesIncludeTax|
|**--requested-delivery-date**|date||requested_delivery_date|requestedDeliveryDate|
|**--salesperson**|string||salesperson|salesperson|
|**--selling-postal-address**|object|postalAddressType|selling_postal_address|sellingPostalAddress|
|**--shipping-postal-address**|object|postalAddressType|shipping_postal_address|shippingPostalAddress|
|**--ship-to-contact**|string||ship_to_contact|shipToContact|
|**--ship-to-name**|string||ship_to_name|shipToName|
|**--status**|string||status|status|
|**--total-amount-excluding-tax**|number||total_amount_excluding_tax|totalAmountExcludingTax|
|**--total-amount-including-tax**|number||total_amount_including_tax|totalAmountIncludingTax|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--currency**|object|currency|currency|currency|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--sales-order-lines**|array||sales_order_lines|salesOrderLines|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||microsoft_graph_customer_currency_code|currencyCode|
|**--customer-currency-id**|uuid||microsoft_graph_customer_currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||microsoft_graph_customer_email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-customer-number**|string||microsoft_graph_customer_number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||microsoft_graph_customer_payment_terms_id_payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||microsoft_graph_customer_phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|microsoft_graph_currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|microsoft_graph_payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company create-sale-order-line

create-sale-order-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-order-line|CreateSalesOrderLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--invoiced-quantity**|number||invoiced_quantity|invoicedQuantity|
|**--invoice-quantity**|number||invoice_quantity|invoiceQuantity|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--shipped-quantity**|number||shipped_quantity|shippedQuantity|
|**--ship-quantity**|number||ship_quantity|shipQuantity|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company create-sale-quote

create-sale-quote a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-quote|CreateSalesQuotes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--accepted-date**|date||accepted_date|acceptedDate|
|**--billing-postal-address**|object|postalAddressType|billing_postal_address|billingPostalAddress|
|**--bill-to-customer-id**|uuid||bill_to_customer_id|billToCustomerId|
|**--bill-to-customer-number**|string||bill_to_customer_number|billToCustomerNumber|
|**--bill-to-name**|string||bill_to_name|billToName|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-name**|string||customer_name|customerName|
|**--customer-number**|string||customer_number|customerNumber|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--document-date**|date||document_date|documentDate|
|**--due-date**|date||due_date|dueDate|
|**--email**|string||email|email|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--salesperson**|string||salesperson|salesperson|
|**--selling-postal-address**|object|postalAddressType|selling_postal_address|sellingPostalAddress|
|**--sent-date**|date-time||sent_date|sentDate|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--shipping-postal-address**|object|postalAddressType|shipping_postal_address|shippingPostalAddress|
|**--ship-to-contact**|string||ship_to_contact|shipToContact|
|**--ship-to-name**|string||ship_to_name|shipToName|
|**--status**|string||status|status|
|**--total-amount-excluding-tax**|number||total_amount_excluding_tax|totalAmountExcludingTax|
|**--total-amount-including-tax**|number||total_amount_including_tax|totalAmountIncludingTax|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--valid-until-date**|date||valid_until_date|validUntilDate|
|**--currency**|object|currency|currency|currency|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--sales-quote-lines**|array||sales_quote_lines|salesQuoteLines|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||microsoft_graph_customer_currency_code|currencyCode|
|**--customer-currency-id**|uuid||microsoft_graph_customer_currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||microsoft_graph_customer_email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-customer-number**|string||microsoft_graph_customer_number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||microsoft_graph_customer_payment_terms_id_payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||microsoft_graph_customer_phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||microsoft_graph_customer_shipment_method_id_shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|microsoft_graph_currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|microsoft_graph_payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|microsoft_graph_shipment_method|shipmentMethod|

### financials financial-company create-sale-quote-line

create-sale-quote-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-quote-line|CreateSalesQuoteLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company create-shipment-method

create-shipment-method a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-shipment-method|CreateShipmentMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company create-tax-area

create-tax-area a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-tax-area|CreateTaxAreas|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--tax-type**|string||tax_type|taxType|

### financials financial-company create-tax-group

create-tax-group a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-tax-group|CreateTaxGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--tax-type**|string||tax_type|taxType|

### financials financial-company create-unit-of-measure

create-unit-of-measure a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-unit-of-measure|CreateUnitsOfMeasure|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--international-standard-code**|string||international_standard_code|internationalStandardCode|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company create-vendor

create-vendor a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-vendor|CreateVendors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--balance**|number||balance|balance|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|

### financials financial-company delete

delete a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccounts|
|delete|DeleteAgedAccountsPayable|
|delete|DeleteAgedAccountsReceivable|
|delete|DeleteCompanyInformation|
|delete|DeleteCountriesRegions|
|delete|DeleteCurrencies|
|delete|DeleteCustomerPaymentJournals|
|delete|DeleteCustomerPayments|
|delete|DeleteCustomers|
|delete|DeleteDimensions|
|delete|DeleteDimensionValues|
|delete|DeleteEmployees|
|delete|DeleteGeneralLedgerEntries|
|delete|DeleteItemCategories|
|delete|DeleteItems|
|delete|DeleteJournalLines|
|delete|DeleteJournals|
|delete|DeletePaymentMethods|
|delete|DeletePaymentTerms|
|delete|DeletePicture|
|delete|DeletePurchaseInvoiceLines|
|delete|DeletePurchaseInvoices|
|delete|DeleteSalesCreditMemoLines|
|delete|DeleteSalesCreditMemos|
|delete|DeleteSalesInvoiceLines|
|delete|DeleteSalesInvoices|
|delete|DeleteSalesOrderLines|
|delete|DeleteSalesOrders|
|delete|DeleteSalesQuoteLines|
|delete|DeleteSalesQuotes|
|delete|DeleteShipmentMethods|
|delete|DeleteTaxAreas|
|delete|DeleteTaxGroups|
|delete|DeleteUnitsOfMeasure|
|delete|DeleteVendors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--account-id**|string|key: id of account|account_id|account-id|
|**--aged-accounts-payable-id**|string|key: id of agedAccountsPayable|aged_accounts_payable_id|agedAccountsPayable-id|
|**--aged-accounts-receivable-id**|string|key: id of agedAccountsReceivable|aged_accounts_receivable_id|agedAccountsReceivable-id|
|**--company-information-id**|string|key: id of companyInformation|company_information_id|companyInformation-id|
|**--country-region-id**|string|key: id of countryRegion|country_region_id|countryRegion-id|
|**--currency-id**|string|key: id of currency|currency_id|currency-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--dimension-id**|string|key: id of dimension|dimension_id|dimension-id|
|**--dimension-value-id**|string|key: id of dimensionValue|dimension_value_id|dimensionValue-id|
|**--employee-id**|string|key: id of employee|employee_id|employee-id|
|**--general-ledger-entry-id**|string|key: id of generalLedgerEntry|general_ledger_entry_id|generalLedgerEntry-id|
|**--item-category-id**|string|key: id of itemCategory|item_category_id|itemCategory-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--payment-method-id**|string|key: id of paymentMethod|payment_method_id|paymentMethod-id|
|**--payment-term-id**|string|key: id of paymentTerm|payment_term_id|paymentTerm-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--shipment-method-id**|string|key: id of shipmentMethod|shipment_method_id|shipmentMethod-id|
|**--tax-area-id**|string|key: id of taxArea|tax_area_id|taxArea-id|
|**--tax-group-id**|string|key: id of taxGroup|tax_group_id|taxGroup-id|
|**--unit-of-measure-id**|string|key: id of unitOfMeasure|unit_of_measure_id|unitOfMeasure-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company get-account

get-account a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--account-id**|string|key: id of account|account_id|account-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-aged-account-payable

get-aged-account-payable a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-aged-account-payable|GetAgedAccountsPayable|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--aged-accounts-payable-id**|string|key: id of agedAccountsPayable|aged_accounts_payable_id|agedAccountsPayable-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-aged-account-receivable

get-aged-account-receivable a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-aged-account-receivable|GetAgedAccountsReceivable|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--aged-accounts-receivable-id**|string|key: id of agedAccountsReceivable|aged_accounts_receivable_id|agedAccountsReceivable-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-company-information

get-company-information a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-company-information|GetCompanyInformation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--company-information-id**|string|key: id of companyInformation|company_information_id|companyInformation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-company-information-picture

get-company-information-picture a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-company-information-picture|GetCompanyInformationPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--company-information-id**|string|key: id of companyInformation|company_information_id|companyInformation-id|

### financials financial-company get-country-region

get-country-region a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-country-region|GetCountriesRegions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--country-region-id**|string|key: id of countryRegion|country_region_id|countryRegion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-currency

get-currency a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrencies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--currency-id**|string|key: id of currency|currency_id|currency-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-customer

get-customer a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer|GetCustomers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-customer-payment

get-customer-payment a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer-payment|GetCustomerPayments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-customer-payment-journal

get-customer-payment-journal a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer-payment-journal|GetCustomerPaymentJournals|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-dimension

get-dimension a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-dimension|GetDimensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--dimension-id**|string|key: id of dimension|dimension_id|dimension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-dimension-value

get-dimension-value a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-dimension-value|GetDimensionValues|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--dimension-value-id**|string|key: id of dimensionValue|dimension_value_id|dimensionValue-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-employee

get-employee a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-employee|GetEmployees|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--employee-id**|string|key: id of employee|employee_id|employee-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-general-ledger-entry

get-general-ledger-entry a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-general-ledger-entry|GetGeneralLedgerEntries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--general-ledger-entry-id**|string|key: id of generalLedgerEntry|general_ledger_entry_id|generalLedgerEntry-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-item

get-item a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-item-category

get-item-category a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-category-id**|string|key: id of itemCategory|item_category_id|itemCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-journal

get-journal a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-journal|GetJournals|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-journal-line

get-journal-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-journal-line|GetJournalLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-payment-method

get-payment-method a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-method|GetPaymentMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--payment-method-id**|string|key: id of paymentMethod|payment_method_id|paymentMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-payment-term

get-payment-term a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerms|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--payment-term-id**|string|key: id of paymentTerm|payment_term_id|paymentTerm-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-picture

get-picture a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-picture-content

get-picture-content a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company get-purchase-invoice

get-purchase-invoice a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-purchase-invoice|GetPurchaseInvoices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-purchase-invoice-line

get-purchase-invoice-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-purchase-invoice-line|GetPurchaseInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-sale-credit-memo

get-sale-credit-memo a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-credit-memo|GetSalesCreditMemos|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-sale-credit-memo-line

get-sale-credit-memo-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-credit-memo-line|GetSalesCreditMemoLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-sale-invoice

get-sale-invoice a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-invoice|GetSalesInvoices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-sale-invoice-line

get-sale-invoice-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-invoice-line|GetSalesInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-sale-order

get-sale-order a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-order|GetSalesOrders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-sale-order-line

get-sale-order-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-order-line|GetSalesOrderLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-sale-quote

get-sale-quote a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-quote|GetSalesQuotes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-sale-quote-line

get-sale-quote-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-quote-line|GetSalesQuoteLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-shipment-method

get-shipment-method a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shipment-method|GetShipmentMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--shipment-method-id**|string|key: id of shipmentMethod|shipment_method_id|shipmentMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-tax-area

get-tax-area a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-tax-area|GetTaxAreas|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--tax-area-id**|string|key: id of taxArea|tax_area_id|taxArea-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-tax-group

get-tax-group a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-tax-group|GetTaxGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--tax-group-id**|string|key: id of taxGroup|tax_group_id|taxGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-unit-of-measure

get-unit-of-measure a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-unit-of-measure|GetUnitsOfMeasure|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--unit-of-measure-id**|string|key: id of unitOfMeasure|unit_of_measure_id|unitOfMeasure-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company get-vendor

get-vendor a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-vendor|GetVendors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-account

list-account a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-account|ListAccounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-aged-account-payable

list-aged-account-payable a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-aged-account-payable|ListAgedAccountsPayable|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-aged-account-receivable

list-aged-account-receivable a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-aged-account-receivable|ListAgedAccountsReceivable|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-company-information

list-company-information a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-company-information|ListCompanyInformation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-country-region

list-country-region a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-country-region|ListCountriesRegions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-currency

list-currency a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-currency|ListCurrencies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-customer

list-customer a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-customer|ListCustomers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-customer-payment

list-customer-payment a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-customer-payment|ListCustomerPayments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-customer-payment-journal

list-customer-payment-journal a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-customer-payment-journal|ListCustomerPaymentJournals|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-dimension

list-dimension a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-dimension|ListDimensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-dimension-value

list-dimension-value a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-dimension-value|ListDimensionValues|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-employee

list-employee a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-employee|ListEmployees|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-general-ledger-entry

list-general-ledger-entry a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-general-ledger-entry|ListGeneralLedgerEntries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-item

list-item a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-item|ListItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-item-category

list-item-category a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-item-category|ListItemCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-journal

list-journal a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-journal|ListJournals|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-journal-line

list-journal-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-journal-line|ListJournalLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-payment-method

list-payment-method a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-payment-method|ListPaymentMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-payment-term

list-payment-term a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-payment-term|ListPaymentTerms|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-picture

list-picture a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-purchase-invoice

list-purchase-invoice a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-purchase-invoice|ListPurchaseInvoices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-purchase-invoice-line

list-purchase-invoice-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-purchase-invoice-line|ListPurchaseInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-sale-credit-memo

list-sale-credit-memo a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-credit-memo|ListSalesCreditMemos|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-sale-credit-memo-line

list-sale-credit-memo-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-credit-memo-line|ListSalesCreditMemoLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-sale-invoice

list-sale-invoice a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-invoice|ListSalesInvoices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-sale-invoice-line

list-sale-invoice-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-invoice-line|ListSalesInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-sale-order

list-sale-order a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-order|ListSalesOrders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-sale-order-line

list-sale-order-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-order-line|ListSalesOrderLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-sale-quote

list-sale-quote a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-quote|ListSalesQuotes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-sale-quote-line

list-sale-quote-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-quote-line|ListSalesQuoteLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-shipment-method

list-shipment-method a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-shipment-method|ListShipmentMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-tax-area

list-tax-area a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-tax-area|ListTaxAreas|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-tax-group

list-tax-group a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-tax-group|ListTaxGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-unit-of-measure

list-unit-of-measure a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-unit-of-measure|ListUnitsOfMeasure|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company list-vendor

list-vendor a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-vendor|ListVendors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company set-company-information-picture

set-company-information-picture a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-company-information-picture|SetCompanyInformationPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--company-information-id**|string|key: id of companyInformation|company_information_id|companyInformation-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company set-picture-content

set-picture-content a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company update-account

update-account a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--account-id**|string|key: id of account|account_id|account-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company update-aged-account-payable

update-aged-account-payable a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-aged-account-payable|UpdateAgedAccountsPayable|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--aged-accounts-payable-id**|string|key: id of agedAccountsPayable|aged_accounts_payable_id|agedAccountsPayable-id|
|**--id**|string|Read-only.|id|id|
|**--aged-as-of-date**|date||aged_as_of_date|agedAsOfDate|
|**--balance-due**|number||balance_due|balanceDue|
|**--currency-code**|string||currency_code|currencyCode|
|**--current-amount**|number||current_amount|currentAmount|
|**--name**|string||name|name|
|**--period1-amount**|number||period1_amount|period1Amount|
|**--period2-amount**|number||period2_amount|period2Amount|
|**--period3-amount**|number||period3_amount|period3Amount|
|**--period-length-filter**|string||period_length_filter|periodLengthFilter|
|**--vendor-number**|string||vendor_number|vendorNumber|

### financials financial-company update-aged-account-receivable

update-aged-account-receivable a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-aged-account-receivable|UpdateAgedAccountsReceivable|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--aged-accounts-receivable-id**|string|key: id of agedAccountsReceivable|aged_accounts_receivable_id|agedAccountsReceivable-id|
|**--id**|string|Read-only.|id|id|
|**--aged-as-of-date**|date||aged_as_of_date|agedAsOfDate|
|**--balance-due**|number||balance_due|balanceDue|
|**--currency-code**|string||currency_code|currencyCode|
|**--current-amount**|number||current_amount|currentAmount|
|**--customer-number**|string||customer_number|customerNumber|
|**--name**|string||name|name|
|**--period1-amount**|number||period1_amount|period1Amount|
|**--period2-amount**|number||period2_amount|period2Amount|
|**--period3-amount**|number||period3_amount|period3Amount|
|**--period-length-filter**|string||period_length_filter|periodLengthFilter|

### financials financial-company update-company-information

update-company-information a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-company-information|UpdateCompanyInformation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--company-information-id**|string|key: id of companyInformation|company_information_id|companyInformation-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--currency-code**|string||currency_code|currencyCode|
|**--current-fiscal-year-start-date**|date||current_fiscal_year_start_date|currentFiscalYearStartDate|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--fax-number**|string||fax_number|faxNumber|
|**--industry**|string||industry|industry|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--phone-number**|string||phone_number|phoneNumber|
|**--picture**|byte-array||picture|picture|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--website**|string||website|website|

### financials financial-company update-country-region

update-country-region a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-country-region|UpdateCountriesRegions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--country-region-id**|string|key: id of countryRegion|country_region_id|countryRegion-id|
|**--id**|string|Read-only.|id|id|
|**--address-format**|string||address_format|addressFormat|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company update-currency

update-currency a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrencies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--currency-id**|string|key: id of currency|currency_id|currency-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company update-customer

update-customer a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-customer|UpdateCustomers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--type**|string||type|type|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company update-customer-payment

update-customer-payment a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-customer-payment|UpdateCustomerPayments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--amount**|number||amount|amount|
|**--applies-to-invoice-id**|uuid||applies_to_invoice_id|appliesToInvoiceId|
|**--applies-to-invoice-number**|string||applies_to_invoice_number|appliesToInvoiceNumber|
|**--comment**|string||comment|comment|
|**--contact-id**|string||contact_id|contactId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-number**|string||customer_number|customerNumber|
|**--description**|string||description|description|
|**--document-number**|string||document_number|documentNumber|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--journal-display-name**|string||journal_display_name|journalDisplayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--line-number**|integer||line_number|lineNumber|
|**--posting-date**|date||posting_date|postingDate|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||currency_code|currencyCode|
|**--customer-currency-id**|uuid||currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company update-customer-payment-journal

update-customer-payment-journal a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-customer-payment-journal|UpdateCustomerPaymentJournals|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--id**|string|Read-only.|id|id|
|**--balancing-account-id**|uuid||balancing_account_id|balancingAccountId|
|**--balancing-account-number**|string||balancing_account_number|balancingAccountNumber|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--account**|object|account|account|account|
|**--customer-payments**|array||customer_payments|customerPayments|

### financials financial-company update-dimension

update-dimension a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-dimension|UpdateDimensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--dimension-id**|string|key: id of dimension|dimension_id|dimension-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--dimension-values**|array||dimension_values|dimensionValues|

### financials financial-company update-dimension-value

update-dimension-value a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-dimension-value|UpdateDimensionValues|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--dimension-value-id**|string|key: id of dimensionValue|dimension_value_id|dimensionValue-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company update-employee

update-employee a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-employee|UpdateEmployees|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--employee-id**|string|key: id of employee|employee_id|employee-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--birth-date**|date||birth_date|birthDate|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--employment-date**|date||employment_date|employmentDate|
|**--given-name**|string||given_name|givenName|
|**--job-title**|string||job_title|jobTitle|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--middle-name**|string||middle_name|middleName|
|**--mobile-phone**|string||mobile_phone|mobilePhone|
|**--number**|string||number|number|
|**--personal-email**|string||personal_email|personalEmail|
|**--phone-number**|string||phone_number|phoneNumber|
|**--statistics-group-code**|string||statistics_group_code|statisticsGroupCode|
|**--status**|string||status|status|
|**--surname**|string||surname|surname|
|**--termination-date**|date||termination_date|terminationDate|
|**--picture**|array||picture|picture|

### financials financial-company update-general-ledger-entry

update-general-ledger-entry a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-general-ledger-entry|UpdateGeneralLedgerEntries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--general-ledger-entry-id**|string|key: id of generalLedgerEntry|general_ledger_entry_id|generalLedgerEntry-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--account-number**|string||account_number|accountNumber|
|**--credit-amount**|number||credit_amount|creditAmount|
|**--debit-amount**|number||debit_amount|debitAmount|
|**--description**|string||description|description|
|**--document-number**|string||document_number|documentNumber|
|**--document-type**|string||document_type|documentType|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--posting-date**|date||posting_date|postingDate|
|**--account**|object|account|account|account|

### financials financial-company update-item

update-item a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company update-item-category

update-item-category a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-category-id**|string|key: id of itemCategory|item_category_id|itemCategory-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company update-journal

update-journal a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-journal|UpdateJournals|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--id**|string|Read-only.|id|id|
|**--balancing-account-id**|uuid||balancing_account_id|balancingAccountId|
|**--balancing-account-number**|string||balancing_account_number|balancingAccountNumber|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--account**|object|account|account|account|
|**--journal-lines**|array||journal_lines|journalLines|

### financials financial-company update-journal-line

update-journal-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-journal-line|UpdateJournalLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--account-number**|string||account_number|accountNumber|
|**--amount**|number||amount|amount|
|**--comment**|string||comment|comment|
|**--description**|string||description|description|
|**--document-number**|string||document_number|documentNumber|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--journal-display-name**|string||journal_display_name|journalDisplayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--line-number**|integer||line_number|lineNumber|
|**--posting-date**|date||posting_date|postingDate|
|**--account**|object|account|account|account|

### financials financial-company update-payment-method

update-payment-method a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-method|UpdatePaymentMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--payment-method-id**|string|key: id of paymentMethod|payment_method_id|paymentMethod-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company update-payment-term

update-payment-term a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerms|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--payment-term-id**|string|key: id of paymentTerm|payment_term_id|paymentTerm-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company update-picture

update-picture a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company update-purchase-invoice

update-purchase-invoice a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-purchase-invoice|UpdatePurchaseInvoices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--buy-from-address**|object|postalAddressType|buy_from_address|buyFromAddress|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--due-date**|date||due_date|dueDate|
|**--invoice-date**|date||invoice_date|invoiceDate|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--pay-to-address**|object|postalAddressType|pay_to_address|payToAddress|
|**--pay-to-contact**|string||pay_to_contact|payToContact|
|**--pay-to-name**|string||pay_to_name|payToName|
|**--pay-to-vendor-id**|uuid||pay_to_vendor_id|payToVendorId|
|**--pay-to-vendor-number**|string||pay_to_vendor_number|payToVendorNumber|
|**--prices-include-tax**|boolean||prices_include_tax|pricesIncludeTax|
|**--ship-to-address**|object|postalAddressType|ship_to_address|shipToAddress|
|**--ship-to-contact**|string||ship_to_contact|shipToContact|
|**--ship-to-name**|string||ship_to_name|shipToName|
|**--status**|string||status|status|
|**--total-amount-excluding-tax**|number||total_amount_excluding_tax|totalAmountExcludingTax|
|**--total-amount-including-tax**|number||total_amount_including_tax|totalAmountIncludingTax|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--vendor-id**|uuid||vendor_id|vendorId|
|**--vendor-invoice-number**|string||vendor_invoice_number|vendorInvoiceNumber|
|**--vendor-name**|string||vendor_name|vendorName|
|**--vendor-number**|string||vendor_number|vendorNumber|
|**--currency**|object|currency|currency|currency|
|**--purchase-invoice-lines**|array||purchase_invoice_lines|purchaseInvoiceLines|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--vendor-address**|object|postalAddressType|address|address|
|**--vendor-balance**|number||balance|balance|
|**--vendor-blocked**|string||blocked|blocked|
|**--vendor-currency-code**|string||microsoft_graph_vendor_currency_code|currencyCode|
|**--vendor-currency-id**|uuid||microsoft_graph_vendor_currency_id|currencyId|
|**--vendor-display-name**|string||display_name|displayName|
|**--vendor-email**|string||email|email|
|**--vendor-last-modified-date-time**|date-time||microsoft_graph_vendor_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-vendor-number**|string||microsoft_graph_vendor_number|number|
|**--vendor-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--vendor-payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--vendor-phone-number**|string||phone_number|phoneNumber|
|**--vendor-tax-liable**|boolean||tax_liable|taxLiable|
|**--vendor-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--vendor-website**|string||website|website|
|**--vendor-currency**|object|currency|microsoft_graph_currency|currency|
|**--vendor-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--vendor-payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--vendor-picture**|array||picture|picture|

### financials financial-company update-purchase-invoice-line

update-purchase-invoice-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-purchase-invoice-line|UpdatePurchaseInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--expected-receipt-date**|date||expected_receipt_date|expectedReceiptDate|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-cost**|number||unit_cost|unitCost|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||number_unit_cost|unitCost|
|**--item-unit-price**|number||unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company update-sale-credit-memo

update-sale-credit-memo a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-credit-memo|UpdateSalesCreditMemos|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--id**|string|Read-only.|id|id|
|**--billing-postal-address**|object|postalAddressType|billing_postal_address|billingPostalAddress|
|**--bill-to-customer-id**|uuid||bill_to_customer_id|billToCustomerId|
|**--bill-to-customer-number**|string||bill_to_customer_number|billToCustomerNumber|
|**--bill-to-name**|string||bill_to_name|billToName|
|**--credit-memo-date**|date||credit_memo_date|creditMemoDate|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-name**|string||customer_name|customerName|
|**--customer-number**|string||customer_number|customerNumber|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--due-date**|date||due_date|dueDate|
|**--email**|string||email|email|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--invoice-id**|uuid||invoice_id|invoiceId|
|**--invoice-number**|string||invoice_number|invoiceNumber|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--prices-include-tax**|boolean||prices_include_tax|pricesIncludeTax|
|**--salesperson**|string||salesperson|salesperson|
|**--selling-postal-address**|object|postalAddressType|selling_postal_address|sellingPostalAddress|
|**--status**|string||status|status|
|**--total-amount-excluding-tax**|number||total_amount_excluding_tax|totalAmountExcludingTax|
|**--total-amount-including-tax**|number||total_amount_including_tax|totalAmountIncludingTax|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--currency**|object|currency|currency|currency|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--sales-credit-memo-lines**|array||sales_credit_memo_lines|salesCreditMemoLines|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||microsoft_graph_customer_currency_code|currencyCode|
|**--customer-currency-id**|uuid||microsoft_graph_customer_currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||microsoft_graph_customer_email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-customer-number**|string||microsoft_graph_customer_number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||microsoft_graph_customer_payment_terms_id_payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||microsoft_graph_customer_phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|microsoft_graph_currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|microsoft_graph_payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company update-sale-credit-memo-line

update-sale-credit-memo-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-credit-memo-line|UpdateSalesCreditMemoLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company update-sale-invoice

update-sale-invoice a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-invoice|UpdateSalesInvoices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--billing-postal-address**|object|postalAddressType|billing_postal_address|billingPostalAddress|
|**--bill-to-customer-id**|uuid||bill_to_customer_id|billToCustomerId|
|**--bill-to-customer-number**|string||bill_to_customer_number|billToCustomerNumber|
|**--bill-to-name**|string||bill_to_name|billToName|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-name**|string||customer_name|customerName|
|**--customer-number**|string||customer_number|customerNumber|
|**--customer-purchase-order-reference**|string||customer_purchase_order_reference|customerPurchaseOrderReference|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--due-date**|date||due_date|dueDate|
|**--email**|string||email|email|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--invoice-date**|date||invoice_date|invoiceDate|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--order-id**|uuid||order_id|orderId|
|**--order-number**|string||order_number|orderNumber|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--prices-include-tax**|boolean||prices_include_tax|pricesIncludeTax|
|**--salesperson**|string||salesperson|salesperson|
|**--selling-postal-address**|object|postalAddressType|selling_postal_address|sellingPostalAddress|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--shipping-postal-address**|object|postalAddressType|shipping_postal_address|shippingPostalAddress|
|**--ship-to-contact**|string||ship_to_contact|shipToContact|
|**--ship-to-name**|string||ship_to_name|shipToName|
|**--status**|string||status|status|
|**--total-amount-excluding-tax**|number||total_amount_excluding_tax|totalAmountExcludingTax|
|**--total-amount-including-tax**|number||total_amount_including_tax|totalAmountIncludingTax|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--currency**|object|currency|currency|currency|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--sales-invoice-lines**|array||sales_invoice_lines|salesInvoiceLines|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||microsoft_graph_customer_currency_code|currencyCode|
|**--customer-currency-id**|uuid||microsoft_graph_customer_currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||microsoft_graph_customer_email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-customer-number**|string||microsoft_graph_customer_number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||microsoft_graph_customer_payment_terms_id_payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||microsoft_graph_customer_phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||microsoft_graph_customer_shipment_method_id_shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|microsoft_graph_currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|microsoft_graph_payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|microsoft_graph_shipment_method|shipmentMethod|

### financials financial-company update-sale-invoice-line

update-sale-invoice-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-invoice-line|UpdateSalesInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company update-sale-order

update-sale-order a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-order|UpdateSalesOrders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--id**|string|Read-only.|id|id|
|**--billing-postal-address**|object|postalAddressType|billing_postal_address|billingPostalAddress|
|**--bill-to-customer-id**|uuid||bill_to_customer_id|billToCustomerId|
|**--bill-to-customer-number**|string||bill_to_customer_number|billToCustomerNumber|
|**--bill-to-name**|string||bill_to_name|billToName|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-name**|string||customer_name|customerName|
|**--customer-number**|string||customer_number|customerNumber|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--email**|string||email|email|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--fully-shipped**|boolean||fully_shipped|fullyShipped|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--order-date**|date||order_date|orderDate|
|**--partial-shipping**|boolean||partial_shipping|partialShipping|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--prices-include-tax**|boolean||prices_include_tax|pricesIncludeTax|
|**--requested-delivery-date**|date||requested_delivery_date|requestedDeliveryDate|
|**--salesperson**|string||salesperson|salesperson|
|**--selling-postal-address**|object|postalAddressType|selling_postal_address|sellingPostalAddress|
|**--shipping-postal-address**|object|postalAddressType|shipping_postal_address|shippingPostalAddress|
|**--ship-to-contact**|string||ship_to_contact|shipToContact|
|**--ship-to-name**|string||ship_to_name|shipToName|
|**--status**|string||status|status|
|**--total-amount-excluding-tax**|number||total_amount_excluding_tax|totalAmountExcludingTax|
|**--total-amount-including-tax**|number||total_amount_including_tax|totalAmountIncludingTax|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--currency**|object|currency|currency|currency|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--sales-order-lines**|array||sales_order_lines|salesOrderLines|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||microsoft_graph_customer_currency_code|currencyCode|
|**--customer-currency-id**|uuid||microsoft_graph_customer_currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||microsoft_graph_customer_email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-customer-number**|string||microsoft_graph_customer_number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||microsoft_graph_customer_payment_terms_id_payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||microsoft_graph_customer_phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|microsoft_graph_currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|microsoft_graph_payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company update-sale-order-line

update-sale-order-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-order-line|UpdateSalesOrderLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--invoiced-quantity**|number||invoiced_quantity|invoicedQuantity|
|**--invoice-quantity**|number||invoice_quantity|invoiceQuantity|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--shipped-quantity**|number||shipped_quantity|shippedQuantity|
|**--ship-quantity**|number||ship_quantity|shipQuantity|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company update-sale-quote

update-sale-quote a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-quote|UpdateSalesQuotes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--accepted-date**|date||accepted_date|acceptedDate|
|**--billing-postal-address**|object|postalAddressType|billing_postal_address|billingPostalAddress|
|**--bill-to-customer-id**|uuid||bill_to_customer_id|billToCustomerId|
|**--bill-to-customer-number**|string||bill_to_customer_number|billToCustomerNumber|
|**--bill-to-name**|string||bill_to_name|billToName|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-name**|string||customer_name|customerName|
|**--customer-number**|string||customer_number|customerNumber|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--document-date**|date||document_date|documentDate|
|**--due-date**|date||due_date|dueDate|
|**--email**|string||email|email|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--salesperson**|string||salesperson|salesperson|
|**--selling-postal-address**|object|postalAddressType|selling_postal_address|sellingPostalAddress|
|**--sent-date**|date-time||sent_date|sentDate|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--shipping-postal-address**|object|postalAddressType|shipping_postal_address|shippingPostalAddress|
|**--ship-to-contact**|string||ship_to_contact|shipToContact|
|**--ship-to-name**|string||ship_to_name|shipToName|
|**--status**|string||status|status|
|**--total-amount-excluding-tax**|number||total_amount_excluding_tax|totalAmountExcludingTax|
|**--total-amount-including-tax**|number||total_amount_including_tax|totalAmountIncludingTax|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--valid-until-date**|date||valid_until_date|validUntilDate|
|**--currency**|object|currency|currency|currency|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--sales-quote-lines**|array||sales_quote_lines|salesQuoteLines|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||microsoft_graph_customer_currency_code|currencyCode|
|**--customer-currency-id**|uuid||microsoft_graph_customer_currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||microsoft_graph_customer_email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-customer-number**|string||microsoft_graph_customer_number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||microsoft_graph_customer_payment_terms_id_payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||microsoft_graph_customer_phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||microsoft_graph_customer_shipment_method_id_shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|microsoft_graph_currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|microsoft_graph_payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|microsoft_graph_shipment_method|shipmentMethod|

### financials financial-company update-sale-quote-line

update-sale-quote-line a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-quote-line|UpdateSalesQuoteLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company update-shipment-method

update-shipment-method a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shipment-method|UpdateShipmentMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--shipment-method-id**|string|key: id of shipmentMethod|shipment_method_id|shipmentMethod-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company update-tax-area

update-tax-area a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-tax-area|UpdateTaxAreas|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--tax-area-id**|string|key: id of taxArea|tax_area_id|taxArea-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--tax-type**|string||tax_type|taxType|

### financials financial-company update-tax-group

update-tax-group a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-tax-group|UpdateTaxGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--tax-group-id**|string|key: id of taxGroup|tax_group_id|taxGroup-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--tax-type**|string||tax_type|taxType|

### financials financial-company update-unit-of-measure

update-unit-of-measure a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-unit-of-measure|UpdateUnitsOfMeasure|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--unit-of-measure-id**|string|key: id of unitOfMeasure|unit_of_measure_id|unitOfMeasure-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--international-standard-code**|string||international_standard_code|internationalStandardCode|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company update-vendor

update-vendor a financials financial-company.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company|financials.companies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-vendor|UpdateVendors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--balance**|number||balance|balance|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|

### financials financial-company-customer create-picture

create-picture a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-customer delete

delete a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteCurrency|
|delete|DeletePaymentMethod|
|delete|DeletePaymentTerm|
|delete|DeleteShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-customer get-currency

get-currency a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer get-payment-method

get-payment-method a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-method|GetPaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer get-payment-term

get-payment-term a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer get-picture

get-picture a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer get-picture-content

get-picture-content a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-customer get-shipment-method

get-shipment-method a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shipment-method|GetShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer list-picture

list-picture a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer set-picture-content

set-picture-content a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-customer update-currency

update-currency a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-customer update-payment-method

update-payment-method a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-method|UpdatePaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-customer update-payment-term

update-payment-term a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-customer update-picture

update-picture a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-customer update-shipment-method

update-shipment-method a financials financial-company-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer|financials.companies.customers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shipment-method|UpdateShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-id**|string|key: id of customer|customer_id|customer-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-customer-payment delete

delete a financials financial-company-customer-payment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment|financials.companies.customerPayments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-customer-payment get-customer

get-customer a financials financial-company-customer-payment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment|financials.companies.customerPayments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer|GetCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment update-customer

update-customer a financials financial-company-customer-payment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment|financials.companies.customerPayments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-customer|UpdateCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--type**|string||type|type|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company-customer-payment-customer create-picture

create-picture a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-customer-payment-customer delete

delete a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteCurrency|
|delete|DeletePaymentMethod|
|delete|DeletePaymentTerm|
|delete|DeleteShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-customer-payment-customer get-currency

get-currency a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-customer get-payment-method

get-payment-method a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-method|GetPaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-customer get-payment-term

get-payment-term a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-customer get-picture

get-picture a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-customer get-picture-content

get-picture-content a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-customer-payment-customer get-shipment-method

get-shipment-method a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shipment-method|GetShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-customer list-picture

list-picture a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-customer set-picture-content

set-picture-content a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-customer-payment-customer update-currency

update-currency a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-customer-payment-customer update-payment-method

update-payment-method a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-method|UpdatePaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-customer-payment-customer update-payment-term

update-payment-term a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-customer-payment-customer update-picture

update-picture a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-customer-payment-customer update-shipment-method

update-shipment-method a financials financial-company-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-customer|financials.companies.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shipment-method|UpdateShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-customer-payment-journal create-customer-payment

create-customer-payment a financials financial-company-customer-payment-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal|financials.companies.customerPaymentJournals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-customer-payment|CreateCustomerPayments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--id**|string|Read-only.|id|id|
|**--amount**|number||amount|amount|
|**--applies-to-invoice-id**|uuid||applies_to_invoice_id|appliesToInvoiceId|
|**--applies-to-invoice-number**|string||applies_to_invoice_number|appliesToInvoiceNumber|
|**--comment**|string||comment|comment|
|**--contact-id**|string||contact_id|contactId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-number**|string||customer_number|customerNumber|
|**--description**|string||description|description|
|**--document-number**|string||document_number|documentNumber|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--journal-display-name**|string||journal_display_name|journalDisplayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--line-number**|integer||line_number|lineNumber|
|**--posting-date**|date||posting_date|postingDate|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||currency_code|currencyCode|
|**--customer-currency-id**|uuid||currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company-customer-payment-journal delete

delete a financials financial-company-customer-payment-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal|financials.companies.customerPaymentJournals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCustomerPayments|
|delete|DeleteAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-customer-payment-journal get-account

get-account a financials financial-company-customer-payment-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal|financials.companies.customerPaymentJournals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-journal get-customer-payment

get-customer-payment a financials financial-company-customer-payment-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal|financials.companies.customerPaymentJournals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer-payment|GetCustomerPayments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-journal list-customer-payment

list-customer-payment a financials financial-company-customer-payment-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal|financials.companies.customerPaymentJournals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-customer-payment|ListCustomerPayments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-journal update-account

update-account a financials financial-company-customer-payment-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal|financials.companies.customerPaymentJournals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-customer-payment-journal update-customer-payment

update-customer-payment a financials financial-company-customer-payment-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal|financials.companies.customerPaymentJournals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-customer-payment|UpdateCustomerPayments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--amount**|number||amount|amount|
|**--applies-to-invoice-id**|uuid||applies_to_invoice_id|appliesToInvoiceId|
|**--applies-to-invoice-number**|string||applies_to_invoice_number|appliesToInvoiceNumber|
|**--comment**|string||comment|comment|
|**--contact-id**|string||contact_id|contactId|
|**--customer-id**|uuid||customer_id|customerId|
|**--customer-number**|string||customer_number|customerNumber|
|**--description**|string||description|description|
|**--document-number**|string||document_number|documentNumber|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--journal-display-name**|string||journal_display_name|journalDisplayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--line-number**|integer||line_number|lineNumber|
|**--posting-date**|date||posting_date|postingDate|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--customer-address**|object|postalAddressType|address|address|
|**--customer-blocked**|string||blocked|blocked|
|**--customer-currency-code**|string||currency_code|currencyCode|
|**--customer-currency-id**|uuid||currency_id|currencyId|
|**--customer-display-name**|string||display_name|displayName|
|**--customer-email**|string||email|email|
|**--customer-last-modified-date-time**|date-time||microsoft_graph_customer_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--customer-payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--customer-payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--customer-phone-number**|string||phone_number|phoneNumber|
|**--customer-shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--customer-tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--customer-tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--customer-tax-liable**|boolean||tax_liable|taxLiable|
|**--customer-tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--customer-type**|string||type|type|
|**--customer-website**|string||website|website|
|**--customer-currency**|object|currency|currency|currency|
|**--customer-payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--customer-payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--customer-picture**|array||picture|picture|
|**--customer-shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company-customer-payment-journal-customer-payment delete

delete a financials financial-company-customer-payment-journal-customer-payment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment|financials.companies.customerPaymentJournals.customerPayments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-customer-payment-journal-customer-payment get-customer

get-customer a financials financial-company-customer-payment-journal-customer-payment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment|financials.companies.customerPaymentJournals.customerPayments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer|GetCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-journal-customer-payment update-customer

update-customer a financials financial-company-customer-payment-journal-customer-payment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment|financials.companies.customerPaymentJournals.customerPayments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-customer|UpdateCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--type**|string||type|type|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company-customer-payment-journal-customer-payment-customer create-picture

create-picture a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-customer-payment-journal-customer-payment-customer delete

delete a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteCurrency|
|delete|DeletePaymentMethod|
|delete|DeletePaymentTerm|
|delete|DeleteShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-customer-payment-journal-customer-payment-customer get-currency

get-currency a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-journal-customer-payment-customer get-payment-method

get-payment-method a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-method|GetPaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-journal-customer-payment-customer get-payment-term

get-payment-term a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-journal-customer-payment-customer get-picture

get-picture a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-journal-customer-payment-customer get-picture-content

get-picture-content a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-customer-payment-journal-customer-payment-customer get-shipment-method

get-shipment-method a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shipment-method|GetShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-journal-customer-payment-customer list-picture

list-picture a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-customer-payment-journal-customer-payment-customer set-picture-content

set-picture-content a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-customer-payment-journal-customer-payment-customer update-currency

update-currency a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-customer-payment-journal-customer-payment-customer update-payment-method

update-payment-method a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-method|UpdatePaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-customer-payment-journal-customer-payment-customer update-payment-term

update-payment-term a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-customer-payment-journal-customer-payment-customer update-picture

update-picture a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-customer-payment-journal-customer-payment-customer update-shipment-method

update-shipment-method a financials financial-company-customer-payment-journal-customer-payment-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-customer-payment-journal-customer-payment-customer|financials.companies.customerPaymentJournals.customerPayments.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shipment-method|UpdateShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--customer-payment-journal-id**|string|key: id of customerPaymentJournal|customer_payment_journal_id|customerPaymentJournal-id|
|**--customer-payment-id**|string|key: id of customerPayment|customer_payment_id|customerPayment-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-dimension create-dimension-value

create-dimension-value a financials financial-company-dimension.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-dimension|financials.companies.dimensions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-dimension-value|CreateDimensionValues|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--dimension-id**|string|key: id of dimension|dimension_id|dimension-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-dimension delete

delete a financials financial-company-dimension.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-dimension|financials.companies.dimensions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDimensionValues|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--dimension-id**|string|key: id of dimension|dimension_id|dimension-id|
|**--dimension-value-id**|string|key: id of dimensionValue|dimension_value_id|dimensionValue-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-dimension get-dimension-value

get-dimension-value a financials financial-company-dimension.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-dimension|financials.companies.dimensions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-dimension-value|GetDimensionValues|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--dimension-id**|string|key: id of dimension|dimension_id|dimension-id|
|**--dimension-value-id**|string|key: id of dimensionValue|dimension_value_id|dimensionValue-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-dimension list-dimension-value

list-dimension-value a financials financial-company-dimension.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-dimension|financials.companies.dimensions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-dimension-value|ListDimensionValues|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--dimension-id**|string|key: id of dimension|dimension_id|dimension-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-dimension update-dimension-value

update-dimension-value a financials financial-company-dimension.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-dimension|financials.companies.dimensions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-dimension-value|UpdateDimensionValues|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--dimension-id**|string|key: id of dimension|dimension_id|dimension-id|
|**--dimension-value-id**|string|key: id of dimensionValue|dimension_value_id|dimensionValue-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-employee create-picture

create-picture a financials financial-company-employee.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-employee|financials.companies.employees|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--employee-id**|string|key: id of employee|employee_id|employee-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-employee delete

delete a financials financial-company-employee.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-employee|financials.companies.employees|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--employee-id**|string|key: id of employee|employee_id|employee-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-employee get-picture

get-picture a financials financial-company-employee.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-employee|financials.companies.employees|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--employee-id**|string|key: id of employee|employee_id|employee-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-employee get-picture-content

get-picture-content a financials financial-company-employee.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-employee|financials.companies.employees|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--employee-id**|string|key: id of employee|employee_id|employee-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-employee list-picture

list-picture a financials financial-company-employee.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-employee|financials.companies.employees|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--employee-id**|string|key: id of employee|employee_id|employee-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-employee set-picture-content

set-picture-content a financials financial-company-employee.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-employee|financials.companies.employees|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--employee-id**|string|key: id of employee|employee_id|employee-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-employee update-picture

update-picture a financials financial-company-employee.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-employee|financials.companies.employees|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--employee-id**|string|key: id of employee|employee_id|employee-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-general-ledger-entry delete

delete a financials financial-company-general-ledger-entry.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-general-ledger-entry|financials.companies.generalLedgerEntries|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--general-ledger-entry-id**|string|key: id of generalLedgerEntry|general_ledger_entry_id|generalLedgerEntry-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-general-ledger-entry get-account

get-account a financials financial-company-general-ledger-entry.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-general-ledger-entry|financials.companies.generalLedgerEntries|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--general-ledger-entry-id**|string|key: id of generalLedgerEntry|general_ledger_entry_id|generalLedgerEntry-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-general-ledger-entry update-account

update-account a financials financial-company-general-ledger-entry.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-general-ledger-entry|financials.companies.generalLedgerEntries|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--general-ledger-entry-id**|string|key: id of generalLedgerEntry|general_ledger_entry_id|generalLedgerEntry-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-item create-picture

create-picture a financials financial-company-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-item|financials.companies.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-item delete

delete a financials financial-company-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-item|financials.companies.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-item get-item-category

get-item-category a financials financial-company-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-item|financials.companies.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-item get-picture

get-picture a financials financial-company-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-item|financials.companies.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-item get-picture-content

get-picture-content a financials financial-company-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-item|financials.companies.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-item list-picture

list-picture a financials financial-company-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-item|financials.companies.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-item set-picture-content

set-picture-content a financials financial-company-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-item|financials.companies.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-item update-item-category

update-item-category a financials financial-company-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-item|financials.companies.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-item update-picture

update-picture a financials financial-company-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-item|financials.companies.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--item-id**|string|key: id of item|item_id|item-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-journal create-journal-line

create-journal-line a financials financial-company-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal|financials.companies.journals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-journal-line|CreateJournalLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--account-number**|string||account_number|accountNumber|
|**--amount**|number||amount|amount|
|**--comment**|string||comment|comment|
|**--description**|string||description|description|
|**--document-number**|string||document_number|documentNumber|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--journal-display-name**|string||journal_display_name|journalDisplayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--line-number**|integer||line_number|lineNumber|
|**--posting-date**|date||posting_date|postingDate|
|**--account**|object|account|account|account|

### financials financial-company-journal delete

delete a financials financial-company-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal|financials.companies.journals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteJournalLines|
|delete|DeleteAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-journal get-account

get-account a financials financial-company-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal|financials.companies.journals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-journal get-journal-line

get-journal-line a financials financial-company-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal|financials.companies.journals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-journal-line|GetJournalLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-journal list-journal-line

list-journal-line a financials financial-company-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal|financials.companies.journals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-journal-line|ListJournalLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-journal post

post a financials financial-company-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal|financials.companies.journals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|post|post|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|

### financials financial-company-journal update-account

update-account a financials financial-company-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal|financials.companies.journals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-journal update-journal-line

update-journal-line a financials financial-company-journal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal|financials.companies.journals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-journal-line|UpdateJournalLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--account-number**|string||account_number|accountNumber|
|**--amount**|number||amount|amount|
|**--comment**|string||comment|comment|
|**--description**|string||description|description|
|**--document-number**|string||document_number|documentNumber|
|**--external-document-number**|string||external_document_number|externalDocumentNumber|
|**--journal-display-name**|string||journal_display_name|journalDisplayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--line-number**|integer||line_number|lineNumber|
|**--posting-date**|date||posting_date|postingDate|
|**--account**|object|account|account|account|

### financials financial-company-journal-journal-line delete

delete a financials financial-company-journal-journal-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal-journal-line|financials.companies.journals.journalLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-journal-journal-line get-account

get-account a financials financial-company-journal-journal-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal-journal-line|financials.companies.journals.journalLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-journal-journal-line update-account

update-account a financials financial-company-journal-journal-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal-journal-line|financials.companies.journals.journalLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-id**|string|key: id of journal|journal_id|journal-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-journal-line delete

delete a financials financial-company-journal-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal-line|financials.companies.journalLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-journal-line get-account

get-account a financials financial-company-journal-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal-line|financials.companies.journalLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-journal-line update-account

update-account a financials financial-company-journal-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-journal-line|financials.companies.journalLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--journal-line-id**|string|key: id of journalLine|journal_line_id|journalLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-purchase-invoice create-purchase-invoice-line

create-purchase-invoice-line a financials financial-company-purchase-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice|financials.companies.purchaseInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-purchase-invoice-line|CreatePurchaseInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--expected-receipt-date**|date||expected_receipt_date|expectedReceiptDate|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-cost**|number||unit_cost|unitCost|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||number_unit_cost|unitCost|
|**--item-unit-price**|number||unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company-purchase-invoice delete

delete a financials financial-company-purchase-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice|financials.companies.purchaseInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePurchaseInvoiceLines|
|delete|DeleteCurrency|
|delete|DeleteVendor|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-purchase-invoice get-currency

get-currency a financials financial-company-purchase-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice|financials.companies.purchaseInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice get-purchase-invoice-line

get-purchase-invoice-line a financials financial-company-purchase-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice|financials.companies.purchaseInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-purchase-invoice-line|GetPurchaseInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice get-vendor

get-vendor a financials financial-company-purchase-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice|financials.companies.purchaseInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-vendor|GetVendor|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice list-purchase-invoice-line

list-purchase-invoice-line a financials financial-company-purchase-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice|financials.companies.purchaseInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-purchase-invoice-line|ListPurchaseInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice post

post a financials financial-company-purchase-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice|financials.companies.purchaseInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|post|post|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|

### financials financial-company-purchase-invoice update-currency

update-currency a financials financial-company-purchase-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice|financials.companies.purchaseInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-purchase-invoice update-purchase-invoice-line

update-purchase-invoice-line a financials financial-company-purchase-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice|financials.companies.purchaseInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-purchase-invoice-line|UpdatePurchaseInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--expected-receipt-date**|date||expected_receipt_date|expectedReceiptDate|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-cost**|number||unit_cost|unitCost|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||number_unit_cost|unitCost|
|**--item-unit-price**|number||unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company-purchase-invoice update-vendor

update-vendor a financials financial-company-purchase-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice|financials.companies.purchaseInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-vendor|UpdateVendor|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--balance**|number||balance|balance|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|

### financials financial-company-purchase-invoice-line delete

delete a financials financial-company-purchase-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line|financials.companies.purchaseInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-purchase-invoice-line get-account

get-account a financials financial-company-purchase-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line|financials.companies.purchaseInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-line get-item

get-item a financials financial-company-purchase-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line|financials.companies.purchaseInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-line update-account

update-account a financials financial-company-purchase-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line|financials.companies.purchaseInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-purchase-invoice-line update-item

update-item a financials financial-company-purchase-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line|financials.companies.purchaseInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company-purchase-invoice-line-item create-picture

create-picture a financials financial-company-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line-item|financials.companies.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-purchase-invoice-line-item delete

delete a financials financial-company-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line-item|financials.companies.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-purchase-invoice-line-item get-item-category

get-item-category a financials financial-company-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line-item|financials.companies.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-line-item get-picture

get-picture a financials financial-company-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line-item|financials.companies.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-line-item get-picture-content

get-picture-content a financials financial-company-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line-item|financials.companies.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-purchase-invoice-line-item list-picture

list-picture a financials financial-company-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line-item|financials.companies.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-line-item set-picture-content

set-picture-content a financials financial-company-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line-item|financials.companies.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-purchase-invoice-line-item update-item-category

update-item-category a financials financial-company-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line-item|financials.companies.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-purchase-invoice-line-item update-picture

update-picture a financials financial-company-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-line-item|financials.companies.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-purchase-invoice-purchase-invoice-line delete

delete a financials financial-company-purchase-invoice-purchase-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line|financials.companies.purchaseInvoices.purchaseInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-purchase-invoice-purchase-invoice-line get-account

get-account a financials financial-company-purchase-invoice-purchase-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line|financials.companies.purchaseInvoices.purchaseInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-purchase-invoice-line get-item

get-item a financials financial-company-purchase-invoice-purchase-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line|financials.companies.purchaseInvoices.purchaseInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-purchase-invoice-line update-account

update-account a financials financial-company-purchase-invoice-purchase-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line|financials.companies.purchaseInvoices.purchaseInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-purchase-invoice-purchase-invoice-line update-item

update-item a financials financial-company-purchase-invoice-purchase-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line|financials.companies.purchaseInvoices.purchaseInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company-purchase-invoice-purchase-invoice-line-item create-picture

create-picture a financials financial-company-purchase-invoice-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line-item|financials.companies.purchaseInvoices.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-purchase-invoice-purchase-invoice-line-item delete

delete a financials financial-company-purchase-invoice-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line-item|financials.companies.purchaseInvoices.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-purchase-invoice-purchase-invoice-line-item get-item-category

get-item-category a financials financial-company-purchase-invoice-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line-item|financials.companies.purchaseInvoices.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-purchase-invoice-line-item get-picture

get-picture a financials financial-company-purchase-invoice-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line-item|financials.companies.purchaseInvoices.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-purchase-invoice-line-item get-picture-content

get-picture-content a financials financial-company-purchase-invoice-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line-item|financials.companies.purchaseInvoices.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-purchase-invoice-purchase-invoice-line-item list-picture

list-picture a financials financial-company-purchase-invoice-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line-item|financials.companies.purchaseInvoices.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-purchase-invoice-line-item set-picture-content

set-picture-content a financials financial-company-purchase-invoice-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line-item|financials.companies.purchaseInvoices.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-purchase-invoice-purchase-invoice-line-item update-item-category

update-item-category a financials financial-company-purchase-invoice-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line-item|financials.companies.purchaseInvoices.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-purchase-invoice-purchase-invoice-line-item update-picture

update-picture a financials financial-company-purchase-invoice-purchase-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-purchase-invoice-line-item|financials.companies.purchaseInvoices.purchaseInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--purchase-invoice-line-id**|string|key: id of purchaseInvoiceLine|purchase_invoice_line_id|purchaseInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-purchase-invoice-vendor create-picture

create-picture a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-purchase-invoice-vendor delete

delete a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteCurrency|
|delete|DeletePaymentMethod|
|delete|DeletePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-purchase-invoice-vendor get-currency

get-currency a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-vendor get-payment-method

get-payment-method a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-method|GetPaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-vendor get-payment-term

get-payment-term a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-vendor get-picture

get-picture a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-vendor get-picture-content

get-picture-content a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-purchase-invoice-vendor list-picture

list-picture a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-purchase-invoice-vendor set-picture-content

set-picture-content a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-purchase-invoice-vendor update-currency

update-currency a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-purchase-invoice-vendor update-payment-method

update-payment-method a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-method|UpdatePaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-purchase-invoice-vendor update-payment-term

update-payment-term a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-purchase-invoice-vendor update-picture

update-picture a financials financial-company-purchase-invoice-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-purchase-invoice-vendor|financials.companies.purchaseInvoices.vendor|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--purchase-invoice-id**|string|key: id of purchaseInvoice|purchase_invoice_id|purchaseInvoice-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-credit-memo create-sale-credit-memo-line

create-sale-credit-memo-line a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-credit-memo-line|CreateSalesCreditMemoLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company-sale-credit-memo delete

delete a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSalesCreditMemoLines|
|delete|DeleteCurrency|
|delete|DeleteCustomer|
|delete|DeletePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-credit-memo get-currency

get-currency a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo get-customer

get-customer a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer|GetCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo get-payment-term

get-payment-term a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo get-sale-credit-memo-line

get-sale-credit-memo-line a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-credit-memo-line|GetSalesCreditMemoLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo list-sale-credit-memo-line

list-sale-credit-memo-line a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-credit-memo-line|ListSalesCreditMemoLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo update-currency

update-currency a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-sale-credit-memo update-customer

update-customer a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-customer|UpdateCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--type**|string||type|type|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company-sale-credit-memo update-payment-term

update-payment-term a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-credit-memo update-sale-credit-memo-line

update-sale-credit-memo-line a financials financial-company-sale-credit-memo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo|financials.companies.salesCreditMemos|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-credit-memo-line|UpdateSalesCreditMemoLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company-sale-credit-memo-customer create-picture

create-picture a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-credit-memo-customer delete

delete a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteCurrency|
|delete|DeletePaymentMethod|
|delete|DeletePaymentTerm|
|delete|DeleteShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-credit-memo-customer get-currency

get-currency a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-customer get-payment-method

get-payment-method a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-method|GetPaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-customer get-payment-term

get-payment-term a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-customer get-picture

get-picture a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-customer get-picture-content

get-picture-content a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-credit-memo-customer get-shipment-method

get-shipment-method a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shipment-method|GetShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-customer list-picture

list-picture a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-customer set-picture-content

set-picture-content a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-credit-memo-customer update-currency

update-currency a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-sale-credit-memo-customer update-payment-method

update-payment-method a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-method|UpdatePaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-credit-memo-customer update-payment-term

update-payment-term a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-credit-memo-customer update-picture

update-picture a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-credit-memo-customer update-shipment-method

update-shipment-method a financials financial-company-sale-credit-memo-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-customer|financials.companies.salesCreditMemos.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shipment-method|UpdateShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-credit-memo-line delete

delete a financials financial-company-sale-credit-memo-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line|financials.companies.salesCreditMemoLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-credit-memo-line get-account

get-account a financials financial-company-sale-credit-memo-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line|financials.companies.salesCreditMemoLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-line get-item

get-item a financials financial-company-sale-credit-memo-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line|financials.companies.salesCreditMemoLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-line update-account

update-account a financials financial-company-sale-credit-memo-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line|financials.companies.salesCreditMemoLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-sale-credit-memo-line update-item

update-item a financials financial-company-sale-credit-memo-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line|financials.companies.salesCreditMemoLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company-sale-credit-memo-line-item create-picture

create-picture a financials financial-company-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line-item|financials.companies.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-credit-memo-line-item delete

delete a financials financial-company-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line-item|financials.companies.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-credit-memo-line-item get-item-category

get-item-category a financials financial-company-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line-item|financials.companies.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-line-item get-picture

get-picture a financials financial-company-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line-item|financials.companies.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-line-item get-picture-content

get-picture-content a financials financial-company-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line-item|financials.companies.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-credit-memo-line-item list-picture

list-picture a financials financial-company-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line-item|financials.companies.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-line-item set-picture-content

set-picture-content a financials financial-company-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line-item|financials.companies.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-credit-memo-line-item update-item-category

update-item-category a financials financial-company-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line-item|financials.companies.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-credit-memo-line-item update-picture

update-picture a financials financial-company-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-line-item|financials.companies.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-credit-memo-sale-credit-memo-line delete

delete a financials financial-company-sale-credit-memo-sale-credit-memo-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line|financials.companies.salesCreditMemos.salesCreditMemoLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-credit-memo-sale-credit-memo-line get-account

get-account a financials financial-company-sale-credit-memo-sale-credit-memo-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line|financials.companies.salesCreditMemos.salesCreditMemoLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-sale-credit-memo-line get-item

get-item a financials financial-company-sale-credit-memo-sale-credit-memo-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line|financials.companies.salesCreditMemos.salesCreditMemoLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-sale-credit-memo-line update-account

update-account a financials financial-company-sale-credit-memo-sale-credit-memo-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line|financials.companies.salesCreditMemos.salesCreditMemoLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-sale-credit-memo-sale-credit-memo-line update-item

update-item a financials financial-company-sale-credit-memo-sale-credit-memo-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line|financials.companies.salesCreditMemos.salesCreditMemoLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company-sale-credit-memo-sale-credit-memo-line-item create-picture

create-picture a financials financial-company-sale-credit-memo-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line-item|financials.companies.salesCreditMemos.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-credit-memo-sale-credit-memo-line-item delete

delete a financials financial-company-sale-credit-memo-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line-item|financials.companies.salesCreditMemos.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-credit-memo-sale-credit-memo-line-item get-item-category

get-item-category a financials financial-company-sale-credit-memo-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line-item|financials.companies.salesCreditMemos.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-sale-credit-memo-line-item get-picture

get-picture a financials financial-company-sale-credit-memo-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line-item|financials.companies.salesCreditMemos.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-sale-credit-memo-line-item get-picture-content

get-picture-content a financials financial-company-sale-credit-memo-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line-item|financials.companies.salesCreditMemos.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-credit-memo-sale-credit-memo-line-item list-picture

list-picture a financials financial-company-sale-credit-memo-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line-item|financials.companies.salesCreditMemos.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-credit-memo-sale-credit-memo-line-item set-picture-content

set-picture-content a financials financial-company-sale-credit-memo-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line-item|financials.companies.salesCreditMemos.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-credit-memo-sale-credit-memo-line-item update-item-category

update-item-category a financials financial-company-sale-credit-memo-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line-item|financials.companies.salesCreditMemos.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-credit-memo-sale-credit-memo-line-item update-picture

update-picture a financials financial-company-sale-credit-memo-sale-credit-memo-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-credit-memo-sale-credit-memo-line-item|financials.companies.salesCreditMemos.salesCreditMemoLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-credit-memo-id**|string|key: id of salesCreditMemo|sales_credit_memo_id|salesCreditMemo-id|
|**--sales-credit-memo-line-id**|string|key: id of salesCreditMemoLine|sales_credit_memo_line_id|salesCreditMemoLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-invoice cancel

cancel a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|

### financials financial-company-sale-invoice cancel-and-send

cancel-and-send a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel-and-send|cancelAndSend|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|

### financials financial-company-sale-invoice create-sale-invoice-line

create-sale-invoice-line a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-invoice-line|CreateSalesInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company-sale-invoice delete

delete a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSalesInvoiceLines|
|delete|DeleteCurrency|
|delete|DeleteCustomer|
|delete|DeletePaymentTerm|
|delete|DeleteShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-invoice get-currency

get-currency a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice get-customer

get-customer a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer|GetCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice get-payment-term

get-payment-term a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice get-sale-invoice-line

get-sale-invoice-line a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-invoice-line|GetSalesInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice get-shipment-method

get-shipment-method a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shipment-method|GetShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice list-sale-invoice-line

list-sale-invoice-line a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-invoice-line|ListSalesInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice post

post a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|post|post|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|

### financials financial-company-sale-invoice post-and-send

post-and-send a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|post-and-send|postAndSend|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|

### financials financial-company-sale-invoice send

send a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send|send|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|

### financials financial-company-sale-invoice update-currency

update-currency a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-sale-invoice update-customer

update-customer a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-customer|UpdateCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--type**|string||type|type|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company-sale-invoice update-payment-term

update-payment-term a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-invoice update-sale-invoice-line

update-sale-invoice-line a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-invoice-line|UpdateSalesInvoiceLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company-sale-invoice update-shipment-method

update-shipment-method a financials financial-company-sale-invoice.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice|financials.companies.salesInvoices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shipment-method|UpdateShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-invoice-customer create-picture

create-picture a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-invoice-customer delete

delete a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteCurrency|
|delete|DeletePaymentMethod|
|delete|DeletePaymentTerm|
|delete|DeleteShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-invoice-customer get-currency

get-currency a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-customer get-payment-method

get-payment-method a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-method|GetPaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-customer get-payment-term

get-payment-term a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-customer get-picture

get-picture a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-customer get-picture-content

get-picture-content a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-invoice-customer get-shipment-method

get-shipment-method a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shipment-method|GetShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-customer list-picture

list-picture a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-customer set-picture-content

set-picture-content a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-invoice-customer update-currency

update-currency a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-sale-invoice-customer update-payment-method

update-payment-method a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-method|UpdatePaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-invoice-customer update-payment-term

update-payment-term a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-invoice-customer update-picture

update-picture a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-invoice-customer update-shipment-method

update-shipment-method a financials financial-company-sale-invoice-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-customer|financials.companies.salesInvoices.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shipment-method|UpdateShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-invoice-line delete

delete a financials financial-company-sale-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line|financials.companies.salesInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-invoice-line get-account

get-account a financials financial-company-sale-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line|financials.companies.salesInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-line get-item

get-item a financials financial-company-sale-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line|financials.companies.salesInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-line update-account

update-account a financials financial-company-sale-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line|financials.companies.salesInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-sale-invoice-line update-item

update-item a financials financial-company-sale-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line|financials.companies.salesInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company-sale-invoice-line-item create-picture

create-picture a financials financial-company-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line-item|financials.companies.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-invoice-line-item delete

delete a financials financial-company-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line-item|financials.companies.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-invoice-line-item get-item-category

get-item-category a financials financial-company-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line-item|financials.companies.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-line-item get-picture

get-picture a financials financial-company-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line-item|financials.companies.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-line-item get-picture-content

get-picture-content a financials financial-company-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line-item|financials.companies.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-invoice-line-item list-picture

list-picture a financials financial-company-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line-item|financials.companies.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-line-item set-picture-content

set-picture-content a financials financial-company-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line-item|financials.companies.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-invoice-line-item update-item-category

update-item-category a financials financial-company-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line-item|financials.companies.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-invoice-line-item update-picture

update-picture a financials financial-company-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-line-item|financials.companies.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-invoice-sale-invoice-line delete

delete a financials financial-company-sale-invoice-sale-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line|financials.companies.salesInvoices.salesInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-invoice-sale-invoice-line get-account

get-account a financials financial-company-sale-invoice-sale-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line|financials.companies.salesInvoices.salesInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-sale-invoice-line get-item

get-item a financials financial-company-sale-invoice-sale-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line|financials.companies.salesInvoices.salesInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-sale-invoice-line update-account

update-account a financials financial-company-sale-invoice-sale-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line|financials.companies.salesInvoices.salesInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-sale-invoice-sale-invoice-line update-item

update-item a financials financial-company-sale-invoice-sale-invoice-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line|financials.companies.salesInvoices.salesInvoiceLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company-sale-invoice-sale-invoice-line-item create-picture

create-picture a financials financial-company-sale-invoice-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line-item|financials.companies.salesInvoices.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-invoice-sale-invoice-line-item delete

delete a financials financial-company-sale-invoice-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line-item|financials.companies.salesInvoices.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-invoice-sale-invoice-line-item get-item-category

get-item-category a financials financial-company-sale-invoice-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line-item|financials.companies.salesInvoices.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-sale-invoice-line-item get-picture

get-picture a financials financial-company-sale-invoice-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line-item|financials.companies.salesInvoices.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-sale-invoice-line-item get-picture-content

get-picture-content a financials financial-company-sale-invoice-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line-item|financials.companies.salesInvoices.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-invoice-sale-invoice-line-item list-picture

list-picture a financials financial-company-sale-invoice-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line-item|financials.companies.salesInvoices.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-invoice-sale-invoice-line-item set-picture-content

set-picture-content a financials financial-company-sale-invoice-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line-item|financials.companies.salesInvoices.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-invoice-sale-invoice-line-item update-item-category

update-item-category a financials financial-company-sale-invoice-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line-item|financials.companies.salesInvoices.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-invoice-sale-invoice-line-item update-picture

update-picture a financials financial-company-sale-invoice-sale-invoice-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-invoice-sale-invoice-line-item|financials.companies.salesInvoices.salesInvoiceLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-invoice-id**|string|key: id of salesInvoice|sales_invoice_id|salesInvoice-id|
|**--sales-invoice-line-id**|string|key: id of salesInvoiceLine|sales_invoice_line_id|salesInvoiceLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-order create-sale-order-line

create-sale-order-line a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-order-line|CreateSalesOrderLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--invoiced-quantity**|number||invoiced_quantity|invoicedQuantity|
|**--invoice-quantity**|number||invoice_quantity|invoiceQuantity|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--shipped-quantity**|number||shipped_quantity|shippedQuantity|
|**--ship-quantity**|number||ship_quantity|shipQuantity|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company-sale-order delete

delete a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSalesOrderLines|
|delete|DeleteCurrency|
|delete|DeleteCustomer|
|delete|DeletePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-order get-currency

get-currency a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order get-customer

get-customer a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer|GetCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order get-payment-term

get-payment-term a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order get-sale-order-line

get-sale-order-line a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-order-line|GetSalesOrderLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order list-sale-order-line

list-sale-order-line a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-order-line|ListSalesOrderLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order update-currency

update-currency a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-sale-order update-customer

update-customer a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-customer|UpdateCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--type**|string||type|type|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company-sale-order update-payment-term

update-payment-term a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-order update-sale-order-line

update-sale-order-line a financials financial-company-sale-order.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order|financials.companies.salesOrders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-order-line|UpdateSalesOrderLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--invoice-discount-allocation**|number||invoice_discount_allocation|invoiceDiscountAllocation|
|**--invoiced-quantity**|number||invoiced_quantity|invoicedQuantity|
|**--invoice-quantity**|number||invoice_quantity|invoiceQuantity|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--shipment-date**|date||shipment_date|shipmentDate|
|**--shipped-quantity**|number||shipped_quantity|shippedQuantity|
|**--ship-quantity**|number||ship_quantity|shipQuantity|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company-sale-order-customer create-picture

create-picture a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-order-customer delete

delete a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteCurrency|
|delete|DeletePaymentMethod|
|delete|DeletePaymentTerm|
|delete|DeleteShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-order-customer get-currency

get-currency a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-customer get-payment-method

get-payment-method a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-method|GetPaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-customer get-payment-term

get-payment-term a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-customer get-picture

get-picture a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-customer get-picture-content

get-picture-content a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-order-customer get-shipment-method

get-shipment-method a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shipment-method|GetShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-customer list-picture

list-picture a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-customer set-picture-content

set-picture-content a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-order-customer update-currency

update-currency a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-sale-order-customer update-payment-method

update-payment-method a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-method|UpdatePaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-order-customer update-payment-term

update-payment-term a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-order-customer update-picture

update-picture a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-order-customer update-shipment-method

update-shipment-method a financials financial-company-sale-order-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-customer|financials.companies.salesOrders.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shipment-method|UpdateShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-order-line delete

delete a financials financial-company-sale-order-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line|financials.companies.salesOrderLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-order-line get-account

get-account a financials financial-company-sale-order-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line|financials.companies.salesOrderLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-line get-item

get-item a financials financial-company-sale-order-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line|financials.companies.salesOrderLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-line update-account

update-account a financials financial-company-sale-order-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line|financials.companies.salesOrderLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-sale-order-line update-item

update-item a financials financial-company-sale-order-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line|financials.companies.salesOrderLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company-sale-order-line-item create-picture

create-picture a financials financial-company-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line-item|financials.companies.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-order-line-item delete

delete a financials financial-company-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line-item|financials.companies.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-order-line-item get-item-category

get-item-category a financials financial-company-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line-item|financials.companies.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-line-item get-picture

get-picture a financials financial-company-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line-item|financials.companies.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-line-item get-picture-content

get-picture-content a financials financial-company-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line-item|financials.companies.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-order-line-item list-picture

list-picture a financials financial-company-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line-item|financials.companies.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-line-item set-picture-content

set-picture-content a financials financial-company-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line-item|financials.companies.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-order-line-item update-item-category

update-item-category a financials financial-company-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line-item|financials.companies.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-order-line-item update-picture

update-picture a financials financial-company-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-line-item|financials.companies.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-order-sale-order-line delete

delete a financials financial-company-sale-order-sale-order-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line|financials.companies.salesOrders.salesOrderLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-order-sale-order-line get-account

get-account a financials financial-company-sale-order-sale-order-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line|financials.companies.salesOrders.salesOrderLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-sale-order-line get-item

get-item a financials financial-company-sale-order-sale-order-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line|financials.companies.salesOrders.salesOrderLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-sale-order-line update-account

update-account a financials financial-company-sale-order-sale-order-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line|financials.companies.salesOrders.salesOrderLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-sale-order-sale-order-line update-item

update-item a financials financial-company-sale-order-sale-order-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line|financials.companies.salesOrders.salesOrderLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company-sale-order-sale-order-line-item create-picture

create-picture a financials financial-company-sale-order-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line-item|financials.companies.salesOrders.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-order-sale-order-line-item delete

delete a financials financial-company-sale-order-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line-item|financials.companies.salesOrders.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-order-sale-order-line-item get-item-category

get-item-category a financials financial-company-sale-order-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line-item|financials.companies.salesOrders.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-sale-order-line-item get-picture

get-picture a financials financial-company-sale-order-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line-item|financials.companies.salesOrders.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-sale-order-line-item get-picture-content

get-picture-content a financials financial-company-sale-order-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line-item|financials.companies.salesOrders.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-order-sale-order-line-item list-picture

list-picture a financials financial-company-sale-order-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line-item|financials.companies.salesOrders.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-order-sale-order-line-item set-picture-content

set-picture-content a financials financial-company-sale-order-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line-item|financials.companies.salesOrders.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-order-sale-order-line-item update-item-category

update-item-category a financials financial-company-sale-order-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line-item|financials.companies.salesOrders.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-order-sale-order-line-item update-picture

update-picture a financials financial-company-sale-order-sale-order-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-order-sale-order-line-item|financials.companies.salesOrders.salesOrderLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-order-id**|string|key: id of salesOrder|sales_order_id|salesOrder-id|
|**--sales-order-line-id**|string|key: id of salesOrderLine|sales_order_line_id|salesOrderLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-quote create-sale-quote-line

create-sale-quote-line a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sale-quote-line|CreateSalesQuoteLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company-sale-quote delete

delete a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSalesQuoteLines|
|delete|DeleteCurrency|
|delete|DeleteCustomer|
|delete|DeletePaymentTerm|
|delete|DeleteShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-quote get-currency

get-currency a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote get-customer

get-customer a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer|GetCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote get-payment-term

get-payment-term a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote get-sale-quote-line

get-sale-quote-line a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sale-quote-line|GetSalesQuoteLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote get-shipment-method

get-shipment-method a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shipment-method|GetShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote list-sale-quote-line

list-sale-quote-line a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sale-quote-line|ListSalesQuoteLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote make-invoice

make-invoice a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|make-invoice|makeInvoice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|

### financials financial-company-sale-quote send

send a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send|send|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|

### financials financial-company-sale-quote update-currency

update-currency a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-sale-quote update-customer

update-customer a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-customer|UpdateCustomer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|postalAddressType|address|address|
|**--blocked**|string||blocked|blocked|
|**--currency-code**|string||currency_code|currencyCode|
|**--currency-id**|uuid||currency_id|currencyId|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--payment-method-id**|uuid||payment_method_id|paymentMethodId|
|**--payment-terms-id**|uuid||payment_terms_id|paymentTermsId|
|**--phone-number**|string||phone_number|phoneNumber|
|**--shipment-method-id**|uuid||shipment_method_id|shipmentMethodId|
|**--tax-area-display-name**|string||tax_area_display_name|taxAreaDisplayName|
|**--tax-area-id**|uuid||tax_area_id|taxAreaId|
|**--tax-liable**|boolean||tax_liable|taxLiable|
|**--tax-registration-number**|string||tax_registration_number|taxRegistrationNumber|
|**--type**|string||type|type|
|**--website**|string||website|website|
|**--currency**|object|currency|currency|currency|
|**--payment-method**|object|paymentMethod|payment_method|paymentMethod|
|**--payment-term**|object|paymentTerm|payment_term|paymentTerm|
|**--picture**|array||picture|picture|
|**--shipment-method**|object|shipmentMethod|shipment_method|shipmentMethod|

### financials financial-company-sale-quote update-payment-term

update-payment-term a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-quote update-sale-quote-line

update-sale-quote-line a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sale-quote-line|UpdateSalesQuoteLines|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--id**|string|Read-only.|id|id|
|**--account-id**|uuid||account_id|accountId|
|**--amount-excluding-tax**|number||amount_excluding_tax|amountExcludingTax|
|**--amount-including-tax**|number||amount_including_tax|amountIncludingTax|
|**--description**|string||description|description|
|**--discount-amount**|number||discount_amount|discountAmount|
|**--discount-applied-before-tax**|boolean||discount_applied_before_tax|discountAppliedBeforeTax|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--document-id**|uuid||document_id|documentId|
|**--item-id**|uuid||item_id|itemId|
|**--line-type**|string||line_type|lineType|
|**--net-amount**|number||net_amount|netAmount|
|**--net-amount-including-tax**|number||net_amount_including_tax|netAmountIncludingTax|
|**--net-tax-amount**|number||net_tax_amount|netTaxAmount|
|**--quantity**|number||quantity|quantity|
|**--sequence**|integer||sequence|sequence|
|**--tax-code**|string||tax_code|taxCode|
|**--tax-percent**|number||tax_percent|taxPercent|
|**--total-tax-amount**|number||total_tax_amount|totalTaxAmount|
|**--unit-of-measure-id**|uuid||unit_of_measure_id|unitOfMeasureId|
|**--unit-price**|number||unit_price|unitPrice|
|**--account**|object|account|account|account|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--item-base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--item-blocked**|boolean||blocked|blocked|
|**--item-display-name**|string||display_name|displayName|
|**--item-gtin**|string||gtin|gtin|
|**--item-inventory**|number||inventory|inventory|
|**--item-item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-item-category-id**|uuid||item_category_id|itemCategoryId|
|**--item-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--item-number**|string||number|number|
|**--item-price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--item-tax-group-code**|string||tax_group_code|taxGroupCode|
|**--item-tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--item-type**|string||type|type|
|**--item-unit-cost**|number||unit_cost|unitCost|
|**--item-unit-price**|number||number_unit_price|unitPrice|
|**--item-item-category**|object|itemCategory|item_category|itemCategory|
|**--item-picture**|array||picture|picture|

### financials financial-company-sale-quote update-shipment-method

update-shipment-method a financials financial-company-sale-quote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote|financials.companies.salesQuotes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shipment-method|UpdateShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-quote-customer create-picture

create-picture a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-quote-customer delete

delete a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteCurrency|
|delete|DeletePaymentMethod|
|delete|DeletePaymentTerm|
|delete|DeleteShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-quote-customer get-currency

get-currency a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-customer get-payment-method

get-payment-method a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-method|GetPaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-customer get-payment-term

get-payment-term a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-customer get-picture

get-picture a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-customer get-picture-content

get-picture-content a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-quote-customer get-shipment-method

get-shipment-method a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shipment-method|GetShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-customer list-picture

list-picture a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-customer set-picture-content

set-picture-content a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-quote-customer update-currency

update-currency a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-sale-quote-customer update-payment-method

update-payment-method a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-method|UpdatePaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-quote-customer update-payment-term

update-payment-term a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-quote-customer update-picture

update-picture a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-quote-customer update-shipment-method

update-shipment-method a financials financial-company-sale-quote-customer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-customer|financials.companies.salesQuotes.customer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shipment-method|UpdateShipmentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-quote-line delete

delete a financials financial-company-sale-quote-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line|financials.companies.salesQuoteLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-quote-line get-account

get-account a financials financial-company-sale-quote-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line|financials.companies.salesQuoteLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-line get-item

get-item a financials financial-company-sale-quote-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line|financials.companies.salesQuoteLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-line update-account

update-account a financials financial-company-sale-quote-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line|financials.companies.salesQuoteLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-sale-quote-line update-item

update-item a financials financial-company-sale-quote-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line|financials.companies.salesQuoteLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company-sale-quote-line-item create-picture

create-picture a financials financial-company-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line-item|financials.companies.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-quote-line-item delete

delete a financials financial-company-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line-item|financials.companies.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-quote-line-item get-item-category

get-item-category a financials financial-company-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line-item|financials.companies.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-line-item get-picture

get-picture a financials financial-company-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line-item|financials.companies.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-line-item get-picture-content

get-picture-content a financials financial-company-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line-item|financials.companies.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-quote-line-item list-picture

list-picture a financials financial-company-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line-item|financials.companies.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-line-item set-picture-content

set-picture-content a financials financial-company-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line-item|financials.companies.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-quote-line-item update-item-category

update-item-category a financials financial-company-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line-item|financials.companies.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-quote-line-item update-picture

update-picture a financials financial-company-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-line-item|financials.companies.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-quote-sale-quote-line delete

delete a financials financial-company-sale-quote-sale-quote-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line|financials.companies.salesQuotes.salesQuoteLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-quote-sale-quote-line get-account

get-account a financials financial-company-sale-quote-sale-quote-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line|financials.companies.salesQuotes.salesQuoteLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-sale-quote-line get-item

get-item a financials financial-company-sale-quote-sale-quote-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line|financials.companies.salesQuotes.salesQuoteLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-sale-quote-line update-account

update-account a financials financial-company-sale-quote-sale-quote-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line|financials.companies.salesQuotes.salesQuoteLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--id**|string|Read-only.|id|id|
|**--blocked**|boolean||blocked|blocked|
|**--category**|string||category|category|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--sub-category**|string||sub_category|subCategory|

### financials financial-company-sale-quote-sale-quote-line update-item

update-item a financials financial-company-sale-quote-sale-quote-line.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line|financials.companies.salesQuotes.salesQuoteLines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--id**|string|Read-only.|id|id|
|**--base-unit-of-measure-id**|uuid||base_unit_of_measure_id|baseUnitOfMeasureId|
|**--blocked**|boolean||blocked|blocked|
|**--display-name**|string||display_name|displayName|
|**--gtin**|string||gtin|gtin|
|**--inventory**|number||inventory|inventory|
|**--item-category-code**|string||item_category_code|itemCategoryCode|
|**--item-category-id**|uuid||item_category_id|itemCategoryId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--number**|string||number|number|
|**--price-includes-tax**|boolean||price_includes_tax|priceIncludesTax|
|**--tax-group-code**|string||tax_group_code|taxGroupCode|
|**--tax-group-id**|uuid||tax_group_id|taxGroupId|
|**--type**|string||type|type|
|**--unit-cost**|number||unit_cost|unitCost|
|**--unit-price**|number||unit_price|unitPrice|
|**--item-category**|object|itemCategory|item_category|itemCategory|
|**--picture**|array||picture|picture|

### financials financial-company-sale-quote-sale-quote-line-item create-picture

create-picture a financials financial-company-sale-quote-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line-item|financials.companies.salesQuotes.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-sale-quote-sale-quote-line-item delete

delete a financials financial-company-sale-quote-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line-item|financials.companies.salesQuotes.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-sale-quote-sale-quote-line-item get-item-category

get-item-category a financials financial-company-sale-quote-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line-item|financials.companies.salesQuotes.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-category|GetItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-sale-quote-line-item get-picture

get-picture a financials financial-company-sale-quote-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line-item|financials.companies.salesQuotes.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-sale-quote-line-item get-picture-content

get-picture-content a financials financial-company-sale-quote-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line-item|financials.companies.salesQuotes.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-sale-quote-sale-quote-line-item list-picture

list-picture a financials financial-company-sale-quote-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line-item|financials.companies.salesQuotes.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-sale-quote-sale-quote-line-item set-picture-content

set-picture-content a financials financial-company-sale-quote-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line-item|financials.companies.salesQuotes.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-sale-quote-sale-quote-line-item update-item-category

update-item-category a financials financial-company-sale-quote-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line-item|financials.companies.salesQuotes.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-category|UpdateItemCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-sale-quote-sale-quote-line-item update-picture

update-picture a financials financial-company-sale-quote-sale-quote-line-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-sale-quote-sale-quote-line-item|financials.companies.salesQuotes.salesQuoteLines.item|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--sales-quote-id**|string|key: id of salesQuote|sales_quote_id|salesQuote-id|
|**--sales-quote-line-id**|string|key: id of salesQuoteLine|sales_quote_line_id|salesQuoteLine-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-vendor create-picture

create-picture a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-picture|CreatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-company-vendor delete

delete a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePicture|
|delete|DeleteCurrency|
|delete|DeletePaymentMethod|
|delete|DeletePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--if-match**|string|ETag|if_match|If-Match|

### financials financial-company-vendor get-currency

get-currency a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-currency|GetCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-vendor get-payment-method

get-payment-method a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-method|GetPaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-vendor get-payment-term

get-payment-term a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-payment-term|GetPaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-vendor get-picture

get-picture a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture|GetPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-vendor get-picture-content

get-picture-content a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-picture-content|GetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|

### financials financial-company-vendor list-picture

list-picture a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-picture|ListPicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-company-vendor set-picture-content

set-picture-content a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-picture-content|SetPictureContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--data**|binary|New media content.|data|data|

### financials financial-company-vendor update-currency

update-currency a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-currency|UpdateCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--id**|string|Read-only.|id|id|
|**--amount-decimal-places**|string||amount_decimal_places|amountDecimalPlaces|
|**--amount-rounding-precision**|number||amount_rounding_precision|amountRoundingPrecision|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--symbol**|string||symbol|symbol|

### financials financial-company-vendor update-payment-method

update-payment-method a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-method|UpdatePaymentMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--id**|string|Read-only.|id|id|
|**--code**|string||code|code|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-vendor update-payment-term

update-payment-term a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-payment-term|UpdatePaymentTerm|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--id**|string|Read-only.|id|id|
|**--calculate-discount-on-credit-memos**|boolean||calculate_discount_on_credit_memos|calculateDiscountOnCreditMemos|
|**--code**|string||code|code|
|**--discount-date-calculation**|string||discount_date_calculation|discountDateCalculation|
|**--discount-percent**|number||discount_percent|discountPercent|
|**--display-name**|string||display_name|displayName|
|**--due-date-calculation**|string||due_date_calculation|dueDateCalculation|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### financials financial-company-vendor update-picture

update-picture a financials financial-company-vendor.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-company-vendor|financials.companies.vendors|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-picture|UpdatePicture|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--company-id**|string|key: id of company|company_id|company-id|
|**--vendor-id**|string|key: id of vendor|vendor_id|vendor-id|
|**--picture-id**|string|key: id of picture|picture_id|picture-id|
|**--id**|string|Read-only.|id|id|
|**--content**|byte-array||content|content|
|**--content-type**|string||content_type|contentType|
|**--height**|integer||height|height|
|**--width**|integer||width|width|

### financials financial-financial get-financial

get-financial a financials financial-financial.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-financial|financials.financials|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-financial|GetFinancials|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### financials financial-financial update-financial

update-financial a financials financial-financial.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|financials financial-financial|financials.financials|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-financial|UpdateFinancials|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--companies**|array||companies|companies|
