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
|**--web-home-page-url**|string|Home page or landing page of the application.|home_page_url|homePageUrl|
|**--web-implicit-grant-settings**|object|implicitGrantSettings|implicit_grant_settings|implicitGrantSettings|
|**--web-logout-url**|string|Specifies the URL that will be used by Microsoft's authorization service to logout an user using front-channel, back-channel or SAML logout protocols.|logout_url|logoutUrl|
|**--web-redirect-uris**|array|Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.|redirect_uris|redirectUris|
|**--optional-claims-access-token**|array|The optional claims returned in the JWT access token.|access_token|accessToken|
|**--optional-claims-id-token**|array|The optional claims returned in the JWT ID token.|id_token|idToken|
|**--optional-claims-saml2token**|array|The optional claims returned in the SAML token.|saml2_token|saml2Token|
|**--api-accept-mapped-claims**|boolean|When true, allows an application to use claims mapping without specifying a custom signing key.|accept_mapped_claims|acceptMappedClaims|
|**--api-known-client-applications**|array|Used for bundling consent if you have a solution that contains two parts: a client app and a custom web API app. If you set the appID of the client app to this value, the user only consents once to the client app. Azure AD knows that consenting to the client means implicitly consenting to the web API and automatically provisions service principals for both APIs at the same time. Both the client and the web API app must be registered in the same tenant.|known_client_applications|knownClientApplications|
|**--api-oauth2permission-scopes**|array|The definition of the delegated permissions exposed by the web API represented by this application registration. These delegated permissions may be requested by a client application, and may be granted by users or administrators during consent. Delegated permissions are sometimes referred to as OAuth 2.0 scopes.|oauth2_permission_scopes|oauth2PermissionScopes|
|**--api-pre-authorized-applications**|array|Lists the client applications that are pre-authorized with the specified delegated permissions to access this application's APIs. Users are not required to consent to any pre-authorized application (for the permissions specified). However, any additional permissions not listed in preAuthorizedApplications (requested through incremental consent for example) will require user consent.|pre_authorized_applications|preAuthorizedApplications|
|**--api-requested-access-token-version**|integer|Specifies the access token version expected by this resource. This changes the version and format of the JWT produced independent of the endpoint or client used to request the access token.  The endpoint used, v1.0 or v2.0, is chosen by the client and only impacts the version of id_tokens. Resources need to explicitly configure requestedAccessTokenVersion to indicate the supported access token format.  Possible values for requestedAccessTokenVersion are 1, 2, or null. If the value is null, this defaults to 1, which corresponds to the v1.0 endpoint.  If signInAudience on the application is configured as AzureADandPersonalMicrosoftAccount, the value for this property must be 2|requested_access_token_version|requestedAccessTokenVersion|

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
|**--web-home-page-url**|string|Home page or landing page of the application.|home_page_url|homePageUrl|
|**--web-implicit-grant-settings**|object|implicitGrantSettings|implicit_grant_settings|implicitGrantSettings|
|**--web-logout-url**|string|Specifies the URL that will be used by Microsoft's authorization service to logout an user using front-channel, back-channel or SAML logout protocols.|logout_url|logoutUrl|
|**--web-redirect-uris**|array|Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.|redirect_uris|redirectUris|
|**--optional-claims-access-token**|array|The optional claims returned in the JWT access token.|access_token|accessToken|
|**--optional-claims-id-token**|array|The optional claims returned in the JWT ID token.|id_token|idToken|
|**--optional-claims-saml2token**|array|The optional claims returned in the SAML token.|saml2_token|saml2Token|
|**--api-accept-mapped-claims**|boolean|When true, allows an application to use claims mapping without specifying a custom signing key.|accept_mapped_claims|acceptMappedClaims|
|**--api-known-client-applications**|array|Used for bundling consent if you have a solution that contains two parts: a client app and a custom web API app. If you set the appID of the client app to this value, the user only consents once to the client app. Azure AD knows that consenting to the client means implicitly consenting to the web API and automatically provisions service principals for both APIs at the same time. Both the client and the web API app must be registered in the same tenant.|known_client_applications|knownClientApplications|
|**--api-oauth2permission-scopes**|array|The definition of the delegated permissions exposed by the web API represented by this application registration. These delegated permissions may be requested by a client application, and may be granted by users or administrators during consent. Delegated permissions are sometimes referred to as OAuth 2.0 scopes.|oauth2_permission_scopes|oauth2PermissionScopes|
|**--api-pre-authorized-applications**|array|Lists the client applications that are pre-authorized with the specified delegated permissions to access this application's APIs. Users are not required to consent to any pre-authorized application (for the permissions specified). However, any additional permissions not listed in preAuthorizedApplications (requested through incremental consent for example) will require user consent.|pre_authorized_applications|preAuthorizedApplications|
|**--api-requested-access-token-version**|integer|Specifies the access token version expected by this resource. This changes the version and format of the JWT produced independent of the endpoint or client used to request the access token.  The endpoint used, v1.0 or v2.0, is chosen by the client and only impacts the version of id_tokens. Resources need to explicitly configure requestedAccessTokenVersion to indicate the supported access token format.  Possible values for requestedAccessTokenVersion are 1, 2, or null. If the value is null, this defaults to 1, which corresponds to the v1.0 endpoint.  If signInAudience on the application is configured as AzureADandPersonalMicrosoftAccount, the value for this property must be 2|requested_access_token_version|requestedAccessTokenVersion|

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
|**--saml-single-sign-on-settings-relay-state**|string|The relative URI the service provider would redirect to after completion of the single sign-on flow.|relay_state|relayState|

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
|**--saml-single-sign-on-settings-relay-state**|string|The relative URI the service provider would redirect to after completion of the single sign-on flow.|relay_state|relayState|

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
