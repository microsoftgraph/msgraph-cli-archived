# Azure CLI Module Creation Report

### users user create

create a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--sign-in-activity**|object|signInActivity|sign_in_activity|signInActivity|
|**--account-enabled**|boolean|true if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.|account_enabled|accountEnabled|
|**--age-group**|string|Sets the age group of the user. Allowed values: null, minor, notAdult and adult. Refer to the legal age group property definitions for further information.|age_group|ageGroup|
|**--assigned-licenses**|array|The licenses that are assigned to the user. Not nullable.|assigned_licenses|assignedLicenses|
|**--assigned-plans**|array|The plans that are assigned to the user. Read-only. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|The telephone numbers for the user. NOTE: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--city**|string|The city in which the user is located. Supports $filter.|city|city|
|**--company-name**|string|The company name which the user is associated. This property can be useful for describing the company that an external user comes from. The maximum length of the company name is 64 chararcters.Returned only on $select.|company_name|companyName|
|**--consent-provided-for-minor**|string|Sets whether consent has been obtained for minors. Allowed values: null, granted, denied and notRequired. Refer to the legal age group property definitions for further information.|consent_provided_for_minor|consentProvidedForMinor|
|**--country**|string|The country/region in which the user is located; for example, 'US' or 'UK'. Supports $filter.|country|country|
|**--created-date-time**|date-time|The created date of the user object.|created_date_time|createdDateTime|
|**--creation-type**|string|Indicates whether the user account was created as a regular school or work account (null), an external account (Invitation), a local account for an Azure Active Directory B2C tenant (LocalAccount) or self-service sign-up using email verification (EmailVerified). Read-only.|creation_type|creationType|
|**--department**|string|The name for the department in which the user works. Supports $filter.|department|department|
|**--device-keys**|array||device_keys|deviceKeys|
|**--display-name**|string|The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.|display_name|displayName|
|**--employee-hire-date**|date-time|The date and time when the user was hired or will start work in case of a future hire. Returned only on $select. Supports $filter.|employee_hire_date|employeeHireDate|
|**--employee-id**|string|The employee identifier assigned to the user by the organization. Returned only on $select. Supports $filter.|employee_id|employeeId|
|**--employee-org-data**|object|employeeOrgData|employee_org_data|employeeOrgData|
|**--employee-type**|string|Captures enterprise worker type: Employee, Contractor, Consultant, Vendor, etc. Returned only on $select. Supports $filter.|employee_type|employeeType|
|**--external-user-state**|string|For an external user invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Returned only on $select. Supports $filter with the supported values. For example: $filter=externalUserState eq 'PendingAcceptance'.|external_user_state|externalUserState|
|**--external-user-state-change-date-time**|string|Shows the timestamp for the latest change to the externalUserState property. Returned only on $select.|external_user_state_change_date_time|externalUserStateChangeDateTime|
|**--fax-number**|string|The fax number of the user.|fax_number|faxNumber|
|**--given-name**|string|The given name (first name) of the user. Supports $filter.|given_name|givenName|
|**--identities**|array|Represents the identities that can be used to sign in to this user account. An identity can be provided by Microsoft (also known as a local account), by organizations, or by social identity providers such as Facebook, Google, and Microsoft, and tied to a user account. May contain multiple items with the same signInType value. Supports $filter.|identities|identities|
|**--im-addresses**|array|The instant message voice over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only.|im_addresses|imAddresses|
|**--info-catalogs**|array||info_catalogs|infoCatalogs|
|**--is-resource-account**|boolean|Do not use – reserved for future use.|is_resource_account|isResourceAccount|
|**--job-title**|string|The user's job title. Supports $filter.|job_title|jobTitle|
|**--last-password-change-date-time**|date-time|The time when this Azure AD user last changed their password. The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_password_change_date_time|lastPasswordChangeDateTime|
|**--legal-age-group-classification**|string|Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, minorWithOutParentalConsent, minorWithParentalConsent, minorNoParentalConsentRequired, notAdult and adult. Refer to the legal age group property definitions for further information.)|legal_age_group_classification|legalAgeGroupClassification|
|**--license-assignment-states**|array|State of license assignments for this user. Read-only.|license_assignment_states|licenseAssignmentStates|
|**--mail**|string|The SMTP address for the user, for example, 'jeff@contoso.onmicrosoft.com'. Supports $filter.|mail|mail|
|**--mail-nickname**|string|The mail alias for the user. This property must be specified when a user is created. Supports $filter.|mail_nickname|mailNickname|
|**--mobile-phone**|string|The primary cellular telephone number for the user.|mobile_phone|mobilePhone|
|**--office-location**|string|The office location in the user's place of business.|office_location|officeLocation|
|**--on-premises-distinguished-name**|string|Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.|on_premises_distinguished_name|onPremisesDistinguishedName|
|**--on-premises-domain-name**|string|Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--on-premises-extension-attributes**|object|onPremisesExtensionAttributes|on_premises_extension_attributes|onPremisesExtensionAttributes|
|**--on-premises-immutable-id**|string|This property is used to associate an on-premises Active Directory user account to their Azure AD user object. This property must be specified when creating a new user account in the Graph if you are using a federated domain for the user's userPrincipalName (UPN) property. Important: The $ and _ characters cannot be used when specifying this property. Supports $filter.|on_premises_immutable_id|onPremisesImmutableId|
|**--on-premises-last-sync-date-time**|date-time|Indicates the last time at which the object was synced with the on-premises directory; for example: '2013-02-16T03:04:54Z'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sam-account-name**|string|Contains the on-premises samAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--on-premises-user-principal-name**|string|Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.|on_premises_user_principal_name|onPremisesUserPrincipalName|
|**--other-mails**|array|A list of additional email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com']. Supports $filter.|other_mails|otherMails|
|**--password-policies**|string|Specifies password policies for the user. This value is an enumeration with one possible value being 'DisableStrongPassword', which allows weaker passwords than the default policy to be specified. 'DisablePasswordExpiration' can also be specified. The two may be specified together; for example: 'DisablePasswordExpiration, DisableStrongPassword'.|password_policies|passwordPolicies|
|**--password-profile**|object|passwordProfile|password_profile|passwordProfile|
|**--postal-code**|string|The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.|postal_code|postalCode|
|**--preferred-data-location**|string||preferred_data_location|preferredDataLocation|
|**--preferred-language**|string|The preferred language for the user. Should follow ISO 639-1 Code; for example 'en-US'.|preferred_language|preferredLanguage|
|**--provisioned-plans**|array|The plans that are provisioned for the user. Read-only. Not nullable.|provisioned_plans|provisionedPlans|
|**--proxy-addresses**|array|For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com'] The any operator is required for filter expressions on multi-valued properties. Read-only, Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--refresh-tokens-valid-from-date-time**|date-time|Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Returned only on $select. Read-only.|refresh_tokens_valid_from_date_time|refreshTokensValidFromDateTime|
|**--show-in-address-list**|boolean|true if the Outlook global address list should contain this user, otherwise false. If not set, this will be treated as true. For users invited through the invitation manager, this property will be set to false.|show_in_address_list|showInAddressList|
|**--sign-in-sessions-valid-from-date-time**|date-time|Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Read-only. Use revokeSignInSessions to reset.|sign_in_sessions_valid_from_date_time|signInSessionsValidFromDateTime|
|**--state**|string|The state or province in the user's address. Supports $filter.|state|state|
|**--street-address**|string|The street address of the user's place of business.|street_address|streetAddress|
|**--surname**|string|The user's surname (family name or last name). Supports $filter.|surname|surname|
|**--usage-location**|string|A two letter country code (ISO standard 3166). Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries.  Examples include: 'US', 'JP', and 'GB'. Not nullable. Supports $filter.|usage_location|usageLocation|
|**--user-principal-name**|string|The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization. Supports $filter and $orderby.|user_principal_name|userPrincipalName|
|**--user-type**|string|A string value that can be used to classify user types in your directory, such as 'Member' and 'Guest'. Supports $filter.|user_type|userType|
|**--device-enrollment-limit**|integer|The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.|device_enrollment_limit|deviceEnrollmentLimit|
|**--about-me**|string|A freeform text entry field for the user to describe themselves.|about_me|aboutMe|
|**--birthday**|date-time|The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|birthday|birthday|
|**--hire-date**|date-time|The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned only on $select.  Note: This property is specific to SharePoint Online. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs.|hire_date|hireDate|
|**--interests**|array|A list for the user to describe their interests.|interests|interests|
|**--my-site**|string|The URL for the user's personal site.|my_site|mySite|
|**--past-projects**|array|A list for the user to enumerate their past projects.|past_projects|pastProjects|
|**--preferred-name**|string|The preferred name for the user.|preferred_name|preferredName|
|**--responsibilities**|array|A list for the user to enumerate their responsibilities.|responsibilities|responsibilities|
|**--schools**|array|A list for the user to enumerate the schools they have attended.|schools|schools|
|**--skills**|array|A list for the user to enumerate their skills.|skills|skills|
|**--app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--created-objects**|array|Directory objects that were created by the user. Read-only. Nullable.|created_objects|createdObjects|
|**--direct-reports**|array|The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable.|direct_reports|directReports|
|**--license-details**|array|A collection of this user's license details. Read-only.|license_details|licenseDetails|
|**--manager**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|manager|manager|
|**--member-of**|array|The groups and directory roles that the user is a member of. Read-only. Nullable.|member_of|memberOf|
|**--owned-devices**|array|Devices that are owned by the user. Read-only. Nullable.|owned_devices|ownedDevices|
|**--owned-objects**|array|Directory objects that are owned by the user. Read-only. Nullable.|owned_objects|ownedObjects|
|**--registered-devices**|array|Devices that are registered for the user. Read-only. Nullable.|registered_devices|registeredDevices|
|**--scoped-role-member-of**|array||scoped_role_member_of|scopedRoleMemberOf|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--calendar**|object|calendar|calendar|calendar|
|**--calendar-groups**|array|The user's calendar groups. Read-only. Nullable.|calendar_groups|calendarGroups|
|**--calendars**|array|The user's calendars. Read-only. Nullable.|calendars|calendars|
|**--calendar-view**|array|The calendar view for the calendar. Read-only. Nullable.|calendar_view|calendarView|
|**--contact-folders**|array|The user's contacts folders. Read-only. Nullable.|contact_folders|contactFolders|
|**--contacts**|array|The user's contacts. Read-only. Nullable.|contacts|contacts|
|**--events**|array|The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.|events|events|
|**--joined-groups**|array||joined_groups|joinedGroups|
|**--mail-folders**|array|The user's mail folders. Read-only. Nullable.|mail_folders|mailFolders|
|**--messages**|array|The messages in a mailbox or folder. Read-only. Nullable.|messages|messages|
|**--people**|array|People that are relevant to the user. Read-only. Nullable.|people|people|
|**--photo**|object|profilePhoto|photo|photo|
|**--photos**|array||photos|photos|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|A collection of drives available for this user. Read-only.|drives|drives|
|**--followed-sites**|array||followed_sites|followedSites|
|**--extensions**|array|The collection of open extensions defined for the user. Read-only. Nullable.|extensions|extensions|
|**--app-consent-requests-for-approval**|array||app_consent_requests_for_approval|appConsentRequestsForApproval|
|**--approvals**|array||approvals|approvals|
|**--pending-access-review-instances**|array||pending_access_review_instances|pendingAccessReviewInstances|
|**--agreement-acceptances**|array||agreement_acceptances|agreementAcceptances|
|**--device-enrollment-configurations**|array||device_enrollment_configurations|deviceEnrollmentConfigurations|
|**--managed-devices**|array|The managed devices associated with the user.|managed_devices|managedDevices|
|**--managed-app-registrations**|array|Zero or more managed app registrations that belong to the user.|managed_app_registrations|managedAppRegistrations|
|**--windows-information-protection-device-registrations**|array|Zero or more WIP device registrations that belong to the user.|windows_information_protection_device_registrations|windowsInformationProtectionDeviceRegistrations|
|**--device-management-troubleshooting-events**|array|The list of troubleshooting events for this user.|device_management_troubleshooting_events|deviceManagementTroubleshootingEvents|
|**--mobile-app-intent-and-states**|array|The list of troubleshooting events for this user.|mobile_app_intent_and_states|mobileAppIntentAndStates|
|**--mobile-app-troubleshooting-events**|array|The list of mobile app troubleshooting events for this user.|mobile_app_troubleshooting_events|mobileAppTroubleshootingEvents|
|**--notifications**|array||notifications|notifications|
|**--insights**|object|itemInsights|insights|insights|
|**--activities**|array|The user's activities across devices. Read-only. Nullable.|activities|activities|
|**--devices**|array||devices|devices|
|**--online-meetings**|array||online_meetings|onlineMeetings|
|**--presence**|object|presence|presence|presence|
|**--chats**|array||chats|chats|
|**--joined-teams**|array||joined_teams|joinedTeams|
|**--todo-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--todo-lists**|array||lists|lists|
|**--teamwork-id**|string|Read-only.|id1|id|
|**--teamwork-installed-apps**|array|The apps installed in the personal scope of this user.|installed_apps|installedApps|
|**--authentication-id**|string|Read-only.|id2|id|
|**--authentication-email-methods**|array||email_methods|emailMethods|
|**--authentication-fido2methods**|array||fido2_methods|fido2Methods|
|**--authentication-methods**|array||methods|methods|
|**--authentication-microsoft-authenticator-methods**|array||microsoft_authenticator_methods|microsoftAuthenticatorMethods|
|**--authentication-oath-methods**|array||oath_methods|oathMethods|
|**--authentication-operations**|array||operations|operations|
|**--authentication-passwordless-microsoft-authenticator-methods**|array||passwordless_microsoft_authenticator_methods|passwordlessMicrosoftAuthenticatorMethods|
|**--authentication-password-methods**|array||password_methods|passwordMethods|
|**--authentication-phone-methods**|array||phone_methods|phoneMethods|
|**--authentication-security-question-methods**|array||security_question_methods|securityQuestionMethods|
|**--authentication-temporary-access-pass-methods**|array||temporary_access_pass_methods|temporaryAccessPassMethods|
|**--profile-id**|string|Read-only.|id3|id|
|**--profile-account**|array||account|account|
|**--profile-addresses**|array||addresses|addresses|
|**--profile-anniversaries**|array||anniversaries|anniversaries|
|**--profile-awards**|array||awards|awards|
|**--profile-certifications**|array||certifications|certifications|
|**--profile-educational-activities**|array||educational_activities|educationalActivities|
|**--profile-emails**|array||emails|emails|
|**--profile-interests**|array||microsoft_graph_profile_interests|interests|
|**--profile-languages**|array||languages|languages|
|**--profile-names**|array||names|names|
|**--profile-notes**|array||notes|notes|
|**--profile-patents**|array||patents|patents|
|**--profile-phones**|array||phones|phones|
|**--profile-positions**|array||positions|positions|
|**--profile-projects**|array||projects|projects|
|**--profile-publications**|array||publications|publications|
|**--profile-skills**|array||microsoft_graph_profile_skills|skills|
|**--profile-web-accounts**|array||web_accounts|webAccounts|
|**--profile-websites**|array||websites|websites|
|**--onenote-id**|string|Read-only.|id4|id|
|**--onenote-notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--onenote-operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|microsoft_graph_onenote_operations|operations|
|**--onenote-pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|pages|pages|
|**--onenote-resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--onenote-section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--onenote-sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--settings-id**|string|Read-only.|id5|id|
|**--settings-contribution-to-content-discovery-as-organization-disabled**|boolean||contribution_to_content_discovery_as_organization_disabled|contributionToContentDiscoveryAsOrganizationDisabled|
|**--settings-contribution-to-content-discovery-disabled**|boolean||contribution_to_content_discovery_disabled|contributionToContentDiscoveryDisabled|
|**--settings-shift-preferences-id**|string|Read-only.|id6|id|
|**--settings-shift-preferences-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|microsoft_graph_change_tracked_entity_created_date_time_created_date_time|createdDateTime|
|**--settings-shift-preferences-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--settings-shift-preferences-last-modified-by-application**|object|identity|application|application|
|**--settings-shift-preferences-last-modified-by-device**|object|identity|device|device|
|**--settings-shift-preferences-last-modified-by-user**|object|identity|user|user|
|**--settings-shift-preferences-created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--settings-shift-preferences-created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--settings-shift-preferences-created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--settings-shift-preferences-availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|
|**--settings-regional-and-language-settings-id**|string|Read-only.|id7|id|
|**--settings-regional-and-language-settings-authoring-languages**|array||authoring_languages|authoringLanguages|
|**--settings-regional-and-language-settings-default-display-language**|object|localeInfo|default_display_language|defaultDisplayLanguage|
|**--settings-regional-and-language-settings-default-regional-format**|object|localeInfo|default_regional_format|defaultRegionalFormat|
|**--settings-regional-and-language-settings-default-speech-input-language**|object|localeInfo|default_speech_input_language|defaultSpeechInputLanguage|
|**--settings-regional-and-language-settings-default-translation-language**|object|localeInfo|default_translation_language|defaultTranslationLanguage|
|**--settings-regional-and-language-settings-regional-format-overrides**|object|regionalFormatOverrides|regional_format_overrides|regionalFormatOverrides|
|**--planner-id**|string|Read-only.|id8|id|
|**--planner-favorite-plan-references**|dictionary|plannerFavoritePlanReferenceCollection|favorite_plan_references|favoritePlanReferences|
|**--planner-recent-plan-references**|dictionary|plannerRecentPlanReferenceCollection|recent_plan_references|recentPlanReferences|
|**--planner-all**|array||all|all|
|**--planner-favorite-plans**|array||favorite_plans|favoritePlans|
|**--planner-plans**|array|Read-only. Nullable. Returns the plannerTasks assigned to the user.|plans|plans|
|**--planner-recent-plans**|array||recent_plans|recentPlans|
|**--planner-tasks**|array|Read-only. Nullable. Returns the plannerPlans shared with the user.|tasks|tasks|
|**--outlook-id**|string|Read-only.|id9|id|
|**--outlook-master-categories**|array|A list of categories defined for the user.|master_categories|masterCategories|
|**--outlook-task-folders**|array||task_folders|taskFolders|
|**--outlook-task-groups**|array||task_groups|taskGroups|
|**--outlook-tasks**|array||microsoft_graph_outlook_user_tasks|tasks|
|**--inference-classification-id**|string|Read-only.|id10|id|
|**--inference-classification-overrides**|array|A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.|overrides|overrides|
|**--information-protection-id**|string|Read-only.|id11|id|
|**--information-protection-policy**|object|informationProtectionPolicy|policy|policy|
|**--information-protection-data-loss-prevention-policies**|array||data_loss_prevention_policies|dataLossPreventionPolicies|
|**--information-protection-sensitivity-labels**|array||sensitivity_labels|sensitivityLabels|
|**--information-protection-sensitivity-policy-settings**|object|sensitivityPolicySettings|sensitivity_policy_settings|sensitivityPolicySettings|
|**--information-protection-threat-assessment-requests**|array||threat_assessment_requests|threatAssessmentRequests|
|**--analytics-id**|string|Read-only.|id12|id|
|**--analytics-settings**|object|settings|settings|settings|
|**--analytics-activity-statistics**|array||activity_statistics|activityStatistics|
|**--mailbox-settings-archive-folder**|string|Folder ID of an archive folder for the user.|archive_folder|archiveFolder|
|**--mailbox-settings-automatic-replies-setting**|object|automaticRepliesSetting|automatic_replies_setting|automaticRepliesSetting|
|**--mailbox-settings-date-format**|string|The date format for the user's mailbox.|date_format|dateFormat|
|**--mailbox-settings-delegate-meeting-message-delivery-options**|choice||delegate_meeting_message_delivery_options|delegateMeetingMessageDeliveryOptions|
|**--mailbox-settings-language**|object|localeInfo|language|language|
|**--mailbox-settings-time-format**|string|The time format for the user's mailbox.|time_format|timeFormat|
|**--mailbox-settings-time-zone**|string|The default time zone for the user's mailbox.|time_zone|timeZone|
|**--mailbox-settings-user-purpose**|object|userPurpose|user_purpose|userPurpose|
|**--mailbox-settings-user-purpose-v2**|choice||user_purpose_v2|userPurposeV2|
|**--mailbox-settings-working-hours**|object|workingHours|working_hours|workingHours|

### users user create-extension

create-extension a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

### users user create-license-detail

create-license-detail a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-license-detail|CreateLicenseDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--service-plans**|array|Information about the service plans assigned with the license. Read-only, Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related SubscribedSku object. Read-only|sku_id|skuId|
|**--sku-part-number**|string|Unique SKU display name. Equal to the skuPartNumber on the related SubscribedSku object; for example: 'AAD_Premium'. Read-only|sku_part_number|skuPartNumber|

### users user create-notification

create-notification a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-notification|CreateNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--display-time-to-live**|integer||display_time_to_live|displayTimeToLive|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--group-name**|string||group_name|groupName|
|**--priority**|choice||priority|priority|
|**--target-host-name**|string||target_host_name|targetHostName|
|**--target-policy**|object|targetPolicyEndpoints|target_policy|targetPolicy|
|**--payload-raw-content**|string||raw_content|rawContent|
|**--payload-visual-content**|object|visualProperties|visual_content|visualContent|

### users user create-photo

create-photo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-photo|CreatePhotos|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

### users user create-ref-created-object

create-ref-created-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-created-object|CreateRefCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-direct-report

create-ref-direct-report a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-direct-report|CreateRefDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-member-of

create-ref-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member-of|CreateRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-owned-device

create-ref-owned-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owned-device|CreateRefOwnedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-owned-object

create-ref-owned-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owned-object|CreateRefOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-registered-device

create-ref-registered-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-registered-device|CreateRefRegisteredDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-transitive-member-of

create-ref-transitive-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-transitive-member-of|CreateRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user delete

delete a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensions|
|delete|DeleteLicenseDetails|
|delete|DeleteNotifications|
|delete|DeletePhotos|
|delete|DeleteRefManager|
|delete|DeleteOutlook|
|delete|DeletePhoto|
|delete|DeleteSettings|
|delete|DeleteTodo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--license-details-id**|string|key: id of licenseDetails|license_details_id|licenseDetails-id|
|**--notification-id**|string|key: id of notification|notification_id|notification-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user get

get a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--consistency-level**|string|Indicates the requested consistency level.|consistency_level|ConsistencyLevel|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user get-extension

get-extension a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user get-license-detail

get-license-detail a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-license-detail|GetLicenseDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--license-details-id**|string|key: id of licenseDetails|license_details_id|licenseDetails-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user get-manager

get-manager a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-manager|GetManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user get-notification

get-notification a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-notification|GetNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notification-id**|string|key: id of notification|notification_id|notification-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user get-outlook

get-outlook a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-outlook|GetOutlook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user get-photo

get-photo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-photo|GetPhotos|
|get-photo|GetPhoto|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user get-photo-content

get-photo-content a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-photo-content|GetPhotosContent|
|get-photo-content|GetPhotoContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|

### users user get-ref-manager

get-ref-manager a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-manager|GetRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### users user get-setting

get-setting a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-setting|GetSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user get-todo

get-todo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-todo|GetTodo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list

list a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--consistency-level**|string|Indicates the requested consistency level.|consistency_level|ConsistencyLevel|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-created-object

list-created-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-created-object|ListCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-direct-report

list-direct-report a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-direct-report|ListDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-extension

list-extension a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-license-detail

list-license-detail a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-license-detail|ListLicenseDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-member-of

list-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member-of|ListMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-notification

list-notification a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-notification|ListNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-owned-device

list-owned-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-owned-device|ListOwnedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-owned-object

list-owned-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-owned-object|ListOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-photo

list-photo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-photo|ListPhotos|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-ref-created-object

list-ref-created-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-created-object|ListRefCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-direct-report

list-ref-direct-report a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-direct-report|ListRefDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-member-of

list-ref-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member-of|ListRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-owned-device

list-ref-owned-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owned-device|ListRefOwnedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-owned-object

list-ref-owned-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owned-object|ListRefOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-registered-device

list-ref-registered-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-registered-device|ListRefRegisteredDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-transitive-member-of

list-ref-transitive-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-transitive-member-of|ListRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-registered-device

list-registered-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-registered-device|ListRegisteredDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-transitive-member-of

list-transitive-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-transitive-member-of|ListTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user set-photo-content

set-photo-content a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-photo-content|SetPhotosContent|
|set-photo-content|SetPhotoContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--data**|binary|New media content.|data|data|

### users user set-ref-manager

set-ref-manager a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-manager|SetRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### users user update

update a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--sign-in-activity**|object|signInActivity|sign_in_activity|signInActivity|
|**--account-enabled**|boolean|true if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.|account_enabled|accountEnabled|
|**--age-group**|string|Sets the age group of the user. Allowed values: null, minor, notAdult and adult. Refer to the legal age group property definitions for further information.|age_group|ageGroup|
|**--assigned-licenses**|array|The licenses that are assigned to the user. Not nullable.|assigned_licenses|assignedLicenses|
|**--assigned-plans**|array|The plans that are assigned to the user. Read-only. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|The telephone numbers for the user. NOTE: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--city**|string|The city in which the user is located. Supports $filter.|city|city|
|**--company-name**|string|The company name which the user is associated. This property can be useful for describing the company that an external user comes from. The maximum length of the company name is 64 chararcters.Returned only on $select.|company_name|companyName|
|**--consent-provided-for-minor**|string|Sets whether consent has been obtained for minors. Allowed values: null, granted, denied and notRequired. Refer to the legal age group property definitions for further information.|consent_provided_for_minor|consentProvidedForMinor|
|**--country**|string|The country/region in which the user is located; for example, 'US' or 'UK'. Supports $filter.|country|country|
|**--created-date-time**|date-time|The created date of the user object.|created_date_time|createdDateTime|
|**--creation-type**|string|Indicates whether the user account was created as a regular school or work account (null), an external account (Invitation), a local account for an Azure Active Directory B2C tenant (LocalAccount) or self-service sign-up using email verification (EmailVerified). Read-only.|creation_type|creationType|
|**--department**|string|The name for the department in which the user works. Supports $filter.|department|department|
|**--device-keys**|array||device_keys|deviceKeys|
|**--display-name**|string|The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.|display_name|displayName|
|**--employee-hire-date**|date-time|The date and time when the user was hired or will start work in case of a future hire. Returned only on $select. Supports $filter.|employee_hire_date|employeeHireDate|
|**--employee-id**|string|The employee identifier assigned to the user by the organization. Returned only on $select. Supports $filter.|employee_id|employeeId|
|**--employee-org-data**|object|employeeOrgData|employee_org_data|employeeOrgData|
|**--employee-type**|string|Captures enterprise worker type: Employee, Contractor, Consultant, Vendor, etc. Returned only on $select. Supports $filter.|employee_type|employeeType|
|**--external-user-state**|string|For an external user invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Returned only on $select. Supports $filter with the supported values. For example: $filter=externalUserState eq 'PendingAcceptance'.|external_user_state|externalUserState|
|**--external-user-state-change-date-time**|string|Shows the timestamp for the latest change to the externalUserState property. Returned only on $select.|external_user_state_change_date_time|externalUserStateChangeDateTime|
|**--fax-number**|string|The fax number of the user.|fax_number|faxNumber|
|**--given-name**|string|The given name (first name) of the user. Supports $filter.|given_name|givenName|
|**--identities**|array|Represents the identities that can be used to sign in to this user account. An identity can be provided by Microsoft (also known as a local account), by organizations, or by social identity providers such as Facebook, Google, and Microsoft, and tied to a user account. May contain multiple items with the same signInType value. Supports $filter.|identities|identities|
|**--im-addresses**|array|The instant message voice over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only.|im_addresses|imAddresses|
|**--info-catalogs**|array||info_catalogs|infoCatalogs|
|**--is-resource-account**|boolean|Do not use – reserved for future use.|is_resource_account|isResourceAccount|
|**--job-title**|string|The user's job title. Supports $filter.|job_title|jobTitle|
|**--last-password-change-date-time**|date-time|The time when this Azure AD user last changed their password. The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_password_change_date_time|lastPasswordChangeDateTime|
|**--legal-age-group-classification**|string|Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, minorWithOutParentalConsent, minorWithParentalConsent, minorNoParentalConsentRequired, notAdult and adult. Refer to the legal age group property definitions for further information.)|legal_age_group_classification|legalAgeGroupClassification|
|**--license-assignment-states**|array|State of license assignments for this user. Read-only.|license_assignment_states|licenseAssignmentStates|
|**--mail**|string|The SMTP address for the user, for example, 'jeff@contoso.onmicrosoft.com'. Supports $filter.|mail|mail|
|**--mail-nickname**|string|The mail alias for the user. This property must be specified when a user is created. Supports $filter.|mail_nickname|mailNickname|
|**--mobile-phone**|string|The primary cellular telephone number for the user.|mobile_phone|mobilePhone|
|**--office-location**|string|The office location in the user's place of business.|office_location|officeLocation|
|**--on-premises-distinguished-name**|string|Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.|on_premises_distinguished_name|onPremisesDistinguishedName|
|**--on-premises-domain-name**|string|Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--on-premises-extension-attributes**|object|onPremisesExtensionAttributes|on_premises_extension_attributes|onPremisesExtensionAttributes|
|**--on-premises-immutable-id**|string|This property is used to associate an on-premises Active Directory user account to their Azure AD user object. This property must be specified when creating a new user account in the Graph if you are using a federated domain for the user's userPrincipalName (UPN) property. Important: The $ and _ characters cannot be used when specifying this property. Supports $filter.|on_premises_immutable_id|onPremisesImmutableId|
|**--on-premises-last-sync-date-time**|date-time|Indicates the last time at which the object was synced with the on-premises directory; for example: '2013-02-16T03:04:54Z'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sam-account-name**|string|Contains the on-premises samAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--on-premises-user-principal-name**|string|Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.|on_premises_user_principal_name|onPremisesUserPrincipalName|
|**--other-mails**|array|A list of additional email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com']. Supports $filter.|other_mails|otherMails|
|**--password-policies**|string|Specifies password policies for the user. This value is an enumeration with one possible value being 'DisableStrongPassword', which allows weaker passwords than the default policy to be specified. 'DisablePasswordExpiration' can also be specified. The two may be specified together; for example: 'DisablePasswordExpiration, DisableStrongPassword'.|password_policies|passwordPolicies|
|**--password-profile**|object|passwordProfile|password_profile|passwordProfile|
|**--postal-code**|string|The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.|postal_code|postalCode|
|**--preferred-data-location**|string||preferred_data_location|preferredDataLocation|
|**--preferred-language**|string|The preferred language for the user. Should follow ISO 639-1 Code; for example 'en-US'.|preferred_language|preferredLanguage|
|**--provisioned-plans**|array|The plans that are provisioned for the user. Read-only. Not nullable.|provisioned_plans|provisionedPlans|
|**--proxy-addresses**|array|For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com'] The any operator is required for filter expressions on multi-valued properties. Read-only, Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--refresh-tokens-valid-from-date-time**|date-time|Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Returned only on $select. Read-only.|refresh_tokens_valid_from_date_time|refreshTokensValidFromDateTime|
|**--show-in-address-list**|boolean|true if the Outlook global address list should contain this user, otherwise false. If not set, this will be treated as true. For users invited through the invitation manager, this property will be set to false.|show_in_address_list|showInAddressList|
|**--sign-in-sessions-valid-from-date-time**|date-time|Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Read-only. Use revokeSignInSessions to reset.|sign_in_sessions_valid_from_date_time|signInSessionsValidFromDateTime|
|**--state**|string|The state or province in the user's address. Supports $filter.|state|state|
|**--street-address**|string|The street address of the user's place of business.|street_address|streetAddress|
|**--surname**|string|The user's surname (family name or last name). Supports $filter.|surname|surname|
|**--usage-location**|string|A two letter country code (ISO standard 3166). Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries.  Examples include: 'US', 'JP', and 'GB'. Not nullable. Supports $filter.|usage_location|usageLocation|
|**--user-principal-name**|string|The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization. Supports $filter and $orderby.|user_principal_name|userPrincipalName|
|**--user-type**|string|A string value that can be used to classify user types in your directory, such as 'Member' and 'Guest'. Supports $filter.|user_type|userType|
|**--device-enrollment-limit**|integer|The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.|device_enrollment_limit|deviceEnrollmentLimit|
|**--about-me**|string|A freeform text entry field for the user to describe themselves.|about_me|aboutMe|
|**--birthday**|date-time|The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|birthday|birthday|
|**--hire-date**|date-time|The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned only on $select.  Note: This property is specific to SharePoint Online. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs.|hire_date|hireDate|
|**--interests**|array|A list for the user to describe their interests.|interests|interests|
|**--my-site**|string|The URL for the user's personal site.|my_site|mySite|
|**--past-projects**|array|A list for the user to enumerate their past projects.|past_projects|pastProjects|
|**--preferred-name**|string|The preferred name for the user.|preferred_name|preferredName|
|**--responsibilities**|array|A list for the user to enumerate their responsibilities.|responsibilities|responsibilities|
|**--schools**|array|A list for the user to enumerate the schools they have attended.|schools|schools|
|**--skills**|array|A list for the user to enumerate their skills.|skills|skills|
|**--app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--created-objects**|array|Directory objects that were created by the user. Read-only. Nullable.|created_objects|createdObjects|
|**--direct-reports**|array|The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable.|direct_reports|directReports|
|**--license-details**|array|A collection of this user's license details. Read-only.|license_details|licenseDetails|
|**--manager**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|manager|manager|
|**--member-of**|array|The groups and directory roles that the user is a member of. Read-only. Nullable.|member_of|memberOf|
|**--owned-devices**|array|Devices that are owned by the user. Read-only. Nullable.|owned_devices|ownedDevices|
|**--owned-objects**|array|Directory objects that are owned by the user. Read-only. Nullable.|owned_objects|ownedObjects|
|**--registered-devices**|array|Devices that are registered for the user. Read-only. Nullable.|registered_devices|registeredDevices|
|**--scoped-role-member-of**|array||scoped_role_member_of|scopedRoleMemberOf|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--calendar**|object|calendar|calendar|calendar|
|**--calendar-groups**|array|The user's calendar groups. Read-only. Nullable.|calendar_groups|calendarGroups|
|**--calendars**|array|The user's calendars. Read-only. Nullable.|calendars|calendars|
|**--calendar-view**|array|The calendar view for the calendar. Read-only. Nullable.|calendar_view|calendarView|
|**--contact-folders**|array|The user's contacts folders. Read-only. Nullable.|contact_folders|contactFolders|
|**--contacts**|array|The user's contacts. Read-only. Nullable.|contacts|contacts|
|**--events**|array|The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.|events|events|
|**--joined-groups**|array||joined_groups|joinedGroups|
|**--mail-folders**|array|The user's mail folders. Read-only. Nullable.|mail_folders|mailFolders|
|**--messages**|array|The messages in a mailbox or folder. Read-only. Nullable.|messages|messages|
|**--people**|array|People that are relevant to the user. Read-only. Nullable.|people|people|
|**--photo**|object|profilePhoto|photo|photo|
|**--photos**|array||photos|photos|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|A collection of drives available for this user. Read-only.|drives|drives|
|**--followed-sites**|array||followed_sites|followedSites|
|**--extensions**|array|The collection of open extensions defined for the user. Read-only. Nullable.|extensions|extensions|
|**--app-consent-requests-for-approval**|array||app_consent_requests_for_approval|appConsentRequestsForApproval|
|**--approvals**|array||approvals|approvals|
|**--pending-access-review-instances**|array||pending_access_review_instances|pendingAccessReviewInstances|
|**--agreement-acceptances**|array||agreement_acceptances|agreementAcceptances|
|**--device-enrollment-configurations**|array||device_enrollment_configurations|deviceEnrollmentConfigurations|
|**--managed-devices**|array|The managed devices associated with the user.|managed_devices|managedDevices|
|**--managed-app-registrations**|array|Zero or more managed app registrations that belong to the user.|managed_app_registrations|managedAppRegistrations|
|**--windows-information-protection-device-registrations**|array|Zero or more WIP device registrations that belong to the user.|windows_information_protection_device_registrations|windowsInformationProtectionDeviceRegistrations|
|**--device-management-troubleshooting-events**|array|The list of troubleshooting events for this user.|device_management_troubleshooting_events|deviceManagementTroubleshootingEvents|
|**--mobile-app-intent-and-states**|array|The list of troubleshooting events for this user.|mobile_app_intent_and_states|mobileAppIntentAndStates|
|**--mobile-app-troubleshooting-events**|array|The list of mobile app troubleshooting events for this user.|mobile_app_troubleshooting_events|mobileAppTroubleshootingEvents|
|**--notifications**|array||notifications|notifications|
|**--insights**|object|itemInsights|insights|insights|
|**--activities**|array|The user's activities across devices. Read-only. Nullable.|activities|activities|
|**--devices**|array||devices|devices|
|**--online-meetings**|array||online_meetings|onlineMeetings|
|**--presence**|object|presence|presence|presence|
|**--chats**|array||chats|chats|
|**--joined-teams**|array||joined_teams|joinedTeams|
|**--todo-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--todo-lists**|array||lists|lists|
|**--teamwork-id**|string|Read-only.|id1|id|
|**--teamwork-installed-apps**|array|The apps installed in the personal scope of this user.|installed_apps|installedApps|
|**--authentication-id**|string|Read-only.|id2|id|
|**--authentication-email-methods**|array||email_methods|emailMethods|
|**--authentication-fido2methods**|array||fido2_methods|fido2Methods|
|**--authentication-methods**|array||methods|methods|
|**--authentication-microsoft-authenticator-methods**|array||microsoft_authenticator_methods|microsoftAuthenticatorMethods|
|**--authentication-oath-methods**|array||oath_methods|oathMethods|
|**--authentication-operations**|array||operations|operations|
|**--authentication-passwordless-microsoft-authenticator-methods**|array||passwordless_microsoft_authenticator_methods|passwordlessMicrosoftAuthenticatorMethods|
|**--authentication-password-methods**|array||password_methods|passwordMethods|
|**--authentication-phone-methods**|array||phone_methods|phoneMethods|
|**--authentication-security-question-methods**|array||security_question_methods|securityQuestionMethods|
|**--authentication-temporary-access-pass-methods**|array||temporary_access_pass_methods|temporaryAccessPassMethods|
|**--profile-id**|string|Read-only.|id3|id|
|**--profile-account**|array||account|account|
|**--profile-addresses**|array||addresses|addresses|
|**--profile-anniversaries**|array||anniversaries|anniversaries|
|**--profile-awards**|array||awards|awards|
|**--profile-certifications**|array||certifications|certifications|
|**--profile-educational-activities**|array||educational_activities|educationalActivities|
|**--profile-emails**|array||emails|emails|
|**--profile-interests**|array||microsoft_graph_profile_interests|interests|
|**--profile-languages**|array||languages|languages|
|**--profile-names**|array||names|names|
|**--profile-notes**|array||notes|notes|
|**--profile-patents**|array||patents|patents|
|**--profile-phones**|array||phones|phones|
|**--profile-positions**|array||positions|positions|
|**--profile-projects**|array||projects|projects|
|**--profile-publications**|array||publications|publications|
|**--profile-skills**|array||microsoft_graph_profile_skills|skills|
|**--profile-web-accounts**|array||web_accounts|webAccounts|
|**--profile-websites**|array||websites|websites|
|**--onenote-id**|string|Read-only.|id4|id|
|**--onenote-notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--onenote-operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|microsoft_graph_onenote_operations|operations|
|**--onenote-pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|pages|pages|
|**--onenote-resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--onenote-section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--onenote-sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--settings-id**|string|Read-only.|id5|id|
|**--settings-contribution-to-content-discovery-as-organization-disabled**|boolean||contribution_to_content_discovery_as_organization_disabled|contributionToContentDiscoveryAsOrganizationDisabled|
|**--settings-contribution-to-content-discovery-disabled**|boolean||contribution_to_content_discovery_disabled|contributionToContentDiscoveryDisabled|
|**--settings-shift-preferences-id**|string|Read-only.|id6|id|
|**--settings-shift-preferences-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|microsoft_graph_change_tracked_entity_created_date_time_created_date_time|createdDateTime|
|**--settings-shift-preferences-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--settings-shift-preferences-last-modified-by-application**|object|identity|application|application|
|**--settings-shift-preferences-last-modified-by-device**|object|identity|device|device|
|**--settings-shift-preferences-last-modified-by-user**|object|identity|user|user|
|**--settings-shift-preferences-created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--settings-shift-preferences-created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--settings-shift-preferences-created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--settings-shift-preferences-availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|
|**--settings-regional-and-language-settings-id**|string|Read-only.|id7|id|
|**--settings-regional-and-language-settings-authoring-languages**|array||authoring_languages|authoringLanguages|
|**--settings-regional-and-language-settings-default-display-language**|object|localeInfo|default_display_language|defaultDisplayLanguage|
|**--settings-regional-and-language-settings-default-regional-format**|object|localeInfo|default_regional_format|defaultRegionalFormat|
|**--settings-regional-and-language-settings-default-speech-input-language**|object|localeInfo|default_speech_input_language|defaultSpeechInputLanguage|
|**--settings-regional-and-language-settings-default-translation-language**|object|localeInfo|default_translation_language|defaultTranslationLanguage|
|**--settings-regional-and-language-settings-regional-format-overrides**|object|regionalFormatOverrides|regional_format_overrides|regionalFormatOverrides|
|**--planner-id**|string|Read-only.|id8|id|
|**--planner-favorite-plan-references**|dictionary|plannerFavoritePlanReferenceCollection|favorite_plan_references|favoritePlanReferences|
|**--planner-recent-plan-references**|dictionary|plannerRecentPlanReferenceCollection|recent_plan_references|recentPlanReferences|
|**--planner-all**|array||all|all|
|**--planner-favorite-plans**|array||favorite_plans|favoritePlans|
|**--planner-plans**|array|Read-only. Nullable. Returns the plannerTasks assigned to the user.|plans|plans|
|**--planner-recent-plans**|array||recent_plans|recentPlans|
|**--planner-tasks**|array|Read-only. Nullable. Returns the plannerPlans shared with the user.|tasks|tasks|
|**--outlook-id**|string|Read-only.|id9|id|
|**--outlook-master-categories**|array|A list of categories defined for the user.|master_categories|masterCategories|
|**--outlook-task-folders**|array||task_folders|taskFolders|
|**--outlook-task-groups**|array||task_groups|taskGroups|
|**--outlook-tasks**|array||microsoft_graph_outlook_user_tasks|tasks|
|**--inference-classification-id**|string|Read-only.|id10|id|
|**--inference-classification-overrides**|array|A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.|overrides|overrides|
|**--information-protection-id**|string|Read-only.|id11|id|
|**--information-protection-policy**|object|informationProtectionPolicy|policy|policy|
|**--information-protection-data-loss-prevention-policies**|array||data_loss_prevention_policies|dataLossPreventionPolicies|
|**--information-protection-sensitivity-labels**|array||sensitivity_labels|sensitivityLabels|
|**--information-protection-sensitivity-policy-settings**|object|sensitivityPolicySettings|sensitivity_policy_settings|sensitivityPolicySettings|
|**--information-protection-threat-assessment-requests**|array||threat_assessment_requests|threatAssessmentRequests|
|**--analytics-id**|string|Read-only.|id12|id|
|**--analytics-settings**|object|settings|settings|settings|
|**--analytics-activity-statistics**|array||activity_statistics|activityStatistics|
|**--mailbox-settings-archive-folder**|string|Folder ID of an archive folder for the user.|archive_folder|archiveFolder|
|**--mailbox-settings-automatic-replies-setting**|object|automaticRepliesSetting|automatic_replies_setting|automaticRepliesSetting|
|**--mailbox-settings-date-format**|string|The date format for the user's mailbox.|date_format|dateFormat|
|**--mailbox-settings-delegate-meeting-message-delivery-options**|choice||delegate_meeting_message_delivery_options|delegateMeetingMessageDeliveryOptions|
|**--mailbox-settings-language**|object|localeInfo|language|language|
|**--mailbox-settings-time-format**|string|The time format for the user's mailbox.|time_format|timeFormat|
|**--mailbox-settings-time-zone**|string|The default time zone for the user's mailbox.|time_zone|timeZone|
|**--mailbox-settings-user-purpose**|object|userPurpose|user_purpose|userPurpose|
|**--mailbox-settings-user-purpose-v2**|choice||user_purpose_v2|userPurposeV2|
|**--mailbox-settings-working-hours**|object|workingHours|working_hours|workingHours|

### users user update-extension

update-extension a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### users user update-license-detail

update-license-detail a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-license-detail|UpdateLicenseDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--license-details-id**|string|key: id of licenseDetails|license_details_id|licenseDetails-id|
|**--id**|string|Read-only.|id|id|
|**--service-plans**|array|Information about the service plans assigned with the license. Read-only, Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related SubscribedSku object. Read-only|sku_id|skuId|
|**--sku-part-number**|string|Unique SKU display name. Equal to the skuPartNumber on the related SubscribedSku object; for example: 'AAD_Premium'. Read-only|sku_part_number|skuPartNumber|

### users user update-notification

update-notification a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-notification|UpdateNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notification-id**|string|key: id of notification|notification_id|notification-id|
|**--id**|string|Read-only.|id|id|
|**--display-time-to-live**|integer||display_time_to_live|displayTimeToLive|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--group-name**|string||group_name|groupName|
|**--priority**|choice||priority|priority|
|**--target-host-name**|string||target_host_name|targetHostName|
|**--target-policy**|object|targetPolicyEndpoints|target_policy|targetPolicy|
|**--payload-raw-content**|string||raw_content|rawContent|
|**--payload-visual-content**|object|visualProperties|visual_content|visualContent|

### users user update-outlook

update-outlook a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-outlook|UpdateOutlook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--master-categories**|array|A list of categories defined for the user.|master_categories|masterCategories|
|**--task-folders**|array||task_folders|taskFolders|
|**--task-groups**|array||task_groups|taskGroups|
|**--tasks**|array||tasks|tasks|

### users user update-photo

update-photo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-photo|UpdatePhotos|
|update-photo|UpdatePhoto|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

### users user update-setting

update-setting a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-setting|UpdateSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--contribution-to-content-discovery-as-organization-disabled**|boolean||contribution_to_content_discovery_as_organization_disabled|contributionToContentDiscoveryAsOrganizationDisabled|
|**--contribution-to-content-discovery-disabled**|boolean||contribution_to_content_discovery_disabled|contributionToContentDiscoveryDisabled|
|**--shift-preferences-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--shift-preferences-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--shift-preferences-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--shift-preferences-last-modified-by-application**|object|identity|application|application|
|**--shift-preferences-last-modified-by-device**|object|identity|device|device|
|**--shift-preferences-last-modified-by-user**|object|identity|user|user|
|**--shift-preferences-created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--shift-preferences-created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--shift-preferences-created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--shift-preferences-availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|
|**--regional-and-language-settings-id**|string|Read-only.|id1|id|
|**--regional-and-language-settings-authoring-languages**|array||authoring_languages|authoringLanguages|
|**--regional-and-language-settings-default-display-language**|object|localeInfo|default_display_language|defaultDisplayLanguage|
|**--regional-and-language-settings-default-regional-format**|object|localeInfo|default_regional_format|defaultRegionalFormat|
|**--regional-and-language-settings-default-speech-input-language**|object|localeInfo|default_speech_input_language|defaultSpeechInputLanguage|
|**--regional-and-language-settings-default-translation-language**|object|localeInfo|default_translation_language|defaultTranslationLanguage|
|**--regional-and-language-settings-regional-format-overrides**|object|regionalFormatOverrides|regional_format_overrides|regionalFormatOverrides|

### users user update-todo

update-todo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-todo|UpdateTodo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--lists**|array||lists|lists|

### users user-outlook create-master-category

create-master-category a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-master-category|CreateMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--color**|choice||color|color|
|**--display-name**|string|A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.|display_name|displayName|

### users user-outlook create-task

create-task a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook create-task-folder

create-task-folder a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-folder|CreateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--name**|string||name|name|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--tasks**|array||tasks|tasks|

### users user-outlook create-task-group

create-task-group a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-group|CreateTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--group-key**|uuid||group_key|groupKey|
|**--is-default-group**|boolean||is_default_group|isDefaultGroup|
|**--name**|string||name|name|
|**--task-folders**|array||task_folders|taskFolders|

### users user-outlook delete

delete a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteMasterCategories|
|delete|DeleteTaskFolders|
|delete|DeleteTaskGroups|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-category-id**|string|key: id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook get-master-category

get-master-category a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-master-category|GetMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-category-id**|string|key: id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook get-task

get-task a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook get-task-folder

get-task-folder a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-folder|GetTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook get-task-group

get-task-group a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-group|GetTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook list-master-category

list-master-category a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-master-category|ListMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook list-task

list-task a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook list-task-folder

list-task-folder a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-folder|ListTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook list-task-group

list-task-group a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-group|ListTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook update-master-category

update-master-category a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-master-category|UpdateMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-category-id**|string|key: id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--id**|string|Read-only.|id|id|
|**--color**|choice||color|color|
|**--display-name**|string|A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.|display_name|displayName|

### users user-outlook update-task

update-task a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook update-task-folder

update-task-folder a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task-folder|UpdateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--name**|string||name|name|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--tasks**|array||tasks|tasks|

### users user-outlook update-task-group

update-task-group a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task-group|UpdateTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--group-key**|uuid||group_key|groupKey|
|**--is-default-group**|boolean||is_default_group|isDefaultGroup|
|**--name**|string||name|name|
|**--task-folders**|array||task_folders|taskFolders|

### users user-outlook-task create-attachment

create-attachment a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task create-multi-value-extended-property

create-multi-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task create-single-value-extended-property

create-single-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task delete

delete a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task get-attachment

get-attachment a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task get-multi-value-extended-property

get-multi-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task get-single-value-extended-property

get-single-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task list-attachment

list-attachment a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task list-multi-value-extended-property

list-multi-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task list-single-value-extended-property

list-single-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task update-attachment

update-attachment a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task update-multi-value-extended-property

update-multi-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task update-single-value-extended-property

update-single-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-folder create-multi-value-extended-property

create-multi-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-folder create-single-value-extended-property

create-single-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-folder create-task

create-task a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook-task-folder delete

delete a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task-folder get-multi-value-extended-property

get-multi-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder get-single-value-extended-property

get-single-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder get-task

get-task a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder list-multi-value-extended-property

list-multi-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder list-single-value-extended-property

list-single-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder list-task

list-task a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder update-multi-value-extended-property

update-multi-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-folder update-single-value-extended-property

update-single-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-folder update-task

update-task a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook-task-folder-task create-attachment

create-attachment a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task-folder-task create-multi-value-extended-property

create-multi-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-folder-task create-single-value-extended-property

create-single-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-folder-task delete

delete a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task-folder-task get-attachment

get-attachment a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task get-multi-value-extended-property

get-multi-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task get-single-value-extended-property

get-single-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task list-attachment

list-attachment a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task list-multi-value-extended-property

list-multi-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task list-single-value-extended-property

list-single-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task update-attachment

update-attachment a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task-folder-task update-multi-value-extended-property

update-multi-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-folder-task update-single-value-extended-property

update-single-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-group create-task-folder

create-task-folder a users user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-folder|CreateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--name**|string||name|name|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--tasks**|array||tasks|tasks|

### users user-outlook-task-group delete

delete a users user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task-group get-task-folder

get-task-folder a users user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-folder|GetTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group list-task-folder

list-task-folder a users user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-folder|ListTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group update-task-folder

update-task-folder a users user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task-folder|UpdateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--name**|string||name|name|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--tasks**|array||tasks|tasks|

### users user-outlook-task-group-task-folder create-multi-value-extended-property

create-multi-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-group-task-folder create-single-value-extended-property

create-single-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-group-task-folder create-task

create-task a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook-task-group-task-folder delete

delete a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task-group-task-folder get-multi-value-extended-property

get-multi-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder get-single-value-extended-property

get-single-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder get-task

get-task a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder list-multi-value-extended-property

list-multi-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder list-single-value-extended-property

list-single-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder list-task

list-task a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder update-multi-value-extended-property

update-multi-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-group-task-folder update-single-value-extended-property

update-single-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-group-task-folder update-task

update-task a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook-task-group-task-folder-task create-attachment

create-attachment a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task-group-task-folder-task create-multi-value-extended-property

create-multi-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-group-task-folder-task create-single-value-extended-property

create-single-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-group-task-folder-task delete

delete a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task-group-task-folder-task get-attachment

get-attachment a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task get-multi-value-extended-property

get-multi-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task get-single-value-extended-property

get-single-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task list-attachment

list-attachment a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task list-multi-value-extended-property

list-multi-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task list-single-value-extended-property

list-single-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task update-attachment

update-attachment a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task-group-task-folder-task update-multi-value-extended-property

update-multi-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-group-task-folder-task update-single-value-extended-property

update-single-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-setting delete

delete a users user-setting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-setting|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRegionalAndLanguageSettings|
|delete|DeleteShiftPreferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-setting get-regional-and-language-setting

get-regional-and-language-setting a users user-setting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-setting|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-regional-and-language-setting|GetRegionalAndLanguageSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-setting get-shift-preference

get-shift-preference a users user-setting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-setting|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shift-preference|GetShiftPreferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-setting update-regional-and-language-setting

update-regional-and-language-setting a users user-setting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-setting|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-regional-and-language-setting|UpdateRegionalAndLanguageSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--authoring-languages**|array||authoring_languages|authoringLanguages|
|**--default-display-language**|object|localeInfo|default_display_language|defaultDisplayLanguage|
|**--default-regional-format**|object|localeInfo|default_regional_format|defaultRegionalFormat|
|**--default-speech-input-language**|object|localeInfo|default_speech_input_language|defaultSpeechInputLanguage|
|**--default-translation-language**|object|localeInfo|default_translation_language|defaultTranslationLanguage|
|**--regional-format-overrides**|object|regionalFormatOverrides|regional_format_overrides|regionalFormatOverrides|

### users user-setting update-shift-preference

update-shift-preference a users user-setting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-setting|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shift-preference|UpdateShiftPreferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|

### users user-todo create-list

create-list a users user-todo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo|users.todo|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-list|CreateLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--is-owner**|boolean||is_owner|isOwner|
|**--is-shared**|boolean||is_shared|isShared|
|**--wellknown-list-name**|choice||wellknown_list_name|wellknownListName|
|**--extensions**|array||extensions|extensions|
|**--tasks**|array||tasks|tasks|

### users user-todo delete

delete a users user-todo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo|users.todo|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-todo get-list

get-list a users user-todo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo|users.todo|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list|GetLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo list-list

list-list a users user-todo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo|users.todo|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-list|ListLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo update-list

update-list a users user-todo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo|users.todo|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-list|UpdateLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--is-owner**|boolean||is_owner|isOwner|
|**--is-shared**|boolean||is_shared|isShared|
|**--wellknown-list-name**|choice||wellknown_list_name|wellknownListName|
|**--extensions**|array||extensions|extensions|
|**--tasks**|array||tasks|tasks|

### users user-todo-list create-extension

create-extension a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--id**|string|Read-only.|id|id|

### users user-todo-list create-task

create-task a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--id**|string|Read-only.|id|id|
|**--body**|object|itemBody|body|body|
|**--body-last-modified-date-time**|date-time||body_last_modified_date_time|bodyLastModifiedDateTime|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--status**|choice||status|status|
|**--title**|string||title|title|
|**--extensions**|array||extensions|extensions|
|**--linked-resources**|array||linked_resources|linkedResources|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-todo-list delete

delete a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensions|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-todo-list get-extension

get-extension a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list get-task

get-task a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list list-extension

list-extension a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list list-task

list-task a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list update-extension

update-extension a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### users user-todo-list update-task

update-task a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--id**|string|Read-only.|id|id|
|**--body**|object|itemBody|body|body|
|**--body-last-modified-date-time**|date-time||body_last_modified_date_time|bodyLastModifiedDateTime|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--status**|choice||status|status|
|**--title**|string||title|title|
|**--extensions**|array||extensions|extensions|
|**--linked-resources**|array||linked_resources|linkedResources|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-todo-list-task create-extension

create-extension a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--id**|string|Read-only.|id|id|

### users user-todo-list-task create-linked-resource

create-linked-resource a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-linked-resource|CreateLinkedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--id**|string|Read-only.|id|id|
|**--application-name**|string||application_name|applicationName|
|**--display-name**|string||display_name|displayName|
|**--external-id**|string||external_id|externalId|
|**--web-url**|string||web_url|webUrl|

### users user-todo-list-task delete

delete a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensions|
|delete|DeleteLinkedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--linked-resource-id**|string|key: id of linkedResource|linked_resource_id|linkedResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-todo-list-task get-extension

get-extension a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list-task get-linked-resource

get-linked-resource a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-linked-resource|GetLinkedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--linked-resource-id**|string|key: id of linkedResource|linked_resource_id|linkedResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list-task list-extension

list-extension a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list-task list-linked-resource

list-linked-resource a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-linked-resource|ListLinkedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list-task update-extension

update-extension a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### users user-todo-list-task update-linked-resource

update-linked-resource a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-linked-resource|UpdateLinkedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--linked-resource-id**|string|key: id of linkedResource|linked_resource_id|linkedResource-id|
|**--id**|string|Read-only.|id|id|
|**--application-name**|string||application_name|applicationName|
|**--display-name**|string||display_name|displayName|
|**--external-id**|string||external_id|externalId|
|**--web-url**|string||web_url|webUrl|
