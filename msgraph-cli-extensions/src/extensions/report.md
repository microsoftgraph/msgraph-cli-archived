# Azure CLI Module Creation Report

### extensions user create-extension

create-extension a extensions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|extensions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

### extensions user get-extension

get-extension a extensions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|extensions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--extension-id**|string|key: extension-id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### extensions user list-extension

list-extension a extensions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|extensions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### extensions user update

update a extensions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|extensions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--extension-id**|string|key: extension-id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|
