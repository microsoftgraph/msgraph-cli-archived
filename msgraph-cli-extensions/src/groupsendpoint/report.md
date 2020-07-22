# Azure CLI Module Creation Report

### groupsendpoint create-endpoint

create-endpoint a groupsendpoint.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsendpoint|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-endpoint|CreateEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--capability**|string||capability|capability|
|**--provider-id**|string||provider_id|providerId|
|**--provider-name**|string||provider_name|providerName|
|**--uri**|string||uri|uri|
|**--provider-resource-id**|string||provider_resource_id|providerResourceId|

### groupsendpoint get-endpoint

get-endpoint a groupsendpoint.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsendpoint|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-endpoint|GetEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--endpoint-id**|string|key: endpoint-id of endpoint|endpoint_id|endpoint-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsendpoint list-endpoint

list-endpoint a groupsendpoint.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsendpoint|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-endpoint|ListEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsendpoint update

update a groupsendpoint.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsendpoint|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--endpoint-id**|string|key: endpoint-id of endpoint|endpoint_id|endpoint-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--capability**|string||capability|capability|
|**--provider-id**|string||provider_id|providerId|
|**--provider-name**|string||provider_name|providerName|
|**--uri**|string||uri|uri|
|**--provider-resource-id**|string||provider_resource_id|providerResourceId|
