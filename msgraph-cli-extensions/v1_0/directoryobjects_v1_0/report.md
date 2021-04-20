# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az directoryobjects_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az directoryobjects_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az directoryobjects directoryobjectsdirectoryobject|directoryObjects.directoryObject|[commands](#CommandsIndirectoryObjects.directoryObject)|
|az directoryobjects directoryobject|directoryObjects|[commands](#CommandsIndirectoryObjects)|

## COMMANDS
### <a name="CommandsIndirectoryObjects">Commands in `az directoryobjects directoryobject` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az directoryobjects directoryobject check-member-group](#directoryObjectscheckMemberGroups)|checkMemberGroups|[Parameters](#ParametersdirectoryObjectscheckMemberGroups)|Not Found|
|[az directoryobjects directoryobject check-member-object](#directoryObjectscheckMemberObjects)|checkMemberObjects|[Parameters](#ParametersdirectoryObjectscheckMemberObjects)|Not Found|
|[az directoryobjects directoryobject get-available-extension-property](#directoryObjectsgetAvailableExtensionProperties)|getAvailableExtensionProperties|[Parameters](#ParametersdirectoryObjectsgetAvailableExtensionProperties)|Not Found|
|[az directoryobjects directoryobject get-by-id](#directoryObjectsgetByIds)|getByIds|[Parameters](#ParametersdirectoryObjectsgetByIds)|Not Found|
|[az directoryobjects directoryobject get-member-group](#directoryObjectsgetMemberGroups)|getMemberGroups|[Parameters](#ParametersdirectoryObjectsgetMemberGroups)|Not Found|
|[az directoryobjects directoryobject get-member-object](#directoryObjectsgetMemberObjects)|getMemberObjects|[Parameters](#ParametersdirectoryObjectsgetMemberObjects)|Not Found|
|[az directoryobjects directoryobject restore](#directoryObjectsrestore)|restore|[Parameters](#ParametersdirectoryObjectsrestore)|Not Found|
|[az directoryobjects directoryobject validate-property](#directoryObjectsvalidateProperties)|validateProperties|[Parameters](#ParametersdirectoryObjectsvalidateProperties)|Not Found|

### <a name="CommandsIndirectoryObjects.directoryObject">Commands in `az directoryobjects directoryobjectsdirectoryobject` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az directoryobjects directoryobjectsdirectoryobject create-directory-object](#directoryObjects.directoryObjectCreateDirectoryObject)|CreateDirectoryObject|[Parameters](#ParametersdirectoryObjects.directoryObjectCreateDirectoryObject)|Not Found|
|[az directoryobjects directoryobjectsdirectoryobject delete-directory-object](#directoryObjects.directoryObjectDeleteDirectoryObject)|DeleteDirectoryObject|[Parameters](#ParametersdirectoryObjects.directoryObjectDeleteDirectoryObject)|Not Found|
|[az directoryobjects directoryobjectsdirectoryobject list-directory-object](#directoryObjects.directoryObjectListDirectoryObject)|ListDirectoryObject|[Parameters](#ParametersdirectoryObjects.directoryObjectListDirectoryObject)|Not Found|
|[az directoryobjects directoryobjectsdirectoryobject show-directory-object](#directoryObjects.directoryObjectGetDirectoryObject)|GetDirectoryObject|[Parameters](#ParametersdirectoryObjects.directoryObjectGetDirectoryObject)|Not Found|
|[az directoryobjects directoryobjectsdirectoryobject update-directory-object](#directoryObjects.directoryObjectUpdateDirectoryObject)|UpdateDirectoryObject|[Parameters](#ParametersdirectoryObjects.directoryObjectUpdateDirectoryObject)|Not Found|


## COMMAND DETAILS

### group `az directoryobjects directoryobject`
#### <a name="directoryObjectscheckMemberGroups">Command `az directoryobjects directoryobject check-member-group`</a>

##### <a name="ParametersdirectoryObjectscheckMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--group-ids**|array||group_ids|groupIds|

#### <a name="directoryObjectscheckMemberObjects">Command `az directoryobjects directoryobject check-member-object`</a>

##### <a name="ParametersdirectoryObjectscheckMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--ids**|array||ids|ids|

#### <a name="directoryObjectsgetAvailableExtensionProperties">Command `az directoryobjects directoryobject get-available-extension-property`</a>

##### <a name="ParametersdirectoryObjectsgetAvailableExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

#### <a name="directoryObjectsgetByIds">Command `az directoryobjects directoryobject get-by-id`</a>

##### <a name="ParametersdirectoryObjectsgetByIds">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

#### <a name="directoryObjectsgetMemberGroups">Command `az directoryobjects directoryobject get-member-group`</a>

##### <a name="ParametersdirectoryObjectsgetMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="directoryObjectsgetMemberObjects">Command `az directoryobjects directoryobject get-member-object`</a>

##### <a name="ParametersdirectoryObjectsgetMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="directoryObjectsrestore">Command `az directoryobjects directoryobject restore`</a>

##### <a name="ParametersdirectoryObjectsrestore">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|

#### <a name="directoryObjectsvalidateProperties">Command `az directoryobjects directoryobject validate-property`</a>

##### <a name="ParametersdirectoryObjectsvalidateProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### group `az directoryobjects directoryobjectsdirectoryobject`
#### <a name="directoryObjects.directoryObjectCreateDirectoryObject">Command `az directoryobjects directoryobjectsdirectoryobject create-directory-object`</a>

##### <a name="ParametersdirectoryObjects.directoryObjectCreateDirectoryObject">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

#### <a name="directoryObjects.directoryObjectDeleteDirectoryObject">Command `az directoryobjects directoryobjectsdirectoryobject delete-directory-object`</a>

##### <a name="ParametersdirectoryObjects.directoryObjectDeleteDirectoryObject">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="directoryObjects.directoryObjectListDirectoryObject">Command `az directoryobjects directoryobjectsdirectoryobject list-directory-object`</a>

##### <a name="ParametersdirectoryObjects.directoryObjectListDirectoryObject">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryObjects.directoryObjectGetDirectoryObject">Command `az directoryobjects directoryobjectsdirectoryobject show-directory-object`</a>

##### <a name="ParametersdirectoryObjects.directoryObjectGetDirectoryObject">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryObjects.directoryObjectUpdateDirectoryObject">Command `az directoryobjects directoryobjectsdirectoryobject update-directory-object`</a>

##### <a name="ParametersdirectoryObjects.directoryObjectUpdateDirectoryObject">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
