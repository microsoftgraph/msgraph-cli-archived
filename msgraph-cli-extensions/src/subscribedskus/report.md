# Azure CLI Module Creation Report

### subscribedskus subscribed-sku-subscribed-sku create-subscribed-sku

create-subscribed-sku a subscribedskus subscribed-sku-subscribed-sku.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|subscribedskus subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-subscribed-sku|CreateSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--capability-status**|string|Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.|capability_status|capabilityStatus|
|**--consumed-units**|integer|The number of licenses that have been assigned.|consumed_units|consumedUnits|
|**--prepaid-units**|object|licenseUnitsDetail|prepaid_units|prepaidUnits|
|**--service-plans**|array|Information about the service plans that are available with the SKU. Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|The unique identifier (GUID) for the service SKU.|sku_id|skuId|
|**--sku-part-number**|string|The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.|sku_part_number|skuPartNumber|
|**--applies-to**|string|For example, 'User' or 'Company'.|applies_to|appliesTo|

### subscribedskus subscribed-sku-subscribed-sku delete

delete a subscribedskus subscribed-sku-subscribed-sku.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|subscribedskus subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: subscribedSku-id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--if-match**|string|ETag|if_match|If-Match|

### subscribedskus subscribed-sku-subscribed-sku get-subscribed-sku

get-subscribed-sku a subscribedskus subscribed-sku-subscribed-sku.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|subscribedskus subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-subscribed-sku|GetSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: subscribedSku-id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### subscribedskus subscribed-sku-subscribed-sku list-subscribed-sku

list-subscribed-sku a subscribedskus subscribed-sku-subscribed-sku.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|subscribedskus subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-subscribed-sku|ListSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### subscribedskus subscribed-sku-subscribed-sku update

update a subscribedskus subscribed-sku-subscribed-sku.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|subscribedskus subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: subscribedSku-id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--id**|string|Read-only.|id|id|
|**--capability-status**|string|Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.|capability_status|capabilityStatus|
|**--consumed-units**|integer|The number of licenses that have been assigned.|consumed_units|consumedUnits|
|**--prepaid-units**|object|licenseUnitsDetail|prepaid_units|prepaidUnits|
|**--service-plans**|array|Information about the service plans that are available with the SKU. Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|The unique identifier (GUID) for the service SKU.|sku_id|skuId|
|**--sku-part-number**|string|The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.|sku_part_number|skuPartNumber|
|**--applies-to**|string|For example, 'User' or 'Company'.|applies_to|appliesTo|
