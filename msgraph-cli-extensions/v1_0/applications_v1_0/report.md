# Azure CLI Module Creation Report

### applications application add-key

add-key a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|add-key|addKey|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--key-credential**|object|keyCredential|key_credential|keyCredential|
|**--password-credential**|object|passwordCredential|password_credential|passwordCredential|
|**--proof**|string||proof|proof|

### applications application add-password

add-password a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|add-password|addPassword|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--password-credential**|object|passwordCredential|password_credential|passwordCredential|

### applications application check-member-group

check-member-group a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--group-ids**|array||group_ids|groupIds|

### applications application check-member-object

check-member-object a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--ids**|array||ids|ids|

### applications application create-extension-property

create-extension-property a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension-property|CreateExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--app-display-name**|string|Display name of the application object on which this extension property is defined. Read-only.|app_display_name|appDisplayName|
|**--data-type**|string|Specifies the data type of the value the extension property can hold. Following values are supported. Not nullable. Binary - 256 bytes maximumBooleanDateTime - Must be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger - 64-bit value.String - 256 characters maximum|data_type|dataType|
|**--is-synced-from-on-premises**|boolean|Indicates if this extension property was sycned from onpremises directory using Azure AD Connect. Read-only.|is_synced_from_on_premises|isSyncedFromOnPremises|
|**--name**|string|Name of the extension property. Not nullable.|name|name|
|**--target-objects**|array|Following values are supported. Not nullable. UserGroupOrganizationDeviceApplication|target_objects|targetObjects|

### applications application create-ref-home-realm-discovery-policy

create-ref-home-realm-discovery-policy a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-home-realm-discovery-policy|CreateRefHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications application create-ref-owner

create-ref-owner a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owner|CreateRefOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications application create-ref-token-issuance-policy

create-ref-token-issuance-policy a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-token-issuance-policy|CreateRefTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications application create-ref-token-lifetime-policy

create-ref-token-lifetime-policy a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-token-lifetime-policy|CreateRefTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications application delete

delete a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensionProperties|
|delete|DeleteRefCreatedOnBehalfOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--extension-property-id**|string|key: id of extensionProperty|extension_property_id|extensionProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### applications application delta

delta a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### applications application get-available-extension-property

get-available-extension-property a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### applications application get-by-id

get-by-id a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### applications application get-created-on-behalf-of

get-created-on-behalf-of a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-created-on-behalf-of|GetCreatedOnBehalfOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications application get-extension-property

get-extension-property a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension-property|GetExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--extension-property-id**|string|key: id of extensionProperty|extension_property_id|extensionProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications application get-member-group

get-member-group a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### applications application get-member-object

get-member-object a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### applications application get-ref-created-on-behalf-of

get-ref-created-on-behalf-of a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-created-on-behalf-of|GetRefCreatedOnBehalfOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|

### applications application list-extension-property

list-extension-property a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension-property|ListExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications application list-home-realm-discovery-policy

list-home-realm-discovery-policy a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-home-realm-discovery-policy|ListHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications application list-owner

list-owner a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-owner|ListOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications application list-ref-home-realm-discovery-policy

list-ref-home-realm-discovery-policy a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-home-realm-discovery-policy|ListRefHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications application list-ref-owner

list-ref-owner a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owner|ListRefOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications application list-ref-token-issuance-policy

list-ref-token-issuance-policy a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-token-issuance-policy|ListRefTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications application list-ref-token-lifetime-policy

list-ref-token-lifetime-policy a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-token-lifetime-policy|ListRefTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications application list-token-issuance-policy

list-token-issuance-policy a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-token-issuance-policy|ListTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications application list-token-lifetime-policy

list-token-lifetime-policy a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-token-lifetime-policy|ListTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications application remove-key

remove-key a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remove-key|removeKey|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--key-id**|uuid||key_id|keyId|
|**--proof**|string||proof|proof|

### applications application remove-password

remove-password a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remove-password|removePassword|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--key-id**|uuid||key_id|keyId|

### applications application restore

restore a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|

### applications application set-ref-created-on-behalf-of

set-ref-created-on-behalf-of a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-created-on-behalf-of|SetRefCreatedOnBehalfOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### applications application update-extension-property

update-extension-property a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension-property|UpdateExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--extension-property-id**|string|key: id of extensionProperty|extension_property_id|extensionProperty-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--app-display-name**|string|Display name of the application object on which this extension property is defined. Read-only.|app_display_name|appDisplayName|
|**--data-type**|string|Specifies the data type of the value the extension property can hold. Following values are supported. Not nullable. Binary - 256 bytes maximumBooleanDateTime - Must be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger - 64-bit value.String - 256 characters maximum|data_type|dataType|
|**--is-synced-from-on-premises**|boolean|Indicates if this extension property was sycned from onpremises directory using Azure AD Connect. Read-only.|is_synced_from_on_premises|isSyncedFromOnPremises|
|**--name**|string|Name of the extension property. Not nullable.|name|name|
|**--target-objects**|array|Following values are supported. Not nullable. UserGroupOrganizationDeviceApplication|target_objects|targetObjects|

### applications application validate-property

validate-property a applications application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application|applications|

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

### applications application-application create-application

create-application a applications application-application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application-application|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-application|CreateApplication|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### applications application-application delete

delete a applications application-application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application-application|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteApplication|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--if-match**|string|ETag|if_match|If-Match|

### applications application-application get-application

get-application a applications application-application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application-application|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-application|GetApplication|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications application-application get-logo

get-logo a applications application-application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application-application|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-logo|GetLogo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|

### applications application-application list-application

list-application a applications application-application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application-application|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-application|ListApplication|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications application-application set-logo

set-logo a applications application-application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application-application|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-logo|SetLogo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--data**|binary|New media content.|data|data|

### applications application-application update-application

update-application a applications application-application.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications application-application|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-application|UpdateApplication|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|object|New property values|body|body|

### applications group create-app-role-assignment

create-app-role-assignment a applications group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-app-role-assignment|CreateAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--app-role-id**|uuid|The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. Does not support $filter.|app_role_id|appRoleId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--principal-display-name**|string|The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).|principal_display_name|principalDisplayName|
|**--principal-id**|uuid|The unique identifier (id) for the user, group or service principal being granted the app role. Required on create. Does not support $filter.|principal_id|principalId|
|**--principal-type**|string|The type of the assigned principal. This can either be 'User', 'Group' or 'ServicePrincipal'. Read-only. Does not support $filter.|principal_type|principalType|
|**--resource-display-name**|string|The display name of the resource app's service principal to which the assignment is made. Does not support $filter.|resource_display_name|resourceDisplayName|
|**--resource-id**|uuid|The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).|resource_id|resourceId|

### applications group delete

delete a applications group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

### applications group get-app-role-assignment

get-app-role-assignment a applications group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-app-role-assignment|GetAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications group list-app-role-assignment

list-app-role-assignment a applications group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-app-role-assignment|ListAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications group update-app-role-assignment

update-app-role-assignment a applications group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-app-role-assignment|UpdateAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--app-role-id**|uuid|The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. Does not support $filter.|app_role_id|appRoleId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--principal-display-name**|string|The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).|principal_display_name|principalDisplayName|
|**--principal-id**|uuid|The unique identifier (id) for the user, group or service principal being granted the app role. Required on create. Does not support $filter.|principal_id|principalId|
|**--principal-type**|string|The type of the assigned principal. This can either be 'User', 'Group' or 'ServicePrincipal'. Read-only. Does not support $filter.|principal_type|principalType|
|**--resource-display-name**|string|The display name of the resource app's service principal to which the assignment is made. Does not support $filter.|resource_display_name|resourceDisplayName|
|**--resource-id**|uuid|The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).|resource_id|resourceId|

### applications service-principal add-key

add-key a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|add-key|addKey|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--key-credential**|object|keyCredential|key_credential|keyCredential|
|**--password-credential**|object|passwordCredential|password_credential|passwordCredential|
|**--proof**|string||proof|proof|

### applications service-principal add-password

add-password a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|add-password|addPassword|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--password-credential**|object|passwordCredential|password_credential|passwordCredential|

### applications service-principal check-member-group

check-member-group a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--group-ids**|array||group_ids|groupIds|

### applications service-principal check-member-object

check-member-object a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--ids**|array||ids|ids|

### applications service-principal create-app-role-assigned-to

create-app-role-assigned-to a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-app-role-assigned-to|CreateAppRoleAssignedTo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--app-role-id**|uuid|The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. Does not support $filter.|app_role_id|appRoleId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--principal-display-name**|string|The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).|principal_display_name|principalDisplayName|
|**--principal-id**|uuid|The unique identifier (id) for the user, group or service principal being granted the app role. Required on create. Does not support $filter.|principal_id|principalId|
|**--principal-type**|string|The type of the assigned principal. This can either be 'User', 'Group' or 'ServicePrincipal'. Read-only. Does not support $filter.|principal_type|principalType|
|**--resource-display-name**|string|The display name of the resource app's service principal to which the assignment is made. Does not support $filter.|resource_display_name|resourceDisplayName|
|**--resource-id**|uuid|The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).|resource_id|resourceId|

### applications service-principal create-app-role-assignment

create-app-role-assignment a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-app-role-assignment|CreateAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--app-role-id**|uuid|The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. Does not support $filter.|app_role_id|appRoleId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--principal-display-name**|string|The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).|principal_display_name|principalDisplayName|
|**--principal-id**|uuid|The unique identifier (id) for the user, group or service principal being granted the app role. Required on create. Does not support $filter.|principal_id|principalId|
|**--principal-type**|string|The type of the assigned principal. This can either be 'User', 'Group' or 'ServicePrincipal'. Read-only. Does not support $filter.|principal_type|principalType|
|**--resource-display-name**|string|The display name of the resource app's service principal to which the assignment is made. Does not support $filter.|resource_display_name|resourceDisplayName|
|**--resource-id**|uuid|The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).|resource_id|resourceId|

### applications service-principal create-endpoint

create-endpoint a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-endpoint|CreateEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--capability**|string|Describes the capability that is associated with this resource. (e.g. Messages, Conversations, etc.)  Not nullable. Read-only.|capability|capability|
|**--provider-id**|string|Application id of the publishing underlying service. Not nullable. Read-only.|provider_id|providerId|
|**--provider-name**|string|Name of the publishing underlying service. Read-only.|provider_name|providerName|
|**--provider-resource-id**|string|For Microsoft 365 groups, this is set to a well-known name for the resource (e.g. Yammer.FeedURL etc.). Not nullable. Read-only.|provider_resource_id|providerResourceId|
|**--uri**|string|URL of the published resource. Not nullable. Read-only.|uri|uri|

### applications service-principal create-ref-claim-mapping-policy

create-ref-claim-mapping-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-claim-mapping-policy|CreateRefClaimsMappingPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications service-principal create-ref-created-object

create-ref-created-object a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-created-object|CreateRefCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications service-principal create-ref-home-realm-discovery-policy

create-ref-home-realm-discovery-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-home-realm-discovery-policy|CreateRefHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications service-principal create-ref-member-of

create-ref-member-of a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member-of|CreateRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications service-principal create-ref-oauth2-permission-grant

create-ref-oauth2-permission-grant a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-oauth2-permission-grant|CreateRefOauth2PermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications service-principal create-ref-owned-object

create-ref-owned-object a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owned-object|CreateRefOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications service-principal create-ref-owner

create-ref-owner a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owner|CreateRefOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications service-principal create-ref-token-issuance-policy

create-ref-token-issuance-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-token-issuance-policy|CreateRefTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications service-principal create-ref-token-lifetime-policy

create-ref-token-lifetime-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-token-lifetime-policy|CreateRefTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications service-principal create-ref-transitive-member-of

create-ref-transitive-member-of a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-transitive-member-of|CreateRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications service-principal delete

delete a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAppRoleAssignedTo|
|delete|DeleteAppRoleAssignments|
|delete|DeleteEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--endpoint-id**|string|key: id of endpoint|endpoint_id|endpoint-id|
|**--if-match**|string|ETag|if_match|If-Match|

### applications service-principal delta

delta a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### applications service-principal get-app-role-assigned-to

get-app-role-assigned-to a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-app-role-assigned-to|GetAppRoleAssignedTo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal get-app-role-assignment

get-app-role-assignment a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-app-role-assignment|GetAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal get-available-extension-property

get-available-extension-property a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### applications service-principal get-by-id

get-by-id a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### applications service-principal get-endpoint

get-endpoint a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-endpoint|GetEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--endpoint-id**|string|key: id of endpoint|endpoint_id|endpoint-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal get-member-group

get-member-group a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### applications service-principal get-member-object

get-member-object a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### applications service-principal list-app-role-assigned-to

list-app-role-assigned-to a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-app-role-assigned-to|ListAppRoleAssignedTo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-app-role-assignment

list-app-role-assignment a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-app-role-assignment|ListAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-claim-mapping-policy

list-claim-mapping-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-claim-mapping-policy|ListClaimsMappingPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-created-object

list-created-object a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-created-object|ListCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-endpoint

list-endpoint a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-endpoint|ListEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-home-realm-discovery-policy

list-home-realm-discovery-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-home-realm-discovery-policy|ListHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-member-of

list-member-of a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member-of|ListMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-oauth2-permission-grant

list-oauth2-permission-grant a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-oauth2-permission-grant|ListOauth2PermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-owned-object

list-owned-object a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-owned-object|ListOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-owner

list-owner a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-owner|ListOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-ref-claim-mapping-policy

list-ref-claim-mapping-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-claim-mapping-policy|ListRefClaimsMappingPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications service-principal list-ref-created-object

list-ref-created-object a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-created-object|ListRefCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications service-principal list-ref-home-realm-discovery-policy

list-ref-home-realm-discovery-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-home-realm-discovery-policy|ListRefHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications service-principal list-ref-member-of

list-ref-member-of a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member-of|ListRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications service-principal list-ref-oauth2-permission-grant

list-ref-oauth2-permission-grant a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-oauth2-permission-grant|ListRefOauth2PermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications service-principal list-ref-owned-object

list-ref-owned-object a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owned-object|ListRefOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications service-principal list-ref-owner

list-ref-owner a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owner|ListRefOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications service-principal list-ref-token-issuance-policy

list-ref-token-issuance-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-token-issuance-policy|ListRefTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications service-principal list-ref-token-lifetime-policy

list-ref-token-lifetime-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-token-lifetime-policy|ListRefTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications service-principal list-ref-transitive-member-of

list-ref-transitive-member-of a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-transitive-member-of|ListRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications service-principal list-token-issuance-policy

list-token-issuance-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-token-issuance-policy|ListTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-token-lifetime-policy

list-token-lifetime-policy a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-token-lifetime-policy|ListTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal list-transitive-member-of

list-transitive-member-of a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-transitive-member-of|ListTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal remove-key

remove-key a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remove-key|removeKey|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--key-id**|uuid||key_id|keyId|
|**--proof**|string||proof|proof|

### applications service-principal remove-password

remove-password a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remove-password|removePassword|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--key-id**|uuid||key_id|keyId|

### applications service-principal restore

restore a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|

### applications service-principal update-app-role-assigned-to

update-app-role-assigned-to a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-app-role-assigned-to|UpdateAppRoleAssignedTo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--app-role-id**|uuid|The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. Does not support $filter.|app_role_id|appRoleId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--principal-display-name**|string|The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).|principal_display_name|principalDisplayName|
|**--principal-id**|uuid|The unique identifier (id) for the user, group or service principal being granted the app role. Required on create. Does not support $filter.|principal_id|principalId|
|**--principal-type**|string|The type of the assigned principal. This can either be 'User', 'Group' or 'ServicePrincipal'. Read-only. Does not support $filter.|principal_type|principalType|
|**--resource-display-name**|string|The display name of the resource app's service principal to which the assignment is made. Does not support $filter.|resource_display_name|resourceDisplayName|
|**--resource-id**|uuid|The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).|resource_id|resourceId|

### applications service-principal update-app-role-assignment

update-app-role-assignment a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-app-role-assignment|UpdateAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--app-role-id**|uuid|The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. Does not support $filter.|app_role_id|appRoleId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--principal-display-name**|string|The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).|principal_display_name|principalDisplayName|
|**--principal-id**|uuid|The unique identifier (id) for the user, group or service principal being granted the app role. Required on create. Does not support $filter.|principal_id|principalId|
|**--principal-type**|string|The type of the assigned principal. This can either be 'User', 'Group' or 'ServicePrincipal'. Read-only. Does not support $filter.|principal_type|principalType|
|**--resource-display-name**|string|The display name of the resource app's service principal to which the assignment is made. Does not support $filter.|resource_display_name|resourceDisplayName|
|**--resource-id**|uuid|The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).|resource_id|resourceId|

### applications service-principal update-endpoint

update-endpoint a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-endpoint|UpdateEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--endpoint-id**|string|key: id of endpoint|endpoint_id|endpoint-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--capability**|string|Describes the capability that is associated with this resource. (e.g. Messages, Conversations, etc.)  Not nullable. Read-only.|capability|capability|
|**--provider-id**|string|Application id of the publishing underlying service. Not nullable. Read-only.|provider_id|providerId|
|**--provider-name**|string|Name of the publishing underlying service. Read-only.|provider_name|providerName|
|**--provider-resource-id**|string|For Microsoft 365 groups, this is set to a well-known name for the resource (e.g. Yammer.FeedURL etc.). Not nullable. Read-only.|provider_resource_id|providerResourceId|
|**--uri**|string|URL of the published resource. Not nullable. Read-only.|uri|uri|

### applications service-principal validate-property

validate-property a applications service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal|servicePrincipals|

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

### applications service-principal-service-principal create-service-principal

create-service-principal a applications service-principal-service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal-service-principal|servicePrincipals.servicePrincipal|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-service-principal|CreateServicePrincipal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### applications service-principal-service-principal delete

delete a applications service-principal-service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal-service-principal|servicePrincipals.servicePrincipal|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteServicePrincipal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--if-match**|string|ETag|if_match|If-Match|

### applications service-principal-service-principal get-service-principal

get-service-principal a applications service-principal-service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal-service-principal|servicePrincipals.servicePrincipal|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-service-principal|GetServicePrincipal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal-service-principal list-service-principal

list-service-principal a applications service-principal-service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal-service-principal|servicePrincipals.servicePrincipal|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-service-principal|ListServicePrincipal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications service-principal-service-principal update-service-principal

update-service-principal a applications service-principal-service-principal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications service-principal-service-principal|servicePrincipals.servicePrincipal|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-service-principal|UpdateServicePrincipal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|object|New property values|body|body|

### applications user create-app-role-assignment

create-app-role-assignment a applications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-app-role-assignment|CreateAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--app-role-id**|uuid|The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. Does not support $filter.|app_role_id|appRoleId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--principal-display-name**|string|The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).|principal_display_name|principalDisplayName|
|**--principal-id**|uuid|The unique identifier (id) for the user, group or service principal being granted the app role. Required on create. Does not support $filter.|principal_id|principalId|
|**--principal-type**|string|The type of the assigned principal. This can either be 'User', 'Group' or 'ServicePrincipal'. Read-only. Does not support $filter.|principal_type|principalType|
|**--resource-display-name**|string|The display name of the resource app's service principal to which the assignment is made. Does not support $filter.|resource_display_name|resourceDisplayName|
|**--resource-id**|uuid|The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).|resource_id|resourceId|

### applications user delete

delete a applications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

### applications user get-app-role-assignment

get-app-role-assignment a applications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-app-role-assignment|GetAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications user list-app-role-assignment

list-app-role-assignment a applications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-app-role-assignment|ListAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### applications user update-app-role-assignment

update-app-role-assignment a applications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-app-role-assignment|UpdateAppRoleAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--app-role-id**|uuid|The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. Does not support $filter.|app_role_id|appRoleId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--principal-display-name**|string|The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).|principal_display_name|principalDisplayName|
|**--principal-id**|uuid|The unique identifier (id) for the user, group or service principal being granted the app role. Required on create. Does not support $filter.|principal_id|principalId|
|**--principal-type**|string|The type of the assigned principal. This can either be 'User', 'Group' or 'ServicePrincipal'. Read-only. Does not support $filter.|principal_type|principalType|
|**--resource-display-name**|string|The display name of the resource app's service principal to which the assignment is made. Does not support $filter.|resource_display_name|resourceDisplayName|
|**--resource-id**|uuid|The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).|resource_id|resourceId|
