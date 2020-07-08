# Azure CLI Module Creation Report

### permissions group create-permission-grant

create-permission-grant a permissions group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|permissions group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-permission-grant|CreatePermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--client-id**|string||client_id|clientId|
|**--client-app-id**|string||client_app_id|clientAppId|
|**--resource-app-id**|string||resource_app_id|resourceAppId|
|**--permission-type**|string||permission_type|permissionType|
|**--permission**|string||permission|permission|

### permissions group get-permission-grant

get-permission-grant a permissions group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|permissions group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission-grant|GetPermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--resource-specific-permission-grant-id**|string|key: resourceSpecificPermissionGrant-id of resourceSpecificPermissionGrant|resource_specific_permission_grant_id|resourceSpecificPermissionGrant-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### permissions group list-permission-grant

list-permission-grant a permissions group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|permissions group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-permission-grant|ListPermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### permissions group update

update a permissions group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|permissions group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--resource-specific-permission-grant-id**|string|key: resourceSpecificPermissionGrant-id of resourceSpecificPermissionGrant|resource_specific_permission_grant_id|resourceSpecificPermissionGrant-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--client-id**|string||client_id|clientId|
|**--client-app-id**|string||client_app_id|clientAppId|
|**--resource-app-id**|string||resource_app_id|resourceAppId|
|**--permission-type**|string||permission_type|permissionType|
|**--permission**|string||permission|permission|
