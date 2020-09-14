# Azure CLI Module Creation Report

### usersuser create-user

create-user a usersuser.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersuser|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user|CreateUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### usersuser delete

delete a usersuser.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersuser|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

### usersuser get-presence

get-presence a usersuser.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersuser|users|

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

### usersuser get-user

get-user a usersuser.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersuser|users.user|

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

### usersuser list-user

list-user a usersuser.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersuser|users.user|

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

### usersuser update-presence

update-presence a usersuser.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersuser|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-presence|UpdatePresence|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--availability**|string||availability|availability|
|**--activity**|string||activity|activity|

### usersuser update-user

update-user a usersuser.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersuser|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user|UpdateUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--body**|object|New property values|body|body|
