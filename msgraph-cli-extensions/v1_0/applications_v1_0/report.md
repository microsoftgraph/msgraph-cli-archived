# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az applications_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az applications_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az applications application|applications.application|[commands](#CommandsInapplications.application)|
|az applications application|applications|[commands](#CommandsInapplications)|
|az applications group|groups|[commands](#CommandsIngroups)|
|az applications service-principal-service-principal|servicePrincipals.servicePrincipal|[commands](#CommandsInservicePrincipals.servicePrincipal)|
|az applications service-principal|servicePrincipals|[commands](#CommandsInservicePrincipals)|
|az applications user|users|[commands](#CommandsInusers)|

## COMMANDS
### <a name="CommandsInapplications.application">Commands in `az applications application` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az applications application list](#applications.applicationListApplication)|ListApplication|[Parameters](#Parametersapplications.applicationListApplication)|Not Found|
|[az applications application create](#applications.applicationUpdateApplication)|UpdateApplication|[Parameters](#Parametersapplications.applicationUpdateApplication)|Not Found|
|[az applications application create](#applications.applicationCreateApplication)|CreateApplication|[Parameters](#Parametersapplications.applicationCreateApplication)|Not Found|
|[az applications application delete-application](#applications.applicationDeleteApplication)|DeleteApplication|[Parameters](#Parametersapplications.applicationDeleteApplication)|Not Found|
|[az applications application set-logo](#applications.applicationSetLogo)|SetLogo|[Parameters](#Parametersapplications.applicationSetLogo)|Not Found|
|[az applications application show-application](#applications.applicationGetApplication)|GetApplication|[Parameters](#Parametersapplications.applicationGetApplication)|Not Found|
|[az applications application show-logo](#applications.applicationGetLogo)|GetLogo|[Parameters](#Parametersapplications.applicationGetLogo)|Not Found|

### <a name="CommandsInapplications">Commands in `az applications application` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az applications application add-key](#applicationsaddKey)|addKey|[Parameters](#ParametersapplicationsaddKey)|Not Found|
|[az applications application add-password](#applicationsaddPassword)|addPassword|[Parameters](#ParametersapplicationsaddPassword)|Not Found|
|[az applications application check-member-group](#applicationscheckMemberGroups)|checkMemberGroups|[Parameters](#ParametersapplicationscheckMemberGroups)|Not Found|
|[az applications application check-member-object](#applicationscheckMemberObjects)|checkMemberObjects|[Parameters](#ParametersapplicationscheckMemberObjects)|Not Found|
|[az applications application create-extension-property](#applicationsCreateExtensionProperties)|CreateExtensionProperties|[Parameters](#ParametersapplicationsCreateExtensionProperties)|Not Found|
|[az applications application create-ref-home-realm-discovery-policy](#applicationsCreateRefHomeRealmDiscoveryPolicies)|CreateRefHomeRealmDiscoveryPolicies|[Parameters](#ParametersapplicationsCreateRefHomeRealmDiscoveryPolicies)|Not Found|
|[az applications application create-ref-owner](#applicationsCreateRefOwners)|CreateRefOwners|[Parameters](#ParametersapplicationsCreateRefOwners)|Not Found|
|[az applications application create-ref-token-issuance-policy](#applicationsCreateRefTokenIssuancePolicies)|CreateRefTokenIssuancePolicies|[Parameters](#ParametersapplicationsCreateRefTokenIssuancePolicies)|Not Found|
|[az applications application create-ref-token-lifetime-policy](#applicationsCreateRefTokenLifetimePolicies)|CreateRefTokenLifetimePolicies|[Parameters](#ParametersapplicationsCreateRefTokenLifetimePolicies)|Not Found|
|[az applications application delete-extension-property](#applicationsDeleteExtensionProperties)|DeleteExtensionProperties|[Parameters](#ParametersapplicationsDeleteExtensionProperties)|Not Found|
|[az applications application delete-ref-created-on-behalf-of](#applicationsDeleteRefCreatedOnBehalfOf)|DeleteRefCreatedOnBehalfOf|[Parameters](#ParametersapplicationsDeleteRefCreatedOnBehalfOf)|Not Found|
|[az applications application delta](#applicationsdelta)|delta|[Parameters](#Parametersapplicationsdelta)|Not Found|
|[az applications application get-available-extension-property](#applicationsgetAvailableExtensionProperties)|getAvailableExtensionProperties|[Parameters](#ParametersapplicationsgetAvailableExtensionProperties)|Not Found|
|[az applications application get-by-id](#applicationsgetByIds)|getByIds|[Parameters](#ParametersapplicationsgetByIds)|Not Found|
|[az applications application get-member-group](#applicationsgetMemberGroups)|getMemberGroups|[Parameters](#ParametersapplicationsgetMemberGroups)|Not Found|
|[az applications application get-member-object](#applicationsgetMemberObjects)|getMemberObjects|[Parameters](#ParametersapplicationsgetMemberObjects)|Not Found|
|[az applications application list-extension-property](#applicationsListExtensionProperties)|ListExtensionProperties|[Parameters](#ParametersapplicationsListExtensionProperties)|Not Found|
|[az applications application list-home-realm-discovery-policy](#applicationsListHomeRealmDiscoveryPolicies)|ListHomeRealmDiscoveryPolicies|[Parameters](#ParametersapplicationsListHomeRealmDiscoveryPolicies)|Not Found|
|[az applications application list-owner](#applicationsListOwners)|ListOwners|[Parameters](#ParametersapplicationsListOwners)|Not Found|
|[az applications application list-ref-home-realm-discovery-policy](#applicationsListRefHomeRealmDiscoveryPolicies)|ListRefHomeRealmDiscoveryPolicies|[Parameters](#ParametersapplicationsListRefHomeRealmDiscoveryPolicies)|Not Found|
|[az applications application list-ref-owner](#applicationsListRefOwners)|ListRefOwners|[Parameters](#ParametersapplicationsListRefOwners)|Not Found|
|[az applications application list-ref-token-issuance-policy](#applicationsListRefTokenIssuancePolicies)|ListRefTokenIssuancePolicies|[Parameters](#ParametersapplicationsListRefTokenIssuancePolicies)|Not Found|
|[az applications application list-ref-token-lifetime-policy](#applicationsListRefTokenLifetimePolicies)|ListRefTokenLifetimePolicies|[Parameters](#ParametersapplicationsListRefTokenLifetimePolicies)|Not Found|
|[az applications application list-token-issuance-policy](#applicationsListTokenIssuancePolicies)|ListTokenIssuancePolicies|[Parameters](#ParametersapplicationsListTokenIssuancePolicies)|Not Found|
|[az applications application list-token-lifetime-policy](#applicationsListTokenLifetimePolicies)|ListTokenLifetimePolicies|[Parameters](#ParametersapplicationsListTokenLifetimePolicies)|Not Found|
|[az applications application remove-key](#applicationsremoveKey)|removeKey|[Parameters](#ParametersapplicationsremoveKey)|Not Found|
|[az applications application remove-password](#applicationsremovePassword)|removePassword|[Parameters](#ParametersapplicationsremovePassword)|Not Found|
|[az applications application restore](#applicationsrestore)|restore|[Parameters](#Parametersapplicationsrestore)|Not Found|
|[az applications application set-ref-created-on-behalf-of](#applicationsSetRefCreatedOnBehalfOf)|SetRefCreatedOnBehalfOf|[Parameters](#ParametersapplicationsSetRefCreatedOnBehalfOf)|Not Found|
|[az applications application show-created-on-behalf-of](#applicationsGetCreatedOnBehalfOf)|GetCreatedOnBehalfOf|[Parameters](#ParametersapplicationsGetCreatedOnBehalfOf)|Not Found|
|[az applications application show-extension-property](#applicationsGetExtensionProperties)|GetExtensionProperties|[Parameters](#ParametersapplicationsGetExtensionProperties)|Not Found|
|[az applications application show-ref-created-on-behalf-of](#applicationsGetRefCreatedOnBehalfOf)|GetRefCreatedOnBehalfOf|[Parameters](#ParametersapplicationsGetRefCreatedOnBehalfOf)|Not Found|
|[az applications application update-extension-property](#applicationsUpdateExtensionProperties)|UpdateExtensionProperties|[Parameters](#ParametersapplicationsUpdateExtensionProperties)|Not Found|
|[az applications application validate-property](#applicationsvalidateProperties)|validateProperties|[Parameters](#ParametersapplicationsvalidateProperties)|Not Found|

### <a name="CommandsIngroups">Commands in `az applications group` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az applications group create-app-role-assignment](#groupsCreateAppRoleAssignments)|CreateAppRoleAssignments|[Parameters](#ParametersgroupsCreateAppRoleAssignments)|Not Found|
|[az applications group delete-app-role-assignment](#groupsDeleteAppRoleAssignments)|DeleteAppRoleAssignments|[Parameters](#ParametersgroupsDeleteAppRoleAssignments)|Not Found|
|[az applications group list-app-role-assignment](#groupsListAppRoleAssignments)|ListAppRoleAssignments|[Parameters](#ParametersgroupsListAppRoleAssignments)|Not Found|
|[az applications group show-app-role-assignment](#groupsGetAppRoleAssignments)|GetAppRoleAssignments|[Parameters](#ParametersgroupsGetAppRoleAssignments)|Not Found|
|[az applications group update-app-role-assignment](#groupsUpdateAppRoleAssignments)|UpdateAppRoleAssignments|[Parameters](#ParametersgroupsUpdateAppRoleAssignments)|Not Found|

### <a name="CommandsInservicePrincipals">Commands in `az applications service-principal` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az applications service-principal add-key](#servicePrincipalsaddKey)|addKey|[Parameters](#ParametersservicePrincipalsaddKey)|Not Found|
|[az applications service-principal add-password](#servicePrincipalsaddPassword)|addPassword|[Parameters](#ParametersservicePrincipalsaddPassword)|Not Found|
|[az applications service-principal check-member-group](#servicePrincipalscheckMemberGroups)|checkMemberGroups|[Parameters](#ParametersservicePrincipalscheckMemberGroups)|Not Found|
|[az applications service-principal check-member-object](#servicePrincipalscheckMemberObjects)|checkMemberObjects|[Parameters](#ParametersservicePrincipalscheckMemberObjects)|Not Found|
|[az applications service-principal create-app-role-assigned-to](#servicePrincipalsCreateAppRoleAssignedTo)|CreateAppRoleAssignedTo|[Parameters](#ParametersservicePrincipalsCreateAppRoleAssignedTo)|Not Found|
|[az applications service-principal create-app-role-assignment](#servicePrincipalsCreateAppRoleAssignments)|CreateAppRoleAssignments|[Parameters](#ParametersservicePrincipalsCreateAppRoleAssignments)|Not Found|
|[az applications service-principal create-endpoint](#servicePrincipalsCreateEndpoints)|CreateEndpoints|[Parameters](#ParametersservicePrincipalsCreateEndpoints)|Not Found|
|[az applications service-principal create-ref-claim-mapping-policy](#servicePrincipalsCreateRefClaimsMappingPolicies)|CreateRefClaimsMappingPolicies|[Parameters](#ParametersservicePrincipalsCreateRefClaimsMappingPolicies)|Not Found|
|[az applications service-principal create-ref-created-object](#servicePrincipalsCreateRefCreatedObjects)|CreateRefCreatedObjects|[Parameters](#ParametersservicePrincipalsCreateRefCreatedObjects)|Not Found|
|[az applications service-principal create-ref-home-realm-discovery-policy](#servicePrincipalsCreateRefHomeRealmDiscoveryPolicies)|CreateRefHomeRealmDiscoveryPolicies|[Parameters](#ParametersservicePrincipalsCreateRefHomeRealmDiscoveryPolicies)|Not Found|
|[az applications service-principal create-ref-member-of](#servicePrincipalsCreateRefMemberOf)|CreateRefMemberOf|[Parameters](#ParametersservicePrincipalsCreateRefMemberOf)|Not Found|
|[az applications service-principal create-ref-oauth2-permission-grant](#servicePrincipalsCreateRefOauth2PermissionGrants)|CreateRefOauth2PermissionGrants|[Parameters](#ParametersservicePrincipalsCreateRefOauth2PermissionGrants)|Not Found|
|[az applications service-principal create-ref-owned-object](#servicePrincipalsCreateRefOwnedObjects)|CreateRefOwnedObjects|[Parameters](#ParametersservicePrincipalsCreateRefOwnedObjects)|Not Found|
|[az applications service-principal create-ref-owner](#servicePrincipalsCreateRefOwners)|CreateRefOwners|[Parameters](#ParametersservicePrincipalsCreateRefOwners)|Not Found|
|[az applications service-principal create-ref-token-issuance-policy](#servicePrincipalsCreateRefTokenIssuancePolicies)|CreateRefTokenIssuancePolicies|[Parameters](#ParametersservicePrincipalsCreateRefTokenIssuancePolicies)|Not Found|
|[az applications service-principal create-ref-token-lifetime-policy](#servicePrincipalsCreateRefTokenLifetimePolicies)|CreateRefTokenLifetimePolicies|[Parameters](#ParametersservicePrincipalsCreateRefTokenLifetimePolicies)|Not Found|
|[az applications service-principal create-ref-transitive-member-of](#servicePrincipalsCreateRefTransitiveMemberOf)|CreateRefTransitiveMemberOf|[Parameters](#ParametersservicePrincipalsCreateRefTransitiveMemberOf)|Not Found|
|[az applications service-principal delete-app-role-assigned-to](#servicePrincipalsDeleteAppRoleAssignedTo)|DeleteAppRoleAssignedTo|[Parameters](#ParametersservicePrincipalsDeleteAppRoleAssignedTo)|Not Found|
|[az applications service-principal delete-app-role-assignment](#servicePrincipalsDeleteAppRoleAssignments)|DeleteAppRoleAssignments|[Parameters](#ParametersservicePrincipalsDeleteAppRoleAssignments)|Not Found|
|[az applications service-principal delete-endpoint](#servicePrincipalsDeleteEndpoints)|DeleteEndpoints|[Parameters](#ParametersservicePrincipalsDeleteEndpoints)|Not Found|
|[az applications service-principal delta](#servicePrincipalsdelta)|delta|[Parameters](#ParametersservicePrincipalsdelta)|Not Found|
|[az applications service-principal get-available-extension-property](#servicePrincipalsgetAvailableExtensionProperties)|getAvailableExtensionProperties|[Parameters](#ParametersservicePrincipalsgetAvailableExtensionProperties)|Not Found|
|[az applications service-principal get-by-id](#servicePrincipalsgetByIds)|getByIds|[Parameters](#ParametersservicePrincipalsgetByIds)|Not Found|
|[az applications service-principal get-member-group](#servicePrincipalsgetMemberGroups)|getMemberGroups|[Parameters](#ParametersservicePrincipalsgetMemberGroups)|Not Found|
|[az applications service-principal get-member-object](#servicePrincipalsgetMemberObjects)|getMemberObjects|[Parameters](#ParametersservicePrincipalsgetMemberObjects)|Not Found|
|[az applications service-principal list-app-role-assigned-to](#servicePrincipalsListAppRoleAssignedTo)|ListAppRoleAssignedTo|[Parameters](#ParametersservicePrincipalsListAppRoleAssignedTo)|Not Found|
|[az applications service-principal list-app-role-assignment](#servicePrincipalsListAppRoleAssignments)|ListAppRoleAssignments|[Parameters](#ParametersservicePrincipalsListAppRoleAssignments)|Not Found|
|[az applications service-principal list-claim-mapping-policy](#servicePrincipalsListClaimsMappingPolicies)|ListClaimsMappingPolicies|[Parameters](#ParametersservicePrincipalsListClaimsMappingPolicies)|Not Found|
|[az applications service-principal list-created-object](#servicePrincipalsListCreatedObjects)|ListCreatedObjects|[Parameters](#ParametersservicePrincipalsListCreatedObjects)|Not Found|
|[az applications service-principal list-endpoint](#servicePrincipalsListEndpoints)|ListEndpoints|[Parameters](#ParametersservicePrincipalsListEndpoints)|Not Found|
|[az applications service-principal list-home-realm-discovery-policy](#servicePrincipalsListHomeRealmDiscoveryPolicies)|ListHomeRealmDiscoveryPolicies|[Parameters](#ParametersservicePrincipalsListHomeRealmDiscoveryPolicies)|Not Found|
|[az applications service-principal list-member-of](#servicePrincipalsListMemberOf)|ListMemberOf|[Parameters](#ParametersservicePrincipalsListMemberOf)|Not Found|
|[az applications service-principal list-oauth2-permission-grant](#servicePrincipalsListOauth2PermissionGrants)|ListOauth2PermissionGrants|[Parameters](#ParametersservicePrincipalsListOauth2PermissionGrants)|Not Found|
|[az applications service-principal list-owned-object](#servicePrincipalsListOwnedObjects)|ListOwnedObjects|[Parameters](#ParametersservicePrincipalsListOwnedObjects)|Not Found|
|[az applications service-principal list-owner](#servicePrincipalsListOwners)|ListOwners|[Parameters](#ParametersservicePrincipalsListOwners)|Not Found|
|[az applications service-principal list-ref-claim-mapping-policy](#servicePrincipalsListRefClaimsMappingPolicies)|ListRefClaimsMappingPolicies|[Parameters](#ParametersservicePrincipalsListRefClaimsMappingPolicies)|Not Found|
|[az applications service-principal list-ref-created-object](#servicePrincipalsListRefCreatedObjects)|ListRefCreatedObjects|[Parameters](#ParametersservicePrincipalsListRefCreatedObjects)|Not Found|
|[az applications service-principal list-ref-home-realm-discovery-policy](#servicePrincipalsListRefHomeRealmDiscoveryPolicies)|ListRefHomeRealmDiscoveryPolicies|[Parameters](#ParametersservicePrincipalsListRefHomeRealmDiscoveryPolicies)|Not Found|
|[az applications service-principal list-ref-member-of](#servicePrincipalsListRefMemberOf)|ListRefMemberOf|[Parameters](#ParametersservicePrincipalsListRefMemberOf)|Not Found|
|[az applications service-principal list-ref-oauth2-permission-grant](#servicePrincipalsListRefOauth2PermissionGrants)|ListRefOauth2PermissionGrants|[Parameters](#ParametersservicePrincipalsListRefOauth2PermissionGrants)|Not Found|
|[az applications service-principal list-ref-owned-object](#servicePrincipalsListRefOwnedObjects)|ListRefOwnedObjects|[Parameters](#ParametersservicePrincipalsListRefOwnedObjects)|Not Found|
|[az applications service-principal list-ref-owner](#servicePrincipalsListRefOwners)|ListRefOwners|[Parameters](#ParametersservicePrincipalsListRefOwners)|Not Found|
|[az applications service-principal list-ref-token-issuance-policy](#servicePrincipalsListRefTokenIssuancePolicies)|ListRefTokenIssuancePolicies|[Parameters](#ParametersservicePrincipalsListRefTokenIssuancePolicies)|Not Found|
|[az applications service-principal list-ref-token-lifetime-policy](#servicePrincipalsListRefTokenLifetimePolicies)|ListRefTokenLifetimePolicies|[Parameters](#ParametersservicePrincipalsListRefTokenLifetimePolicies)|Not Found|
|[az applications service-principal list-ref-transitive-member-of](#servicePrincipalsListRefTransitiveMemberOf)|ListRefTransitiveMemberOf|[Parameters](#ParametersservicePrincipalsListRefTransitiveMemberOf)|Not Found|
|[az applications service-principal list-token-issuance-policy](#servicePrincipalsListTokenIssuancePolicies)|ListTokenIssuancePolicies|[Parameters](#ParametersservicePrincipalsListTokenIssuancePolicies)|Not Found|
|[az applications service-principal list-token-lifetime-policy](#servicePrincipalsListTokenLifetimePolicies)|ListTokenLifetimePolicies|[Parameters](#ParametersservicePrincipalsListTokenLifetimePolicies)|Not Found|
|[az applications service-principal list-transitive-member-of](#servicePrincipalsListTransitiveMemberOf)|ListTransitiveMemberOf|[Parameters](#ParametersservicePrincipalsListTransitiveMemberOf)|Not Found|
|[az applications service-principal remove-key](#servicePrincipalsremoveKey)|removeKey|[Parameters](#ParametersservicePrincipalsremoveKey)|Not Found|
|[az applications service-principal remove-password](#servicePrincipalsremovePassword)|removePassword|[Parameters](#ParametersservicePrincipalsremovePassword)|Not Found|
|[az applications service-principal restore](#servicePrincipalsrestore)|restore|[Parameters](#ParametersservicePrincipalsrestore)|Not Found|
|[az applications service-principal show-app-role-assigned-to](#servicePrincipalsGetAppRoleAssignedTo)|GetAppRoleAssignedTo|[Parameters](#ParametersservicePrincipalsGetAppRoleAssignedTo)|Not Found|
|[az applications service-principal show-app-role-assignment](#servicePrincipalsGetAppRoleAssignments)|GetAppRoleAssignments|[Parameters](#ParametersservicePrincipalsGetAppRoleAssignments)|Not Found|
|[az applications service-principal show-endpoint](#servicePrincipalsGetEndpoints)|GetEndpoints|[Parameters](#ParametersservicePrincipalsGetEndpoints)|Not Found|
|[az applications service-principal update-app-role-assigned-to](#servicePrincipalsUpdateAppRoleAssignedTo)|UpdateAppRoleAssignedTo|[Parameters](#ParametersservicePrincipalsUpdateAppRoleAssignedTo)|Not Found|
|[az applications service-principal update-app-role-assignment](#servicePrincipalsUpdateAppRoleAssignments)|UpdateAppRoleAssignments|[Parameters](#ParametersservicePrincipalsUpdateAppRoleAssignments)|Not Found|
|[az applications service-principal update-endpoint](#servicePrincipalsUpdateEndpoints)|UpdateEndpoints|[Parameters](#ParametersservicePrincipalsUpdateEndpoints)|Not Found|
|[az applications service-principal validate-property](#servicePrincipalsvalidateProperties)|validateProperties|[Parameters](#ParametersservicePrincipalsvalidateProperties)|Not Found|

### <a name="CommandsInservicePrincipals.servicePrincipal">Commands in `az applications service-principal-service-principal` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az applications service-principal-service-principal create-service-principal](#servicePrincipals.servicePrincipalCreateServicePrincipal)|CreateServicePrincipal|[Parameters](#ParametersservicePrincipals.servicePrincipalCreateServicePrincipal)|Not Found|
|[az applications service-principal-service-principal delete-service-principal](#servicePrincipals.servicePrincipalDeleteServicePrincipal)|DeleteServicePrincipal|[Parameters](#ParametersservicePrincipals.servicePrincipalDeleteServicePrincipal)|Not Found|
|[az applications service-principal-service-principal list-service-principal](#servicePrincipals.servicePrincipalListServicePrincipal)|ListServicePrincipal|[Parameters](#ParametersservicePrincipals.servicePrincipalListServicePrincipal)|Not Found|
|[az applications service-principal-service-principal show-service-principal](#servicePrincipals.servicePrincipalGetServicePrincipal)|GetServicePrincipal|[Parameters](#ParametersservicePrincipals.servicePrincipalGetServicePrincipal)|Not Found|
|[az applications service-principal-service-principal update-service-principal](#servicePrincipals.servicePrincipalUpdateServicePrincipal)|UpdateServicePrincipal|[Parameters](#ParametersservicePrincipals.servicePrincipalUpdateServicePrincipal)|Not Found|

### <a name="CommandsInusers">Commands in `az applications user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az applications user create-app-role-assignment](#usersCreateAppRoleAssignments)|CreateAppRoleAssignments|[Parameters](#ParametersusersCreateAppRoleAssignments)|Not Found|
|[az applications user delete-app-role-assignment](#usersDeleteAppRoleAssignments)|DeleteAppRoleAssignments|[Parameters](#ParametersusersDeleteAppRoleAssignments)|Not Found|
|[az applications user list-app-role-assignment](#usersListAppRoleAssignments)|ListAppRoleAssignments|[Parameters](#ParametersusersListAppRoleAssignments)|Not Found|
|[az applications user show-app-role-assignment](#usersGetAppRoleAssignments)|GetAppRoleAssignments|[Parameters](#ParametersusersGetAppRoleAssignments)|Not Found|
|[az applications user update-app-role-assignment](#usersUpdateAppRoleAssignments)|UpdateAppRoleAssignments|[Parameters](#ParametersusersUpdateAppRoleAssignments)|Not Found|


## COMMAND DETAILS

### group `az applications application`
#### <a name="applications.applicationListApplication">Command `az applications application list`</a>

##### <a name="Parametersapplications.applicationListApplication">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="applications.applicationUpdateApplication">Command `az applications application create`</a>

##### <a name="Parametersapplications.applicationUpdateApplication">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--add-ins**|array|Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This will let services like Microsoft 365 call the application in the context of a document the user is working on.|add_ins|addIns|
|**--app-id**|string|The unique identifier for the application that is assigned to an application by Azure AD. Not nullable. Read-only.|app_id|appId|
|**--application-template-id**|string||application_template_id|applicationTemplateId|
|**--app-roles**|array|The collection of roles the application declares. With app role assignments, these roles can be assigned to users, groups, or other applications' service principals. Not nullable.|app_roles|appRoles|
|**--created-date-time**|date-time|The date and time the application was registered. Read-only.|created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string|The display name for the application.|display_name|displayName|
|**--group-membership-claims**|string|Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values:NoneSecurityGroup: For security groups and Azure AD rolesAll: This will get all of the security groups, distribution groups, and Azure AD directory roles that the signed-in user is a member of|group_membership_claims|groupMembershipClaims|
|**--identifier-uris**|array|The URIs that identify the application within its Azure AD tenant, or within a verified custom domain if the application is multi-tenant. For more information see Application Objects and Service Principal Objects. The any operator is required for filter expressions on multi-valued properties. Not nullable.|identifier_uris|identifierUris|
|**--info**|object|informationalUrl|info|info|
|**--is-device-only-auth-supported**|boolean||is_device_only_auth_supported|isDeviceOnlyAuthSupported|
|**--is-fallback-public-client**|boolean|Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false which means the fallback application type is confidential client such as web app. There are certain scenarios where Azure AD cannot determine the client application type (e.g. ROPC flow where it is configured without specifying a redirect URI). In those cases Azure AD will interpret the application type based on the value of this property.|is_fallback_public_client|isFallbackPublicClient|
|**--key-credentials**|array|The collection of key credentials associated with the application Not nullable.|key_credentials|keyCredentials|
|**--logo**|byte-array|The main logo for the application. Not nullable.|logo|logo|
|**--notes**|string||notes|notes|
|**--oauth2-require-post-response**|boolean||oauth2_require_post_response|oauth2RequirePostResponse|
|**--parental-control-settings**|object|parentalControlSettings|parental_control_settings|parentalControlSettings|
|**--password-credentials**|array|The collection of password credentials associated with the application. Not nullable.|password_credentials|passwordCredentials|
|**--public-client**|object|publicClientApplication|public_client|publicClient|
|**--publisher-domain**|string|The verified publisher domain for the application. Read-only.|publisher_domain|publisherDomain|
|**--required-resource-access**|array|Specifies resources that this application requires access to and the set of OAuth permission scopes and application roles that it needs under each of those resources. This pre-configuration of required resource access drives the consent experience. Not nullable.|required_resource_access|requiredResourceAccess|
|**--sign-in-audience**|string|Specifies the Microsoft accounts that are supported for the current application. Supported values are:AzureADMyOrg: Users with a Microsoft work or school account in my organization’s Azure AD tenant (single tenant)AzureADMultipleOrgs: Users with a Microsoft work or school account in any organization’s Azure AD tenant (multi-tenant)AzureADandPersonalMicrosoftAccount: Users with a personal Microsoft account, or a work or school account in any organization’s Azure AD tenant.|sign_in_audience|signInAudience|
|**--tags**|array|Custom strings that can be used to categorize and identify the application. Not nullable.|tags|tags|
|**--token-encryption-key-id**|uuid|Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.|token_encryption_key_id|tokenEncryptionKeyId|
|**--created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--extension-properties**|array|Read-only. Nullable.|extension_properties|extensionProperties|
|**--home-realm-discovery-policies**|array||home_realm_discovery_policies|homeRealmDiscoveryPolicies|
|**--owners**|array|Directory objects that are owners of the application. The owners are a set of non-admin users who are allowed to modify this object. Requires version 2013-11-08 or newer. Read-only. Nullable.|owners|owners|
|**--token-issuance-policies**|array||token_issuance_policies|tokenIssuancePolicies|
|**--token-lifetime-policies**|array||token_lifetime_policies|tokenLifetimePolicies|
|**--home-page-url**|string|Home page or landing page of the application.|home_page_url|homePageUrl|
|**--implicit-grant-settings**|object|implicitGrantSettings|implicit_grant_settings|implicitGrantSettings|
|**--logout-url**|string|Specifies the URL that will be used by Microsoft's authorization service to logout an user using front-channel, back-channel or SAML logout protocols.|logout_url|logoutUrl|
|**--redirect-uris**|array|Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.|redirect_uris|redirectUris|
|**--access-token**|array|The optional claims returned in the JWT access token.|access_token|accessToken|
|**--id-token**|array|The optional claims returned in the JWT ID token.|id_token|idToken|
|**--saml2-token**|array|The optional claims returned in the SAML token.|saml2_token|saml2Token|
|**--accept-mapped-claims**|boolean|When true, allows an application to use claims mapping without specifying a custom signing key.|accept_mapped_claims|acceptMappedClaims|
|**--known-client-applications**|array|Used for bundling consent if you have a solution that contains two parts: a client app and a custom web API app. If you set the appID of the client app to this value, the user only consents once to the client app. Azure AD knows that consenting to the client means implicitly consenting to the web API and automatically provisions service principals for both APIs at the same time. Both the client and the web API app must be registered in the same tenant.|known_client_applications|knownClientApplications|
|**--oauth2-permission-scopes**|array|The definition of the delegated permissions exposed by the web API represented by this application registration. These delegated permissions may be requested by a client application, and may be granted by users or administrators during consent. Delegated permissions are sometimes referred to as OAuth 2.0 scopes.|oauth2_permission_scopes|oauth2PermissionScopes|
|**--pre-authorized-applications**|array|Lists the client applications that are pre-authorized with the specified delegated permissions to access this application's APIs. Users are not required to consent to any pre-authorized application (for the permissions specified). However, any additional permissions not listed in preAuthorizedApplications (requested through incremental consent for example) will require user consent.|pre_authorized_applications|preAuthorizedApplications|
|**--requested-access-token-version**|integer|Specifies the access token version expected by this resource. This changes the version and format of the JWT produced independent of the endpoint or client used to request the access token.  The endpoint used, v1.0 or v2.0, is chosen by the client and only impacts the version of id_tokens. Resources need to explicitly configure requestedAccessTokenVersion to indicate the supported access token format.  Possible values for requestedAccessTokenVersion are 1, 2, or null. If the value is null, this defaults to 1, which corresponds to the v1.0 endpoint.  If signInAudience on the application is configured as AzureADandPersonalMicrosoftAccount, the value for this property must be 2|requested_access_token_version|requestedAccessTokenVersion|

#### <a name="applications.applicationCreateApplication">Command `az applications application create`</a>

##### <a name="Parametersapplications.applicationCreateApplication">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="applications.applicationDeleteApplication">Command `az applications application delete-application`</a>

##### <a name="Parametersapplications.applicationDeleteApplication">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="applications.applicationSetLogo">Command `az applications application set-logo`</a>

##### <a name="Parametersapplications.applicationSetLogo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--data**|binary|New media content.|data|data|

#### <a name="applications.applicationGetApplication">Command `az applications application show-application`</a>

##### <a name="Parametersapplications.applicationGetApplication">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="applications.applicationGetLogo">Command `az applications application show-logo`</a>

##### <a name="Parametersapplications.applicationGetLogo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|

### group `az applications application`
#### <a name="applicationsaddKey">Command `az applications application add-key`</a>

##### <a name="ParametersapplicationsaddKey">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--key-credential**|object|keyCredential|key_credential|keyCredential|
|**--password-credential**|object|passwordCredential|password_credential|passwordCredential|
|**--proof**|string||proof|proof|

#### <a name="applicationsaddPassword">Command `az applications application add-password`</a>

##### <a name="ParametersapplicationsaddPassword">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--password-credential**|object|passwordCredential|password_credential|passwordCredential|

#### <a name="applicationscheckMemberGroups">Command `az applications application check-member-group`</a>

##### <a name="ParametersapplicationscheckMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--group-ids**|array||group_ids|groupIds|

#### <a name="applicationscheckMemberObjects">Command `az applications application check-member-object`</a>

##### <a name="ParametersapplicationscheckMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--ids**|array||ids|ids|

#### <a name="applicationsCreateExtensionProperties">Command `az applications application create-extension-property`</a>

##### <a name="ParametersapplicationsCreateExtensionProperties">Parameters</a> 
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

#### <a name="applicationsCreateRefHomeRealmDiscoveryPolicies">Command `az applications application create-ref-home-realm-discovery-policy`</a>

##### <a name="ParametersapplicationsCreateRefHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="applicationsCreateRefOwners">Command `az applications application create-ref-owner`</a>

##### <a name="ParametersapplicationsCreateRefOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="applicationsCreateRefTokenIssuancePolicies">Command `az applications application create-ref-token-issuance-policy`</a>

##### <a name="ParametersapplicationsCreateRefTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="applicationsCreateRefTokenLifetimePolicies">Command `az applications application create-ref-token-lifetime-policy`</a>

##### <a name="ParametersapplicationsCreateRefTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="applicationsDeleteExtensionProperties">Command `az applications application delete-extension-property`</a>

##### <a name="ParametersapplicationsDeleteExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--extension-property-id**|string|key: id of extensionProperty|extension_property_id|extensionProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="applicationsDeleteRefCreatedOnBehalfOf">Command `az applications application delete-ref-created-on-behalf-of`</a>

##### <a name="ParametersapplicationsDeleteRefCreatedOnBehalfOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="applicationsdelta">Command `az applications application delta`</a>

##### <a name="Parametersapplicationsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="applicationsgetAvailableExtensionProperties">Command `az applications application get-available-extension-property`</a>

##### <a name="ParametersapplicationsgetAvailableExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

#### <a name="applicationsgetByIds">Command `az applications application get-by-id`</a>

##### <a name="ParametersapplicationsgetByIds">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

#### <a name="applicationsgetMemberGroups">Command `az applications application get-member-group`</a>

##### <a name="ParametersapplicationsgetMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="applicationsgetMemberObjects">Command `az applications application get-member-object`</a>

##### <a name="ParametersapplicationsgetMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="applicationsListExtensionProperties">Command `az applications application list-extension-property`</a>

##### <a name="ParametersapplicationsListExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="applicationsListHomeRealmDiscoveryPolicies">Command `az applications application list-home-realm-discovery-policy`</a>

##### <a name="ParametersapplicationsListHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="applicationsListOwners">Command `az applications application list-owner`</a>

##### <a name="ParametersapplicationsListOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="applicationsListRefHomeRealmDiscoveryPolicies">Command `az applications application list-ref-home-realm-discovery-policy`</a>

##### <a name="ParametersapplicationsListRefHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="applicationsListRefOwners">Command `az applications application list-ref-owner`</a>

##### <a name="ParametersapplicationsListRefOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="applicationsListRefTokenIssuancePolicies">Command `az applications application list-ref-token-issuance-policy`</a>

##### <a name="ParametersapplicationsListRefTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="applicationsListRefTokenLifetimePolicies">Command `az applications application list-ref-token-lifetime-policy`</a>

##### <a name="ParametersapplicationsListRefTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="applicationsListTokenIssuancePolicies">Command `az applications application list-token-issuance-policy`</a>

##### <a name="ParametersapplicationsListTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="applicationsListTokenLifetimePolicies">Command `az applications application list-token-lifetime-policy`</a>

##### <a name="ParametersapplicationsListTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="applicationsremoveKey">Command `az applications application remove-key`</a>

##### <a name="ParametersapplicationsremoveKey">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--key-id**|uuid||key_id|keyId|
|**--proof**|string||proof|proof|

#### <a name="applicationsremovePassword">Command `az applications application remove-password`</a>

##### <a name="ParametersapplicationsremovePassword">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--key-id**|uuid||key_id|keyId|

#### <a name="applicationsrestore">Command `az applications application restore`</a>

##### <a name="Parametersapplicationsrestore">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|

#### <a name="applicationsSetRefCreatedOnBehalfOf">Command `az applications application set-ref-created-on-behalf-of`</a>

##### <a name="ParametersapplicationsSetRefCreatedOnBehalfOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="applicationsGetCreatedOnBehalfOf">Command `az applications application show-created-on-behalf-of`</a>

##### <a name="ParametersapplicationsGetCreatedOnBehalfOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="applicationsGetExtensionProperties">Command `az applications application show-extension-property`</a>

##### <a name="ParametersapplicationsGetExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|
|**--extension-property-id**|string|key: id of extensionProperty|extension_property_id|extensionProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="applicationsGetRefCreatedOnBehalfOf">Command `az applications application show-ref-created-on-behalf-of`</a>

##### <a name="ParametersapplicationsGetRefCreatedOnBehalfOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-id**|string|key: id of application|application_id|application-id|

#### <a name="applicationsUpdateExtensionProperties">Command `az applications application update-extension-property`</a>

##### <a name="ParametersapplicationsUpdateExtensionProperties">Parameters</a> 
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

#### <a name="applicationsvalidateProperties">Command `az applications application validate-property`</a>

##### <a name="ParametersapplicationsvalidateProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### group `az applications group`
#### <a name="groupsCreateAppRoleAssignments">Command `az applications group create-app-role-assignment`</a>

##### <a name="ParametersgroupsCreateAppRoleAssignments">Parameters</a> 
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

#### <a name="groupsDeleteAppRoleAssignments">Command `az applications group delete-app-role-assignment`</a>

##### <a name="ParametersgroupsDeleteAppRoleAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsListAppRoleAssignments">Command `az applications group list-app-role-assignment`</a>

##### <a name="ParametersgroupsListAppRoleAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetAppRoleAssignments">Command `az applications group show-app-role-assignment`</a>

##### <a name="ParametersgroupsGetAppRoleAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsUpdateAppRoleAssignments">Command `az applications group update-app-role-assignment`</a>

##### <a name="ParametersgroupsUpdateAppRoleAssignments">Parameters</a> 
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

### group `az applications service-principal`
#### <a name="servicePrincipalsaddKey">Command `az applications service-principal add-key`</a>

##### <a name="ParametersservicePrincipalsaddKey">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--key-credential**|object|keyCredential|key_credential|keyCredential|
|**--password-credential**|object|passwordCredential|password_credential|passwordCredential|
|**--proof**|string||proof|proof|

#### <a name="servicePrincipalsaddPassword">Command `az applications service-principal add-password`</a>

##### <a name="ParametersservicePrincipalsaddPassword">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--password-credential**|object|passwordCredential|password_credential|passwordCredential|

#### <a name="servicePrincipalscheckMemberGroups">Command `az applications service-principal check-member-group`</a>

##### <a name="ParametersservicePrincipalscheckMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--group-ids**|array||group_ids|groupIds|

#### <a name="servicePrincipalscheckMemberObjects">Command `az applications service-principal check-member-object`</a>

##### <a name="ParametersservicePrincipalscheckMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--ids**|array||ids|ids|

#### <a name="servicePrincipalsCreateAppRoleAssignedTo">Command `az applications service-principal create-app-role-assigned-to`</a>

##### <a name="ParametersservicePrincipalsCreateAppRoleAssignedTo">Parameters</a> 
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

#### <a name="servicePrincipalsCreateAppRoleAssignments">Command `az applications service-principal create-app-role-assignment`</a>

##### <a name="ParametersservicePrincipalsCreateAppRoleAssignments">Parameters</a> 
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

#### <a name="servicePrincipalsCreateEndpoints">Command `az applications service-principal create-endpoint`</a>

##### <a name="ParametersservicePrincipalsCreateEndpoints">Parameters</a> 
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

#### <a name="servicePrincipalsCreateRefClaimsMappingPolicies">Command `az applications service-principal create-ref-claim-mapping-policy`</a>

##### <a name="ParametersservicePrincipalsCreateRefClaimsMappingPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="servicePrincipalsCreateRefCreatedObjects">Command `az applications service-principal create-ref-created-object`</a>

##### <a name="ParametersservicePrincipalsCreateRefCreatedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="servicePrincipalsCreateRefHomeRealmDiscoveryPolicies">Command `az applications service-principal create-ref-home-realm-discovery-policy`</a>

##### <a name="ParametersservicePrincipalsCreateRefHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="servicePrincipalsCreateRefMemberOf">Command `az applications service-principal create-ref-member-of`</a>

##### <a name="ParametersservicePrincipalsCreateRefMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="servicePrincipalsCreateRefOauth2PermissionGrants">Command `az applications service-principal create-ref-oauth2-permission-grant`</a>

##### <a name="ParametersservicePrincipalsCreateRefOauth2PermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="servicePrincipalsCreateRefOwnedObjects">Command `az applications service-principal create-ref-owned-object`</a>

##### <a name="ParametersservicePrincipalsCreateRefOwnedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="servicePrincipalsCreateRefOwners">Command `az applications service-principal create-ref-owner`</a>

##### <a name="ParametersservicePrincipalsCreateRefOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="servicePrincipalsCreateRefTokenIssuancePolicies">Command `az applications service-principal create-ref-token-issuance-policy`</a>

##### <a name="ParametersservicePrincipalsCreateRefTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="servicePrincipalsCreateRefTokenLifetimePolicies">Command `az applications service-principal create-ref-token-lifetime-policy`</a>

##### <a name="ParametersservicePrincipalsCreateRefTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="servicePrincipalsCreateRefTransitiveMemberOf">Command `az applications service-principal create-ref-transitive-member-of`</a>

##### <a name="ParametersservicePrincipalsCreateRefTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="servicePrincipalsDeleteAppRoleAssignedTo">Command `az applications service-principal delete-app-role-assigned-to`</a>

##### <a name="ParametersservicePrincipalsDeleteAppRoleAssignedTo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="servicePrincipalsDeleteAppRoleAssignments">Command `az applications service-principal delete-app-role-assignment`</a>

##### <a name="ParametersservicePrincipalsDeleteAppRoleAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="servicePrincipalsDeleteEndpoints">Command `az applications service-principal delete-endpoint`</a>

##### <a name="ParametersservicePrincipalsDeleteEndpoints">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--endpoint-id**|string|key: id of endpoint|endpoint_id|endpoint-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="servicePrincipalsdelta">Command `az applications service-principal delta`</a>

##### <a name="ParametersservicePrincipalsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="servicePrincipalsgetAvailableExtensionProperties">Command `az applications service-principal get-available-extension-property`</a>

##### <a name="ParametersservicePrincipalsgetAvailableExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

#### <a name="servicePrincipalsgetByIds">Command `az applications service-principal get-by-id`</a>

##### <a name="ParametersservicePrincipalsgetByIds">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

#### <a name="servicePrincipalsgetMemberGroups">Command `az applications service-principal get-member-group`</a>

##### <a name="ParametersservicePrincipalsgetMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="servicePrincipalsgetMemberObjects">Command `az applications service-principal get-member-object`</a>

##### <a name="ParametersservicePrincipalsgetMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="servicePrincipalsListAppRoleAssignedTo">Command `az applications service-principal list-app-role-assigned-to`</a>

##### <a name="ParametersservicePrincipalsListAppRoleAssignedTo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListAppRoleAssignments">Command `az applications service-principal list-app-role-assignment`</a>

##### <a name="ParametersservicePrincipalsListAppRoleAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListClaimsMappingPolicies">Command `az applications service-principal list-claim-mapping-policy`</a>

##### <a name="ParametersservicePrincipalsListClaimsMappingPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListCreatedObjects">Command `az applications service-principal list-created-object`</a>

##### <a name="ParametersservicePrincipalsListCreatedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListEndpoints">Command `az applications service-principal list-endpoint`</a>

##### <a name="ParametersservicePrincipalsListEndpoints">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListHomeRealmDiscoveryPolicies">Command `az applications service-principal list-home-realm-discovery-policy`</a>

##### <a name="ParametersservicePrincipalsListHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListMemberOf">Command `az applications service-principal list-member-of`</a>

##### <a name="ParametersservicePrincipalsListMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListOauth2PermissionGrants">Command `az applications service-principal list-oauth2-permission-grant`</a>

##### <a name="ParametersservicePrincipalsListOauth2PermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListOwnedObjects">Command `az applications service-principal list-owned-object`</a>

##### <a name="ParametersservicePrincipalsListOwnedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListOwners">Command `az applications service-principal list-owner`</a>

##### <a name="ParametersservicePrincipalsListOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListRefClaimsMappingPolicies">Command `az applications service-principal list-ref-claim-mapping-policy`</a>

##### <a name="ParametersservicePrincipalsListRefClaimsMappingPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="servicePrincipalsListRefCreatedObjects">Command `az applications service-principal list-ref-created-object`</a>

##### <a name="ParametersservicePrincipalsListRefCreatedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="servicePrincipalsListRefHomeRealmDiscoveryPolicies">Command `az applications service-principal list-ref-home-realm-discovery-policy`</a>

##### <a name="ParametersservicePrincipalsListRefHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="servicePrincipalsListRefMemberOf">Command `az applications service-principal list-ref-member-of`</a>

##### <a name="ParametersservicePrincipalsListRefMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="servicePrincipalsListRefOauth2PermissionGrants">Command `az applications service-principal list-ref-oauth2-permission-grant`</a>

##### <a name="ParametersservicePrincipalsListRefOauth2PermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="servicePrincipalsListRefOwnedObjects">Command `az applications service-principal list-ref-owned-object`</a>

##### <a name="ParametersservicePrincipalsListRefOwnedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="servicePrincipalsListRefOwners">Command `az applications service-principal list-ref-owner`</a>

##### <a name="ParametersservicePrincipalsListRefOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="servicePrincipalsListRefTokenIssuancePolicies">Command `az applications service-principal list-ref-token-issuance-policy`</a>

##### <a name="ParametersservicePrincipalsListRefTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="servicePrincipalsListRefTokenLifetimePolicies">Command `az applications service-principal list-ref-token-lifetime-policy`</a>

##### <a name="ParametersservicePrincipalsListRefTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="servicePrincipalsListRefTransitiveMemberOf">Command `az applications service-principal list-ref-transitive-member-of`</a>

##### <a name="ParametersservicePrincipalsListRefTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="servicePrincipalsListTokenIssuancePolicies">Command `az applications service-principal list-token-issuance-policy`</a>

##### <a name="ParametersservicePrincipalsListTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListTokenLifetimePolicies">Command `az applications service-principal list-token-lifetime-policy`</a>

##### <a name="ParametersservicePrincipalsListTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsListTransitiveMemberOf">Command `az applications service-principal list-transitive-member-of`</a>

##### <a name="ParametersservicePrincipalsListTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsremoveKey">Command `az applications service-principal remove-key`</a>

##### <a name="ParametersservicePrincipalsremoveKey">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--key-id**|uuid||key_id|keyId|
|**--proof**|string||proof|proof|

#### <a name="servicePrincipalsremovePassword">Command `az applications service-principal remove-password`</a>

##### <a name="ParametersservicePrincipalsremovePassword">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--key-id**|uuid||key_id|keyId|

#### <a name="servicePrincipalsrestore">Command `az applications service-principal restore`</a>

##### <a name="ParametersservicePrincipalsrestore">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|

#### <a name="servicePrincipalsGetAppRoleAssignedTo">Command `az applications service-principal show-app-role-assigned-to`</a>

##### <a name="ParametersservicePrincipalsGetAppRoleAssignedTo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsGetAppRoleAssignments">Command `az applications service-principal show-app-role-assignment`</a>

##### <a name="ParametersservicePrincipalsGetAppRoleAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsGetEndpoints">Command `az applications service-principal show-endpoint`</a>

##### <a name="ParametersservicePrincipalsGetEndpoints">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--endpoint-id**|string|key: id of endpoint|endpoint_id|endpoint-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipalsUpdateAppRoleAssignedTo">Command `az applications service-principal update-app-role-assigned-to`</a>

##### <a name="ParametersservicePrincipalsUpdateAppRoleAssignedTo">Parameters</a> 
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

#### <a name="servicePrincipalsUpdateAppRoleAssignments">Command `az applications service-principal update-app-role-assignment`</a>

##### <a name="ParametersservicePrincipalsUpdateAppRoleAssignments">Parameters</a> 
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

#### <a name="servicePrincipalsUpdateEndpoints">Command `az applications service-principal update-endpoint`</a>

##### <a name="ParametersservicePrincipalsUpdateEndpoints">Parameters</a> 
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

#### <a name="servicePrincipalsvalidateProperties">Command `az applications service-principal validate-property`</a>

##### <a name="ParametersservicePrincipalsvalidateProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### group `az applications service-principal-service-principal`
#### <a name="servicePrincipals.servicePrincipalCreateServicePrincipal">Command `az applications service-principal-service-principal create-service-principal`</a>

##### <a name="ParametersservicePrincipals.servicePrincipalCreateServicePrincipal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--account-enabled**|boolean|true if the service principal account is enabled; otherwise, false.|account_enabled|accountEnabled|
|**--add-ins**|array|Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This will let services like Microsoft 365 call the application in the context of a document the user is working on.|add_ins|addIns|
|**--alternative-names**|array|Used to retrieve service principals by subscription, identify resource group and full resource ids for managed identities.|alternative_names|alternativeNames|
|**--app-description**|string||app_description|appDescription|
|**--app-display-name**|string|The display name exposed by the associated application.|app_display_name|appDisplayName|
|**--app-id**|string|The unique identifier for the associated application (its appId property).|app_id|appId|
|**--application-template-id**|string|Unique identifier of the applicationTemplate that the servicePrincipal was created from. Read-only.|application_template_id|applicationTemplateId|
|**--app-owner-organization-id**|uuid|Contains the tenant id where the application is registered. This is applicable only to service principals backed by applications.|app_owner_organization_id|appOwnerOrganizationId|
|**--app-role-assignment-required**|boolean|Specifies whether users or other service principals need to be granted an app role assignment for this service principal before users can sign in or apps can get tokens. The default value is false. Not nullable.|app_role_assignment_required|appRoleAssignmentRequired|
|**--app-roles**|array|The roles exposed by the application which this service principal represents. For more information see the appRoles property definition on the application entity. Not nullable.|app_roles|appRoles|
|**--description**|string||description|description|
|**--display-name**|string|The display name for the service principal.|display_name|displayName|
|**--homepage**|string|Home page or landing page of the application.|homepage|homepage|
|**--info**|object|informationalUrl|info|info|
|**--key-credentials**|array|The collection of key credentials associated with the service principal. Not nullable.|key_credentials|keyCredentials|
|**--login-url**|string|Specifies the URL where the service provider redirects the user to Azure AD to authenticate. Azure AD uses the URL to launch the application from Microsoft 365 or the Azure AD My Apps. When blank, Azure AD performs IdP-initiated sign-on for applications configured with SAML-based single sign-on. The user launches the application from Microsoft 365, the Azure AD My Apps, or the Azure AD SSO URL.|login_url|loginUrl|
|**--logout-url**|string|Specifies the URL that will be used by Microsoft's authorization service to logout an user using OpenId Connect front-channel, back-channel or SAML logout protocols.|logout_url|logoutUrl|
|**--notes**|string||notes|notes|
|**--notification-email-addresses**|array|Specifies the list of email addresses where Azure AD sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Azure AD Gallery applications.|notification_email_addresses|notificationEmailAddresses|
|**--oauth2-permission-scopes**|array|The delegated permissions exposed by the application. For more information see the oauth2PermissionScopes property on the application entity's api property. Not nullable.|oauth2_permission_scopes|oauth2PermissionScopes|
|**--password-credentials**|array|The collection of password credentials associated with the service principal. Not nullable.|password_credentials|passwordCredentials|
|**--preferred-single-sign-on-mode**|string|Specifies the single sign-on mode configured for this application. Azure AD uses the preferred single sign-on mode to launch the application from Microsoft 365 or the Azure AD My Apps. The supported values are password, saml, external, and oidc.|preferred_single_sign_on_mode|preferredSingleSignOnMode|
|**--preferred-token-signing-key-thumbprint**|string||preferred_token_signing_key_thumbprint|preferredTokenSigningKeyThumbprint|
|**--reply-urls**|array|The URLs that user tokens are sent to for sign in with the associated application, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to for the associated application. Not nullable.|reply_urls|replyUrls|
|**--service-principal-names**|array|Contains the list of identifiersUris, copied over from the associated application. Additional values can be added to hybrid applications. These values can be used to identify the permissions exposed by this app within Azure AD. For example,Client apps can specify a resource URI which is based on the values of this property to acquire an access token, which is the URI returned in the 'aud' claim.The any operator is required for filter expressions on multi-valued properties. Not nullable.|service_principal_names|servicePrincipalNames|
|**--service-principal-type**|string|Identifies if the service principal represents an application or a managed identity. This is set by Azure AD internally. For a service principal that represents an application this is set as Application. For a service principal that represent a managed identity this is set as ManagedIdentity.|service_principal_type|servicePrincipalType|
|**--tags**|array|Custom strings that can be used to categorize and identify the service principal. Not nullable.|tags|tags|
|**--token-encryption-key-id**|uuid|Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD issues tokens for this application encrypted using the key specified by this property. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.|token_encryption_key_id|tokenEncryptionKeyId|
|**--app-role-assigned-to**|array|Principals (users, groups, and service principals) that are assigned to this service principal. Read-only.|app_role_assigned_to|appRoleAssignedTo|
|**--app-role-assignments**|array|Applications that this service principal is assigned to. Read-only. Nullable.|app_role_assignments|appRoleAssignments|
|**--claims-mapping-policies**|array|The claimsMappingPolicies assigned to this service principal.|claims_mapping_policies|claimsMappingPolicies|
|**--created-objects**|array|Directory objects created by this service principal. Read-only. Nullable.|created_objects|createdObjects|
|**--endpoints**|array|Endpoints available for discovery. Services like Sharepoint populate this property with a tenant specific SharePoint endpoints that other applications can discover and use in their experiences.|endpoints|endpoints|
|**--home-realm-discovery-policies**|array|The homeRealmDiscoveryPolicies assigned to this service principal.|home_realm_discovery_policies|homeRealmDiscoveryPolicies|
|**--member-of**|array|Roles that this service principal is a member of. HTTP Methods: GET Read-only. Nullable.|member_of|memberOf|
|**--oauth2-permission-grants**|array|Delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. Read-only. Nullable.|oauth2_permission_grants|oauth2PermissionGrants|
|**--owned-objects**|array|Directory objects that are owned by this service principal. Read-only. Nullable.|owned_objects|ownedObjects|
|**--owners**|array|Directory objects that are owners of this servicePrincipal. The owners are a set of non-admin users or servicePrincipals who are allowed to modify this object. Read-only. Nullable.|owners|owners|
|**--token-issuance-policies**|array|The tokenIssuancePolicies assigned to this service principal.|token_issuance_policies|tokenIssuancePolicies|
|**--token-lifetime-policies**|array|The tokenLifetimePolicies assigned to this service principal.|token_lifetime_policies|tokenLifetimePolicies|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--relay-state**|string|The relative URI the service provider would redirect to after completion of the single sign-on flow.|relay_state|relayState|

#### <a name="servicePrincipals.servicePrincipalDeleteServicePrincipal">Command `az applications service-principal-service-principal delete-service-principal`</a>

##### <a name="ParametersservicePrincipals.servicePrincipalDeleteServicePrincipal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="servicePrincipals.servicePrincipalListServicePrincipal">Command `az applications service-principal-service-principal list-service-principal`</a>

##### <a name="ParametersservicePrincipals.servicePrincipalListServicePrincipal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipals.servicePrincipalGetServicePrincipal">Command `az applications service-principal-service-principal show-service-principal`</a>

##### <a name="ParametersservicePrincipals.servicePrincipalGetServicePrincipal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="servicePrincipals.servicePrincipalUpdateServicePrincipal">Command `az applications service-principal-service-principal update-service-principal`</a>

##### <a name="ParametersservicePrincipals.servicePrincipalUpdateServicePrincipal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--service-principal-id**|string|key: id of servicePrincipal|service_principal_id|servicePrincipal-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--account-enabled**|boolean|true if the service principal account is enabled; otherwise, false.|account_enabled|accountEnabled|
|**--add-ins**|array|Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This will let services like Microsoft 365 call the application in the context of a document the user is working on.|add_ins|addIns|
|**--alternative-names**|array|Used to retrieve service principals by subscription, identify resource group and full resource ids for managed identities.|alternative_names|alternativeNames|
|**--app-description**|string||app_description|appDescription|
|**--app-display-name**|string|The display name exposed by the associated application.|app_display_name|appDisplayName|
|**--app-id**|string|The unique identifier for the associated application (its appId property).|app_id|appId|
|**--application-template-id**|string|Unique identifier of the applicationTemplate that the servicePrincipal was created from. Read-only.|application_template_id|applicationTemplateId|
|**--app-owner-organization-id**|uuid|Contains the tenant id where the application is registered. This is applicable only to service principals backed by applications.|app_owner_organization_id|appOwnerOrganizationId|
|**--app-role-assignment-required**|boolean|Specifies whether users or other service principals need to be granted an app role assignment for this service principal before users can sign in or apps can get tokens. The default value is false. Not nullable.|app_role_assignment_required|appRoleAssignmentRequired|
|**--app-roles**|array|The roles exposed by the application which this service principal represents. For more information see the appRoles property definition on the application entity. Not nullable.|app_roles|appRoles|
|**--description**|string||description|description|
|**--display-name**|string|The display name for the service principal.|display_name|displayName|
|**--homepage**|string|Home page or landing page of the application.|homepage|homepage|
|**--info**|object|informationalUrl|info|info|
|**--key-credentials**|array|The collection of key credentials associated with the service principal. Not nullable.|key_credentials|keyCredentials|
|**--login-url**|string|Specifies the URL where the service provider redirects the user to Azure AD to authenticate. Azure AD uses the URL to launch the application from Microsoft 365 or the Azure AD My Apps. When blank, Azure AD performs IdP-initiated sign-on for applications configured with SAML-based single sign-on. The user launches the application from Microsoft 365, the Azure AD My Apps, or the Azure AD SSO URL.|login_url|loginUrl|
|**--logout-url**|string|Specifies the URL that will be used by Microsoft's authorization service to logout an user using OpenId Connect front-channel, back-channel or SAML logout protocols.|logout_url|logoutUrl|
|**--notes**|string||notes|notes|
|**--notification-email-addresses**|array|Specifies the list of email addresses where Azure AD sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Azure AD Gallery applications.|notification_email_addresses|notificationEmailAddresses|
|**--oauth2-permission-scopes**|array|The delegated permissions exposed by the application. For more information see the oauth2PermissionScopes property on the application entity's api property. Not nullable.|oauth2_permission_scopes|oauth2PermissionScopes|
|**--password-credentials**|array|The collection of password credentials associated with the service principal. Not nullable.|password_credentials|passwordCredentials|
|**--preferred-single-sign-on-mode**|string|Specifies the single sign-on mode configured for this application. Azure AD uses the preferred single sign-on mode to launch the application from Microsoft 365 or the Azure AD My Apps. The supported values are password, saml, external, and oidc.|preferred_single_sign_on_mode|preferredSingleSignOnMode|
|**--preferred-token-signing-key-thumbprint**|string||preferred_token_signing_key_thumbprint|preferredTokenSigningKeyThumbprint|
|**--reply-urls**|array|The URLs that user tokens are sent to for sign in with the associated application, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to for the associated application. Not nullable.|reply_urls|replyUrls|
|**--service-principal-names**|array|Contains the list of identifiersUris, copied over from the associated application. Additional values can be added to hybrid applications. These values can be used to identify the permissions exposed by this app within Azure AD. For example,Client apps can specify a resource URI which is based on the values of this property to acquire an access token, which is the URI returned in the 'aud' claim.The any operator is required for filter expressions on multi-valued properties. Not nullable.|service_principal_names|servicePrincipalNames|
|**--service-principal-type**|string|Identifies if the service principal represents an application or a managed identity. This is set by Azure AD internally. For a service principal that represents an application this is set as Application. For a service principal that represent a managed identity this is set as ManagedIdentity.|service_principal_type|servicePrincipalType|
|**--tags**|array|Custom strings that can be used to categorize and identify the service principal. Not nullable.|tags|tags|
|**--token-encryption-key-id**|uuid|Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD issues tokens for this application encrypted using the key specified by this property. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.|token_encryption_key_id|tokenEncryptionKeyId|
|**--app-role-assigned-to**|array|Principals (users, groups, and service principals) that are assigned to this service principal. Read-only.|app_role_assigned_to|appRoleAssignedTo|
|**--app-role-assignments**|array|Applications that this service principal is assigned to. Read-only. Nullable.|app_role_assignments|appRoleAssignments|
|**--claims-mapping-policies**|array|The claimsMappingPolicies assigned to this service principal.|claims_mapping_policies|claimsMappingPolicies|
|**--created-objects**|array|Directory objects created by this service principal. Read-only. Nullable.|created_objects|createdObjects|
|**--endpoints**|array|Endpoints available for discovery. Services like Sharepoint populate this property with a tenant specific SharePoint endpoints that other applications can discover and use in their experiences.|endpoints|endpoints|
|**--home-realm-discovery-policies**|array|The homeRealmDiscoveryPolicies assigned to this service principal.|home_realm_discovery_policies|homeRealmDiscoveryPolicies|
|**--member-of**|array|Roles that this service principal is a member of. HTTP Methods: GET Read-only. Nullable.|member_of|memberOf|
|**--oauth2-permission-grants**|array|Delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. Read-only. Nullable.|oauth2_permission_grants|oauth2PermissionGrants|
|**--owned-objects**|array|Directory objects that are owned by this service principal. Read-only. Nullable.|owned_objects|ownedObjects|
|**--owners**|array|Directory objects that are owners of this servicePrincipal. The owners are a set of non-admin users or servicePrincipals who are allowed to modify this object. Read-only. Nullable.|owners|owners|
|**--token-issuance-policies**|array|The tokenIssuancePolicies assigned to this service principal.|token_issuance_policies|tokenIssuancePolicies|
|**--token-lifetime-policies**|array|The tokenLifetimePolicies assigned to this service principal.|token_lifetime_policies|tokenLifetimePolicies|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--relay-state**|string|The relative URI the service provider would redirect to after completion of the single sign-on flow.|relay_state|relayState|

### group `az applications user`
#### <a name="usersCreateAppRoleAssignments">Command `az applications user create-app-role-assignment`</a>

##### <a name="ParametersusersCreateAppRoleAssignments">Parameters</a> 
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

#### <a name="usersDeleteAppRoleAssignments">Command `az applications user delete-app-role-assignment`</a>

##### <a name="ParametersusersDeleteAppRoleAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListAppRoleAssignments">Command `az applications user list-app-role-assignment`</a>

##### <a name="ParametersusersListAppRoleAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetAppRoleAssignments">Command `az applications user show-app-role-assignment`</a>

##### <a name="ParametersusersGetAppRoleAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--app-role-assignment-id**|string|key: id of appRoleAssignment|app_role_assignment_id|appRoleAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateAppRoleAssignments">Command `az applications user update-app-role-assignment`</a>

##### <a name="ParametersusersUpdateAppRoleAssignments">Parameters</a> 
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
