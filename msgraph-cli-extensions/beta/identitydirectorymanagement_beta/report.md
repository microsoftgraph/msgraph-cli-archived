# Azure CLI Module Creation Report

### identitydirectorymanagement check-member-group

check-member-group a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--group-ids**|array||group_ids|groupIds|

### identitydirectorymanagement check-member-object

check-member-object a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--ids**|array||ids|ids|

### identitydirectorymanagement create-administrative-unit

create-administrative-unit a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-administrative-unit|CreateAdministrativeUnits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|An optional description for the administrative unit.|description|description|
|**--display-name**|string|Display name for the administrative unit.|display_name|displayName|
|**--visibility**|string|Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the adminstrative unit.|visibility|visibility|
|**--members**|array|Users and groups that are members of this Adminsitrative Unit. HTTP Methods: GET (list members), POST (add members), DELETE (remove members).|members|members|
|**--scoped-role-members**|array|Scoped-role members of this Administrative Unit.  HTTP Methods: GET (list scopedRoleMemberships), POST (add scopedRoleMembership), DELETE (remove scopedRoleMembership).|scoped_role_members|scopedRoleMembers|
|**--extensions**|array||extensions|extensions|

### identitydirectorymanagement create-apply-to

create-apply-to a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory.featureRolloutPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-apply-to|CreateAppliesTo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--feature-rollout-policy-id**|string|key: id of featureRolloutPolicy|feature_rollout_policy_id|featureRolloutPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

### identitydirectorymanagement create-command

create-command a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-command|CreateCommands|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--id**|string|Read-only.|id|id|
|**--app-service-name**|string||app_service_name|appServiceName|
|**--error**|string||error|error|
|**--package-family-name**|string||package_family_name|packageFamilyName|
|**--payload**|dictionary|payloadRequest|payload|payload|
|**--permission-ticket**|string||permission_ticket|permissionTicket|
|**--post-back-uri**|string||post_back_uri|postBackUri|
|**--status**|string||status|status|
|**--type**|string||type|type|
|**--responsepayload-id**|string|Read-only.|microsoft_graph_entity_id|id|

### identitydirectorymanagement create-contract

create-contract a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-contract|CreateContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--contract-type**|string|Type of contract.Possible values are: SyndicationPartner - Partner that exclusively resells and manages O365 and Intune for this customer. They resell and support their customers. BreadthPartner - Partner has the ability to provide administrative support for this customer. However, the partner is not allowed to resell to the customer.ResellerPartner - Partner that is similar to a syndication partner, except that the partner doesn’t have exclusive access to a tenant. In the syndication case, the customer cannot buy additional direct subscriptions from Microsoft or from other partners.|contract_type|contractType|
|**--customer-id**|uuid|The unique identifier for the customer tenant referenced by this partnership. Corresponds to the id property of the customer tenant's organization resource.|customer_id|customerId|
|**--default-domain-name**|string|A copy of the customer tenant's default domain name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's default domain name changes.|default_domain_name|defaultDomainName|
|**--display-name**|string|A copy of the customer tenant's display name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's display name changes.|display_name|displayName|

### identitydirectorymanagement create-deleted-item

create-deleted-item a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-deleted-item|CreateDeletedItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

### identitydirectorymanagement create-device

create-device a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices.device|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-device|CreateDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### identitydirectorymanagement create-directory-role

create-directory-role a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles.directoryRole|

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

### identitydirectorymanagement create-directory-role-template

create-directory-role-template a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoleTemplates.directoryRoleTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-role-template|CreateDirectoryRoleTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description to set for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name to set for the directory role. Read-only.|display_name|displayName|

### identitydirectorymanagement create-directory-setting

create-directory-setting a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|settings.directorySetting|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-setting|CreateDirectorySetting|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--template-id**|string||template_id|templateId|
|**--values**|array||values|values|

### identitydirectorymanagement create-directory-setting-template

create-directory-setting-template a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directorySettingTemplates.directorySettingTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-setting-template|CreateDirectorySettingTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--values**|array||values|values|

### identitydirectorymanagement create-domain

create-domain a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-domain|CreateDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--authentication-type**|string|Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Azure AD performs user authentication.Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. This property is read-only and is not nullable.|authentication_type|authenticationType|
|**--availability-status**|string|This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.|availability_status|availabilityStatus|
|**--is-admin-managed**|boolean|The value of the property is false if the DNS record management of the domain has been delegated to Microsoft 365. Otherwise, the value is true. Not nullable|is_admin_managed|isAdminManaged|
|**--is-default**|boolean|True if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable|is_default|isDefault|
|**--is-initial**|boolean|True if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable|is_initial|isInitial|
|**--is-root**|boolean|True if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable|is_root|isRoot|
|**--is-verified**|boolean|True if the domain has completed domain ownership verification. Not nullable|is_verified|isVerified|
|**--password-notification-window-in-days**|integer|Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.|password_notification_window_in_days|passwordNotificationWindowInDays|
|**--password-validity-period-in-days**|integer|Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.|password_validity_period_in_days|passwordValidityPeriodInDays|
|**--state**|object|domainState|state|state|
|**--supported-services**|array|The capabilities assigned to the domain.Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, YammerNot nullable|supported_services|supportedServices|
|**--domain-name-references**|array|Read-only, Nullable|domain_name_references|domainNameReferences|
|**--service-configuration-records**|array|DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services.Read-only, Nullable|service_configuration_records|serviceConfigurationRecords|
|**--verification-dns-records**|array|DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD.Read-only, Nullable|verification_dns_records|verificationDnsRecords|

### identitydirectorymanagement create-extension

create-extension a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--id**|string|Read-only.|id|id|

### identitydirectorymanagement create-feature-rollout-policy

create-feature-rollout-policy a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-feature-rollout-policy|CreateFeatureRolloutPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--feature**|choice||feature|feature|
|**--is-applied-to-organization**|boolean||is_applied_to_organization|isAppliedToOrganization|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--applies-to**|array||applies_to|appliesTo|

### identitydirectorymanagement create-org-contact

create-org-contact a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contacts.orgContact|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-org-contact|CreateOrgContact|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--addresses**|array||addresses|addresses|
|**--company-name**|string||company_name|companyName|
|**--department**|string||department|department|
|**--display-name**|string||display_name|displayName|
|**--given-name**|string||given_name|givenName|
|**--job-title**|string||job_title|jobTitle|
|**--mail**|string||mail|mail|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-premises-last-sync-date-time**|date-time||on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-provisioning-errors**|array||on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sync-enabled**|boolean||on_premises_sync_enabled|onPremisesSyncEnabled|
|**--phones**|array||phones|phones|
|**--proxy-addresses**|array||proxy_addresses|proxyAddresses|
|**--surname**|string||surname|surname|
|**--direct-reports**|array||direct_reports|directReports|
|**--manager**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|manager|manager|
|**--member-of**|array||member_of|memberOf|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|

### identitydirectorymanagement create-organization

create-organization a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization.organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-organization|CreateOrganization|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-plans**|array|The collection of service plans associated with the tenant. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|Telephone number for the organization. NOTE: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--city**|string|City name of the address for the organization.|city|city|
|**--country**|string|Country/region name of the address for the organization.|country|country|
|**--country-letter-code**|string|Country/region abbreviation for the organization.|country_letter_code|countryLetterCode|
|**--created-date-time**|date-time|Timestamp of when the organization was created. The value cannot be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--directory-size-quota**|object|directorySizeQuota|directory_size_quota|directorySizeQuota|
|**--display-name**|string|The display name for the tenant.|display_name|displayName|
|**--is-multiple-data-locations-for-services-enabled**|boolean|true if organization is Multi-Geo enabled; false if organization is not Multi-Geo enabled; null (default). Read-only. For more information, see OneDrive Online Multi-Geo.|is_multiple_data_locations_for_services_enabled|isMultipleDataLocationsForServicesEnabled|
|**--marketing-notification-emails**|array|Not nullable.|marketing_notification_emails|marketingNotificationEmails|
|**--on-premises-last-sync-date-time**|date-time|The time and date at which the tenant was last synced with the on-premise directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default).|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--postal-code**|string|Postal code of the address for the organization.|postal_code|postalCode|
|**--preferred-language**|string|The preferred language for the organization. Should follow ISO 639-1 Code; for example 'en'.|preferred_language|preferredLanguage|
|**--privacy-profile**|object|privacyProfile|privacy_profile|privacyProfile|
|**--provisioned-plans**|array|Not nullable.|provisioned_plans|provisionedPlans|
|**--security-compliance-notification-mails**|array||security_compliance_notification_mails|securityComplianceNotificationMails|
|**--security-compliance-notification-phones**|array||security_compliance_notification_phones|securityComplianceNotificationPhones|
|**--state**|string|State name of the address for the organization.|state|state|
|**--street**|string|Street name of the address for organization.|street|street|
|**--technical-notification-mails**|array|Not nullable.|technical_notification_mails|technicalNotificationMails|
|**--verified-domains**|array|The collection of domains associated with this tenant. Not nullable.|verified_domains|verifiedDomains|
|**--certificate-connector-setting**|object|Certificate connector settings.|certificate_connector_setting|certificateConnectorSetting|
|**--mobile-device-management-authority**|choice||mobile_device_management_authority|mobileDeviceManagementAuthority|
|**--certificate-based-auth-configuration**|array|Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.|certificate_based_auth_configuration|certificateBasedAuthConfiguration|
|**--extensions**|array|The collection of open extensions defined for the organization. Read-only. Nullable.|extensions|extensions|
|**--settings-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--settings-item-insights**|object|itemInsightsSettings|item_insights|itemInsights|
|**--settings-profile-card-properties**|array||profile_card_properties|profileCardProperties|
|**--branding-id**|string|Read-only.|id1|id|
|**--branding-background-color**|string||background_color|backgroundColor|
|**--branding-background-image**|byte-array||background_image|backgroundImage|
|**--branding-banner-logo**|byte-array||banner_logo|bannerLogo|
|**--branding-sign-in-page-text**|string||sign_in_page_text|signInPageText|
|**--branding-square-logo**|byte-array||square_logo|squareLogo|
|**--branding-username-hint-text**|string||username_hint_text|usernameHintText|
|**--branding-localizations**|array||localizations|localizations|

### identitydirectorymanagement create-profile-card-property

create-profile-card-property a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-profile-card-property|CreateProfileCardProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--id**|string|Read-only.|id|id|
|**--annotations**|array||annotations|annotations|
|**--directory-property-name**|string||directory_property_name|directoryPropertyName|

### identitydirectorymanagement create-ref-direct-report

create-ref-direct-report a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-direct-report|CreateRefDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirectorymanagement create-ref-domain-name-reference

create-ref-domain-name-reference a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-domain-name-reference|CreateRefDomainNameReferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirectorymanagement create-ref-member

create-ref-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member|CreateRefMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirectorymanagement create-ref-member-of

create-ref-member-of a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member-of|CreateRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirectorymanagement create-ref-registered-owner

create-ref-registered-owner a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-registered-owner|CreateRefRegisteredOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirectorymanagement create-ref-registered-user

create-ref-registered-user a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-registered-user|CreateRefRegisteredUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirectorymanagement create-ref-transitive-member-of

create-ref-transitive-member-of a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-transitive-member-of|CreateRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirectorymanagement create-scoped-member

create-scoped-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-scoped-member|CreateScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirectorymanagement create-scoped-role-member

create-scoped-role-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-scoped-role-member|CreateScopedRoleMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-scoped-role-membership-administrative-unit-id-administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|microsoft_graph_scoped_role_membership_administrative_unit_id_administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirectorymanagement create-scoped-role-member-of

create-scoped-role-member-of a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-scoped-role-member-of|CreateScopedRoleMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirectorymanagement create-service-configuration-record

create-service-configuration-record a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-service-configuration-record|CreateServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### identitydirectorymanagement create-subscribed-sku

create-subscribed-sku a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-subscribed-sku|CreateSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--applies-to**|string|For example, 'User' or 'Company'.|applies_to|appliesTo|
|**--capability-status**|string|Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.|capability_status|capabilityStatus|
|**--consumed-units**|integer|The number of licenses that have been assigned.|consumed_units|consumedUnits|
|**--prepaid-units**|object|licenseUnitsDetail|prepaid_units|prepaidUnits|
|**--service-plans**|array|Information about the service plans that are available with the SKU. Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|The unique identifier (GUID) for the service SKU.|sku_id|skuId|
|**--sku-part-number**|string|The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.|sku_part_number|skuPartNumber|

### identitydirectorymanagement create-verification-dns-record

create-verification-dns-record a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-verification-dns-record|CreateVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### identitydirectorymanagement delete

delete a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteScopedRoleMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirectorymanagement delta

delta a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### identitydirectorymanagement force-delete

force-delete a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|force-delete|forceDelete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--disable-user-accounts**|boolean||disable_user_accounts|disableUserAccounts|

### identitydirectorymanagement get-administrative-unit

get-administrative-unit a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-administrative-unit|GetAdministrativeUnits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-apply-to

get-apply-to a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory.featureRolloutPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-apply-to|GetAppliesTo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--feature-rollout-policy-id**|string|key: id of featureRolloutPolicy|feature_rollout_policy_id|featureRolloutPolicy-id|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-branding

get-branding a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-branding|GetBranding|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-by-id

get-by-id a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### identitydirectorymanagement get-command

get-command a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-command|GetCommands|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--command-id**|string|key: id of command|command_id|command-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-contract

get-contract a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-contract|GetContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-deleted-item

get-deleted-item a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-deleted-item|GetDeletedItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-device

get-device a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices.device|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device|GetDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--consistency-level**|string|Indicates the requested consistency level.|consistency_level|ConsistencyLevel|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-directory

get-directory a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory.directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory|GetDirectory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-directory-role

get-directory-role a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-role|GetDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-directory-role-template

get-directory-role-template a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoleTemplates.directoryRoleTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-role-template|GetDirectoryRoleTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-directory-setting

get-directory-setting a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|settings.directorySetting|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-setting|GetDirectorySetting|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-setting-id**|string|key: id of directorySetting|directory_setting_id|directorySetting-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-directory-setting-template

get-directory-setting-template a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directorySettingTemplates.directorySettingTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-setting-template|GetDirectorySettingTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-setting-template-id**|string|key: id of directorySettingTemplate|directory_setting_template_id|directorySettingTemplate-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-domain

get-domain a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-domain|GetDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-extension

get-extension a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-feature-rollout-policy

get-feature-rollout-policy a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-feature-rollout-policy|GetFeatureRolloutPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--feature-rollout-policy-id**|string|key: id of featureRolloutPolicy|feature_rollout_policy_id|featureRolloutPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-item-insight

get-item-insight a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-insight|GetItemInsights|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-manager

get-manager a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-manager|GetManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-member-group

get-member-group a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirectorymanagement get-member-object

get-member-object a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirectorymanagement get-org-contact

get-org-contact a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contacts.orgContact|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-org-contact|GetOrgContact|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--consistency-level**|string|Indicates the requested consistency level.|consistency_level|ConsistencyLevel|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-organization

get-organization a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization.organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-organization|GetOrganization|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-profile-card-property

get-profile-card-property a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-profile-card-property|GetProfileCardProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--profile-card-property-id**|string|key: id of profileCardProperty|profile_card_property_id|profileCardProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-ref-manager

get-ref-manager a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-manager|GetRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|

### identitydirectorymanagement get-scoped-member

get-scoped-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-scoped-member|GetScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-scoped-role-member

get-scoped-role-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-scoped-role-member|GetScopedRoleMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-scoped-role-member-of

get-scoped-role-member-of a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-scoped-role-member-of|GetScopedRoleMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-service-configuration-record

get-service-configuration-record a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-service-configuration-record|GetServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-setting

get-setting a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-setting|GetSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-subscribed-sku

get-subscribed-sku a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-subscribed-sku|GetSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement get-user-owned-object

get-user-owned-object a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-owned-object|getUserOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string||user_id|userId|
|**--type**|string||type|type|

### identitydirectorymanagement get-verification-dns-record

get-verification-dns-record a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-verification-dns-record|GetVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-administrative-unit

list-administrative-unit a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-administrative-unit|ListAdministrativeUnits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-apply-to

list-apply-to a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory.featureRolloutPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-apply-to|ListAppliesTo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--feature-rollout-policy-id**|string|key: id of featureRolloutPolicy|feature_rollout_policy_id|featureRolloutPolicy-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-command

list-command a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-command|ListCommands|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-contract

list-contract a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-contract|ListContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-deleted-item

list-deleted-item a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-deleted-item|ListDeletedItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-device

list-device a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices.device|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-device|ListDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--consistency-level**|string|Indicates the requested consistency level.|consistency_level|ConsistencyLevel|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-direct-report

list-direct-report a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-direct-report|ListDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-directory-role

list-directory-role a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles.directoryRole|

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

### identitydirectorymanagement list-directory-role-template

list-directory-role-template a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoleTemplates.directoryRoleTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-directory-role-template|ListDirectoryRoleTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-directory-setting

list-directory-setting a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|settings.directorySetting|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-directory-setting|ListDirectorySetting|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-directory-setting-template

list-directory-setting-template a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directorySettingTemplates.directorySettingTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-directory-setting-template|ListDirectorySettingTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-domain

list-domain a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-domain|ListDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-domain-name-reference

list-domain-name-reference a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-domain-name-reference|ListDomainNameReferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-extension

list-extension a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-feature-rollout-policy

list-feature-rollout-policy a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-feature-rollout-policy|ListFeatureRolloutPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-member

list-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member|ListMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-member-of

list-member-of a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member-of|ListMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-org-contact

list-org-contact a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contacts.orgContact|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-org-contact|ListOrgContact|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--consistency-level**|string|Indicates the requested consistency level.|consistency_level|ConsistencyLevel|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-organization

list-organization a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization.organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-organization|ListOrganization|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-profile-card-property

list-profile-card-property a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-profile-card-property|ListProfileCardProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-ref-direct-report

list-ref-direct-report a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-direct-report|ListRefDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirectorymanagement list-ref-domain-name-reference

list-ref-domain-name-reference a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-domain-name-reference|ListRefDomainNameReferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirectorymanagement list-ref-member

list-ref-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member|ListRefMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirectorymanagement list-ref-member-of

list-ref-member-of a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member-of|ListRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirectorymanagement list-ref-registered-owner

list-ref-registered-owner a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-registered-owner|ListRefRegisteredOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirectorymanagement list-ref-registered-user

list-ref-registered-user a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-registered-user|ListRefRegisteredUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirectorymanagement list-ref-transitive-member-of

list-ref-transitive-member-of a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-transitive-member-of|ListRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirectorymanagement list-registered-owner

list-registered-owner a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-registered-owner|ListRegisteredOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-registered-user

list-registered-user a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-registered-user|ListRegisteredUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-scoped-member

list-scoped-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-scoped-member|ListScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-scoped-role-member

list-scoped-role-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-scoped-role-member|ListScopedRoleMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-scoped-role-member-of

list-scoped-role-member-of a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-scoped-role-member-of|ListScopedRoleMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-service-configuration-record

list-service-configuration-record a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-service-configuration-record|ListServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-subscribed-sku

list-subscribed-sku a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-subscribed-sku|ListSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-transitive-member-of

list-transitive-member-of a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-transitive-member-of|ListTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement list-verification-dns-record

list-verification-dns-record a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-verification-dns-record|ListVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirectorymanagement restore

restore a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|

### identitydirectorymanagement set-mobile-device-management-authority

set-mobile-device-management-authority a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-mobile-device-management-authority|setMobileDeviceManagementAuthority|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|

### identitydirectorymanagement set-ref-manager

set-ref-manager a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-manager|SetRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### identitydirectorymanagement update-administrative-unit

update-administrative-unit a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-administrative-unit|UpdateAdministrativeUnits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|An optional description for the administrative unit.|description|description|
|**--display-name**|string|Display name for the administrative unit.|display_name|displayName|
|**--visibility**|string|Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the adminstrative unit.|visibility|visibility|
|**--members**|array|Users and groups that are members of this Adminsitrative Unit. HTTP Methods: GET (list members), POST (add members), DELETE (remove members).|members|members|
|**--scoped-role-members**|array|Scoped-role members of this Administrative Unit.  HTTP Methods: GET (list scopedRoleMemberships), POST (add scopedRoleMembership), DELETE (remove scopedRoleMembership).|scoped_role_members|scopedRoleMembers|
|**--extensions**|array||extensions|extensions|

### identitydirectorymanagement update-apply-to

update-apply-to a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory.featureRolloutPolicies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-apply-to|UpdateAppliesTo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--feature-rollout-policy-id**|string|key: id of featureRolloutPolicy|feature_rollout_policy_id|featureRolloutPolicy-id|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

### identitydirectorymanagement update-branding

update-branding a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-branding|UpdateBranding|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--id**|string|Read-only.|id|id|
|**--background-color**|string||background_color|backgroundColor|
|**--background-image**|byte-array||background_image|backgroundImage|
|**--banner-logo**|byte-array||banner_logo|bannerLogo|
|**--sign-in-page-text**|string||sign_in_page_text|signInPageText|
|**--square-logo**|byte-array||square_logo|squareLogo|
|**--username-hint-text**|string||username_hint_text|usernameHintText|
|**--localizations**|array||localizations|localizations|

### identitydirectorymanagement update-command

update-command a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-command|UpdateCommands|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--command-id**|string|key: id of command|command_id|command-id|
|**--id**|string|Read-only.|id|id|
|**--app-service-name**|string||app_service_name|appServiceName|
|**--error**|string||error|error|
|**--package-family-name**|string||package_family_name|packageFamilyName|
|**--payload**|dictionary|payloadRequest|payload|payload|
|**--permission-ticket**|string||permission_ticket|permissionTicket|
|**--post-back-uri**|string||post_back_uri|postBackUri|
|**--status**|string||status|status|
|**--type**|string||type|type|
|**--responsepayload-id**|string|Read-only.|microsoft_graph_entity_id|id|

### identitydirectorymanagement update-contract

update-contract a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-contract|UpdateContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--contract-type**|string|Type of contract.Possible values are: SyndicationPartner - Partner that exclusively resells and manages O365 and Intune for this customer. They resell and support their customers. BreadthPartner - Partner has the ability to provide administrative support for this customer. However, the partner is not allowed to resell to the customer.ResellerPartner - Partner that is similar to a syndication partner, except that the partner doesn’t have exclusive access to a tenant. In the syndication case, the customer cannot buy additional direct subscriptions from Microsoft or from other partners.|contract_type|contractType|
|**--customer-id**|uuid|The unique identifier for the customer tenant referenced by this partnership. Corresponds to the id property of the customer tenant's organization resource.|customer_id|customerId|
|**--default-domain-name**|string|A copy of the customer tenant's default domain name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's default domain name changes.|default_domain_name|defaultDomainName|
|**--display-name**|string|A copy of the customer tenant's display name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's display name changes.|display_name|displayName|

### identitydirectorymanagement update-deleted-item

update-deleted-item a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-deleted-item|UpdateDeletedItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

### identitydirectorymanagement update-device

update-device a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|devices.device|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device|UpdateDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|object|New property values|body|body|

### identitydirectorymanagement update-directory

update-directory a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory.directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory|UpdateDirectory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--administrative-units**|array||administrative_units|administrativeUnits|
|**--deleted-items**|array|Recently deleted items. Read-only. Nullable.|deleted_items|deletedItems|
|**--feature-rollout-policies**|array||feature_rollout_policies|featureRolloutPolicies|

### identitydirectorymanagement update-directory-role

update-directory-role a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory-role|UpdateDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name for the directory role. Read-only.|display_name|displayName|
|**--role-template-id**|string|The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only.|role_template_id|roleTemplateId|
|**--members**|array|Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable.|members|members|
|**--scoped-members**|array||scoped_members|scopedMembers|

### identitydirectorymanagement update-directory-role-template

update-directory-role-template a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoleTemplates.directoryRoleTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory-role-template|UpdateDirectoryRoleTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description to set for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name to set for the directory role. Read-only.|display_name|displayName|

### identitydirectorymanagement update-directory-setting

update-directory-setting a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|settings.directorySetting|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory-setting|UpdateDirectorySetting|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-setting-id**|string|key: id of directorySetting|directory_setting_id|directorySetting-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--template-id**|string||template_id|templateId|
|**--values**|array||values|values|

### identitydirectorymanagement update-directory-setting-template

update-directory-setting-template a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directorySettingTemplates.directorySettingTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory-setting-template|UpdateDirectorySettingTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-setting-template-id**|string|key: id of directorySettingTemplate|directory_setting_template_id|directorySettingTemplate-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--values**|array||values|values|

### identitydirectorymanagement update-domain

update-domain a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-domain|UpdateDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--authentication-type**|string|Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Azure AD performs user authentication.Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. This property is read-only and is not nullable.|authentication_type|authenticationType|
|**--availability-status**|string|This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.|availability_status|availabilityStatus|
|**--is-admin-managed**|boolean|The value of the property is false if the DNS record management of the domain has been delegated to Microsoft 365. Otherwise, the value is true. Not nullable|is_admin_managed|isAdminManaged|
|**--is-default**|boolean|True if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable|is_default|isDefault|
|**--is-initial**|boolean|True if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable|is_initial|isInitial|
|**--is-root**|boolean|True if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable|is_root|isRoot|
|**--is-verified**|boolean|True if the domain has completed domain ownership verification. Not nullable|is_verified|isVerified|
|**--password-notification-window-in-days**|integer|Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.|password_notification_window_in_days|passwordNotificationWindowInDays|
|**--password-validity-period-in-days**|integer|Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.|password_validity_period_in_days|passwordValidityPeriodInDays|
|**--state**|object|domainState|state|state|
|**--supported-services**|array|The capabilities assigned to the domain.Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, YammerNot nullable|supported_services|supportedServices|
|**--domain-name-references**|array|Read-only, Nullable|domain_name_references|domainNameReferences|
|**--service-configuration-records**|array|DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services.Read-only, Nullable|service_configuration_records|serviceConfigurationRecords|
|**--verification-dns-records**|array|DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD.Read-only, Nullable|verification_dns_records|verificationDnsRecords|

### identitydirectorymanagement update-extension

update-extension a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### identitydirectorymanagement update-feature-rollout-policy

update-feature-rollout-policy a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-feature-rollout-policy|UpdateFeatureRolloutPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--feature-rollout-policy-id**|string|key: id of featureRolloutPolicy|feature_rollout_policy_id|featureRolloutPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--feature**|choice||feature|feature|
|**--is-applied-to-organization**|boolean||is_applied_to_organization|isAppliedToOrganization|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--applies-to**|array||applies_to|appliesTo|

### identitydirectorymanagement update-item-insight

update-item-insight a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item-insight|UpdateItemInsights|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--id**|string|Read-only.|id|id|
|**--disabled-for-group**|string||disabled_for_group|disabledForGroup|
|**--is-enabled-in-organization**|boolean||is_enabled_in_organization|isEnabledInOrganization|

### identitydirectorymanagement update-org-contact

update-org-contact a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|contacts.orgContact|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-org-contact|UpdateOrgContact|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--addresses**|array||addresses|addresses|
|**--company-name**|string||company_name|companyName|
|**--department**|string||department|department|
|**--display-name**|string||display_name|displayName|
|**--given-name**|string||given_name|givenName|
|**--job-title**|string||job_title|jobTitle|
|**--mail**|string||mail|mail|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-premises-last-sync-date-time**|date-time||on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-provisioning-errors**|array||on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sync-enabled**|boolean||on_premises_sync_enabled|onPremisesSyncEnabled|
|**--phones**|array||phones|phones|
|**--proxy-addresses**|array||proxy_addresses|proxyAddresses|
|**--surname**|string||surname|surname|
|**--direct-reports**|array||direct_reports|directReports|
|**--manager**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|manager|manager|
|**--member-of**|array||member_of|memberOf|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|

### identitydirectorymanagement update-organization

update-organization a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization.organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-organization|UpdateOrganization|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-plans**|array|The collection of service plans associated with the tenant. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|Telephone number for the organization. NOTE: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--city**|string|City name of the address for the organization.|city|city|
|**--country**|string|Country/region name of the address for the organization.|country|country|
|**--country-letter-code**|string|Country/region abbreviation for the organization.|country_letter_code|countryLetterCode|
|**--created-date-time**|date-time|Timestamp of when the organization was created. The value cannot be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--directory-size-quota**|object|directorySizeQuota|directory_size_quota|directorySizeQuota|
|**--display-name**|string|The display name for the tenant.|display_name|displayName|
|**--is-multiple-data-locations-for-services-enabled**|boolean|true if organization is Multi-Geo enabled; false if organization is not Multi-Geo enabled; null (default). Read-only. For more information, see OneDrive Online Multi-Geo.|is_multiple_data_locations_for_services_enabled|isMultipleDataLocationsForServicesEnabled|
|**--marketing-notification-emails**|array|Not nullable.|marketing_notification_emails|marketingNotificationEmails|
|**--on-premises-last-sync-date-time**|date-time|The time and date at which the tenant was last synced with the on-premise directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default).|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--postal-code**|string|Postal code of the address for the organization.|postal_code|postalCode|
|**--preferred-language**|string|The preferred language for the organization. Should follow ISO 639-1 Code; for example 'en'.|preferred_language|preferredLanguage|
|**--privacy-profile**|object|privacyProfile|privacy_profile|privacyProfile|
|**--provisioned-plans**|array|Not nullable.|provisioned_plans|provisionedPlans|
|**--security-compliance-notification-mails**|array||security_compliance_notification_mails|securityComplianceNotificationMails|
|**--security-compliance-notification-phones**|array||security_compliance_notification_phones|securityComplianceNotificationPhones|
|**--state**|string|State name of the address for the organization.|state|state|
|**--street**|string|Street name of the address for organization.|street|street|
|**--technical-notification-mails**|array|Not nullable.|technical_notification_mails|technicalNotificationMails|
|**--verified-domains**|array|The collection of domains associated with this tenant. Not nullable.|verified_domains|verifiedDomains|
|**--certificate-connector-setting**|object|Certificate connector settings.|certificate_connector_setting|certificateConnectorSetting|
|**--mobile-device-management-authority**|choice||mobile_device_management_authority|mobileDeviceManagementAuthority|
|**--certificate-based-auth-configuration**|array|Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.|certificate_based_auth_configuration|certificateBasedAuthConfiguration|
|**--extensions**|array|The collection of open extensions defined for the organization. Read-only. Nullable.|extensions|extensions|
|**--settings-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--settings-item-insights**|object|itemInsightsSettings|item_insights|itemInsights|
|**--settings-profile-card-properties**|array||profile_card_properties|profileCardProperties|
|**--branding-id**|string|Read-only.|id1|id|
|**--branding-background-color**|string||background_color|backgroundColor|
|**--branding-background-image**|byte-array||background_image|backgroundImage|
|**--branding-banner-logo**|byte-array||banner_logo|bannerLogo|
|**--branding-sign-in-page-text**|string||sign_in_page_text|signInPageText|
|**--branding-square-logo**|byte-array||square_logo|squareLogo|
|**--branding-username-hint-text**|string||username_hint_text|usernameHintText|
|**--branding-localizations**|array||localizations|localizations|

### identitydirectorymanagement update-profile-card-property

update-profile-card-property a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-profile-card-property|UpdateProfileCardProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--profile-card-property-id**|string|key: id of profileCardProperty|profile_card_property_id|profileCardProperty-id|
|**--id**|string|Read-only.|id|id|
|**--annotations**|array||annotations|annotations|
|**--directory-property-name**|string||directory_property_name|directoryPropertyName|

### identitydirectorymanagement update-scoped-member

update-scoped-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-scoped-member|UpdateScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirectorymanagement update-scoped-role-member

update-scoped-role-member a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-scoped-role-member|UpdateScopedRoleMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-scoped-role-membership-administrative-unit-id-administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|microsoft_graph_scoped_role_membership_administrative_unit_id_administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirectorymanagement update-scoped-role-member-of

update-scoped-role-member-of a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-scoped-role-member-of|UpdateScopedRoleMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirectorymanagement update-service-configuration-record

update-service-configuration-record a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-service-configuration-record|UpdateServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### identitydirectorymanagement update-setting

update-setting a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-setting|UpdateSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--id**|string|Read-only.|id|id|
|**--item-insights**|object|itemInsightsSettings|item_insights|itemInsights|
|**--profile-card-properties**|array||profile_card_properties|profileCardProperties|

### identitydirectorymanagement update-subscribed-sku

update-subscribed-sku a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-subscribed-sku|UpdateSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--id**|string|Read-only.|id|id|
|**--applies-to**|string|For example, 'User' or 'Company'.|applies_to|appliesTo|
|**--capability-status**|string|Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.|capability_status|capabilityStatus|
|**--consumed-units**|integer|The number of licenses that have been assigned.|consumed_units|consumedUnits|
|**--prepaid-units**|object|licenseUnitsDetail|prepaid_units|prepaidUnits|
|**--service-plans**|array|Information about the service plans that are available with the SKU. Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|The unique identifier (GUID) for the service SKU.|sku_id|skuId|
|**--sku-part-number**|string|The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.|sku_part_number|skuPartNumber|

### identitydirectorymanagement update-verification-dns-record

update-verification-dns-record a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-verification-dns-record|UpdateVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### identitydirectorymanagement validate-property

validate-property a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|organization|

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

### identitydirectorymanagement verify

verify a identitydirectorymanagement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirectorymanagement|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|verify|verify|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
