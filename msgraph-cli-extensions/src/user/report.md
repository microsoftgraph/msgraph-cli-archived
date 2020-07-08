# Azure CLI Module Creation Report

### user user get-presence

get-presence a user user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|user user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-presence|GetPresence|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### user user update

update a user user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|user user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePresence|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--availability**|string||availability|availability|
|**--activity**|string||activity|activity|

### user user-user create-user

create-user a user user-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|user user-user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user|CreateUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### user user-user delete

delete a user user-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|user user-user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

### user user-user get-user

get-user a user user-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|user user-user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user|GetUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### user user-user list-user

list-user a user user-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|user user-user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user|ListUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### user user-user update

update a user user-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|user user-user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--body**|object|New property values|body|body|
