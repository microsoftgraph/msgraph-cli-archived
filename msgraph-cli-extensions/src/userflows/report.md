# Azure CLI Module Creation Report

### userflows identity create-user-flow

create-user-flow a userflows identity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userflows identity|identity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user-flow|CreateUserFlows|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-flow-type**|choice|userFlowType|user_flow_type|userFlowType|
|**--user-flow-type-version**|number||user_flow_type_version|userFlowTypeVersion|

### userflows identity get-user-flow

get-user-flow a userflows identity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userflows identity|identity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-flow|GetUserFlows|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-user-flow-id**|string|key: identityUserFlow-id of identityUserFlow|identity_user_flow_id|identityUserFlow-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userflows identity list-user-flow

list-user-flow a userflows identity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userflows identity|identity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user-flow|ListUserFlows|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userflows identity update

update a userflows identity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userflows identity|identity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateUserFlows|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-user-flow-id**|string|key: identityUserFlow-id of identityUserFlow|identity_user_flow_id|identityUserFlow-id|
|**--id**|string|Read-only.|id|id|
|**--user-flow-type**|choice|userFlowType|user_flow_type|userFlowType|
|**--user-flow-type-version**|number||user_flow_type_version|userFlowTypeVersion|
