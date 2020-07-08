# Azure CLI Module Creation Report

### policies policy create-activity-based-timeout-policy

create-activity-based-timeout-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity-based-timeout-policy|CreateActivityBasedTimeoutPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

### policies policy create-claim-mapping-policy

create-claim-mapping-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-claim-mapping-policy|CreateClaimsMappingPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

### policies policy create-conditional-access-policy

create-conditional-access-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-conditional-access-policy|CreateConditionalAccessPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--modified-date-time**|date-time||modified_date_time|modifiedDateTime|
|**--display-name**|string||display_name|displayName|
|**--description**|string||description|description|
|**--state**|choice|conditionalAccessPolicyState|state|state|
|**--grant-controls**|object|conditionalAccessGrantControls|grant_controls|grantControls|
|**--session-controls-cloud-app-security**|object|cloudAppSecuritySessionControl|cloud_app_security|cloudAppSecurity|
|**--session-controls-sign-in-frequency**|object|signInFrequencySessionControl|sign_in_frequency|signInFrequency|
|**--session-controls-persistent-browser**|object|persistentBrowserSessionControl|persistent_browser|persistentBrowser|
|**--session-controls-application-enforced-restrictions-is-enabled**|boolean||is_enabled|isEnabled|
|**--conditions-applications**|object|conditionalAccessApplications|applications|applications|
|**--conditions-users**|object|conditionalAccessUsers|users|users|
|**--conditions-sign-in-risk-levels**|array||sign_in_risk_levels|signInRiskLevels|
|**--conditions-platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--conditions-locations**|object|conditionalAccessLocations|locations|locations|
|**--conditions-client-app-types**|array||client_app_types|clientAppTypes|
|**--conditions-device-states**|object|conditionalAccessDeviceStates|device_states|deviceStates|
|**--conditions-devices**|object|conditionalAccessDevices|devices|devices|

### policies policy create-home-realm-discovery-policy

create-home-realm-discovery-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-home-realm-discovery-policy|CreateHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

### policies policy create-token-issuance-policy

create-token-issuance-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-token-issuance-policy|CreateTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

### policies policy create-token-lifetime-policy

create-token-lifetime-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-token-lifetime-policy|CreateTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

### policies policy get-activity-based-timeout-policy

get-activity-based-timeout-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-based-timeout-policy|GetActivityBasedTimeoutPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--activity-based-timeout-policy-id**|string|key: activityBasedTimeoutPolicy-id of activityBasedTimeoutPolicy|activity_based_timeout_policy_id|activityBasedTimeoutPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy get-admin-consent-request-policy

get-admin-consent-request-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-admin-consent-request-policy|GetAdminConsentRequestPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy get-claim-mapping-policy

get-claim-mapping-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-claim-mapping-policy|GetClaimsMappingPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--claims-mapping-policy-id**|string|key: claimsMappingPolicy-id of claimsMappingPolicy|claims_mapping_policy_id|claimsMappingPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy get-conditional-access-policy

get-conditional-access-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-conditional-access-policy|GetConditionalAccessPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: conditionalAccessPolicy-id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy get-home-realm-discovery-policy

get-home-realm-discovery-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-home-realm-discovery-policy|GetHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--home-realm-discovery-policy-id**|string|key: homeRealmDiscoveryPolicy-id of homeRealmDiscoveryPolicy|home_realm_discovery_policy_id|homeRealmDiscoveryPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy get-identity-security-default-enforcement-policy

get-identity-security-default-enforcement-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-identity-security-default-enforcement-policy|GetIdentitySecurityDefaultsEnforcementPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy get-token-issuance-policy

get-token-issuance-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-token-issuance-policy|GetTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-issuance-policy-id**|string|key: tokenIssuancePolicy-id of tokenIssuancePolicy|token_issuance_policy_id|tokenIssuancePolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy get-token-lifetime-policy

get-token-lifetime-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-token-lifetime-policy|GetTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-lifetime-policy-id**|string|key: tokenLifetimePolicy-id of tokenLifetimePolicy|token_lifetime_policy_id|tokenLifetimePolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy list-activity-based-timeout-policy

list-activity-based-timeout-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity-based-timeout-policy|ListActivityBasedTimeoutPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy list-claim-mapping-policy

list-claim-mapping-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-claim-mapping-policy|ListClaimsMappingPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy list-conditional-access-policy

list-conditional-access-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-conditional-access-policy|ListConditionalAccessPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy list-home-realm-discovery-policy

list-home-realm-discovery-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-home-realm-discovery-policy|ListHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy list-token-issuance-policy

list-token-issuance-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-token-issuance-policy|ListTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy list-token-lifetime-policy

list-token-lifetime-policy a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-token-lifetime-policy|ListTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy update

update a policies policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateActivityBasedTimeoutPolicies|
|update|UpdateClaimsMappingPolicies|
|update|UpdateConditionalAccessPolicies|
|update|UpdateHomeRealmDiscoveryPolicies|
|update|UpdateTokenIssuancePolicies|
|update|UpdateTokenLifetimePolicies|
|update|UpdateAdminConsentRequestPolicy|
|update|UpdateIdentitySecurityDefaultsEnforcementPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--activity-based-timeout-policy-id**|string|key: activityBasedTimeoutPolicy-id of activityBasedTimeoutPolicy|activity_based_timeout_policy_id|activityBasedTimeoutPolicy-id|
|**--claims-mapping-policy-id**|string|key: claimsMappingPolicy-id of claimsMappingPolicy|claims_mapping_policy_id|claimsMappingPolicy-id|
|**--conditional-access-policy-id**|string|key: conditionalAccessPolicy-id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--home-realm-discovery-policy-id**|string|key: homeRealmDiscoveryPolicy-id of homeRealmDiscoveryPolicy|home_realm_discovery_policy_id|homeRealmDiscoveryPolicy-id|
|**--token-issuance-policy-id**|string|key: tokenIssuancePolicy-id of tokenIssuancePolicy|token_issuance_policy_id|tokenIssuancePolicy-id|
|**--token-lifetime-policy-id**|string|key: tokenLifetimePolicy-id of tokenLifetimePolicy|token_lifetime_policy_id|tokenLifetimePolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--modified-date-time**|date-time||modified_date_time|modifiedDateTime|
|**--state**|choice|conditionalAccessPolicyState|state|state|
|**--grant-controls**|object|conditionalAccessGrantControls|grant_controls|grantControls|
|**--session-controls-cloud-app-security**|object|cloudAppSecuritySessionControl|cloud_app_security|cloudAppSecurity|
|**--session-controls-sign-in-frequency**|object|signInFrequencySessionControl|sign_in_frequency|signInFrequency|
|**--session-controls-persistent-browser**|object|persistentBrowserSessionControl|persistent_browser|persistentBrowser|
|**--session-controls-application-enforced-restrictions-is-enabled**|boolean||is_enabled|isEnabled|
|**--conditions-applications**|object|conditionalAccessApplications|applications|applications|
|**--conditions-users**|object|conditionalAccessUsers|users|users|
|**--conditions-sign-in-risk-levels**|array||sign_in_risk_levels|signInRiskLevels|
|**--conditions-platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--conditions-locations**|object|conditionalAccessLocations|locations|locations|
|**--conditions-client-app-types**|array||client_app_types|clientAppTypes|
|**--conditions-device-states**|object|conditionalAccessDeviceStates|device_states|deviceStates|
|**--conditions-devices**|object|conditionalAccessDevices|devices|devices|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--version**|integer||version|version|
|**--notify-reviewers**|boolean||notify_reviewers|notifyReviewers|
|**--reminders-enabled**|boolean||reminders_enabled|remindersEnabled|
|**--request-duration-in-days**|integer||request_duration_in_days|requestDurationInDays|
|**--reviewers**|array||reviewers|reviewers|

### policies policy-policy-root get-policy-root

get-policy-root a policies policy-policy-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy-policy-root|policies.policyRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-policy-root|GetPolicyRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### policies policy-policy-root update

update a policies policy-policy-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|policies policy-policy-root|policies.policyRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePolicyRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-based-timeout-policies**|array||activity_based_timeout_policies|activityBasedTimeoutPolicies|
|**--claims-mapping-policies**|array||claims_mapping_policies|claimsMappingPolicies|
|**--home-realm-discovery-policies**|array||home_realm_discovery_policies|homeRealmDiscoveryPolicies|
|**--token-issuance-policies**|array||token_issuance_policies|tokenIssuancePolicies|
|**--token-lifetime-policies**|array||token_lifetime_policies|tokenLifetimePolicies|
|**--identity-security-defaults-enforcement-policy**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|identity_security_defaults_enforcement_policy|identitySecurityDefaultsEnforcementPolicy|
|**--conditional-access-policies**|array||conditional_access_policies|conditionalAccessPolicies|
|**--admin-consent-request-policy-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--admin-consent-request-policy-is-enabled**|boolean||is_enabled|isEnabled|
|**--admin-consent-request-policy-version**|integer||version|version|
|**--admin-consent-request-policy-notify-reviewers**|boolean||notify_reviewers|notifyReviewers|
|**--admin-consent-request-policy-reminders-enabled**|boolean||reminders_enabled|remindersEnabled|
|**--admin-consent-request-policy-request-duration-in-days**|integer||request_duration_in_days|requestDurationInDays|
|**--admin-consent-request-policy-reviewers**|array||reviewers|reviewers|
