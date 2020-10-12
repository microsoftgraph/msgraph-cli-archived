# Azure CLI Module Creation Report

### applications add-key

add-key a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications add-password

add-password a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|add-password|addPassword|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--password-credential**|object|passwordCredential|password_credential|passwordCredential|

### applications check-member-group

check-member-group a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--group-ids**|array||group_ids|groupIds|

### applications check-member-object

check-member-object a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--ids**|array||ids|ids|

### applications create-app-role-assigned-to

create-app-role-assigned-to a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications create-app-role-assignment

create-app-role-assignment a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|users|

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

### applications create-application

create-application a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-application|CreateApplication|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### applications create-endpoint

create-endpoint a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications create-extension-property

create-extension-property a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications|

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

### applications create-ref-claim-mapping-policy

create-ref-claim-mapping-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-claim-mapping-policy|CreateRefClaimsMappingPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications create-ref-created-object

create-ref-created-object a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-created-object|CreateRefCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications create-ref-home-realm-discovery-policy

create-ref-home-realm-discovery-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-home-realm-discovery-policy|CreateRefHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications create-ref-member-of

create-ref-member-of a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member-of|CreateRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications create-ref-oauth2-permission-grant

create-ref-oauth2-permission-grant a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-oauth2-permission-grant|CreateRefOauth2PermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications create-ref-owned-object

create-ref-owned-object a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owned-object|CreateRefOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications create-ref-owner

create-ref-owner a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owner|CreateRefOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications create-ref-token-issuance-policy

create-ref-token-issuance-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-token-issuance-policy|CreateRefTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications create-ref-token-lifetime-policy

create-ref-token-lifetime-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-token-lifetime-policy|CreateRefTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications create-ref-transitive-member-of

create-ref-transitive-member-of a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-transitive-member-of|CreateRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### applications create-service-principal

create-service-principal a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals.servicePrincipal|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-service-principal|CreateServicePrincipal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### applications delete

delete a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|users|

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

### applications delta

delta a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### applications get-app-role-assigned-to

get-app-role-assigned-to a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications get-app-role-assignment

get-app-role-assignment a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|users|

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

### applications get-application

get-application a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications.application|

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

### applications get-available-extension-property

get-available-extension-property a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### applications get-by-id

get-by-id a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### applications get-created-on-behalf-of

get-created-on-behalf-of a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications|

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

### applications get-endpoint

get-endpoint a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications get-extension-property

get-extension-property a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications|

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

### applications get-logo

get-logo a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-logo|GetLogo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|

### applications get-member-group

get-member-group a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### applications get-member-object

get-member-object a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### applications get-ref-created-on-behalf-of

get-ref-created-on-behalf-of a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-created-on-behalf-of|GetRefCreatedOnBehalfOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|

### applications get-service-principal

get-service-principal a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals.servicePrincipal|

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

### applications list-app-role-assigned-to

list-app-role-assigned-to a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-app-role-assignment

list-app-role-assignment a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|users|

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

### applications list-application

list-application a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications.application|

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

### applications list-claim-mapping-policy

list-claim-mapping-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-created-object

list-created-object a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-endpoint

list-endpoint a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-extension-property

list-extension-property a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications|

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

### applications list-home-realm-discovery-policy

list-home-realm-discovery-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-member-of

list-member-of a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-oauth2-permission-grant

list-oauth2-permission-grant a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-owned-object

list-owned-object a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-owner

list-owner a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-ref-claim-mapping-policy

list-ref-claim-mapping-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-claim-mapping-policy|ListRefClaimsMappingPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications list-ref-created-object

list-ref-created-object a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-created-object|ListRefCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications list-ref-home-realm-discovery-policy

list-ref-home-realm-discovery-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-home-realm-discovery-policy|ListRefHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications list-ref-member-of

list-ref-member-of a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member-of|ListRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications list-ref-oauth2-permission-grant

list-ref-oauth2-permission-grant a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-oauth2-permission-grant|ListRefOauth2PermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications list-ref-owned-object

list-ref-owned-object a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owned-object|ListRefOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications list-ref-owner

list-ref-owner a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owner|ListRefOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications list-ref-token-issuance-policy

list-ref-token-issuance-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-token-issuance-policy|ListRefTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications list-ref-token-lifetime-policy

list-ref-token-lifetime-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-token-lifetime-policy|ListRefTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications list-ref-transitive-member-of

list-ref-transitive-member-of a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-transitive-member-of|ListRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### applications list-service-principal

list-service-principal a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals.servicePrincipal|

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

### applications list-token-issuance-policy

list-token-issuance-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-token-lifetime-policy

list-token-lifetime-policy a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications list-transitive-member-of

list-transitive-member-of a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications remove-key

remove-key a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications remove-password

remove-password a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remove-password|removePassword|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--key-id**|uuid||key_id|keyId|

### applications restore

restore a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|

### applications set-logo

set-logo a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-logo|SetLogo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--data**|binary|New media content.|data|data|

### applications set-ref-created-on-behalf-of

set-ref-created-on-behalf-of a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-created-on-behalf-of|SetRefCreatedOnBehalfOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### applications update-app-role-assigned-to

update-app-role-assigned-to a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications update-app-role-assignment

update-app-role-assignment a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|users|

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

### applications update-application

update-application a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications.application|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-application|UpdateApplication|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|object|New property values|body|body|

### applications update-endpoint

update-endpoint a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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

### applications update-extension-property

update-extension-property a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|applications|

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

### applications update-service-principal

update-service-principal a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals.servicePrincipal|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-service-principal|UpdateServicePrincipal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|object|New property values|body|body|

### applications validate-property

validate-property a applications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|applications|servicePrincipals|

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
