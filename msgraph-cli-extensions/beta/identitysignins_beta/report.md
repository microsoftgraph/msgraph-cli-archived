# Azure CLI Module Creation Report

### identitysignins available-provider-type

available-provider-type a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identityProviders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|available-provider-type|availableProviderTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### identitysignins confirm-compromised

confirm-compromised a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|confirm-compromised|confirmCompromised|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-ids**|array||user_ids|userIds|

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

### identitysignins create-authorization-policy

create-authorization-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-authorization-policy|CreateAuthorizationPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--allowed-to-sign-up-email-based-subscriptions**|boolean||allowed_to_sign_up_email_based_subscriptions|allowedToSignUpEmailBasedSubscriptions|
|**--allowed-to-use-sspr**|boolean||allowed_to_use_sspr|allowedToUseSSPR|
|**--allow-email-verified-users-to-join-organization**|boolean||allow_email_verified_users_to_join_organization|allowEmailVerifiedUsersToJoinOrganization|
|**--allow-invites-from**|choice||allow_invites_from|allowInvitesFrom|
|**--block-msol-power-shell**|boolean||block_msol_power_shell|blockMsolPowerShell|
|**--default-user-role-permissions**|object|defaultUserRolePermissions|default_user_role_permissions|defaultUserRolePermissions|
|**--enabled-preview-features**|array||enabled_preview_features|enabledPreviewFeatures|
|**--guest-user-role-id**|uuid||guest_user_role_id|guestUserRoleId|
|**--permission-grant-policy-ids-assigned-to-default-user-role**|array||permission_grant_policy_ids_assigned_to_default_user_role|permissionGrantPolicyIdsAssignedToDefaultUserRole|

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
|**--conditions-client-applications**|object|conditionalAccessClientApplications|client_applications|clientApplications|
|**--conditions-client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--conditions-devices**|object|conditionalAccessDevices|devices|devices|
|**--conditions-device-states**|object|conditionalAccessDeviceStates|device_states|deviceStates|
|**--conditions-locations**|object|conditionalAccessLocations|locations|locations|
|**--conditions-platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--conditions-sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--conditions-user-risk-levels**|array||user_risk_levels|userRiskLevels|
|**--conditions-users**|object|conditionalAccessUsers|users|users|

### identitysignins create-data-loss-prevention-policy

create-data-loss-prevention-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-data-loss-prevention-policy|CreateDataLossPreventionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--name**|string||name|name|

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

### identitysignins create-email-method

create-email-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-email-method|CreateEmailMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

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

### identitysignins create-fido2-method

create-fido2-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-fido2-method|CreateFido2Methods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

### identitysignins create-history

create-history a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-history|CreateHistory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean|Indicates whether the user is deleted. Possible values are: true, false|is_deleted|isDeleted|
|**--is-processing**|boolean|Indicates wehther a user's risky state is being processed by the backend|is_processing|isProcessing|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-last-updated-date-time**|date-time|The date and time that the risky user was last updated.|risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--user-display-name**|string|Risky user display name.|user_display_name|userDisplayName|
|**--user-principal-name**|string|Risky user principal name.|user_principal_name|userPrincipalName|
|**--history**|array|The activity related to user risk level change|history|history|
|**--activity**|object|riskUserActivity|activity|activity|
|**--initiated-by**|string|The id of actor that does the operation.|initiated_by|initiatedBy|
|**--user-id**|string|The id of the user.|user_id|userId|

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
|**--reset-redemption**|boolean||reset_redemption|resetRedemption|
|**--send-invitation-message**|boolean|Indicates whether an email should be sent to the user being invited or not. The default is false.|send_invitation_message|sendInvitationMessage|
|**--status**|string|The status of the invitation. Possible values: PendingAcceptance, Completed, InProgress, and Error|status|status|
|**--invited-user**|object|Represents an Azure Active Directory user object.|invited_user|invitedUser|
|**--invited-user-message-info-cc-recipients**|array|Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.|cc_recipients|ccRecipients|
|**--invited-user-message-info-customized-message-body**|string|Customized message body you want to send if you don't want the default message.|customized_message_body|customizedMessageBody|
|**--invited-user-message-info-message-language**|string|The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.|message_language|messageLanguage|

### identitysignins create-key-set

create-key-set a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-key-set|CreateKeySets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--keys**|array||keys|keys|

### identitysignins create-label

create-label a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.policy|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-label|CreateLabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--color**|string||color|color|
|**--description**|string||description|description|
|**--is-active**|boolean||is_active|isActive|
|**--name**|string||name|name|
|**--parent**|object|parentLabelDetails|parent|parent|
|**--sensitivity**|integer||sensitivity|sensitivity|
|**--tooltip**|string||tooltip|tooltip|

### identitysignins create-method

create-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-method|CreateMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

### identitysignins create-microsoft-authenticator-method

create-microsoft-authenticator-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-microsoft-authenticator-method|CreateMicrosoftAuthenticatorMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

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
|**--expiry-time**|date-time||expiry_time|expiryTime|
|**--principal-id**|string|The id of the user on behalf of whom the client is authorized to access the resource, when consentType is Principal. If consentType is AllPrincipals this value is null. Required when consentType is Principal.|principal_id|principalId|
|**--resource-id**|string|The id of the resource service principal to which access is authorized. This identifies the API which the client is authorized to attempt to call on behalf of a signed-in user.|resource_id|resourceId|
|**--scope**|string|A space-separated list of the claim values for delegated permissions which should be included in access tokens for the resource application (the API). For example, openid User.Read GroupMember.Read.All. Each claim value should match the value field of one of the delegated permissions defined by the API, listed in the publishedPermissionScopes property of the resource service principal.|scope|scope|
|**--start-time**|date-time||start_time|startTime|

### identitysignins create-oath-method

create-oath-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-oath-method|CreateOathMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

### identitysignins create-operation

create-operation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-operation|CreateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-action-date-time**|date-time||last_action_date_time|lastActionDateTime|
|**--resource-location**|string||resource_location|resourceLocation|
|**--status**|choice||status|status|
|**--status-detail**|string||status_detail|statusDetail|

### identitysignins create-password-method

create-password-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-password-method|CreatePasswordMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--creation-date-time**|date-time||creation_date_time|creationDateTime|
|**--password**|string||password|password|

### identitysignins create-passwordless-microsoft-authenticator-method

create-passwordless-microsoft-authenticator-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-passwordless-microsoft-authenticator-method|CreatePasswordlessMicrosoftAuthenticatorMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

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

### identitysignins create-phone-method

create-phone-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-phone-method|CreatePhoneMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--phone-number**|string||phone_number|phoneNumber|
|**--phone-type**|choice||phone_type|phoneType|
|**--sms-sign-in-state**|choice||sms_sign_in_state|smsSignInState|

### identitysignins create-policy

create-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-policy|CreatePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|

### identitysignins create-private-link-resource-policy

create-private-link-resource-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-private-link-resource-policy|CreatePrivateLinkResourcePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--allowed-tenant-ids**|array||allowed_tenant_ids|allowedTenantIds|
|**--arm-resource-id**|string||arm_resource_id|armResourceId|

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

### identitysignins create-risk-detection

create-risk-detection a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskDetections.riskDetection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-risk-detection|CreateRiskDetection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity**|choice||activity|activity|
|**--activity-date-time**|date-time|Date and time that the risky activity occurred.|activity_date_time|activityDateTime|
|**--additional-info**|string|Additional information associated with the risk detection in JSON format.|additional_info|additionalInfo|
|**--correlation-id**|string|Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.|correlation_id|correlationId|
|**--detected-date-time**|date-time|Date and time that the risk was detected.|detected_date_time|detectedDateTime|
|**--detection-timing-type**|choice||detection_timing_type|detectionTimingType|
|**--ip-address**|string|Provides the IP address of the client from where the risk occurred.|ip_address|ipAddress|
|**--last-updated-date-time**|date-time|Date and time that the risk detection was last updated.|last_updated_date_time|lastUpdatedDateTime|
|**--request-id**|string|Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.|request_id|requestId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-type**|string|The type of risk event detected. The possible values are unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence, genericadminConfirmedUserCompromised, mcasImpossibleTravel, mcasSuspiciousInboxManipulationRules, investigationsThreatIntelligenceSigninLinked, maliciousIPAddressValidCredentialsBlockedIP, and unknownFutureValue. If the risk detection is a premium detection, will show generic|risk_event_type|riskEventType|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--risk-type**|choice||risk_type|riskType|
|**--source**|string|Source of the risk detection. For example, 'activeDirectory'.|source|source|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-display-name**|string|The user principal name (UPN) of the user.|user_display_name|userDisplayName|
|**--user-id**|string|Unique ID of the user.|user_id|userId|
|**--user-principal-name**|string|The user principal name (UPN) of the user.|user_principal_name|userPrincipalName|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|

### identitysignins create-risky-user

create-risky-user a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskyUsers.riskyUser|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-risky-user|CreateRiskyUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean|Indicates whether the user is deleted. Possible values are: true, false|is_deleted|isDeleted|
|**--is-processing**|boolean|Indicates wehther a user's risky state is being processed by the backend|is_processing|isProcessing|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-last-updated-date-time**|date-time|The date and time that the risky user was last updated.|risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--user-display-name**|string|Risky user display name.|user_display_name|userDisplayName|
|**--user-principal-name**|string|Risky user principal name.|user_principal_name|userPrincipalName|
|**--history**|array|The activity related to user risk level change|history|history|

### identitysignins create-security-question-method

create-security-question-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-security-question-method|CreateSecurityQuestionMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

### identitysignins create-sensitivity-label

create-sensitivity-label a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sensitivity-label|CreateSensitivityLabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--applicable-to**|choice||applicable_to|applicableTo|
|**--application-mode**|choice||application_mode|applicationMode|
|**--assigned-policies**|array||assigned_policies|assignedPolicies|
|**--auto-labeling**|object|autoLabeling|auto_labeling|autoLabeling|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-default**|boolean||is_default|isDefault|
|**--is-endpoint-protection-enabled**|boolean||is_endpoint_protection_enabled|isEndpointProtectionEnabled|
|**--label-actions**|array||label_actions|labelActions|
|**--name**|string||name|name|
|**--priority**|integer||priority|priority|
|**--tool-tip**|string||tool_tip|toolTip|
|**--sublabels**|array||sublabels|sublabels|

### identitysignins create-sublabel

create-sublabel a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.sensitivityLabels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sublabel|CreateSublabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--id**|string|Read-only.|id|id|
|**--applicable-to**|choice||applicable_to|applicableTo|
|**--application-mode**|choice||application_mode|applicationMode|
|**--assigned-policies**|array||assigned_policies|assignedPolicies|
|**--auto-labeling**|object|autoLabeling|auto_labeling|autoLabeling|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-default**|boolean||is_default|isDefault|
|**--is-endpoint-protection-enabled**|boolean||is_endpoint_protection_enabled|isEndpointProtectionEnabled|
|**--label-actions**|array||label_actions|labelActions|
|**--name**|string||name|name|
|**--priority**|integer||priority|priority|
|**--tool-tip**|string||tool_tip|toolTip|
|**--sublabels**|array||sublabels|sublabels|

### identitysignins create-temporary-access-pass-method

create-temporary-access-pass-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-temporary-access-pass-method|CreateTemporaryAccessPassMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

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

### identitysignins create-user-flow

create-user-flow a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user-flow|CreateUserFlows|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-flow-type**|choice||user_flow_type|userFlowType|
|**--user-flow-type-version**|number||user_flow_type_version|userFlowTypeVersion|

### identitysignins delete

delete a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteEmailMethods|
|delete|DeleteFido2Methods|
|delete|DeleteMethods|
|delete|DeleteMicrosoftAuthenticatorMethods|
|delete|DeleteOathMethods|
|delete|DeleteOperations|
|delete|DeletePasswordlessMicrosoftAuthenticatorMethods|
|delete|DeletePasswordMethods|
|delete|DeletePhoneMethods|
|delete|DeleteSecurityQuestionMethods|
|delete|DeleteTemporaryAccessPassMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--email-authentication-method-id**|string|key: id of emailAuthenticationMethod|email_authentication_method_id|emailAuthenticationMethod-id|
|**--fido2-authentication-method-id**|string|key: id of fido2AuthenticationMethod|fido2_authentication_method_id|fido2AuthenticationMethod-id|
|**--authentication-method-id**|string|key: id of authenticationMethod|authentication_method_id|authenticationMethod-id|
|**--microsoft-authenticator-authentication-method-id**|string|key: id of microsoftAuthenticatorAuthenticationMethod|microsoft_authenticator_authentication_method_id|microsoftAuthenticatorAuthenticationMethod-id|
|**--software-oath-authentication-method-id**|string|key: id of softwareOathAuthenticationMethod|software_oath_authentication_method_id|softwareOathAuthenticationMethod-id|
|**--long-running-operation-id**|string|key: id of longRunningOperation|long_running_operation_id|longRunningOperation-id|
|**--passwordless-microsoft-authenticator-authentication-method-id**|string|key: id of passwordlessMicrosoftAuthenticatorAuthenticationMethod|passwordless_microsoft_authenticator_authentication_method_id|passwordlessMicrosoftAuthenticatorAuthenticationMethod-id|
|**--password-authentication-method-id**|string|key: id of passwordAuthenticationMethod|password_authentication_method_id|passwordAuthenticationMethod-id|
|**--phone-authentication-method-id**|string|key: id of phoneAuthenticationMethod|phone_authentication_method_id|phoneAuthenticationMethod-id|
|**--security-question-authentication-method-id**|string|key: id of securityQuestionAuthenticationMethod|security_question_authentication_method_id|securityQuestionAuthenticationMethod-id|
|**--temporary-access-pass-authentication-method-id**|string|key: id of temporaryAccessPassAuthenticationMethod|temporary_access_pass_authentication_method_id|temporaryAccessPassAuthenticationMethod-id|
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

### identitysignins dismiss

dismiss a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss|dismiss|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-ids**|array||user_ids|userIds|

### identitysignins evaluate

evaluate a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.sensitivityLabels.sublabels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|evaluate|evaluate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--discovered-sensitive-types**|array||discovered_sensitive_types|discoveredSensitiveTypes|
|**--current-label**|object|currentLabel|current_label|currentLabel|

### identitysignins evaluate-application

evaluate-application a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.policy.labels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|evaluate-application|evaluateApplication|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--labeling-options-assignment-method**|choice||assignment_method|assignmentMethod|
|**--labeling-options-downgrade-justification**|object|downgradeJustification|downgrade_justification|downgradeJustification|
|**--labeling-options-extended-properties**|array||extended_properties|extendedProperties|
|**--labeling-options-label-id**|uuid||label_id|labelId|
|**--content-info-format**|choice||format|format|
|**--content-info-identifier**|string||identifier|identifier|
|**--content-info-metadata**|array||metadata|metadata|
|**--content-info-state**|choice||state|state|

### identitysignins evaluate-classification-result

evaluate-classification-result a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.policy.labels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|evaluate-classification-result|evaluateClassificationResults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--classification-results**|array||classification_results|classificationResults|
|**--content-info-format**|choice||format|format|
|**--content-info-identifier**|string||identifier|identifier|
|**--content-info-metadata**|array||metadata|metadata|
|**--content-info-state**|choice||state|state|

### identitysignins evaluate-label-and-policy

evaluate-label-and-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|evaluate-label-and-policy|evaluateLabelsAndPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--classify-text**|object|textClassificationRequest|classify_text|classifyText|
|**--evaluate-data-loss-prevention-policies-evaluation-input**|object|dlpEvaluationInput|evaluation_input|evaluationInput|
|**--evaluate-data-loss-prevention-policies-notification-info**|object|dlpNotification|notification_info|notificationInfo|
|**--evaluate-data-loss-prevention-policies-target**|string||target|target|
|**--evaluate-sensitivity-labels-current-label**|object|currentLabel|current_label|currentLabel|
|**--evaluate-sensitivity-labels-discovered-sensitive-types**|array||discovered_sensitive_types|discoveredSensitiveTypes|

### identitysignins evaluate-removal

evaluate-removal a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.policy.labels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|evaluate-removal|evaluateRemoval|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--downgrade-justification**|object|downgradeJustification|downgrade_justification|downgradeJustification|
|**--content-info-format**|choice||format|format|
|**--content-info-identifier**|string||identifier|identifier|
|**--content-info-metadata**|array||metadata|metadata|
|**--content-info-state**|choice||state|state|

### identitysignins extract-label

extract-label a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.policy.labels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|extract-label|extractLabel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--content-info-format**|choice||format|format|
|**--content-info-identifier**|string||identifier|identifier|
|**--content-info-metadata**|array||metadata|metadata|
|**--content-info-state**|choice||state|state|

### identitysignins generate-key

generate-key a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework.keySets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|generate-key|generateKey|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--use**|string||use|use|
|**--kty**|string||kty|kty|
|**--nbf**|integer||nbf|nbf|
|**--exp**|integer||exp|exp|

### identitysignins get-active-key

get-active-key a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework.keySets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-active-key|getActiveKey|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|

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

### identitysignins get-admin-consent-request-policy

get-admin-consent-request-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-admin-consent-request-policy|GetAdminConsentRequestPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-authentication

get-authentication a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-authentication|GetAuthentication|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-authentication-flow-policy

get-authentication-flow-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-authentication-flow-policy|GetAuthenticationFlowsPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-authorization-policy

get-authorization-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-authorization-policy|GetAuthorizationPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--authorization-policy-id**|string|key: id of authorizationPolicy|authorization_policy_id|authorizationPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-b2-c-authentication-method-policy

get-b2-c-authentication-method-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-b2-c-authentication-method-policy|GetB2cAuthenticationMethodsPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
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

### identitysignins get-data-loss-prevention-policy

get-data-loss-prevention-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-data-loss-prevention-policy|GetDataLossPreventionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-loss-prevention-policy-id**|string|key: id of dataLossPreventionPolicy|data_loss_prevention_policy_id|dataLossPreventionPolicy-id|
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

### identitysignins get-device-registration-policy

get-device-registration-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device-registration-policy|GetDeviceRegistrationPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-directory-role-access-review-policy

get-directory-role-access-review-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-role-access-review-policy|GetDirectoryRoleAccessReviewPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-email-method

get-email-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-method|GetEmailMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--email-authentication-method-id**|string|key: id of emailAuthenticationMethod|email_authentication_method_id|emailAuthenticationMethod-id|
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

### identitysignins get-fido2-method

get-fido2-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-fido2-method|GetFido2Methods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--fido2-authentication-method-id**|string|key: id of fido2AuthenticationMethod|fido2_authentication_method_id|fido2AuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-history

get-history a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-history|GetHistory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--risky-user-history-item-id**|string|key: id of riskyUserHistoryItem|risky_user_history_item_id|riskyUserHistoryItem-id|
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
|identitysignins|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-information-protection|GetInformationProtection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
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

### identitysignins get-key-set

get-key-set a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-key-set|GetKeySets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-label

get-label a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.policy|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-label|GetLabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--information-protection-label-id**|string|key: id of informationProtectionLabel|information_protection_label_id|informationProtectionLabel-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-method

get-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-method|GetMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--authentication-method-id**|string|key: id of authenticationMethod|authentication_method_id|authenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-microsoft-authenticator-method

get-microsoft-authenticator-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-microsoft-authenticator-method|GetMicrosoftAuthenticatorMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--microsoft-authenticator-authentication-method-id**|string|key: id of microsoftAuthenticatorAuthenticationMethod|microsoft_authenticator_authentication_method_id|microsoftAuthenticatorAuthenticationMethod-id|
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

### identitysignins get-oath-method

get-oath-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-oath-method|GetOathMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--software-oath-authentication-method-id**|string|key: id of softwareOathAuthenticationMethod|software_oath_authentication_method_id|softwareOathAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-operation

get-operation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-operation|GetOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--long-running-operation-id**|string|key: id of longRunningOperation|long_running_operation_id|longRunningOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-password-method

get-password-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-password-method|GetPasswordMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--password-authentication-method-id**|string|key: id of passwordAuthenticationMethod|password_authentication_method_id|passwordAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-passwordless-microsoft-authenticator-method

get-passwordless-microsoft-authenticator-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-passwordless-microsoft-authenticator-method|GetPasswordlessMicrosoftAuthenticatorMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--passwordless-microsoft-authenticator-authentication-method-id**|string|key: id of passwordlessMicrosoftAuthenticatorAuthenticationMethod|passwordless_microsoft_authenticator_authentication_method_id|passwordlessMicrosoftAuthenticatorAuthenticationMethod-id|
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

### identitysignins get-phone-method

get-phone-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-phone-method|GetPhoneMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--phone-authentication-method-id**|string|key: id of phoneAuthenticationMethod|phone_authentication_method_id|phoneAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-policy

get-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-policy|GetPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-policy-id**|string|key: id of trustFrameworkPolicy|trust_framework_policy_id|trustFrameworkPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-policy-content

get-policy-content a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-policy-content|GetPoliciesContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-policy-id**|string|key: id of trustFrameworkPolicy|trust_framework_policy_id|trustFrameworkPolicy-id|

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

### identitysignins get-private-link-resource-policy

get-private-link-resource-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-private-link-resource-policy|GetPrivateLinkResourcePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--private-link-resource-id**|string|key: id of privateLinkResource|private_link_resource_id|privateLinkResource-id|
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

### identitysignins get-risk-detection

get-risk-detection a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskDetections.riskDetection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-risk-detection|GetRiskDetection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risk-detection-id**|string|key: id of riskDetection|risk_detection_id|riskDetection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-risky-user

get-risky-user a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskyUsers.riskyUser|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-risky-user|GetRiskyUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-security-question-method

get-security-question-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-security-question-method|GetSecurityQuestionMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--security-question-authentication-method-id**|string|key: id of securityQuestionAuthenticationMethod|security_question_authentication_method_id|securityQuestionAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-sensitivity-label

get-sensitivity-label a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sensitivity-label|GetSensitivityLabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-sensitivity-policy-setting

get-sensitivity-policy-setting a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sensitivity-policy-setting|GetSensitivityPolicySettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-sublabel

get-sublabel a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.sensitivityLabels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sublabel|GetSublabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--sensitivity-label-id1**|string|key: id of sensitivityLabel|sensitivity_label_id1|sensitivityLabel-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-temporary-access-pass-method

get-temporary-access-pass-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-temporary-access-pass-method|GetTemporaryAccessPassMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--temporary-access-pass-authentication-method-id**|string|key: id of temporaryAccessPassAuthenticationMethod|temporary_access_pass_authentication_method_id|temporaryAccessPassAuthenticationMethod-id|
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

### identitysignins get-trust-framework

get-trust-framework a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework.trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-trust-framework|GetTrustFramework|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins get-user-flow

get-user-flow a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-flow|GetUserFlows|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-user-flow-id**|string|key: id of identityUserFlow|identity_user_flow_id|identityUserFlow-id|
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

### identitysignins list-authorization-policy

list-authorization-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-authorization-policy|ListAuthorizationPolicy|

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

### identitysignins list-data-loss-prevention-policy

list-data-loss-prevention-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-data-loss-prevention-policy|ListDataLossPreventionPolicies|

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

### identitysignins list-email-method

list-email-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-email-method|ListEmailMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
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

### identitysignins list-fido2-method

list-fido2-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-fido2-method|ListFido2Methods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-history

list-history a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-history|ListHistory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
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

### identitysignins list-key-set

list-key-set a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-key-set|ListKeySets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-label

list-label a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.policy|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-label|ListLabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-method

list-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-method|ListMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-microsoft-authenticator-method

list-microsoft-authenticator-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-microsoft-authenticator-method|ListMicrosoftAuthenticatorMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
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

### identitysignins list-oath-method

list-oath-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-oath-method|ListOathMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-operation

list-operation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-operation|ListOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-password-method

list-password-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-password-method|ListPasswordMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-passwordless-microsoft-authenticator-method

list-passwordless-microsoft-authenticator-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-passwordless-microsoft-authenticator-method|ListPasswordlessMicrosoftAuthenticatorMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
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

### identitysignins list-phone-method

list-phone-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-phone-method|ListPhoneMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-policy

list-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework|

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

### identitysignins list-private-link-resource-policy

list-private-link-resource-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-private-link-resource-policy|ListPrivateLinkResourcePolicies|

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

### identitysignins list-risk-detection

list-risk-detection a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskDetections.riskDetection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-risk-detection|ListRiskDetection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-risky-user

list-risky-user a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskyUsers.riskyUser|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-risky-user|ListRiskyUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-security-question-method

list-security-question-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-security-question-method|ListSecurityQuestionMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-sensitivity-label

list-sensitivity-label a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sensitivity-label|ListSensitivityLabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-sublabel

list-sublabel a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.sensitivityLabels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sublabel|ListSublabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins list-temporary-access-pass-method

list-temporary-access-pass-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-temporary-access-pass-method|ListTemporaryAccessPassMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
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

### identitysignins list-user-flow

list-user-flow a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user-flow|ListUserFlows|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitysignins set-policy-content

set-policy-content a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-policy-content|SetPoliciesContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-policy-id**|string|key: id of trustFrameworkPolicy|trust_framework_policy_id|trustFrameworkPolicy-id|
|**--data**|binary|New media content.|data|data|

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

### identitysignins update-admin-consent-request-policy

update-admin-consent-request-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-admin-consent-request-policy|UpdateAdminConsentRequestPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--notify-reviewers**|boolean||notify_reviewers|notifyReviewers|
|**--reminders-enabled**|boolean||reminders_enabled|remindersEnabled|
|**--request-duration-in-days**|integer||request_duration_in_days|requestDurationInDays|
|**--reviewers**|array||reviewers|reviewers|
|**--version**|integer||version|version|

### identitysignins update-authentication

update-authentication a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-authentication|UpdateAuthentication|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--email-methods**|array||email_methods|emailMethods|
|**--fido2-methods**|array||fido2_methods|fido2Methods|
|**--methods**|array||methods|methods|
|**--microsoft-authenticator-methods**|array||microsoft_authenticator_methods|microsoftAuthenticatorMethods|
|**--oath-methods**|array||oath_methods|oathMethods|
|**--operations**|array||operations|operations|
|**--passwordless-microsoft-authenticator-methods**|array||passwordless_microsoft_authenticator_methods|passwordlessMicrosoftAuthenticatorMethods|
|**--password-methods**|array||password_methods|passwordMethods|
|**--phone-methods**|array||phone_methods|phoneMethods|
|**--security-question-methods**|array||security_question_methods|securityQuestionMethods|
|**--temporary-access-pass-methods**|array||temporary_access_pass_methods|temporaryAccessPassMethods|

### identitysignins update-authentication-flow-policy

update-authentication-flow-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-authentication-flow-policy|UpdateAuthenticationFlowsPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--self-service-sign-up-is-enabled**|boolean||is_enabled|isEnabled|

### identitysignins update-authorization-policy

update-authorization-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-authorization-policy|UpdateAuthorizationPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--authorization-policy-id**|string|key: id of authorizationPolicy|authorization_policy_id|authorizationPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--allowed-to-sign-up-email-based-subscriptions**|boolean||allowed_to_sign_up_email_based_subscriptions|allowedToSignUpEmailBasedSubscriptions|
|**--allowed-to-use-sspr**|boolean||allowed_to_use_sspr|allowedToUseSSPR|
|**--allow-email-verified-users-to-join-organization**|boolean||allow_email_verified_users_to_join_organization|allowEmailVerifiedUsersToJoinOrganization|
|**--allow-invites-from**|choice||allow_invites_from|allowInvitesFrom|
|**--block-msol-power-shell**|boolean||block_msol_power_shell|blockMsolPowerShell|
|**--default-user-role-permissions**|object|defaultUserRolePermissions|default_user_role_permissions|defaultUserRolePermissions|
|**--enabled-preview-features**|array||enabled_preview_features|enabledPreviewFeatures|
|**--guest-user-role-id**|uuid||guest_user_role_id|guestUserRoleId|
|**--permission-grant-policy-ids-assigned-to-default-user-role**|array||permission_grant_policy_ids_assigned_to_default_user_role|permissionGrantPolicyIdsAssignedToDefaultUserRole|

### identitysignins update-b2-c-authentication-method-policy

update-b2-c-authentication-method-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-b2-c-authentication-method-policy|UpdateB2cAuthenticationMethodsPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--is-email-password-authentication-enabled**|boolean||is_email_password_authentication_enabled|isEmailPasswordAuthenticationEnabled|
|**--is-phone-one-time-password-authentication-enabled**|boolean||is_phone_one_time_password_authentication_enabled|isPhoneOneTimePasswordAuthenticationEnabled|
|**--is-user-name-authentication-enabled**|boolean||is_user_name_authentication_enabled|isUserNameAuthenticationEnabled|

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
|**--conditions-client-applications**|object|conditionalAccessClientApplications|client_applications|clientApplications|
|**--conditions-client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--conditions-devices**|object|conditionalAccessDevices|devices|devices|
|**--conditions-device-states**|object|conditionalAccessDeviceStates|device_states|deviceStates|
|**--conditions-locations**|object|conditionalAccessLocations|locations|locations|
|**--conditions-platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--conditions-sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--conditions-user-risk-levels**|array||user_risk_levels|userRiskLevels|
|**--conditions-users**|object|conditionalAccessUsers|users|users|

### identitysignins update-data-loss-prevention-policy

update-data-loss-prevention-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-data-loss-prevention-policy|UpdateDataLossPreventionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-loss-prevention-policy-id**|string|key: id of dataLossPreventionPolicy|data_loss_prevention_policy_id|dataLossPreventionPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string||name|name|

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

### identitysignins update-device-registration-policy

update-device-registration-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device-registration-policy|UpdateDeviceRegistrationPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|

### identitysignins update-directory-role-access-review-policy

update-directory-role-access-review-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory-role-access-review-policy|UpdateDirectoryRoleAccessReviewPolicy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--settings-apply-actions**|array||apply_actions|applyActions|
|**--settings-auto-apply-decisions-enabled**|boolean||auto_apply_decisions_enabled|autoApplyDecisionsEnabled|
|**--settings-default-decision**|string||default_decision|defaultDecision|
|**--settings-default-decision-enabled**|boolean||default_decision_enabled|defaultDecisionEnabled|
|**--settings-instance-duration-in-days**|integer||instance_duration_in_days|instanceDurationInDays|
|**--settings-justification-required-on-approval**|boolean||justification_required_on_approval|justificationRequiredOnApproval|
|**--settings-mail-notifications-enabled**|boolean||mail_notifications_enabled|mailNotificationsEnabled|
|**--settings-recommendations-enabled**|boolean||recommendations_enabled|recommendationsEnabled|
|**--settings-reminder-notifications-enabled**|boolean||reminder_notifications_enabled|reminderNotificationsEnabled|
|**--settings-recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--settings-recurrence-range**|object|recurrenceRange|range|range|

### identitysignins update-email-method

update-email-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-email-method|UpdateEmailMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--email-authentication-method-id**|string|key: id of emailAuthenticationMethod|email_authentication_method_id|emailAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

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

### identitysignins update-fido2-method

update-fido2-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-fido2-method|UpdateFido2Methods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--fido2-authentication-method-id**|string|key: id of fido2AuthenticationMethod|fido2_authentication_method_id|fido2AuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

### identitysignins update-history

update-history a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-history|UpdateHistory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--risky-user-history-item-id**|string|key: id of riskyUserHistoryItem|risky_user_history_item_id|riskyUserHistoryItem-id|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean|Indicates whether the user is deleted. Possible values are: true, false|is_deleted|isDeleted|
|**--is-processing**|boolean|Indicates wehther a user's risky state is being processed by the backend|is_processing|isProcessing|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-last-updated-date-time**|date-time|The date and time that the risky user was last updated.|risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--user-display-name**|string|Risky user display name.|user_display_name|userDisplayName|
|**--user-principal-name**|string|Risky user principal name.|user_principal_name|userPrincipalName|
|**--history**|array|The activity related to user risk level change|history|history|
|**--activity**|object|riskUserActivity|activity|activity|
|**--initiated-by**|string|The id of actor that does the operation.|initiated_by|initiatedBy|
|**--user-id**|string|The id of the user.|user_id|userId|

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
|identitysignins|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-information-protection|UpdateInformationProtection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--data-loss-prevention-policies**|array||data_loss_prevention_policies|dataLossPreventionPolicies|
|**--sensitivity-labels**|array||sensitivity_labels|sensitivityLabels|
|**--sensitivity-policy-settings**|object|sensitivityPolicySettings|sensitivity_policy_settings|sensitivityPolicySettings|
|**--threat-assessment-requests**|array||threat_assessment_requests|threatAssessmentRequests|
|**--policy-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--policy-labels**|array||labels|labels|

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
|**--reset-redemption**|boolean||reset_redemption|resetRedemption|
|**--send-invitation-message**|boolean|Indicates whether an email should be sent to the user being invited or not. The default is false.|send_invitation_message|sendInvitationMessage|
|**--status**|string|The status of the invitation. Possible values: PendingAcceptance, Completed, InProgress, and Error|status|status|
|**--invited-user**|object|Represents an Azure Active Directory user object.|invited_user|invitedUser|
|**--invited-user-message-info-cc-recipients**|array|Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.|cc_recipients|ccRecipients|
|**--invited-user-message-info-customized-message-body**|string|Customized message body you want to send if you don't want the default message.|customized_message_body|customizedMessageBody|
|**--invited-user-message-info-message-language**|string|The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.|message_language|messageLanguage|

### identitysignins update-key-set

update-key-set a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-key-set|UpdateKeySets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--id**|string|Read-only.|id|id|
|**--keys**|array||keys|keys|

### identitysignins update-label

update-label a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.policy|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-label|UpdateLabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--information-protection-label-id**|string|key: id of informationProtectionLabel|information_protection_label_id|informationProtectionLabel-id|
|**--id**|string|Read-only.|id|id|
|**--color**|string||color|color|
|**--description**|string||description|description|
|**--is-active**|boolean||is_active|isActive|
|**--name**|string||name|name|
|**--parent**|object|parentLabelDetails|parent|parent|
|**--sensitivity**|integer||sensitivity|sensitivity|
|**--tooltip**|string||tooltip|tooltip|

### identitysignins update-method

update-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-method|UpdateMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--authentication-method-id**|string|key: id of authenticationMethod|authentication_method_id|authenticationMethod-id|
|**--id**|string|Read-only.|id|id|

### identitysignins update-microsoft-authenticator-method

update-microsoft-authenticator-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-microsoft-authenticator-method|UpdateMicrosoftAuthenticatorMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--microsoft-authenticator-authentication-method-id**|string|key: id of microsoftAuthenticatorAuthenticationMethod|microsoft_authenticator_authentication_method_id|microsoftAuthenticatorAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

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
|**--expiry-time**|date-time||expiry_time|expiryTime|
|**--principal-id**|string|The id of the user on behalf of whom the client is authorized to access the resource, when consentType is Principal. If consentType is AllPrincipals this value is null. Required when consentType is Principal.|principal_id|principalId|
|**--resource-id**|string|The id of the resource service principal to which access is authorized. This identifies the API which the client is authorized to attempt to call on behalf of a signed-in user.|resource_id|resourceId|
|**--scope**|string|A space-separated list of the claim values for delegated permissions which should be included in access tokens for the resource application (the API). For example, openid User.Read GroupMember.Read.All. Each claim value should match the value field of one of the delegated permissions defined by the API, listed in the publishedPermissionScopes property of the resource service principal.|scope|scope|
|**--start-time**|date-time||start_time|startTime|

### identitysignins update-oath-method

update-oath-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-oath-method|UpdateOathMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--software-oath-authentication-method-id**|string|key: id of softwareOathAuthenticationMethod|software_oath_authentication_method_id|softwareOathAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

### identitysignins update-operation

update-operation a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-operation|UpdateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--long-running-operation-id**|string|key: id of longRunningOperation|long_running_operation_id|longRunningOperation-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-action-date-time**|date-time||last_action_date_time|lastActionDateTime|
|**--resource-location**|string||resource_location|resourceLocation|
|**--status**|choice||status|status|
|**--status-detail**|string||status_detail|statusDetail|

### identitysignins update-password-method

update-password-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-password-method|UpdatePasswordMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--password-authentication-method-id**|string|key: id of passwordAuthenticationMethod|password_authentication_method_id|passwordAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|
|**--creation-date-time**|date-time||creation_date_time|creationDateTime|
|**--password**|string||password|password|

### identitysignins update-passwordless-microsoft-authenticator-method

update-passwordless-microsoft-authenticator-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-passwordless-microsoft-authenticator-method|UpdatePasswordlessMicrosoftAuthenticatorMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--passwordless-microsoft-authenticator-authentication-method-id**|string|key: id of passwordlessMicrosoftAuthenticatorAuthenticationMethod|passwordless_microsoft_authenticator_authentication_method_id|passwordlessMicrosoftAuthenticatorAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

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

### identitysignins update-phone-method

update-phone-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-phone-method|UpdatePhoneMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--phone-authentication-method-id**|string|key: id of phoneAuthenticationMethod|phone_authentication_method_id|phoneAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|
|**--phone-number**|string||phone_number|phoneNumber|
|**--phone-type**|choice||phone_type|phoneType|
|**--sms-sign-in-state**|choice||sms_sign_in_state|smsSignInState|

### identitysignins update-policy

update-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-policy|UpdatePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-policy-id**|string|key: id of trustFrameworkPolicy|trust_framework_policy_id|trustFrameworkPolicy-id|
|**--id**|string|Read-only.|id|id|

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
|**--b2-c-authentication-methods-policy**|object|b2cAuthenticationMethodsPolicy|b2_c_authentication_methods_policy|b2cAuthenticationMethodsPolicy|
|**--activity-based-timeout-policies**|array||activity_based_timeout_policies|activityBasedTimeoutPolicies|
|**--authorization-policy**|array||authorization_policy|authorizationPolicy|
|**--claims-mapping-policies**|array||claims_mapping_policies|claimsMappingPolicies|
|**--home-realm-discovery-policies**|array||home_realm_discovery_policies|homeRealmDiscoveryPolicies|
|**--permission-grant-policies**|array||permission_grant_policies|permissionGrantPolicies|
|**--private-link-resource-policies**|array||private_link_resource_policies|privateLinkResourcePolicies|
|**--token-issuance-policies**|array||token_issuance_policies|tokenIssuancePolicies|
|**--token-lifetime-policies**|array||token_lifetime_policies|tokenLifetimePolicies|
|**--conditional-access-policies**|array||conditional_access_policies|conditionalAccessPolicies|
|**--identity-security-defaults-enforcement-policy**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|identity_security_defaults_enforcement_policy|identitySecurityDefaultsEnforcementPolicy|
|**--directory-role-access-review-policy-id**|string|Read-only.|id|id|
|**--directory-role-access-review-policy-settings-apply-actions**|array||apply_actions|applyActions|
|**--directory-role-access-review-policy-settings-auto-apply-decisions-enabled**|boolean||auto_apply_decisions_enabled|autoApplyDecisionsEnabled|
|**--directory-role-access-review-policy-settings-default-decision**|string||default_decision|defaultDecision|
|**--directory-role-access-review-policy-settings-default-decision-enabled**|boolean||default_decision_enabled|defaultDecisionEnabled|
|**--directory-role-access-review-policy-settings-instance-duration-in-days**|integer||instance_duration_in_days|instanceDurationInDays|
|**--directory-role-access-review-policy-settings-justification-required-on-approval**|boolean||justification_required_on_approval|justificationRequiredOnApproval|
|**--directory-role-access-review-policy-settings-mail-notifications-enabled**|boolean||mail_notifications_enabled|mailNotificationsEnabled|
|**--directory-role-access-review-policy-settings-recommendations-enabled**|boolean||recommendations_enabled|recommendationsEnabled|
|**--directory-role-access-review-policy-settings-reminder-notifications-enabled**|boolean||reminder_notifications_enabled|reminderNotificationsEnabled|
|**--directory-role-access-review-policy-settings-recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--directory-role-access-review-policy-settings-recurrence-range**|object|recurrenceRange|range|range|
|**--admin-consent-request-policy-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--admin-consent-request-policy-is-enabled**|boolean||is_enabled|isEnabled|
|**--admin-consent-request-policy-notify-reviewers**|boolean||notify_reviewers|notifyReviewers|
|**--admin-consent-request-policy-reminders-enabled**|boolean||reminders_enabled|remindersEnabled|
|**--admin-consent-request-policy-request-duration-in-days**|integer||request_duration_in_days|requestDurationInDays|
|**--admin-consent-request-policy-reviewers**|array||reviewers|reviewers|
|**--admin-consent-request-policy-version**|integer||version|version|
|**--device-registration-policy-id**|string|Read-only.|id1|id|
|**--authentication-flows-policy-id**|string|Read-only.|id2|id|
|**--authentication-flows-policy-description**|string||description|description|
|**--authentication-flows-policy-display-name**|string||display_name|displayName|
|**--authentication-flows-policy-self-service-sign-up-is-enabled**|boolean||is_enabled|isEnabled|

### identitysignins update-private-link-resource-policy

update-private-link-resource-policy a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-private-link-resource-policy|UpdatePrivateLinkResourcePolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--private-link-resource-id**|string|key: id of privateLinkResource|private_link_resource_id|privateLinkResource-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-tenant-ids**|array||allowed_tenant_ids|allowedTenantIds|
|**--arm-resource-id**|string||arm_resource_id|armResourceId|

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

### identitysignins update-risk-detection

update-risk-detection a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskDetections.riskDetection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-risk-detection|UpdateRiskDetection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risk-detection-id**|string|key: id of riskDetection|risk_detection_id|riskDetection-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|choice||activity|activity|
|**--activity-date-time**|date-time|Date and time that the risky activity occurred.|activity_date_time|activityDateTime|
|**--additional-info**|string|Additional information associated with the risk detection in JSON format.|additional_info|additionalInfo|
|**--correlation-id**|string|Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.|correlation_id|correlationId|
|**--detected-date-time**|date-time|Date and time that the risk was detected.|detected_date_time|detectedDateTime|
|**--detection-timing-type**|choice||detection_timing_type|detectionTimingType|
|**--ip-address**|string|Provides the IP address of the client from where the risk occurred.|ip_address|ipAddress|
|**--last-updated-date-time**|date-time|Date and time that the risk detection was last updated.|last_updated_date_time|lastUpdatedDateTime|
|**--request-id**|string|Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.|request_id|requestId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-type**|string|The type of risk event detected. The possible values are unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence, genericadminConfirmedUserCompromised, mcasImpossibleTravel, mcasSuspiciousInboxManipulationRules, investigationsThreatIntelligenceSigninLinked, maliciousIPAddressValidCredentialsBlockedIP, and unknownFutureValue. If the risk detection is a premium detection, will show generic|risk_event_type|riskEventType|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--risk-type**|choice||risk_type|riskType|
|**--source**|string|Source of the risk detection. For example, 'activeDirectory'.|source|source|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-display-name**|string|The user principal name (UPN) of the user.|user_display_name|userDisplayName|
|**--user-id**|string|Unique ID of the user.|user_id|userId|
|**--user-principal-name**|string|The user principal name (UPN) of the user.|user_principal_name|userPrincipalName|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|

### identitysignins update-risky-user

update-risky-user a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|riskyUsers.riskyUser|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-risky-user|UpdateRiskyUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean|Indicates whether the user is deleted. Possible values are: true, false|is_deleted|isDeleted|
|**--is-processing**|boolean|Indicates wehther a user's risky state is being processed by the backend|is_processing|isProcessing|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-last-updated-date-time**|date-time|The date and time that the risky user was last updated.|risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--user-display-name**|string|Risky user display name.|user_display_name|userDisplayName|
|**--user-principal-name**|string|Risky user principal name.|user_principal_name|userPrincipalName|
|**--history**|array|The activity related to user risk level change|history|history|

### identitysignins update-security-question-method

update-security-question-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-security-question-method|UpdateSecurityQuestionMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--security-question-authentication-method-id**|string|key: id of securityQuestionAuthenticationMethod|security_question_authentication_method_id|securityQuestionAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

### identitysignins update-sensitivity-label

update-sensitivity-label a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sensitivity-label|UpdateSensitivityLabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--id**|string|Read-only.|id|id|
|**--applicable-to**|choice||applicable_to|applicableTo|
|**--application-mode**|choice||application_mode|applicationMode|
|**--assigned-policies**|array||assigned_policies|assignedPolicies|
|**--auto-labeling**|object|autoLabeling|auto_labeling|autoLabeling|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-default**|boolean||is_default|isDefault|
|**--is-endpoint-protection-enabled**|boolean||is_endpoint_protection_enabled|isEndpointProtectionEnabled|
|**--label-actions**|array||label_actions|labelActions|
|**--name**|string||name|name|
|**--priority**|integer||priority|priority|
|**--tool-tip**|string||tool_tip|toolTip|
|**--sublabels**|array||sublabels|sublabels|

### identitysignins update-sensitivity-policy-setting

update-sensitivity-policy-setting a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sensitivity-policy-setting|UpdateSensitivityPolicySettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--applicable-to**|choice||applicable_to|applicableTo|
|**--downgrade-sensitivity-requires-justification**|boolean||downgrade_sensitivity_requires_justification|downgradeSensitivityRequiresJustification|
|**--help-web-url**|string||help_web_url|helpWebUrl|
|**--is-mandatory**|boolean||is_mandatory|isMandatory|

### identitysignins update-sublabel

update-sublabel a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|informationProtection.sensitivityLabels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sublabel|UpdateSublabels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--sensitivity-label-id1**|string|key: id of sensitivityLabel|sensitivity_label_id1|sensitivityLabel-id1|
|**--id**|string|Read-only.|id|id|
|**--applicable-to**|choice||applicable_to|applicableTo|
|**--application-mode**|choice||application_mode|applicationMode|
|**--assigned-policies**|array||assigned_policies|assignedPolicies|
|**--auto-labeling**|object|autoLabeling|auto_labeling|autoLabeling|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-default**|boolean||is_default|isDefault|
|**--is-endpoint-protection-enabled**|boolean||is_endpoint_protection_enabled|isEndpointProtectionEnabled|
|**--label-actions**|array||label_actions|labelActions|
|**--name**|string||name|name|
|**--priority**|integer||priority|priority|
|**--tool-tip**|string||tool_tip|toolTip|
|**--sublabels**|array||sublabels|sublabels|

### identitysignins update-temporary-access-pass-method

update-temporary-access-pass-method a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|users.authentication|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-temporary-access-pass-method|UpdateTemporaryAccessPassMethods|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--temporary-access-pass-authentication-method-id**|string|key: id of temporaryAccessPassAuthenticationMethod|temporary_access_pass_authentication_method_id|temporaryAccessPassAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

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

### identitysignins update-trust-framework

update-trust-framework a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework.trustFramework|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-trust-framework|UpdateTrustFramework|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--key-sets**|array||key_sets|keySets|
|**--policies**|array||policies|policies|

### identitysignins update-user-flow

update-user-flow a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|identity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user-flow|UpdateUserFlows|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-user-flow-id**|string|key: id of identityUserFlow|identity_user_flow_id|identityUserFlow-id|
|**--id**|string|Read-only.|id|id|
|**--user-flow-type**|choice||user_flow_type|userFlowType|
|**--user-flow-type-version**|number||user_flow_type_version|userFlowTypeVersion|

### identitysignins upload-certificate

upload-certificate a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework.keySets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|upload-certificate|uploadCertificate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--key**|string||key|key|

### identitysignins upload-pkcs12

upload-pkcs12 a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework.keySets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|upload-pkcs12|uploadPkcs12|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--key**|string||key|key|
|**--password**|string||password|password|

### identitysignins upload-secret

upload-secret a identitysignins.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitysignins|trustFramework.keySets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|upload-secret|uploadSecret|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--use**|string||use|use|
|**--k**|string||k|k|
|**--nbf**|integer||nbf|nbf|
|**--exp**|integer||exp|exp|
