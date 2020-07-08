# Azure CLI Module Creation Report

### extension group create-extension

create-extension a extension group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|extension group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|

### extension group get-extension

get-extension a extension group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|extension group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--extension-id**|string|key: extension-id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### extension group list-extension

list-extension a extension group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|extension group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### extension group update

update a extension group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|extension group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--extension-id**|string|key: extension-id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|
