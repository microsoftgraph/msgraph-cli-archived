# Azure CLI Module Creation Report

### directoryroles directory-role check-member-group

check-member-group a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--group-ids**|array||group_ids|groupIds|

### directoryroles directory-role check-member-object

check-member-object a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--ids**|array||ids|ids|

### directoryroles directory-role create-scoped-member

create-scoped-member a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-scoped-member|CreateScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--id**|string|Read-only.|id|id|
|**--role-id**|string||role_id|roleId|
|**--administrative-unit-id**|string||administrative_unit_id|administrativeUnitId|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|

### directoryroles directory-role delta

delta a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### directoryroles directory-role get-by-id

get-by-id a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### directoryroles directory-role get-member

get-member a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member|GetMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--directory-object-id**|string|key: directoryObject-id of directoryObject|directory_object_id|directoryObject-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### directoryroles directory-role get-member-group

get-member-group a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### directoryroles directory-role get-member-object

get-member-object a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### directoryroles directory-role get-scoped-member

get-scoped-member a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-scoped-member|GetScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--scoped-role-membership-id**|string|key: scopedRoleMembership-id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### directoryroles directory-role get-user-owned-object

get-user-owned-object a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-owned-object|getUserOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string||user_id|userId|
|**--type**|string||type|type|

### directoryroles directory-role list-member

list-member a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member|ListMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### directoryroles directory-role list-scoped-member

list-scoped-member a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-scoped-member|ListScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### directoryroles directory-role restore

restore a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|

### directoryroles directory-role update

update a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--scoped-role-membership-id**|string|key: scopedRoleMembership-id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--id**|string|Read-only.|id|id|
|**--role-id**|string||role_id|roleId|
|**--administrative-unit-id**|string||administrative_unit_id|administrativeUnitId|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|

### directoryroles directory-role validate-property

validate-property a directoryroles directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role|directoryRoles|

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

### directoryroles directory-role-directory-role create-directory-role

create-directory-role a directoryroles directory-role-directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role-directory-role|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-role|CreateDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name for the directory role. Read-only.|display_name|displayName|
|**--role-template-id**|string|The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only.|role_template_id|roleTemplateId|
|**--members**|array|Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable.|members|members|
|**--scoped-members**|array||scoped_members|scopedMembers|

### directoryroles directory-role-directory-role delete

delete a directoryroles directory-role-directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role-directory-role|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--if-match**|string|ETag|if_match|If-Match|

### directoryroles directory-role-directory-role get-directory-role

get-directory-role a directoryroles directory-role-directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role-directory-role|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-role|GetDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### directoryroles directory-role-directory-role list-directory-role

list-directory-role a directoryroles directory-role-directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role-directory-role|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-directory-role|ListDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### directoryroles directory-role-directory-role update

update a directoryroles directory-role-directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|directoryroles directory-role-directory-role|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: directoryRole-id of directoryRole|directory_role_id|directoryRole-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name for the directory role. Read-only.|display_name|displayName|
|**--role-template-id**|string|The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only.|role_template_id|roleTemplateId|
|**--members**|array|Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable.|members|members|
|**--scoped-members**|array||scoped_members|scopedMembers|
