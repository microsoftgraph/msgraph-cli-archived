# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az users|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az users` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az users user|users.user|[commands](#CommandsInusers.user)|
|az users user|users|[commands](#CommandsInusers)|
|az users user-outlook|users.outlook|[commands](#CommandsInusers.outlook)|
|az users user-setting|users.settings|[commands](#CommandsInusers.settings)|

## COMMANDS
### <a name="CommandsInusers.user">Commands in `az users user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az users user list](#users.userListUser)|ListUser|[Parameters](#Parametersusers.userListUser)|Not Found|
|[az users user create](#users.userUpdateUser)|UpdateUser|[Parameters](#Parametersusers.userUpdateUser)|Not Found|
|[az users user create](#users.userCreateUser)|CreateUser|[Parameters](#Parametersusers.userCreateUser)|Not Found|
|[az users user delete-user](#users.userDeleteUser)|DeleteUser|[Parameters](#Parametersusers.userDeleteUser)|Not Found|
|[az users user show-user](#users.userGetUser)|GetUser|[Parameters](#Parametersusers.userGetUser)|Not Found|

### <a name="CommandsInusers">Commands in `az users user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az users user create-extension](#usersCreateExtensions)|CreateExtensions|[Parameters](#ParametersusersCreateExtensions)|Not Found|
|[az users user create-license-detail](#usersCreateLicenseDetails)|CreateLicenseDetails|[Parameters](#ParametersusersCreateLicenseDetails)|Not Found|
|[az users user create-photo](#usersCreatePhotos)|CreatePhotos|[Parameters](#ParametersusersCreatePhotos)|Not Found|
|[az users user create-ref-created-object](#usersCreateRefCreatedObjects)|CreateRefCreatedObjects|[Parameters](#ParametersusersCreateRefCreatedObjects)|Not Found|
|[az users user create-ref-direct-report](#usersCreateRefDirectReports)|CreateRefDirectReports|[Parameters](#ParametersusersCreateRefDirectReports)|Not Found|
|[az users user create-ref-member-of](#usersCreateRefMemberOf)|CreateRefMemberOf|[Parameters](#ParametersusersCreateRefMemberOf)|Not Found|
|[az users user create-ref-oauth2-permission-grant](#usersCreateRefOauth2PermissionGrants)|CreateRefOauth2PermissionGrants|[Parameters](#ParametersusersCreateRefOauth2PermissionGrants)|Not Found|
|[az users user create-ref-owned-device](#usersCreateRefOwnedDevices)|CreateRefOwnedDevices|[Parameters](#ParametersusersCreateRefOwnedDevices)|Not Found|
|[az users user create-ref-owned-object](#usersCreateRefOwnedObjects)|CreateRefOwnedObjects|[Parameters](#ParametersusersCreateRefOwnedObjects)|Not Found|
|[az users user create-ref-registered-device](#usersCreateRefRegisteredDevices)|CreateRefRegisteredDevices|[Parameters](#ParametersusersCreateRefRegisteredDevices)|Not Found|
|[az users user create-ref-transitive-member-of](#usersCreateRefTransitiveMemberOf)|CreateRefTransitiveMemberOf|[Parameters](#ParametersusersCreateRefTransitiveMemberOf)|Not Found|
|[az users user delete-extension](#usersDeleteExtensions)|DeleteExtensions|[Parameters](#ParametersusersDeleteExtensions)|Not Found|
|[az users user delete-license-detail](#usersDeleteLicenseDetails)|DeleteLicenseDetails|[Parameters](#ParametersusersDeleteLicenseDetails)|Not Found|
|[az users user delete-outlook](#usersDeleteOutlook)|DeleteOutlook|[Parameters](#ParametersusersDeleteOutlook)|Not Found|
|[az users user delete-photo](#usersDeletePhotos)|DeletePhotos|[Parameters](#ParametersusersDeletePhotos)|Not Found|
|[az users user delete-photo](#usersDeletePhoto)|DeletePhoto|[Parameters](#ParametersusersDeletePhoto)|Not Found|
|[az users user delete-ref-manager](#usersDeleteRefManager)|DeleteRefManager|[Parameters](#ParametersusersDeleteRefManager)|Not Found|
|[az users user delete-setting](#usersDeleteSettings)|DeleteSettings|[Parameters](#ParametersusersDeleteSettings)|Not Found|
|[az users user list-created-object](#usersListCreatedObjects)|ListCreatedObjects|[Parameters](#ParametersusersListCreatedObjects)|Not Found|
|[az users user list-direct-report](#usersListDirectReports)|ListDirectReports|[Parameters](#ParametersusersListDirectReports)|Not Found|
|[az users user list-extension](#usersListExtensions)|ListExtensions|[Parameters](#ParametersusersListExtensions)|Not Found|
|[az users user list-license-detail](#usersListLicenseDetails)|ListLicenseDetails|[Parameters](#ParametersusersListLicenseDetails)|Not Found|
|[az users user list-member-of](#usersListMemberOf)|ListMemberOf|[Parameters](#ParametersusersListMemberOf)|Not Found|
|[az users user list-oauth2-permission-grant](#usersListOauth2PermissionGrants)|ListOauth2PermissionGrants|[Parameters](#ParametersusersListOauth2PermissionGrants)|Not Found|
|[az users user list-owned-device](#usersListOwnedDevices)|ListOwnedDevices|[Parameters](#ParametersusersListOwnedDevices)|Not Found|
|[az users user list-owned-object](#usersListOwnedObjects)|ListOwnedObjects|[Parameters](#ParametersusersListOwnedObjects)|Not Found|
|[az users user list-photo](#usersListPhotos)|ListPhotos|[Parameters](#ParametersusersListPhotos)|Not Found|
|[az users user list-ref-created-object](#usersListRefCreatedObjects)|ListRefCreatedObjects|[Parameters](#ParametersusersListRefCreatedObjects)|Not Found|
|[az users user list-ref-direct-report](#usersListRefDirectReports)|ListRefDirectReports|[Parameters](#ParametersusersListRefDirectReports)|Not Found|
|[az users user list-ref-member-of](#usersListRefMemberOf)|ListRefMemberOf|[Parameters](#ParametersusersListRefMemberOf)|Not Found|
|[az users user list-ref-oauth2-permission-grant](#usersListRefOauth2PermissionGrants)|ListRefOauth2PermissionGrants|[Parameters](#ParametersusersListRefOauth2PermissionGrants)|Not Found|
|[az users user list-ref-owned-device](#usersListRefOwnedDevices)|ListRefOwnedDevices|[Parameters](#ParametersusersListRefOwnedDevices)|Not Found|
|[az users user list-ref-owned-object](#usersListRefOwnedObjects)|ListRefOwnedObjects|[Parameters](#ParametersusersListRefOwnedObjects)|Not Found|
|[az users user list-ref-registered-device](#usersListRefRegisteredDevices)|ListRefRegisteredDevices|[Parameters](#ParametersusersListRefRegisteredDevices)|Not Found|
|[az users user list-ref-transitive-member-of](#usersListRefTransitiveMemberOf)|ListRefTransitiveMemberOf|[Parameters](#ParametersusersListRefTransitiveMemberOf)|Not Found|
|[az users user list-registered-device](#usersListRegisteredDevices)|ListRegisteredDevices|[Parameters](#ParametersusersListRegisteredDevices)|Not Found|
|[az users user list-transitive-member-of](#usersListTransitiveMemberOf)|ListTransitiveMemberOf|[Parameters](#ParametersusersListTransitiveMemberOf)|Not Found|
|[az users user set-ref-manager](#usersSetRefManager)|SetRefManager|[Parameters](#ParametersusersSetRefManager)|Not Found|
|[az users user show-extension](#usersGetExtensions)|GetExtensions|[Parameters](#ParametersusersGetExtensions)|Not Found|
|[az users user show-license-detail](#usersGetLicenseDetails)|GetLicenseDetails|[Parameters](#ParametersusersGetLicenseDetails)|Not Found|
|[az users user show-manager](#usersGetManager)|GetManager|[Parameters](#ParametersusersGetManager)|Not Found|
|[az users user show-outlook](#usersGetOutlook)|GetOutlook|[Parameters](#ParametersusersGetOutlook)|Not Found|
|[az users user show-photo](#usersGetPhotos)|GetPhotos|[Parameters](#ParametersusersGetPhotos)|Not Found|
|[az users user show-photo](#usersGetPhoto)|GetPhoto|[Parameters](#ParametersusersGetPhoto)|Not Found|
|[az users user show-ref-manager](#usersGetRefManager)|GetRefManager|[Parameters](#ParametersusersGetRefManager)|Not Found|
|[az users user show-setting](#usersGetSettings)|GetSettings|[Parameters](#ParametersusersGetSettings)|Not Found|
|[az users user update-extension](#usersUpdateExtensions)|UpdateExtensions|[Parameters](#ParametersusersUpdateExtensions)|Not Found|
|[az users user update-license-detail](#usersUpdateLicenseDetails)|UpdateLicenseDetails|[Parameters](#ParametersusersUpdateLicenseDetails)|Not Found|
|[az users user update-outlook](#usersUpdateOutlook)|UpdateOutlook|[Parameters](#ParametersusersUpdateOutlook)|Not Found|
|[az users user update-photo](#usersUpdatePhotos)|UpdatePhotos|[Parameters](#ParametersusersUpdatePhotos)|Not Found|
|[az users user update-photo](#usersUpdatePhoto)|UpdatePhoto|[Parameters](#ParametersusersUpdatePhoto)|Not Found|
|[az users user update-setting](#usersUpdateSettings)|UpdateSettings|[Parameters](#ParametersusersUpdateSettings)|Not Found|

### <a name="CommandsInusers.outlook">Commands in `az users user-outlook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az users user-outlook create-master-category](#users.outlookCreateMasterCategories)|CreateMasterCategories|[Parameters](#Parametersusers.outlookCreateMasterCategories)|Not Found|
|[az users user-outlook delete-master-category](#users.outlookDeleteMasterCategories)|DeleteMasterCategories|[Parameters](#Parametersusers.outlookDeleteMasterCategories)|Not Found|
|[az users user-outlook list-master-category](#users.outlookListMasterCategories)|ListMasterCategories|[Parameters](#Parametersusers.outlookListMasterCategories)|Not Found|
|[az users user-outlook show-master-category](#users.outlookGetMasterCategories)|GetMasterCategories|[Parameters](#Parametersusers.outlookGetMasterCategories)|Not Found|
|[az users user-outlook update-master-category](#users.outlookUpdateMasterCategories)|UpdateMasterCategories|[Parameters](#Parametersusers.outlookUpdateMasterCategories)|Not Found|

### <a name="CommandsInusers.settings">Commands in `az users user-setting` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az users user-setting delete-shift-preference](#users.settingsDeleteShiftPreferences)|DeleteShiftPreferences|[Parameters](#Parametersusers.settingsDeleteShiftPreferences)|Not Found|
|[az users user-setting show-shift-preference](#users.settingsGetShiftPreferences)|GetShiftPreferences|[Parameters](#Parametersusers.settingsGetShiftPreferences)|Not Found|
|[az users user-setting update-shift-preference](#users.settingsUpdateShiftPreferences)|UpdateShiftPreferences|[Parameters](#Parametersusers.settingsUpdateShiftPreferences)|Not Found|


## COMMAND DETAILS

### group `az users user`
#### <a name="users.userListUser">Command `az users user list`</a>

##### <a name="Parametersusers.userListUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.userUpdateUser">Command `az users user create`</a>

##### <a name="Parametersusers.userUpdateUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
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
|**--display-name**|string|The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.|display_name|displayName|
|**--employee-id**|string|The employee identifier assigned to the user by the organization. Supports $filter.|employee_id|employeeId|
|**--external-user-state**|string|For an external user invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Returned only on $select. Supports $filter with the supported values. For example: $filter=externalUserState eq 'PendingAcceptance'.|external_user_state|externalUserState|
|**--external-user-state-change-date-time**|date-time|Shows the timestamp for the latest change to the externalUserState property. Returned only on $select.|external_user_state_change_date_time|externalUserStateChangeDateTime|
|**--fax-number**|string|The fax number of the user.|fax_number|faxNumber|
|**--given-name**|string|The given name (first name) of the user. Supports $filter.|given_name|givenName|
|**--identities**|array|Represents the identities that can be used to sign in to this user account. An identity can be provided by Microsoft (also known as a local account), by organizations, or by social identity providers such as Facebook, Google, and Microsoft, and tied to a user account. May contain multiple items with the same signInType value. Supports $filter.|identities|identities|
|**--im-addresses**|array|The instant message voice over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only.|im_addresses|imAddresses|
|**--is-resource-account**|boolean|Do not use – reserved for future use.|is_resource_account|isResourceAccount|
|**--job-title**|string|The user’s job title. Supports $filter.|job_title|jobTitle|
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
|**--on-premises-immutable-id**|string|This property is used to associate an on-premises Active Directory user account to their Azure AD user object. This property must be specified when creating a new user account in the Graph if you are using a federated domain for the user’s userPrincipalName (UPN) property. Important: The $ and _ characters cannot be used when specifying this property. Supports $filter.|on_premises_immutable_id|onPremisesImmutableId|
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
|**--preferred-language**|string|The preferred language for the user. Should follow ISO 639-1 Code; for example 'en-US'.|preferred_language|preferredLanguage|
|**--provisioned-plans**|array|The plans that are provisioned for the user. Read-only. Not nullable.|provisioned_plans|provisionedPlans|
|**--proxy-addresses**|array|For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com'] The any operator is required for filter expressions on multi-valued properties. Read-only, Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--show-in-address-list**|boolean|true if the Outlook global address list should contain this user, otherwise false. If not set, this will be treated as true. For users invited through the invitation manager, this property will be set to false.|show_in_address_list|showInAddressList|
|**--sign-in-sessions-valid-from-date-time**|date-time|Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Read-only. Use revokeSignInSessions to reset.|sign_in_sessions_valid_from_date_time|signInSessionsValidFromDateTime|
|**--state**|string|The state or province in the user's address. Supports $filter.|state|state|
|**--street-address**|string|The street address of the user's place of business.|street_address|streetAddress|
|**--surname**|string|The user's surname (family name or last name). Supports $filter.|surname|surname|
|**--usage-location**|string|A two letter country code (ISO standard 3166). Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries.  Examples include: 'US', 'JP', and 'GB'. Not nullable. Supports $filter.|usage_location|usageLocation|
|**--user-principal-name**|string|The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant’s collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization. Supports $filter and $orderby.|user_principal_name|userPrincipalName|
|**--user-type**|string|A string value that can be used to classify user types in your directory, such as 'Member' and 'Guest'. Supports $filter.|user_type|userType|
|**--device-enrollment-limit**|integer|The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.|device_enrollment_limit|deviceEnrollmentLimit|
|**--about-me**|string|A freeform text entry field for the user to describe themselves.|about_me|aboutMe|
|**--birthday**|date-time|The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|birthday|birthday|
|**--hire-date**|date-time|The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|hire_date|hireDate|
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
|**--oauth2-permission-grants**|array||oauth2_permission_grants|oauth2PermissionGrants|
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
|**--mail-folders**|array|The user's mail folders. Read-only. Nullable.|mail_folders|mailFolders|
|**--messages**|array|The messages in a mailbox or folder. Read-only. Nullable.|messages|messages|
|**--people**|array|People that are relevant to the user. Read-only. Nullable.|people|people|
|**--photo**|object|profilePhoto|photo|photo|
|**--photos**|array||photos|photos|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|A collection of drives available for this user. Read-only.|drives|drives|
|**--followed-sites**|array||followed_sites|followedSites|
|**--extensions**|array|The collection of open extensions defined for the user. Read-only. Nullable.|extensions|extensions|
|**--managed-devices**|array|The managed devices associated with the user.|managed_devices|managedDevices|
|**--managed-app-registrations**|array|Zero or more managed app registrations that belong to the user.|managed_app_registrations|managedAppRegistrations|
|**--device-management-troubleshooting-events**|array|The list of troubleshooting events for this user.|device_management_troubleshooting_events|deviceManagementTroubleshootingEvents|
|**--activities**|array|The user's activities across devices. Read-only. Nullable.|activities|activities|
|**--online-meetings**|array||online_meetings|onlineMeetings|
|**--joined-teams**|array||joined_teams|joinedTeams|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|pages|pages|
|**--resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--id1**|string|Read-only.|id1|id|
|**--contribution-to-content-discovery-as-organization-disabled**|boolean||contribution_to_content_discovery_as_organization_disabled|contributionToContentDiscoveryAsOrganizationDisabled|
|**--contribution-to-content-discovery-disabled**|boolean||contribution_to_content_discovery_disabled|contributionToContentDiscoveryDisabled|
|**--id2**|string|Read-only.|id2|id|
|**--microsoft-graph-change-tracked-entity-created-date-time-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|microsoft_graph_change_tracked_entity_created_date_time_created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|
|**--id3**|string|Read-only.|id3|id|
|**--shared**|array|Calculated relationship identifying documents shared with or by the user. This includes URLs, file attachments, and reference attachments to OneDrive for Business and SharePoint files found in Outlook messages and meetings. This also includes URLs and reference attachments to Teams conversations. Ordered by recency of share.|shared|shared|
|**--trending**|array|Calculated relationship identifying documents trending around a user. Trending documents are calculated based on activity of the user's closest network of people and include files stored in OneDrive for Business and SharePoint. Trending insights help the user to discover potentially useful content that the user has access to, but has never viewed before.|trending|trending|
|**--used**|array|Calculated relationship identifying the latest documents viewed or modified by a user, including OneDrive for Business and SharePoint documents, ranked by recency of use.|used|used|
|**--id4**|string|Read-only.|id4|id|
|**--plans**|array|Read-only. Nullable. Returns the plannerTasks assigned to the user.|plans|plans|
|**--tasks**|array|Read-only. Nullable. Returns the plannerPlans shared with the user.|tasks|tasks|
|**--id5**|string|Read-only.|id5|id|
|**--master-categories**|array|A list of categories defined for the user.|master_categories|masterCategories|
|**--id6**|string|Read-only.|id6|id|
|**--overrides**|array|A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.|overrides|overrides|
|**--archive-folder**|string|Folder ID of an archive folder for the user.|archive_folder|archiveFolder|
|**--automatic-replies-setting**|object|automaticRepliesSetting|automatic_replies_setting|automaticRepliesSetting|
|**--date-format**|string|The date format for the user's mailbox.|date_format|dateFormat|
|**--delegate-meeting-message-delivery-options**|choice||delegate_meeting_message_delivery_options|delegateMeetingMessageDeliveryOptions|
|**--language**|object|localeInfo|language|language|
|**--time-format**|string|The time format for the user's mailbox.|time_format|timeFormat|
|**--time-zone**|string|The default time zone for the user's mailbox.|time_zone|timeZone|
|**--working-hours**|object|workingHours|working_hours|workingHours|

#### <a name="users.userCreateUser">Command `az users user create`</a>

##### <a name="Parametersusers.userCreateUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="users.userDeleteUser">Command `az users user delete-user`</a>

##### <a name="Parametersusers.userDeleteUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.userGetUser">Command `az users user show-user`</a>

##### <a name="Parametersusers.userGetUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az users user`
#### <a name="usersCreateExtensions">Command `az users user create-extension`</a>

##### <a name="ParametersusersCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

#### <a name="usersCreateLicenseDetails">Command `az users user create-license-detail`</a>

##### <a name="ParametersusersCreateLicenseDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--service-plans**|array|Information about the service plans assigned with the license. Read-only, Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related SubscribedSku object. Read-only|sku_id|skuId|
|**--sku-part-number**|string|Unique SKU display name. Equal to the skuPartNumber on the related SubscribedSku object; for example: 'AAD_Premium'. Read-only|sku_part_number|skuPartNumber|

#### <a name="usersCreatePhotos">Command `az users user create-photo`</a>

##### <a name="ParametersusersCreatePhotos">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

#### <a name="usersCreateRefCreatedObjects">Command `az users user create-ref-created-object`</a>

##### <a name="ParametersusersCreateRefCreatedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="usersCreateRefDirectReports">Command `az users user create-ref-direct-report`</a>

##### <a name="ParametersusersCreateRefDirectReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="usersCreateRefMemberOf">Command `az users user create-ref-member-of`</a>

##### <a name="ParametersusersCreateRefMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="usersCreateRefOauth2PermissionGrants">Command `az users user create-ref-oauth2-permission-grant`</a>

##### <a name="ParametersusersCreateRefOauth2PermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="usersCreateRefOwnedDevices">Command `az users user create-ref-owned-device`</a>

##### <a name="ParametersusersCreateRefOwnedDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="usersCreateRefOwnedObjects">Command `az users user create-ref-owned-object`</a>

##### <a name="ParametersusersCreateRefOwnedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="usersCreateRefRegisteredDevices">Command `az users user create-ref-registered-device`</a>

##### <a name="ParametersusersCreateRefRegisteredDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="usersCreateRefTransitiveMemberOf">Command `az users user create-ref-transitive-member-of`</a>

##### <a name="ParametersusersCreateRefTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="usersDeleteExtensions">Command `az users user delete-extension`</a>

##### <a name="ParametersusersDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteLicenseDetails">Command `az users user delete-license-detail`</a>

##### <a name="ParametersusersDeleteLicenseDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--license-details-id**|string|key: id of licenseDetails|license_details_id|licenseDetails-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteOutlook">Command `az users user delete-outlook`</a>

##### <a name="ParametersusersDeleteOutlook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeletePhotos">Command `az users user delete-photo`</a>

##### <a name="ParametersusersDeletePhotos">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeletePhoto">Command `az users user delete-photo`</a>

##### <a name="ParametersusersDeletePhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersDeleteRefManager">Command `az users user delete-ref-manager`</a>

##### <a name="ParametersusersDeleteRefManager">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteSettings">Command `az users user delete-setting`</a>

##### <a name="ParametersusersDeleteSettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListCreatedObjects">Command `az users user list-created-object`</a>

##### <a name="ParametersusersListCreatedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListDirectReports">Command `az users user list-direct-report`</a>

##### <a name="ParametersusersListDirectReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListExtensions">Command `az users user list-extension`</a>

##### <a name="ParametersusersListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListLicenseDetails">Command `az users user list-license-detail`</a>

##### <a name="ParametersusersListLicenseDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListMemberOf">Command `az users user list-member-of`</a>

##### <a name="ParametersusersListMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListOauth2PermissionGrants">Command `az users user list-oauth2-permission-grant`</a>

##### <a name="ParametersusersListOauth2PermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListOwnedDevices">Command `az users user list-owned-device`</a>

##### <a name="ParametersusersListOwnedDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListOwnedObjects">Command `az users user list-owned-object`</a>

##### <a name="ParametersusersListOwnedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListPhotos">Command `az users user list-photo`</a>

##### <a name="ParametersusersListPhotos">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListRefCreatedObjects">Command `az users user list-ref-created-object`</a>

##### <a name="ParametersusersListRefCreatedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="usersListRefDirectReports">Command `az users user list-ref-direct-report`</a>

##### <a name="ParametersusersListRefDirectReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="usersListRefMemberOf">Command `az users user list-ref-member-of`</a>

##### <a name="ParametersusersListRefMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="usersListRefOauth2PermissionGrants">Command `az users user list-ref-oauth2-permission-grant`</a>

##### <a name="ParametersusersListRefOauth2PermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="usersListRefOwnedDevices">Command `az users user list-ref-owned-device`</a>

##### <a name="ParametersusersListRefOwnedDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="usersListRefOwnedObjects">Command `az users user list-ref-owned-object`</a>

##### <a name="ParametersusersListRefOwnedObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="usersListRefRegisteredDevices">Command `az users user list-ref-registered-device`</a>

##### <a name="ParametersusersListRefRegisteredDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="usersListRefTransitiveMemberOf">Command `az users user list-ref-transitive-member-of`</a>

##### <a name="ParametersusersListRefTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="usersListRegisteredDevices">Command `az users user list-registered-device`</a>

##### <a name="ParametersusersListRegisteredDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListTransitiveMemberOf">Command `az users user list-transitive-member-of`</a>

##### <a name="ParametersusersListTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersSetRefManager">Command `az users user set-ref-manager`</a>

##### <a name="ParametersusersSetRefManager">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="usersGetExtensions">Command `az users user show-extension`</a>

##### <a name="ParametersusersGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetLicenseDetails">Command `az users user show-license-detail`</a>

##### <a name="ParametersusersGetLicenseDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--license-details-id**|string|key: id of licenseDetails|license_details_id|licenseDetails-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetManager">Command `az users user show-manager`</a>

##### <a name="ParametersusersGetManager">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetOutlook">Command `az users user show-outlook`</a>

##### <a name="ParametersusersGetOutlook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetPhotos">Command `az users user show-photo`</a>

##### <a name="ParametersusersGetPhotos">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetPhoto">Command `az users user show-photo`</a>

##### <a name="ParametersusersGetPhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersGetRefManager">Command `az users user show-ref-manager`</a>

##### <a name="ParametersusersGetRefManager">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

#### <a name="usersGetSettings">Command `az users user show-setting`</a>

##### <a name="ParametersusersGetSettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateExtensions">Command `az users user update-extension`</a>

##### <a name="ParametersusersUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="usersUpdateLicenseDetails">Command `az users user update-license-detail`</a>

##### <a name="ParametersusersUpdateLicenseDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--license-details-id**|string|key: id of licenseDetails|license_details_id|licenseDetails-id|
|**--id**|string|Read-only.|id|id|
|**--service-plans**|array|Information about the service plans assigned with the license. Read-only, Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related SubscribedSku object. Read-only|sku_id|skuId|
|**--sku-part-number**|string|Unique SKU display name. Equal to the skuPartNumber on the related SubscribedSku object; for example: 'AAD_Premium'. Read-only|sku_part_number|skuPartNumber|

#### <a name="usersUpdateOutlook">Command `az users user update-outlook`</a>

##### <a name="ParametersusersUpdateOutlook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--master-categories**|array|A list of categories defined for the user.|master_categories|masterCategories|

#### <a name="usersUpdatePhotos">Command `az users user update-photo`</a>

##### <a name="ParametersusersUpdatePhotos">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

#### <a name="usersUpdatePhoto">Command `az users user update-photo`</a>

##### <a name="ParametersusersUpdatePhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersUpdateSettings">Command `az users user update-setting`</a>

##### <a name="ParametersusersUpdateSettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--contribution-to-content-discovery-as-organization-disabled**|boolean||contribution_to_content_discovery_as_organization_disabled|contributionToContentDiscoveryAsOrganizationDisabled|
|**--contribution-to-content-discovery-disabled**|boolean||contribution_to_content_discovery_disabled|contributionToContentDiscoveryDisabled|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|

### group `az users user-outlook`
#### <a name="users.outlookCreateMasterCategories">Command `az users user-outlook create-master-category`</a>

##### <a name="Parametersusers.outlookCreateMasterCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--color**|choice||color|color|
|**--display-name**|string|A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.|display_name|displayName|

#### <a name="users.outlookDeleteMasterCategories">Command `az users user-outlook delete-master-category`</a>

##### <a name="Parametersusers.outlookDeleteMasterCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-category-id**|string|key: id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.outlookListMasterCategories">Command `az users user-outlook list-master-category`</a>

##### <a name="Parametersusers.outlookListMasterCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.outlookGetMasterCategories">Command `az users user-outlook show-master-category`</a>

##### <a name="Parametersusers.outlookGetMasterCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-category-id**|string|key: id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.outlookUpdateMasterCategories">Command `az users user-outlook update-master-category`</a>

##### <a name="Parametersusers.outlookUpdateMasterCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-category-id**|string|key: id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--id**|string|Read-only.|id|id|
|**--color**|choice||color|color|
|**--display-name**|string|A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.|display_name|displayName|

### group `az users user-setting`
#### <a name="users.settingsDeleteShiftPreferences">Command `az users user-setting delete-shift-preference`</a>

##### <a name="Parametersusers.settingsDeleteShiftPreferences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.settingsGetShiftPreferences">Command `az users user-setting show-shift-preference`</a>

##### <a name="Parametersusers.settingsGetShiftPreferences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.settingsUpdateShiftPreferences">Command `az users user-setting update-shift-preference`</a>

##### <a name="Parametersusers.settingsUpdateShiftPreferences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|
