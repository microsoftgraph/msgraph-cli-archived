# Azure CLI Module Creation Report

### directoryobjects check-member-group

check-member-group a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--group-ids**|array||group_ids|groupIds|

### directoryobjects check-member-object

check-member-object a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--ids**|array||ids|ids|

### directoryobjects create-directory-object

create-directory-object a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects.directoryObject|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-object|CreateDirectoryObject|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

### directoryobjects delete

delete a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects.directoryObject|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDirectoryObject|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--if-match**|string|ETag|if_match|If-Match|

### directoryobjects get-available-extension-property

get-available-extension-property a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### directoryobjects get-by-id

get-by-id a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### directoryobjects get-directory-object

get-directory-object a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects.directoryObject|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-object|GetDirectoryObject|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### directoryobjects get-member-group

get-member-group a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### directoryobjects get-member-object

get-member-object a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### directoryobjects list-directory-object

list-directory-object a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects.directoryObject|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-directory-object|ListDirectoryObject|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### directoryobjects restore

restore a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|

### directoryobjects update-directory-object

update-directory-object a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects.directoryObject|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory-object|UpdateDirectoryObject|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

### directoryobjects validate-property

validate-property a directoryobjects.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryobjects|directoryObjects|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|validate-property|validateProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|
