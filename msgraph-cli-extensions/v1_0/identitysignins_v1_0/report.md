# Azure CLI Module Creation Report

### identitysignins create-activity-based-timeout-policy

create-activity-based-timeout-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins create-claim-mapping-policy

create-claim-mapping-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins create-conditional-access-policy

create-conditional-access-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-conditional-access-policy|CreateConditionalAccessPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string|Specifies a display name for the conditionalAccessPolicy object.|display_name|displayName|
|**--grant-controls**|object|conditionalAccessGrantControls|grant_controls|grantControls|
|**--modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|modified_date_time|modifiedDateTime|
|**--state**|choice||state|state|
|**--session-controls-application-enforced-restrictions**|object|applicationEnforcedRestrictionsSessionControl|application_enforced_restrictions|applicationEnforcedRestrictions|
|**--session-controls-cloud-app-security**|object|cloudAppSecuritySessionControl|cloud_app_security|cloudAppSecurity|
|**--session-controls-persistent-browser**|object|persistentBrowserSessionControl|persistent_browser|persistentBrowser|
|**--session-controls-sign-in-frequency**|object|signInFrequencySessionControl|sign_in_frequency|signInFrequency|
|**--conditions-applications**|object|conditionalAccessApplications|applications|applications|
|**--conditions-client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--conditions-locations**|object|conditionalAccessLocations|locations|locations|
|**--conditions-platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--conditions-sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--conditions-users**|object|conditionalAccessUsers|users|users|

### identitysignins create-data-policy-operation

create-data-policy-operation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|dataPolicyOperations.dataPolicyOperation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-data-policy-operation|CreateDataPolicyOperation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--completed-date-time**|date-time|Represents when the request for this data policy operation was completed, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Null until the operation completes.|completed_date_time|completedDateTime|
|**--progress**|number|Specifies the progress of an operation.|progress|progress|
|**--status**|choice||status|status|
|**--storage-location**|string|The URL location to where data is being exported for export requests.|storage_location|storageLocation|
|**--submitted-date-time**|date-time|Represents when the request for this data operation was submitted, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|submitted_date_time|submittedDateTime|
|**--user-id**|string|The id for the user on whom the operation is performed.|user_id|userId|

### identitysignins create-exclude

create-exclude a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.permissionGrantPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-exclude|CreateExcludes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--client-application-ids**|array||client_application_ids|clientApplicationIds|
|**--client-application-publisher-ids**|array||client_application_publisher_ids|clientApplicationPublisherIds|
|**--client-applications-from-verified-publisher-only**|boolean||client_applications_from_verified_publisher_only|clientApplicationsFromVerifiedPublisherOnly|
|**--client-application-tenant-ids**|array||client_application_tenant_ids|clientApplicationTenantIds|
|**--permission-classification**|string||permission_classification|permissionClassification|
|**--permissions**|array||permissions|permissions|
|**--permission-type**|choice||permission_type|permissionType|
|**--resource-application**|string||resource_application|resourceApplication|

### identitysignins create-home-realm-discovery-policy

create-home-realm-discovery-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins create-identity-provider

create-identity-provider a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identityProviders.identityProvider|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-identity-provider|CreateIdentityProvider|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string||client_id|clientId|
|**--client-secret**|string||client_secret|clientSecret|
|**--name**|string||name|name|
|**--type**|string||type|type|

### identitysignins create-include

create-include a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.permissionGrantPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-include|CreateIncludes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--client-application-ids**|array||client_application_ids|clientApplicationIds|
|**--client-application-publisher-ids**|array||client_application_publisher_ids|clientApplicationPublisherIds|
|**--client-applications-from-verified-publisher-only**|boolean||client_applications_from_verified_publisher_only|clientApplicationsFromVerifiedPublisherOnly|
|**--client-application-tenant-ids**|array||client_application_tenant_ids|clientApplicationTenantIds|
|**--permission-classification**|string||permission_classification|permissionClassification|
|**--permissions**|array||permissions|permissions|
|**--permission-type**|choice||permission_type|permissionType|
|**--resource-application**|string||resource_application|resourceApplication|

### identitysignins create-invitation

create-invitation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|invitations.invitation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-invitation|CreateInvitation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--invited-user-display-name**|string|The display name of the user being invited.|invited_user_display_name|invitedUserDisplayName|
|**--invited-user-email-address**|string|The email address of the user being invited. Required. The following special characters are not permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.|invited_user_email_address|invitedUserEmailAddress|
|**--invited-user-type**|string|The userType of the user being invited. By default, this is Guest. You can invite as Member if you are a company administrator.|invited_user_type|invitedUserType|
|**--invite-redeem-url**|string|The URL the user can use to redeem their invitation. Read-only|invite_redeem_url|inviteRedeemUrl|
|**--invite-redirect-url**|string|The URL the user should be redirected to once the invitation is redeemed. Required.|invite_redirect_url|inviteRedirectUrl|
|**--send-invitation-message**|boolean|Indicates whether an email should be sent to the user being invited or not. The default is false.|send_invitation_message|sendInvitationMessage|
|**--status**|string|The status of the invitation. Possible values: PendingAcceptance, Completed, InProgress, and Error|status|status|
|**--invited-user**|object|Represents an Azure Active Directory user object.|invited_user|invitedUser|
|**--invited-user-message-info-cc-recipients**|array|Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.|cc_recipients|ccRecipients|
|**--invited-user-message-info-customized-message-body**|string|Customized message body you want to send if you don't want the default message.|customized_message_body|customizedMessageBody|
|**--invited-user-message-info-message-language**|string|The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.|message_language|messageLanguage|

### identitysignins create-named-location

create-named-location a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity.conditionalAccess|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-named-location|CreateNamedLocations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents creation date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|Human-readable name of the location.|display_name|displayName|
|**--modified-date-time**|date-time|The Timestamp type represents last modified date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|modified_date_time|modifiedDateTime|

### identitysignins create-o-auth2-permission-grant

create-o-auth2-permission-grant a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|oauth2PermissionGrants.oAuth2PermissionGrant|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-o-auth2-permission-grant|CreateOAuth2PermissionGrant|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string|The id of the client service principal for the application which is authorized to act on behalf of a signed-in user when accessing an API. Required. Supports $filter (eq only).|client_id|clientId|
|**--consent-type**|string|Indicates if authorization is granted for the client application to impersonate all users or only a specific user. AllPrincipals indicates authorization to impersonate all users. Principal indicates authorization to impersonate a specific user. Consent on behalf of all users can be granted by an administrator. Non-admin users may be authorized to consent on behalf of themselves in some cases, for some delegated permissions. Required. Supports $filter (eq only).|consent_type|consentType|
|**--principal-id**|string|The id of the user on behalf of whom the client is authorized to access the resource, when consentType is Principal. If consentType is AllPrincipals this value is null. Required when consentType is Principal.|principal_id|principalId|
|**--resource-id**|string|The id of the resource service principal to which access is authorized. This identifies the API which the client is authorized to attempt to call on behalf of a signed-in user.|resource_id|resourceId|
|**--scope**|string|A space-separated list of the claim values for delegated permissions which should be included in access tokens for the resource application (the API). For example, openid User.Read GroupMember.Read.All. Each claim value should match the value field of one of the delegated permissions defined by the API, listed in the publishedPermissionScopes property of the resource service principal.|scope|scope|

### identitysignins create-permission-grant-policy

create-permission-grant-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-permission-grant-policy|CreatePermissionGrantPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--excludes**|array||excludes|excludes|
|**--includes**|array||includes|includes|

### identitysignins create-policy

create-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity.conditionalAccess|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-policy|CreatePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string|Specifies a display name for the conditionalAccessPolicy object.|display_name|displayName|
|**--grant-controls**|object|conditionalAccessGrantControls|grant_controls|grantControls|
|**--modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|modified_date_time|modifiedDateTime|
|**--state**|choice||state|state|
|**--session-controls-application-enforced-restrictions**|object|applicationEnforcedRestrictionsSessionControl|application_enforced_restrictions|applicationEnforcedRestrictions|
|**--session-controls-cloud-app-security**|object|cloudAppSecuritySessionControl|cloud_app_security|cloudAppSecurity|
|**--session-controls-persistent-browser**|object|persistentBrowserSessionControl|persistent_browser|persistentBrowser|
|**--session-controls-sign-in-frequency**|object|signInFrequencySessionControl|sign_in_frequency|signInFrequency|
|**--conditions-applications**|object|conditionalAccessApplications|applications|applications|
|**--conditions-client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--conditions-locations**|object|conditionalAccessLocations|locations|locations|
|**--conditions-platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--conditions-sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--conditions-users**|object|conditionalAccessUsers|users|users|

### identitysignins create-ref-certificate-based-auth-configuration

create-ref-certificate-based-auth-configuration a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-certificate-based-auth-configuration|CreateRefCertificateBasedAuthConfiguration|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitysignins create-result

create-result a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.threatAssessmentRequests|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-result|CreateResults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--message**|string|The result message for each threat assessment.|message|message|
|**--result-type**|choice||result_type|resultType|

### identitysignins create-threat-assessment-request

create-threat-assessment-request a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-threat-assessment-request|CreateThreatAssessmentRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--category**|choice||category|category|
|**--content-type**|choice||content_type|contentType|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--expected-assessment**|choice||expected_assessment|expectedAssessment|
|**--request-source**|choice||request_source|requestSource|
|**--status**|choice||status|status|
|**--results**|array|A collection of threat assessment results. Read-only. By default, a GET /threatAssessmentRequests/{id} does not return this property unless you apply $expand on it.|results|results|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### identitysignins create-token-issuance-policy

create-token-issuance-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins create-token-lifetime-policy

create-token-lifetime-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins delete

delete a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.permissionGrantPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExcludes|
|delete|DeleteIncludes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitysignins delta

delta a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|oauth2PermissionGrants|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### identitysignins get-activity-based-timeout-policy

get-activity-based-timeout-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-based-timeout-policy|GetActivityBasedTimeoutPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--activity-based-timeout-policy-id**|string|key: id of activityBasedTimeoutPolicy|activity_based_timeout_policy_id|activityBasedTimeoutPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-claim-mapping-policy

get-claim-mapping-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-claim-mapping-policy|GetClaimsMappingPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--claims-mapping-policy-id**|string|key: id of claimsMappingPolicy|claims_mapping_policy_id|claimsMappingPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-conditional-access

get-conditional-access a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-conditional-access|GetConditionalAccess|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-conditional-access-policy

get-conditional-access-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-conditional-access-policy|GetConditionalAccessPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-data-policy-operation

get-data-policy-operation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|dataPolicyOperations.dataPolicyOperation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-data-policy-operation|GetDataPolicyOperation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-policy-operation-id**|string|key: id of dataPolicyOperation|data_policy_operation_id|dataPolicyOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-exclude

get-exclude a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.permissionGrantPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-exclude|GetExcludes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-home-realm-discovery-policy

get-home-realm-discovery-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-home-realm-discovery-policy|GetHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--home-realm-discovery-policy-id**|string|key: id of homeRealmDiscoveryPolicy|home_realm_discovery_policy_id|homeRealmDiscoveryPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-identity-provider

get-identity-provider a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identityProviders.identityProvider|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-identity-provider|GetIdentityProvider|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: id of identityProvider|identity_provider_id|identityProvider-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-identity-security-default-enforcement-policy

get-identity-security-default-enforcement-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-identity-security-default-enforcement-policy|GetIdentitySecurityDefaultsEnforcementPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-include

get-include a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.permissionGrantPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-include|GetIncludes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-information-protection

get-information-protection a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-information-protection|GetInformationProtection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-invitation

get-invitation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|invitations.invitation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-invitation|GetInvitation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-invited-user

get-invited-user a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|invitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-invited-user|GetInvitedUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-named-location

get-named-location a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity.conditionalAccess|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-named-location|GetNamedLocations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--named-location-id**|string|key: id of namedLocation|named_location_id|namedLocation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-o-auth2-permission-grant

get-o-auth2-permission-grant a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|oauth2PermissionGrants.oAuth2PermissionGrant|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-o-auth2-permission-grant|GetOAuth2PermissionGrant|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--o-auth2-permission-grant-id**|string|key: id of oAuth2PermissionGrant|o_auth2_permission_grant_id|oAuth2PermissionGrant-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-permission-grant-policy

get-permission-grant-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission-grant-policy|GetPermissionGrantPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-policy

get-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity.conditionalAccess|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-policy|GetPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-policy-root

get-policy-root a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.policyRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-policy-root|GetPolicyRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-ref-invited-user

get-ref-invited-user a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|invitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-invited-user|GetRefInvitedUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|

### identitysignins get-result

get-result a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.threatAssessmentRequests|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-result|GetResults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--threat-assessment-result-id**|string|key: id of threatAssessmentResult|threat_assessment_result_id|threatAssessmentResult-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-threat-assessment-request

get-threat-assessment-request a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-threat-assessment-request|GetThreatAssessmentRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-token-issuance-policy

get-token-issuance-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-token-issuance-policy|GetTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-issuance-policy-id**|string|key: id of tokenIssuancePolicy|token_issuance_policy_id|tokenIssuancePolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-token-lifetime-policy

get-token-lifetime-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-token-lifetime-policy|GetTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-lifetime-policy-id**|string|key: id of tokenLifetimePolicy|token_lifetime_policy_id|tokenLifetimePolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-activity-based-timeout-policy

list-activity-based-timeout-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins list-certificate-based-auth-configuration

list-certificate-based-auth-configuration a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-certificate-based-auth-configuration|ListCertificateBasedAuthConfiguration|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-claim-mapping-policy

list-claim-mapping-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins list-conditional-access-policy

list-conditional-access-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins list-data-policy-operation

list-data-policy-operation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|dataPolicyOperations.dataPolicyOperation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-data-policy-operation|ListDataPolicyOperation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-exclude

list-exclude a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.permissionGrantPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-exclude|ListExcludes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-home-realm-discovery-policy

list-home-realm-discovery-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins list-identity-provider

list-identity-provider a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identityProviders.identityProvider|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-identity-provider|ListIdentityProvider|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-include

list-include a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.permissionGrantPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-include|ListIncludes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-invitation

list-invitation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|invitations.invitation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-invitation|ListInvitation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-named-location

list-named-location a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity.conditionalAccess|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-named-location|ListNamedLocations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-o-auth2-permission-grant

list-o-auth2-permission-grant a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|oauth2PermissionGrants.oAuth2PermissionGrant|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-o-auth2-permission-grant|ListOAuth2PermissionGrant|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-permission-grant-policy

list-permission-grant-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-permission-grant-policy|ListPermissionGrantPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-policy

list-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity.conditionalAccess|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-policy|ListPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-ref-certificate-based-auth-configuration

list-ref-certificate-based-auth-configuration a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-certificate-based-auth-configuration|ListRefCertificateBasedAuthConfiguration|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitysignins list-result

list-result a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.threatAssessmentRequests|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-result|ListResults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-threat-assessment-request

list-threat-assessment-request a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-threat-assessment-request|ListThreatAssessmentRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-token-issuance-policy

list-token-issuance-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins list-token-lifetime-policy

list-token-lifetime-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

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

### identitysignins set-ref-invited-user

set-ref-invited-user a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|invitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-invited-user|SetRefInvitedUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### identitysignins update-activity-based-timeout-policy

update-activity-based-timeout-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-activity-based-timeout-policy|UpdateActivityBasedTimeoutPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--activity-based-timeout-policy-id**|string|key: id of activityBasedTimeoutPolicy|activity_based_timeout_policy_id|activityBasedTimeoutPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

### identitysignins update-claim-mapping-policy

update-claim-mapping-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-claim-mapping-policy|UpdateClaimsMappingPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--claims-mapping-policy-id**|string|key: id of claimsMappingPolicy|claims_mapping_policy_id|claimsMappingPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

### identitysignins update-conditional-access

update-conditional-access a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-conditional-access|UpdateConditionalAccess|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--named-locations**|array||named_locations|namedLocations|
|**--policies**|array||policies|policies|

### identitysignins update-conditional-access-policy

update-conditional-access-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-conditional-access-policy|UpdateConditionalAccessPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string|Specifies a display name for the conditionalAccessPolicy object.|display_name|displayName|
|**--grant-controls**|object|conditionalAccessGrantControls|grant_controls|grantControls|
|**--modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|modified_date_time|modifiedDateTime|
|**--state**|choice||state|state|
|**--session-controls-application-enforced-restrictions**|object|applicationEnforcedRestrictionsSessionControl|application_enforced_restrictions|applicationEnforcedRestrictions|
|**--session-controls-cloud-app-security**|object|cloudAppSecuritySessionControl|cloud_app_security|cloudAppSecurity|
|**--session-controls-persistent-browser**|object|persistentBrowserSessionControl|persistent_browser|persistentBrowser|
|**--session-controls-sign-in-frequency**|object|signInFrequencySessionControl|sign_in_frequency|signInFrequency|
|**--conditions-applications**|object|conditionalAccessApplications|applications|applications|
|**--conditions-client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--conditions-locations**|object|conditionalAccessLocations|locations|locations|
|**--conditions-platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--conditions-sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--conditions-users**|object|conditionalAccessUsers|users|users|

### identitysignins update-data-policy-operation

update-data-policy-operation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|dataPolicyOperations.dataPolicyOperation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-data-policy-operation|UpdateDataPolicyOperation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-policy-operation-id**|string|key: id of dataPolicyOperation|data_policy_operation_id|dataPolicyOperation-id|
|**--id**|string|Read-only.|id|id|
|**--completed-date-time**|date-time|Represents when the request for this data policy operation was completed, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Null until the operation completes.|completed_date_time|completedDateTime|
|**--progress**|number|Specifies the progress of an operation.|progress|progress|
|**--status**|choice||status|status|
|**--storage-location**|string|The URL location to where data is being exported for export requests.|storage_location|storageLocation|
|**--submitted-date-time**|date-time|Represents when the request for this data operation was submitted, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|submitted_date_time|submittedDateTime|
|**--user-id**|string|The id for the user on whom the operation is performed.|user_id|userId|

### identitysignins update-exclude

update-exclude a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.permissionGrantPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-exclude|UpdateExcludes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--id**|string|Read-only.|id|id|
|**--client-application-ids**|array||client_application_ids|clientApplicationIds|
|**--client-application-publisher-ids**|array||client_application_publisher_ids|clientApplicationPublisherIds|
|**--client-applications-from-verified-publisher-only**|boolean||client_applications_from_verified_publisher_only|clientApplicationsFromVerifiedPublisherOnly|
|**--client-application-tenant-ids**|array||client_application_tenant_ids|clientApplicationTenantIds|
|**--permission-classification**|string||permission_classification|permissionClassification|
|**--permissions**|array||permissions|permissions|
|**--permission-type**|choice||permission_type|permissionType|
|**--resource-application**|string||resource_application|resourceApplication|

### identitysignins update-home-realm-discovery-policy

update-home-realm-discovery-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-home-realm-discovery-policy|UpdateHomeRealmDiscoveryPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--home-realm-discovery-policy-id**|string|key: id of homeRealmDiscoveryPolicy|home_realm_discovery_policy_id|homeRealmDiscoveryPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

### identitysignins update-identity-provider

update-identity-provider a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identityProviders.identityProvider|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-identity-provider|UpdateIdentityProvider|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: id of identityProvider|identity_provider_id|identityProvider-id|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string||client_id|clientId|
|**--client-secret**|string||client_secret|clientSecret|
|**--name**|string||name|name|
|**--type**|string||type|type|

### identitysignins update-identity-security-default-enforcement-policy

update-identity-security-default-enforcement-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-identity-security-default-enforcement-policy|UpdateIdentitySecurityDefaultsEnforcementPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--is-enabled**|boolean|If set to true, Azure Active Directory security defaults is enabled for the tenant.|is_enabled|isEnabled|

### identitysignins update-include

update-include a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.permissionGrantPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-include|UpdateIncludes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--id**|string|Read-only.|id|id|
|**--client-application-ids**|array||client_application_ids|clientApplicationIds|
|**--client-application-publisher-ids**|array||client_application_publisher_ids|clientApplicationPublisherIds|
|**--client-applications-from-verified-publisher-only**|boolean||client_applications_from_verified_publisher_only|clientApplicationsFromVerifiedPublisherOnly|
|**--client-application-tenant-ids**|array||client_application_tenant_ids|clientApplicationTenantIds|
|**--permission-classification**|string||permission_classification|permissionClassification|
|**--permissions**|array||permissions|permissions|
|**--permission-type**|choice||permission_type|permissionType|
|**--resource-application**|string||resource_application|resourceApplication|

### identitysignins update-information-protection

update-information-protection a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-information-protection|UpdateInformationProtection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--threat-assessment-requests**|array||threat_assessment_requests|threatAssessmentRequests|

### identitysignins update-invitation

update-invitation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|invitations.invitation|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-invitation|UpdateInvitation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--id**|string|Read-only.|id|id|
|**--invited-user-display-name**|string|The display name of the user being invited.|invited_user_display_name|invitedUserDisplayName|
|**--invited-user-email-address**|string|The email address of the user being invited. Required. The following special characters are not permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.|invited_user_email_address|invitedUserEmailAddress|
|**--invited-user-type**|string|The userType of the user being invited. By default, this is Guest. You can invite as Member if you are a company administrator.|invited_user_type|invitedUserType|
|**--invite-redeem-url**|string|The URL the user can use to redeem their invitation. Read-only|invite_redeem_url|inviteRedeemUrl|
|**--invite-redirect-url**|string|The URL the user should be redirected to once the invitation is redeemed. Required.|invite_redirect_url|inviteRedirectUrl|
|**--send-invitation-message**|boolean|Indicates whether an email should be sent to the user being invited or not. The default is false.|send_invitation_message|sendInvitationMessage|
|**--status**|string|The status of the invitation. Possible values: PendingAcceptance, Completed, InProgress, and Error|status|status|
|**--invited-user**|object|Represents an Azure Active Directory user object.|invited_user|invitedUser|
|**--invited-user-message-info-cc-recipients**|array|Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.|cc_recipients|ccRecipients|
|**--invited-user-message-info-customized-message-body**|string|Customized message body you want to send if you don't want the default message.|customized_message_body|customizedMessageBody|
|**--invited-user-message-info-message-language**|string|The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.|message_language|messageLanguage|

### identitysignins update-named-location

update-named-location a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity.conditionalAccess|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-named-location|UpdateNamedLocations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--named-location-id**|string|key: id of namedLocation|named_location_id|namedLocation-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents creation date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|Human-readable name of the location.|display_name|displayName|
|**--modified-date-time**|date-time|The Timestamp type represents last modified date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|modified_date_time|modifiedDateTime|

### identitysignins update-o-auth2-permission-grant

update-o-auth2-permission-grant a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|oauth2PermissionGrants.oAuth2PermissionGrant|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-o-auth2-permission-grant|UpdateOAuth2PermissionGrant|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--o-auth2-permission-grant-id**|string|key: id of oAuth2PermissionGrant|o_auth2_permission_grant_id|oAuth2PermissionGrant-id|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string|The id of the client service principal for the application which is authorized to act on behalf of a signed-in user when accessing an API. Required. Supports $filter (eq only).|client_id|clientId|
|**--consent-type**|string|Indicates if authorization is granted for the client application to impersonate all users or only a specific user. AllPrincipals indicates authorization to impersonate all users. Principal indicates authorization to impersonate a specific user. Consent on behalf of all users can be granted by an administrator. Non-admin users may be authorized to consent on behalf of themselves in some cases, for some delegated permissions. Required. Supports $filter (eq only).|consent_type|consentType|
|**--principal-id**|string|The id of the user on behalf of whom the client is authorized to access the resource, when consentType is Principal. If consentType is AllPrincipals this value is null. Required when consentType is Principal.|principal_id|principalId|
|**--resource-id**|string|The id of the resource service principal to which access is authorized. This identifies the API which the client is authorized to attempt to call on behalf of a signed-in user.|resource_id|resourceId|
|**--scope**|string|A space-separated list of the claim values for delegated permissions which should be included in access tokens for the resource application (the API). For example, openid User.Read GroupMember.Read.All. Each claim value should match the value field of one of the delegated permissions defined by the API, listed in the publishedPermissionScopes property of the resource service principal.|scope|scope|

### identitysignins update-permission-grant-policy

update-permission-grant-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-permission-grant-policy|UpdatePermissionGrantPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--excludes**|array||excludes|excludes|
|**--includes**|array||includes|includes|

### identitysignins update-policy

update-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity.conditionalAccess|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-policy|UpdatePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string|Specifies a display name for the conditionalAccessPolicy object.|display_name|displayName|
|**--grant-controls**|object|conditionalAccessGrantControls|grant_controls|grantControls|
|**--modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|modified_date_time|modifiedDateTime|
|**--state**|choice||state|state|
|**--session-controls-application-enforced-restrictions**|object|applicationEnforcedRestrictionsSessionControl|application_enforced_restrictions|applicationEnforcedRestrictions|
|**--session-controls-cloud-app-security**|object|cloudAppSecuritySessionControl|cloud_app_security|cloudAppSecurity|
|**--session-controls-persistent-browser**|object|persistentBrowserSessionControl|persistent_browser|persistentBrowser|
|**--session-controls-sign-in-frequency**|object|signInFrequencySessionControl|sign_in_frequency|signInFrequency|
|**--conditions-applications**|object|conditionalAccessApplications|applications|applications|
|**--conditions-client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--conditions-locations**|object|conditionalAccessLocations|locations|locations|
|**--conditions-platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--conditions-sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--conditions-users**|object|conditionalAccessUsers|users|users|

### identitysignins update-policy-root

update-policy-root a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies.policyRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-policy-root|UpdatePolicyRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-based-timeout-policies**|array||activity_based_timeout_policies|activityBasedTimeoutPolicies|
|**--claims-mapping-policies**|array||claims_mapping_policies|claimsMappingPolicies|
|**--home-realm-discovery-policies**|array||home_realm_discovery_policies|homeRealmDiscoveryPolicies|
|**--permission-grant-policies**|array||permission_grant_policies|permissionGrantPolicies|
|**--token-issuance-policies**|array||token_issuance_policies|tokenIssuancePolicies|
|**--token-lifetime-policies**|array||token_lifetime_policies|tokenLifetimePolicies|
|**--conditional-access-policies**|array||conditional_access_policies|conditionalAccessPolicies|
|**--identity-security-defaults-enforcement-policy**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|identity_security_defaults_enforcement_policy|identitySecurityDefaultsEnforcementPolicy|

### identitysignins update-result

update-result a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.threatAssessmentRequests|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-result|UpdateResults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--threat-assessment-result-id**|string|key: id of threatAssessmentResult|threat_assessment_result_id|threatAssessmentResult-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--message**|string|The result message for each threat assessment.|message|message|
|**--result-type**|choice||result_type|resultType|

### identitysignins update-threat-assessment-request

update-threat-assessment-request a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-threat-assessment-request|UpdateThreatAssessmentRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--id**|string|Read-only.|id|id|
|**--category**|choice||category|category|
|**--content-type**|choice||content_type|contentType|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--expected-assessment**|choice||expected_assessment|expectedAssessment|
|**--request-source**|choice||request_source|requestSource|
|**--status**|choice||status|status|
|**--results**|array|A collection of threat assessment results. Read-only. By default, a GET /threatAssessmentRequests/{id} does not return this property unless you apply $expand on it.|results|results|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### identitysignins update-token-issuance-policy

update-token-issuance-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-token-issuance-policy|UpdateTokenIssuancePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-issuance-policy-id**|string|key: id of tokenIssuancePolicy|token_issuance_policy_id|tokenIssuancePolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

### identitysignins update-token-lifetime-policy

update-token-lifetime-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-token-lifetime-policy|UpdateTokenLifetimePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-lifetime-policy-id**|string|key: id of tokenLifetimePolicy|token_lifetime_policy_id|tokenLifetimePolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|
