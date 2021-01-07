# Azure CLI Module Creation Report

### devicescorpmgt assign

assign a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|assign|assign|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--assignments**|array||assignments|assignments|

### devicescorpmgt create-android-managed-app-protection

create-android-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-android-managed-app-protection|CreateAndroidManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

### devicescorpmgt create-app

create-app a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-app|CreateApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--mobile-app-identifier**|dictionary|The identifier for a mobile app.|mobile_app_identifier|mobileAppIdentifier|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt create-applied-policy

create-applied-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-applied-policy|CreateAppliedPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt create-assignment

create-assignment a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-assignment|CreateAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--target**|dictionary|Base type for assignment targets.|target|target|

### devicescorpmgt create-default-managed-app-protection

create-default-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-default-managed-app-protection|CreateDefaultManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

### devicescorpmgt create-device-compliance-policy-state

create-device-compliance-policy-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-device-compliance-policy-state|CreateDeviceCompliancePolicyStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the policy for this policyBase|display_name|displayName|
|**--platform-type**|choice||platform_type|platformType|
|**--setting-count**|integer|Count of how many setting a policy holds|setting_count|settingCount|
|**--setting-states**|array||setting_states|settingStates|
|**--state**|choice||state|state|
|**--version**|integer|The version of the policy|version|version|

### devicescorpmgt create-device-configuration-state

create-device-configuration-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-device-configuration-state|CreateDeviceConfigurationStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the policy for this policyBase|display_name|displayName|
|**--platform-type**|choice||platform_type|platformType|
|**--setting-count**|integer|Count of how many setting a policy holds|setting_count|settingCount|
|**--setting-states**|array||setting_states|settingStates|
|**--state**|choice||state|state|
|**--version**|integer|The version of the policy|version|version|

### devicescorpmgt create-device-management-troubleshooting-event

create-device-management-troubleshooting-event a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-device-management-troubleshooting-event|CreateDeviceManagementTroubleshootingEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--correlation-id**|string|Id used for tracing the failure in the service.|correlation_id|correlationId|
|**--event-date-time**|date-time|Time when the event occurred .|event_date_time|eventDateTime|

### devicescorpmgt create-device-state

create-device-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedEBooks.userStateSummary|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-device-state|CreateDeviceStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--id**|string|Read-only.|id|id|
|**--device-id**|string|Device Id.|device_id|deviceId|
|**--device-name**|string|Device name.|device_name|deviceName|
|**--error-code**|string|The error code for install failures.|error_code|errorCode|
|**--install-state**|choice||install_state|installState|
|**--last-sync-date-time**|date-time|Last sync date and time.|last_sync_date_time|lastSyncDateTime|
|**--os-description**|string|OS Description.|os_description|osDescription|
|**--os-version**|string|OS Version.|os_version|osVersion|
|**--user-name**|string|Device User Name.|user_name|userName|

### devicescorpmgt create-device-statuses

create-device-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-device-statuses|CreateDeviceStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--compliance-grace-period-expiration-date-time**|date-time|The DateTime when device compliance grace period expires|compliance_grace_period_expiration_date_time|complianceGracePeriodExpirationDateTime|
|**--device-display-name**|string|Device name of the DevicePolicyStatus.|device_display_name|deviceDisplayName|
|**--device-model**|string|The device model that is being reported|device_model|deviceModel|
|**--last-reported-date-time**|date-time|Last modified date time of the policy report.|last_reported_date_time|lastReportedDateTime|
|**--status**|choice||status|status|
|**--user-name**|string|The User Name that is being reported|user_name|userName|
|**--user-principal-name**|string|UserPrincipalName.|user_principal_name|userPrincipalName|

### devicescorpmgt create-intended-policy

create-intended-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-intended-policy|CreateIntendedPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt create-io-managed-app-protection

create-io-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-io-managed-app-protection|CreateIosManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

### devicescorpmgt create-managed-app-policy

create-managed-app-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-managed-app-policy|CreateManagedAppPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt create-managed-app-registration

create-managed-app-registration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-managed-app-registration|CreateManagedAppRegistrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--app-identifier**|dictionary|The identifier for a mobile app.|app_identifier|appIdentifier|
|**--application-version**|string|App version|application_version|applicationVersion|
|**--created-date-time**|date-time|Date and time of creation|created_date_time|createdDateTime|
|**--device-name**|string|Host device name|device_name|deviceName|
|**--device-tag**|string|App management SDK generated tag, which helps relate apps hosted on the same device. Not guaranteed to relate apps in all conditions.|device_tag|deviceTag|
|**--device-type**|string|Host device type|device_type|deviceType|
|**--flagged-reasons**|array|Zero or more reasons an app registration is flagged. E.g. app running on rooted device|flagged_reasons|flaggedReasons|
|**--last-sync-date-time**|date-time|Date and time of last the app synced with management service.|last_sync_date_time|lastSyncDateTime|
|**--management-sdk-version**|string|App management SDK version|management_sdk_version|managementSdkVersion|
|**--platform-version**|string|Operating System version|platform_version|platformVersion|
|**--user-id**|string|The user Id to who this app registration belongs.|user_id|userId|
|**--version**|string|Version of the entity.|version|version|
|**--applied-policies**|array|Zero or more policys already applied on the registered app when it last synchronized with managment service.|applied_policies|appliedPolicies|
|**--intended-policies**|array|Zero or more policies admin intended for the app as of now.|intended_policies|intendedPolicies|
|**--operations**|array|Zero or more long running operations triggered on the app registration.|operations|operations|

### devicescorpmgt create-managed-app-statuses

create-managed-app-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-managed-app-statuses|CreateManagedAppStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Friendly name of the status report.|display_name|displayName|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt create-managed-device

create-managed-device a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-managed-device|CreateManagedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|New navigation property|body|body|

### devicescorpmgt create-managed-e-book

create-managed-e-book a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-managed-e-book|CreateManagedEBooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time when the eBook file was created.|created_date_time|createdDateTime|
|**--description**|string|Description.|description|description|
|**--display-name**|string|Name of the eBook.|display_name|displayName|
|**--information-url**|string|The more information Url.|information_url|informationUrl|
|**--large-cover**|object|Contains properties for a generic mime content.|large_cover|largeCover|
|**--last-modified-date-time**|date-time|The date and time when the eBook was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--privacy-information-url**|string|The privacy statement Url.|privacy_information_url|privacyInformationUrl|
|**--published-date-time**|date-time|The date and time when the eBook was published.|published_date_time|publishedDateTime|
|**--publisher**|string|Publisher.|publisher|publisher|
|**--assignments**|array|The list of assignments for this eBook.|assignments|assignments|
|**--device-states**|array|The list of installation states for this eBook.|device_states|deviceStates|
|**--install-summary**|object|Contains properties for the installation summary of a book for a device.|install_summary|installSummary|
|**--user-state-summary**|array|The list of installation states for this eBook.|user_state_summary|userStateSummary|

### devicescorpmgt create-mdm-window-information-protection-policy

create-mdm-window-information-protection-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-mdm-window-information-protection-policy|CreateMdmWindowsInformationProtectionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--azure-rights-management-services-allowed**|boolean|Specifies whether to allow Azure RMS encryption for WIP|azure_rights_management_services_allowed|azureRightsManagementServicesAllowed|
|**--data-recovery-certificate**|object|Windows Information Protection DataRecoveryCertificate|data_recovery_certificate|dataRecoveryCertificate|
|**--enforcement-level**|choice||enforcement_level|enforcementLevel|
|**--enterprise-domain**|string|Primary enterprise domain|enterprise_domain|enterpriseDomain|
|**--enterprise-internal-proxy-servers**|array|This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies|enterprise_internal_proxy_servers|enterpriseInternalProxyServers|
|**--enterprise-ip-ranges**|array|Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to|enterprise_ip_ranges|enterpriseIPRanges|
|**--enterprise-ip-ranges-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false|enterprise_ip_ranges_are_authoritative|enterpriseIPRangesAreAuthoritative|
|**--enterprise-network-domain-names**|array|This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to|enterprise_network_domain_names|enterpriseNetworkDomainNames|
|**--enterprise-protected-domain-names**|array|List of enterprise domains to be protected|enterprise_protected_domain_names|enterpriseProtectedDomainNames|
|**--enterprise-proxied-domains**|array|Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy|enterprise_proxied_domains|enterpriseProxiedDomains|
|**--enterprise-proxy-servers**|array|This is a list of proxy servers. Any server not on this list is considered non-enterprise|enterprise_proxy_servers|enterpriseProxyServers|
|**--enterprise-proxy-servers-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false|enterprise_proxy_servers_are_authoritative|enterpriseProxyServersAreAuthoritative|
|**--exempt-apps**|array|Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.|exempt_apps|exemptApps|
|**--icons-visible**|boolean|Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app|icons_visible|iconsVisible|
|**--indexing-encrypted-stores-or-items-blocked**|boolean|This switch is for the Windows Search Indexer, to allow or disallow indexing of items|indexing_encrypted_stores_or_items_blocked|indexingEncryptedStoresOrItemsBlocked|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--neutral-domain-resources**|array|List of domain names that can used for work or personal resource|neutral_domain_resources|neutralDomainResources|
|**--protected-apps**|array|Protected applications can access enterprise data and the data handled by those applications are protected with encryption|protected_apps|protectedApps|
|**--protection-under-lock-config-required**|boolean|Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured|protection_under_lock_config_required|protectionUnderLockConfigRequired|
|**--revoke-on-unenroll-disabled**|boolean|This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.|revoke_on_unenroll_disabled|revokeOnUnenrollDisabled|
|**--rights-management-services-template-id**|uuid|TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access|rights_management_services_template_id|rightsManagementServicesTemplateId|
|**--smb-auto-encrypted-file-extensions**|array|Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary|smb_auto_encrypted_file_extensions|smbAutoEncryptedFileExtensions|
|**--assignments**|array|Navigation property to list of security groups targeted for policy.|assignments|assignments|
|**--exempt-app-locker-files**|array|Another way to input exempt apps through xml files|exempt_app_locker_files|exemptAppLockerFiles|
|**--protected-app-locker-files**|array|Another way to input protected apps through xml files|protected_app_locker_files|protectedAppLockerFiles|

### devicescorpmgt create-mobile-app

create-mobile-app a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-mobile-app|CreateMobileApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the app was created.|created_date_time|createdDateTime|
|**--description**|string|The description of the app.|description|description|
|**--developer**|string|The developer of the app.|developer|developer|
|**--display-name**|string|The admin provided or imported title of the app.|display_name|displayName|
|**--information-url**|string|The more information Url.|information_url|informationUrl|
|**--is-featured**|boolean|The value indicating whether the app is marked as featured by the admin.|is_featured|isFeatured|
|**--large-icon**|object|Contains properties for a generic mime content.|large_icon|largeIcon|
|**--last-modified-date-time**|date-time|The date and time the app was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--notes**|string|Notes for the app.|notes|notes|
|**--owner**|string|The owner of the app.|owner|owner|
|**--privacy-information-url**|string|The privacy statement Url.|privacy_information_url|privacyInformationUrl|
|**--publisher**|string|The publisher of the app.|publisher|publisher|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--assignments**|array|The list of group assignments for this mobile app.|assignments|assignments|
|**--categories**|array|The list of categories for this app.|categories|categories|

### devicescorpmgt create-mobile-app-category

create-mobile-app-category a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-mobile-app-category|CreateMobileAppCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the app category.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time the mobileAppCategory was last modified.|last_modified_date_time|lastModifiedDateTime|

### devicescorpmgt create-mobile-app-configuration

create-mobile-app-configuration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-mobile-app-configuration|CreateMobileAppConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|DateTime the object was created.|created_date_time|createdDateTime|
|**--description**|string|Admin provided description of the Device Configuration.|description|description|
|**--display-name**|string|Admin provided name of the device configuration.|display_name|displayName|
|**--last-modified-date-time**|date-time|DateTime the object was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--targeted-mobile-apps**|array|the associated app.|targeted_mobile_apps|targetedMobileApps|
|**--version**|integer|Version of the device configuration.|version|version|
|**--assignments**|array|The list of group assignemenets for app configration.|assignments|assignments|
|**--device-statuses**|array|List of ManagedDeviceMobileAppConfigurationDeviceStatus.|device_statuses|deviceStatuses|
|**--device-status-summary**|object|Contains properties, inherited properties and actions for an MDM mobile app configuration device status summary.|device_status_summary|deviceStatusSummary|
|**--user-statuses**|array|List of ManagedDeviceMobileAppConfigurationUserStatus.|user_statuses|userStatuses|
|**--user-status-summary**|object|Contains properties, inherited properties and actions for an MDM mobile app configuration user status summary.|user_status_summary|userStatusSummary|

### devicescorpmgt create-operation

create-operation a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-operation|CreateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The operation name.|display_name|displayName|
|**--last-modified-date-time**|date-time|The last time the app operation was modified.|last_modified_date_time|lastModifiedDateTime|
|**--state**|string|The current state of the operation|state|state|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt create-ref-category

create-ref-category a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-category|CreateRefCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### devicescorpmgt create-ref-managed-app-registration

create-ref-managed-app-registration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-managed-app-registration|CreateRefManagedAppRegistrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### devicescorpmgt create-targeted-managed-app-configuration

create-targeted-managed-app-configuration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-targeted-managed-app-configuration|CreateTargetedManagedAppConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--custom-settings**|array|A set of string key and string value pairs to be sent to apps for users to whom the configuration is scoped, unalterned by this service|custom_settings|customSettings|
|**--deployed-app-count**|integer|Count of apps to which the current policy is deployed.|deployed_app_count|deployedAppCount|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--apps**|array|List of apps to which the policy is deployed.|apps|apps|
|**--assignments**|array|Navigation property to list of inclusion and exclusion groups to which the policy is deployed.|assignments|assignments|
|**--deployment-summary-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--deployment-summary-configuration-deployed-user-count**|integer|Not yet documented|configuration_deployed_user_count|configurationDeployedUserCount|
|**--deployment-summary-configuration-deployment-summary-per-app**|array|Not yet documented|configuration_deployment_summary_per_app|configurationDeploymentSummaryPerApp|
|**--deployment-summary-display-name**|string|Not yet documented|microsoft_graph_managed_app_policy_deployment_summary_display_name|displayName|
|**--deployment-summary-last-refresh-time**|date-time|Not yet documented|last_refresh_time|lastRefreshTime|
|**--deployment-summary-version**|string|Version of the entity.|microsoft_graph_managed_app_policy_deployment_summary_version|version|

### devicescorpmgt create-user-state-summary

create-user-state-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedEBooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user-state-summary|CreateUserStateSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--id**|string|Read-only.|id|id|
|**--failed-device-count**|integer|Failed Device Count.|failed_device_count|failedDeviceCount|
|**--installed-device-count**|integer|Installed Device Count.|installed_device_count|installedDeviceCount|
|**--not-installed-device-count**|integer|Not installed device count.|not_installed_device_count|notInstalledDeviceCount|
|**--user-name**|string|User name.|user_name|userName|
|**--device-states**|array|The install state of the eBook.|device_states|deviceStates|

### devicescorpmgt create-user-statuses

create-user-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user-statuses|CreateUserStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--devices-count**|integer|Devices count for that user.|devices_count|devicesCount|
|**--last-reported-date-time**|date-time|Last modified date time of the policy report.|last_reported_date_time|lastReportedDateTime|
|**--status**|choice||status|status|
|**--user-display-name**|string|User name of the DevicePolicyStatus.|user_display_name|userDisplayName|
|**--user-principal-name**|string|UserPrincipalName.|user_principal_name|userPrincipalName|

### devicescorpmgt create-vpp-token

create-vpp-token a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-vpp-token|CreateVppTokens|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--apple-id**|string|The apple Id associated with the given Apple Volume Purchase Program Token.|apple_id|appleId|
|**--automatically-update-apps**|boolean|Whether or not apps for the VPP token will be automatically updated.|automatically_update_apps|automaticallyUpdateApps|
|**--country-or-region**|string|Whether or not apps for the VPP token will be automatically updated.|country_or_region|countryOrRegion|
|**--expiration-date-time**|date-time|The expiration date time of the Apple Volume Purchase Program Token.|expiration_date_time|expirationDateTime|
|**--last-modified-date-time**|date-time|Last modification date time associated with the Apple Volume Purchase Program Token.|last_modified_date_time|lastModifiedDateTime|
|**--last-sync-date-time**|date-time|The last time when an application sync was done with the Apple volume purchase program service using the Apple Volume Purchase Program Token.|last_sync_date_time|lastSyncDateTime|
|**--last-sync-status**|choice||last_sync_status|lastSyncStatus|
|**--organization-name**|string|The organization associated with the Apple Volume Purchase Program Token|organization_name|organizationName|
|**--state**|choice||state|state|
|**--token**|string|The Apple Volume Purchase Program Token string downloaded from the Apple Volume Purchase Program.|token|token|
|**--vpp-token-account-type**|choice||vpp_token_account_type|vppTokenAccountType|

### devicescorpmgt create-window-information-protection-policy

create-window-information-protection-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-window-information-protection-policy|CreateWindowsInformationProtectionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--azure-rights-management-services-allowed**|boolean|Specifies whether to allow Azure RMS encryption for WIP|azure_rights_management_services_allowed|azureRightsManagementServicesAllowed|
|**--data-recovery-certificate**|object|Windows Information Protection DataRecoveryCertificate|data_recovery_certificate|dataRecoveryCertificate|
|**--enforcement-level**|choice||enforcement_level|enforcementLevel|
|**--enterprise-domain**|string|Primary enterprise domain|enterprise_domain|enterpriseDomain|
|**--enterprise-internal-proxy-servers**|array|This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies|enterprise_internal_proxy_servers|enterpriseInternalProxyServers|
|**--enterprise-ip-ranges**|array|Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to|enterprise_ip_ranges|enterpriseIPRanges|
|**--enterprise-ip-ranges-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false|enterprise_ip_ranges_are_authoritative|enterpriseIPRangesAreAuthoritative|
|**--enterprise-network-domain-names**|array|This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to|enterprise_network_domain_names|enterpriseNetworkDomainNames|
|**--enterprise-protected-domain-names**|array|List of enterprise domains to be protected|enterprise_protected_domain_names|enterpriseProtectedDomainNames|
|**--enterprise-proxied-domains**|array|Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy|enterprise_proxied_domains|enterpriseProxiedDomains|
|**--enterprise-proxy-servers**|array|This is a list of proxy servers. Any server not on this list is considered non-enterprise|enterprise_proxy_servers|enterpriseProxyServers|
|**--enterprise-proxy-servers-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false|enterprise_proxy_servers_are_authoritative|enterpriseProxyServersAreAuthoritative|
|**--exempt-apps**|array|Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.|exempt_apps|exemptApps|
|**--icons-visible**|boolean|Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app|icons_visible|iconsVisible|
|**--indexing-encrypted-stores-or-items-blocked**|boolean|This switch is for the Windows Search Indexer, to allow or disallow indexing of items|indexing_encrypted_stores_or_items_blocked|indexingEncryptedStoresOrItemsBlocked|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--neutral-domain-resources**|array|List of domain names that can used for work or personal resource|neutral_domain_resources|neutralDomainResources|
|**--protected-apps**|array|Protected applications can access enterprise data and the data handled by those applications are protected with encryption|protected_apps|protectedApps|
|**--protection-under-lock-config-required**|boolean|Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured|protection_under_lock_config_required|protectionUnderLockConfigRequired|
|**--revoke-on-unenroll-disabled**|boolean|This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.|revoke_on_unenroll_disabled|revokeOnUnenrollDisabled|
|**--rights-management-services-template-id**|uuid|TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access|rights_management_services_template_id|rightsManagementServicesTemplateId|
|**--smb-auto-encrypted-file-extensions**|array|Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary|smb_auto_encrypted_file_extensions|smbAutoEncryptedFileExtensions|
|**--assignments**|array|Navigation property to list of security groups targeted for policy.|assignments|assignments|
|**--exempt-app-locker-files**|array|Another way to input exempt apps through xml files|exempt_app_locker_files|exemptAppLockerFiles|
|**--protected-app-locker-files**|array|Another way to input protected apps through xml files|protected_app_locker_files|protectedAppLockerFiles|
|**--days-without-contact-before-unenroll**|integer|Offline interval before app data is wiped (days)|days_without_contact_before_unenroll|daysWithoutContactBeforeUnenroll|
|**--mdm-enrollment-url**|string|Enrollment url for the MDM|mdm_enrollment_url|mdmEnrollmentUrl|
|**--minutes-of-inactivity-before-device-lock**|integer|Specifies the maximum amount of time (in minutes) allowed after the device is idle that will cause the device to become PIN or password locked.   Range is an integer X where 0 <= X <= 999.|minutes_of_inactivity_before_device_lock|minutesOfInactivityBeforeDeviceLock|
|**--number-of-past-pins-remembered**|integer|Integer value that specifies the number of past PINs that can be associated to a user account that can't be reused. The largest number you can configure for this policy setting is 50. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then storage of previous PINs is not required. This node was added in Windows 10, version 1511. Default is 0.|number_of_past_pins_remembered|numberOfPastPinsRemembered|
|**--password-maximum-attempt-count**|integer|The number of authentication failures allowed before the device will be wiped. A value of 0 disables device wipe functionality. Range is an integer X where 4 <= X <= 16 for desktop and 0 <= X <= 999 for mobile devices.|password_maximum_attempt_count|passwordMaximumAttemptCount|
|**--pin-expiration-days**|integer|Integer value specifies the period of time (in days) that a PIN can be used before the system requires the user to change it. The largest number you can configure for this policy setting is 730. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then the user's PIN will never expire. This node was added in Windows 10, version 1511. Default is 0.|pin_expiration_days|pinExpirationDays|
|**--pin-lowercase-letters**|choice||pin_lowercase_letters|pinLowercaseLetters|
|**--pin-minimum-length**|integer|Integer value that sets the minimum number of characters required for the PIN. Default value is 4. The lowest number you can configure for this policy setting is 4. The largest number you can configure must be less than the number configured in the Maximum PIN length policy setting or the number 127, whichever is the lowest.|pin_minimum_length|pinMinimumLength|
|**--pin-special-characters**|choice||pin_special_characters|pinSpecialCharacters|
|**--pin-uppercase-letters**|choice||pin_uppercase_letters|pinUppercaseLetters|
|**--revoke-on-mdm-handoff-disabled**|boolean|New property in RS2, pending documentation|revoke_on_mdm_handoff_disabled|revokeOnMdmHandoffDisabled|
|**--windows-hello-for-business-blocked**|boolean|Boolean value that sets Windows Hello for Business as a method for signing into Windows.|windows_hello_for_business_blocked|windowsHelloForBusinessBlocked|

### devicescorpmgt delete

delete a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDeviceCompliancePolicyStates|
|delete|DeleteDeviceConfigurationStates|
|delete|DeleteDeviceCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-compliance-policy-state-id**|string|key: id of deviceCompliancePolicyState|device_compliance_policy_state_id|deviceCompliancePolicyState-id|
|**--device-configuration-state-id**|string|key: id of deviceConfigurationState|device_configuration_state_id|deviceConfigurationState-id|
|**--if-match**|string|ETag|if_match|If-Match|

### devicescorpmgt get-android-managed-app-protection

get-android-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-android-managed-app-protection|GetAndroidManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-app

get-app a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-app|GetApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-applied-policy

get-applied-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-applied-policy|GetAppliedPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-assignment

get-assignment a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assignment|GetAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--targeted-managed-app-policy-assignment-id**|string|key: id of targetedManagedAppPolicyAssignment|targeted_managed_app_policy_assignment_id|targetedManagedAppPolicyAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-default-managed-app-protection

get-default-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-default-managed-app-protection|GetDefaultManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-deployment-summary

get-deployment-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-deployment-summary|GetDeploymentSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-device-app-management

get-device-app-management a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device-app-management|GetDeviceAppManagement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-device-category

get-device-category a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device-category|GetDeviceCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-device-compliance-policy-state

get-device-compliance-policy-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device-compliance-policy-state|GetDeviceCompliancePolicyStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-compliance-policy-state-id**|string|key: id of deviceCompliancePolicyState|device_compliance_policy_state_id|deviceCompliancePolicyState-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-device-configuration-state

get-device-configuration-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device-configuration-state|GetDeviceConfigurationStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-configuration-state-id**|string|key: id of deviceConfigurationState|device_configuration_state_id|deviceConfigurationState-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-device-management-troubleshooting-event

get-device-management-troubleshooting-event a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device-management-troubleshooting-event|GetDeviceManagementTroubleshootingEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-management-troubleshooting-event-id**|string|key: id of deviceManagementTroubleshootingEvent|device_management_troubleshooting_event_id|deviceManagementTroubleshootingEvent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-device-state

get-device-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedEBooks.userStateSummary|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device-state|GetDeviceStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--device-install-state-id**|string|key: id of deviceInstallState|device_install_state_id|deviceInstallState-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-device-status-summary

get-device-status-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device-status-summary|GetDeviceStatusSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-device-statuses

get-device-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device-statuses|GetDeviceStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-device-status-id**|string|key: id of managedDeviceMobileAppConfigurationDeviceStatus|managed_device_mobile_app_configuration_device_status_id|managedDeviceMobileAppConfigurationDeviceStatus-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-install-summary

get-install-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedEBooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-install-summary|GetInstallSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-intended-policy

get-intended-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-intended-policy|GetIntendedPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-io-managed-app-protection

get-io-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-io-managed-app-protection|GetIosManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-managed-app-policy

get-managed-app-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-managed-app-policy|GetManagedAppPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-managed-app-registration

get-managed-app-registration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-managed-app-registration|GetManagedAppRegistrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-managed-app-statuses

get-managed-app-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-managed-app-statuses|GetManagedAppStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-status-id**|string|key: id of managedAppStatus|managed_app_status_id|managedAppStatus-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-managed-device

get-managed-device a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-managed-device|GetManagedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-managed-e-book

get-managed-e-book a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-managed-e-book|GetManagedEBooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-mdm-window-information-protection-policy

get-mdm-window-information-protection-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mdm-window-information-protection-policy|GetMdmWindowsInformationProtectionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mdm-windows-information-protection-policy-id**|string|key: id of mdmWindowsInformationProtectionPolicy|mdm_windows_information_protection_policy_id|mdmWindowsInformationProtectionPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-mobile-app

get-mobile-app a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mobile-app|GetMobileApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-mobile-app-category

get-mobile-app-category a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mobile-app-category|GetMobileAppCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-category-id**|string|key: id of mobileAppCategory|mobile_app_category_id|mobileAppCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-mobile-app-configuration

get-mobile-app-configuration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mobile-app-configuration|GetMobileAppConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-operation

get-operation a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-operation|GetOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-operation-id**|string|key: id of managedAppOperation|managed_app_operation_id|managedAppOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-targeted-managed-app-configuration

get-targeted-managed-app-configuration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-targeted-managed-app-configuration|GetTargetedManagedAppConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-user-id-with-flagged-app-registration

get-user-id-with-flagged-app-registration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-id-with-flagged-app-registration|getUserIdsWithFlaggedAppRegistration|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### devicescorpmgt get-user-state-summary

get-user-state-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedEBooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-state-summary|GetUserStateSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-user-status-summary

get-user-status-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-status-summary|GetUserStatusSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-user-statuses

get-user-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-statuses|GetUserStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-user-status-id**|string|key: id of managedDeviceMobileAppConfigurationUserStatus|managed_device_mobile_app_configuration_user_status_id|managedDeviceMobileAppConfigurationUserStatus-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-vpp-token

get-vpp-token a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-vpp-token|GetVppTokens|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vpp-token-id**|string|key: id of vppToken|vpp_token_id|vppToken-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt get-window-information-protection-policy

get-window-information-protection-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-window-information-protection-policy|GetWindowsInformationProtectionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--windows-information-protection-policy-id**|string|key: id of windowsInformationProtectionPolicy|windows_information_protection_policy_id|windowsInformationProtectionPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-android-managed-app-protection

list-android-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-android-managed-app-protection|ListAndroidManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-app

list-app a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-app|ListApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-applied-policy

list-applied-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-applied-policy|ListAppliedPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-assignment

list-assignment a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-assignment|ListAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-category

list-category a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-category|ListCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-default-managed-app-protection

list-default-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-default-managed-app-protection|ListDefaultManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-device-compliance-policy-state

list-device-compliance-policy-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-device-compliance-policy-state|ListDeviceCompliancePolicyStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-device-configuration-state

list-device-configuration-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-device-configuration-state|ListDeviceConfigurationStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-device-management-troubleshooting-event

list-device-management-troubleshooting-event a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-device-management-troubleshooting-event|ListDeviceManagementTroubleshootingEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-device-state

list-device-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedEBooks.userStateSummary|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-device-state|ListDeviceStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-device-statuses

list-device-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-device-statuses|ListDeviceStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-intended-policy

list-intended-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-intended-policy|ListIntendedPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-io-managed-app-protection

list-io-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-io-managed-app-protection|ListIosManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-managed-app-policy

list-managed-app-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-managed-app-policy|ListManagedAppPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-managed-app-registration

list-managed-app-registration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-managed-app-registration|ListManagedAppRegistrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-managed-app-statuses

list-managed-app-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-managed-app-statuses|ListManagedAppStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-managed-device

list-managed-device a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-managed-device|ListManagedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-managed-e-book

list-managed-e-book a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-managed-e-book|ListManagedEBooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-mdm-window-information-protection-policy

list-mdm-window-information-protection-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-mdm-window-information-protection-policy|ListMdmWindowsInformationProtectionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-mobile-app

list-mobile-app a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-mobile-app|ListMobileApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-mobile-app-category

list-mobile-app-category a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-mobile-app-category|ListMobileAppCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-mobile-app-configuration

list-mobile-app-configuration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-mobile-app-configuration|ListMobileAppConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-operation

list-operation a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-operation|ListOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-ref-category

list-ref-category a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-category|ListRefCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### devicescorpmgt list-ref-managed-app-registration

list-ref-managed-app-registration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-managed-app-registration|ListRefManagedAppRegistrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### devicescorpmgt list-targeted-managed-app-configuration

list-targeted-managed-app-configuration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-targeted-managed-app-configuration|ListTargetedManagedAppConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-user-state-summary

list-user-state-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedEBooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user-state-summary|ListUserStateSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-user-statuses

list-user-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user-statuses|ListUserStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-vpp-token

list-vpp-token a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-vpp-token|ListVppTokens|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt list-window-information-protection-policy

list-window-information-protection-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-window-information-protection-policy|ListWindowsInformationProtectionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescorpmgt sync-license

sync-license a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.vppTokens|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|sync-license|syncLicenses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vpp-token-id**|string|key: id of vppToken|vpp_token_id|vppToken-id|

### devicescorpmgt sync-microsoft-store-for-business-app

sync-microsoft-store-for-business-app a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|sync-microsoft-store-for-business-app|syncMicrosoftStoreForBusinessApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### devicescorpmgt target-app

target-app a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|target-app|targetApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--apps**|array||apps|apps|

### devicescorpmgt update-android-managed-app-protection

update-android-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-android-managed-app-protection|UpdateAndroidManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--body**|object|New navigation property values|body|body|

### devicescorpmgt update-app

update-app a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-app|UpdateApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--id**|string|Read-only.|id|id|
|**--mobile-app-identifier**|dictionary|The identifier for a mobile app.|mobile_app_identifier|mobileAppIdentifier|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt update-applied-policy

update-applied-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-applied-policy|UpdateAppliedPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt update-assignment

update-assignment a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assignment|UpdateAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--targeted-managed-app-policy-assignment-id**|string|key: id of targetedManagedAppPolicyAssignment|targeted_managed_app_policy_assignment_id|targetedManagedAppPolicyAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--target**|dictionary|Base type for assignment targets.|target|target|

### devicescorpmgt update-default-managed-app-protection

update-default-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-default-managed-app-protection|UpdateDefaultManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--body**|object|New navigation property values|body|body|

### devicescorpmgt update-deployment-summary

update-deployment-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.targetedManagedAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-deployment-summary|UpdateDeploymentSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--configuration-deployed-user-count**|integer|Not yet documented|configuration_deployed_user_count|configurationDeployedUserCount|
|**--configuration-deployment-summary-per-app**|array|Not yet documented|configuration_deployment_summary_per_app|configurationDeploymentSummaryPerApp|
|**--display-name**|string|Not yet documented|display_name|displayName|
|**--last-refresh-time**|date-time|Not yet documented|last_refresh_time|lastRefreshTime|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt update-device-app-management

update-device-app-management a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device-app-management|UpdateDeviceAppManagement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--is-enabled-for-microsoft-store-for-business**|boolean|Whether the account is enabled for syncing applications from the Microsoft Store for Business.|is_enabled_for_microsoft_store_for_business|isEnabledForMicrosoftStoreForBusiness|
|**--microsoft-store-for-business-language**|string|The locale information used to sync applications from the Microsoft Store for Business. Cultures that are specific to a country/region. The names of these cultures follow RFC 4646 (Windows Vista and later). The format is -<country/regioncode2>, where  is a lowercase two-letter code derived from ISO 639-1 and <country/regioncode2> is an uppercase two-letter code derived from ISO 3166. For example, en-US for English (United States) is a specific culture.|microsoft_store_for_business_language|microsoftStoreForBusinessLanguage|
|**--microsoft-store-for-business-last-completed-application-sync-time**|date-time|The last time an application sync from the Microsoft Store for Business was completed.|microsoft_store_for_business_last_completed_application_sync_time|microsoftStoreForBusinessLastCompletedApplicationSyncTime|
|**--microsoft-store-for-business-last-successful-sync-date-time**|date-time|The last time the apps from the Microsoft Store for Business were synced successfully for the account.|microsoft_store_for_business_last_successful_sync_date_time|microsoftStoreForBusinessLastSuccessfulSyncDateTime|
|**--managed-e-books**|array|The Managed eBook.|managed_e_books|managedEBooks|
|**--mobile-app-categories**|array|The mobile app categories.|mobile_app_categories|mobileAppCategories|
|**--mobile-app-configurations**|array|The Managed Device Mobile Application Configurations.|mobile_app_configurations|mobileAppConfigurations|
|**--mobile-apps**|array|The mobile apps.|mobile_apps|mobileApps|
|**--vpp-tokens**|array|List of Vpp tokens for this organization.|vpp_tokens|vppTokens|
|**--android-managed-app-protections**|array|Android managed app policies.|android_managed_app_protections|androidManagedAppProtections|
|**--default-managed-app-protections**|array|Default managed app policies.|default_managed_app_protections|defaultManagedAppProtections|
|**--ios-managed-app-protections**|array|iOS managed app policies.|ios_managed_app_protections|iosManagedAppProtections|
|**--managed-app-policies**|array|Managed app policies.|managed_app_policies|managedAppPolicies|
|**--managed-app-registrations**|array|The managed app registrations.|managed_app_registrations|managedAppRegistrations|
|**--managed-app-statuses**|array|The managed app statuses.|managed_app_statuses|managedAppStatuses|
|**--mdm-windows-information-protection-policies**|array|Windows information protection for apps running on devices which are MDM enrolled.|mdm_windows_information_protection_policies|mdmWindowsInformationProtectionPolicies|
|**--targeted-managed-app-configurations**|array|Targeted managed app configurations.|targeted_managed_app_configurations|targetedManagedAppConfigurations|
|**--windows-information-protection-policies**|array|Windows information protection for apps running on devices which are not MDM enrolled.|windows_information_protection_policies|windowsInformationProtectionPolicies|

### devicescorpmgt update-device-category

update-device-category a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device-category|UpdateDeviceCategory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Optional description for the device category.|description|description|
|**--display-name**|string|Display name for the device category.|display_name|displayName|

### devicescorpmgt update-device-compliance-policy-state

update-device-compliance-policy-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device-compliance-policy-state|UpdateDeviceCompliancePolicyStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-compliance-policy-state-id**|string|key: id of deviceCompliancePolicyState|device_compliance_policy_state_id|deviceCompliancePolicyState-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the policy for this policyBase|display_name|displayName|
|**--platform-type**|choice||platform_type|platformType|
|**--setting-count**|integer|Count of how many setting a policy holds|setting_count|settingCount|
|**--setting-states**|array||setting_states|settingStates|
|**--state**|choice||state|state|
|**--version**|integer|The version of the policy|version|version|

### devicescorpmgt update-device-configuration-state

update-device-configuration-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device-configuration-state|UpdateDeviceConfigurationStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-configuration-state-id**|string|key: id of deviceConfigurationState|device_configuration_state_id|deviceConfigurationState-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the policy for this policyBase|display_name|displayName|
|**--platform-type**|choice||platform_type|platformType|
|**--setting-count**|integer|Count of how many setting a policy holds|setting_count|settingCount|
|**--setting-states**|array||setting_states|settingStates|
|**--state**|choice||state|state|
|**--version**|integer|The version of the policy|version|version|

### devicescorpmgt update-device-management-troubleshooting-event

update-device-management-troubleshooting-event a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device-management-troubleshooting-event|UpdateDeviceManagementTroubleshootingEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-management-troubleshooting-event-id**|string|key: id of deviceManagementTroubleshootingEvent|device_management_troubleshooting_event_id|deviceManagementTroubleshootingEvent-id|
|**--id**|string|Read-only.|id|id|
|**--correlation-id**|string|Id used for tracing the failure in the service.|correlation_id|correlationId|
|**--event-date-time**|date-time|Time when the event occurred .|event_date_time|eventDateTime|

### devicescorpmgt update-device-state

update-device-state a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedEBooks.userStateSummary|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device-state|UpdateDeviceStates|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--device-install-state-id**|string|key: id of deviceInstallState|device_install_state_id|deviceInstallState-id|
|**--id**|string|Read-only.|id|id|
|**--device-id**|string|Device Id.|device_id|deviceId|
|**--device-name**|string|Device name.|device_name|deviceName|
|**--error-code**|string|The error code for install failures.|error_code|errorCode|
|**--install-state**|choice||install_state|installState|
|**--last-sync-date-time**|date-time|Last sync date and time.|last_sync_date_time|lastSyncDateTime|
|**--os-description**|string|OS Description.|os_description|osDescription|
|**--os-version**|string|OS Version.|os_version|osVersion|
|**--user-name**|string|Device User Name.|user_name|userName|

### devicescorpmgt update-device-status-summary

update-device-status-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device-status-summary|UpdateDeviceStatusSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--configuration-version**|integer|Version of the policy for that overview|configuration_version|configurationVersion|
|**--error-count**|integer|Number of error devices|error_count|errorCount|
|**--failed-count**|integer|Number of failed devices|failed_count|failedCount|
|**--last-update-date-time**|date-time|Last update time|last_update_date_time|lastUpdateDateTime|
|**--not-applicable-count**|integer|Number of not applicable devices|not_applicable_count|notApplicableCount|
|**--pending-count**|integer|Number of pending devices|pending_count|pendingCount|
|**--success-count**|integer|Number of succeeded devices|success_count|successCount|

### devicescorpmgt update-device-statuses

update-device-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device-statuses|UpdateDeviceStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-device-status-id**|string|key: id of managedDeviceMobileAppConfigurationDeviceStatus|managed_device_mobile_app_configuration_device_status_id|managedDeviceMobileAppConfigurationDeviceStatus-id|
|**--id**|string|Read-only.|id|id|
|**--compliance-grace-period-expiration-date-time**|date-time|The DateTime when device compliance grace period expires|compliance_grace_period_expiration_date_time|complianceGracePeriodExpirationDateTime|
|**--device-display-name**|string|Device name of the DevicePolicyStatus.|device_display_name|deviceDisplayName|
|**--device-model**|string|The device model that is being reported|device_model|deviceModel|
|**--last-reported-date-time**|date-time|Last modified date time of the policy report.|last_reported_date_time|lastReportedDateTime|
|**--status**|choice||status|status|
|**--user-name**|string|The User Name that is being reported|user_name|userName|
|**--user-principal-name**|string|UserPrincipalName.|user_principal_name|userPrincipalName|

### devicescorpmgt update-install-summary

update-install-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedEBooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-install-summary|UpdateInstallSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--id**|string|Read-only.|id|id|
|**--failed-device-count**|integer|Number of Devices that have failed to install this book.|failed_device_count|failedDeviceCount|
|**--failed-user-count**|integer|Number of Users that have 1 or more device that failed to install this book.|failed_user_count|failedUserCount|
|**--installed-device-count**|integer|Number of Devices that have successfully installed this book.|installed_device_count|installedDeviceCount|
|**--installed-user-count**|integer|Number of Users whose devices have all succeeded to install this book.|installed_user_count|installedUserCount|
|**--not-installed-device-count**|integer|Number of Devices that does not have this book installed.|not_installed_device_count|notInstalledDeviceCount|
|**--not-installed-user-count**|integer|Number of Users that did not install this book.|not_installed_user_count|notInstalledUserCount|

### devicescorpmgt update-intended-policy

update-intended-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-intended-policy|UpdateIntendedPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt update-io-managed-app-protection

update-io-managed-app-protection a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-io-managed-app-protection|UpdateIosManagedAppProtections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--body**|object|New navigation property values|body|body|

### devicescorpmgt update-managed-app-policy

update-managed-app-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-managed-app-policy|UpdateManagedAppPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt update-managed-app-registration

update-managed-app-registration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-managed-app-registration|UpdateManagedAppRegistrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--id**|string|Read-only.|id|id|
|**--app-identifier**|dictionary|The identifier for a mobile app.|app_identifier|appIdentifier|
|**--application-version**|string|App version|application_version|applicationVersion|
|**--created-date-time**|date-time|Date and time of creation|created_date_time|createdDateTime|
|**--device-name**|string|Host device name|device_name|deviceName|
|**--device-tag**|string|App management SDK generated tag, which helps relate apps hosted on the same device. Not guaranteed to relate apps in all conditions.|device_tag|deviceTag|
|**--device-type**|string|Host device type|device_type|deviceType|
|**--flagged-reasons**|array|Zero or more reasons an app registration is flagged. E.g. app running on rooted device|flagged_reasons|flaggedReasons|
|**--last-sync-date-time**|date-time|Date and time of last the app synced with management service.|last_sync_date_time|lastSyncDateTime|
|**--management-sdk-version**|string|App management SDK version|management_sdk_version|managementSdkVersion|
|**--platform-version**|string|Operating System version|platform_version|platformVersion|
|**--user-id**|string|The user Id to who this app registration belongs.|user_id|userId|
|**--version**|string|Version of the entity.|version|version|
|**--applied-policies**|array|Zero or more policys already applied on the registered app when it last synchronized with managment service.|applied_policies|appliedPolicies|
|**--intended-policies**|array|Zero or more policies admin intended for the app as of now.|intended_policies|intendedPolicies|
|**--operations**|array|Zero or more long running operations triggered on the app registration.|operations|operations|

### devicescorpmgt update-managed-app-statuses

update-managed-app-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-managed-app-statuses|UpdateManagedAppStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-status-id**|string|key: id of managedAppStatus|managed_app_status_id|managedAppStatus-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Friendly name of the status report.|display_name|displayName|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt update-managed-device

update-managed-device a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-managed-device|UpdateManagedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--body**|object|New navigation property values|body|body|

### devicescorpmgt update-managed-e-book

update-managed-e-book a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-managed-e-book|UpdateManagedEBooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time when the eBook file was created.|created_date_time|createdDateTime|
|**--description**|string|Description.|description|description|
|**--display-name**|string|Name of the eBook.|display_name|displayName|
|**--information-url**|string|The more information Url.|information_url|informationUrl|
|**--large-cover**|object|Contains properties for a generic mime content.|large_cover|largeCover|
|**--last-modified-date-time**|date-time|The date and time when the eBook was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--privacy-information-url**|string|The privacy statement Url.|privacy_information_url|privacyInformationUrl|
|**--published-date-time**|date-time|The date and time when the eBook was published.|published_date_time|publishedDateTime|
|**--publisher**|string|Publisher.|publisher|publisher|
|**--assignments**|array|The list of assignments for this eBook.|assignments|assignments|
|**--device-states**|array|The list of installation states for this eBook.|device_states|deviceStates|
|**--install-summary**|object|Contains properties for the installation summary of a book for a device.|install_summary|installSummary|
|**--user-state-summary**|array|The list of installation states for this eBook.|user_state_summary|userStateSummary|

### devicescorpmgt update-mdm-window-information-protection-policy

update-mdm-window-information-protection-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-mdm-window-information-protection-policy|UpdateMdmWindowsInformationProtectionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mdm-windows-information-protection-policy-id**|string|key: id of mdmWindowsInformationProtectionPolicy|mdm_windows_information_protection_policy_id|mdmWindowsInformationProtectionPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--azure-rights-management-services-allowed**|boolean|Specifies whether to allow Azure RMS encryption for WIP|azure_rights_management_services_allowed|azureRightsManagementServicesAllowed|
|**--data-recovery-certificate**|object|Windows Information Protection DataRecoveryCertificate|data_recovery_certificate|dataRecoveryCertificate|
|**--enforcement-level**|choice||enforcement_level|enforcementLevel|
|**--enterprise-domain**|string|Primary enterprise domain|enterprise_domain|enterpriseDomain|
|**--enterprise-internal-proxy-servers**|array|This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies|enterprise_internal_proxy_servers|enterpriseInternalProxyServers|
|**--enterprise-ip-ranges**|array|Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to|enterprise_ip_ranges|enterpriseIPRanges|
|**--enterprise-ip-ranges-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false|enterprise_ip_ranges_are_authoritative|enterpriseIPRangesAreAuthoritative|
|**--enterprise-network-domain-names**|array|This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to|enterprise_network_domain_names|enterpriseNetworkDomainNames|
|**--enterprise-protected-domain-names**|array|List of enterprise domains to be protected|enterprise_protected_domain_names|enterpriseProtectedDomainNames|
|**--enterprise-proxied-domains**|array|Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy|enterprise_proxied_domains|enterpriseProxiedDomains|
|**--enterprise-proxy-servers**|array|This is a list of proxy servers. Any server not on this list is considered non-enterprise|enterprise_proxy_servers|enterpriseProxyServers|
|**--enterprise-proxy-servers-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false|enterprise_proxy_servers_are_authoritative|enterpriseProxyServersAreAuthoritative|
|**--exempt-apps**|array|Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.|exempt_apps|exemptApps|
|**--icons-visible**|boolean|Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app|icons_visible|iconsVisible|
|**--indexing-encrypted-stores-or-items-blocked**|boolean|This switch is for the Windows Search Indexer, to allow or disallow indexing of items|indexing_encrypted_stores_or_items_blocked|indexingEncryptedStoresOrItemsBlocked|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--neutral-domain-resources**|array|List of domain names that can used for work or personal resource|neutral_domain_resources|neutralDomainResources|
|**--protected-apps**|array|Protected applications can access enterprise data and the data handled by those applications are protected with encryption|protected_apps|protectedApps|
|**--protection-under-lock-config-required**|boolean|Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured|protection_under_lock_config_required|protectionUnderLockConfigRequired|
|**--revoke-on-unenroll-disabled**|boolean|This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.|revoke_on_unenroll_disabled|revokeOnUnenrollDisabled|
|**--rights-management-services-template-id**|uuid|TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access|rights_management_services_template_id|rightsManagementServicesTemplateId|
|**--smb-auto-encrypted-file-extensions**|array|Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary|smb_auto_encrypted_file_extensions|smbAutoEncryptedFileExtensions|
|**--assignments**|array|Navigation property to list of security groups targeted for policy.|assignments|assignments|
|**--exempt-app-locker-files**|array|Another way to input exempt apps through xml files|exempt_app_locker_files|exemptAppLockerFiles|
|**--protected-app-locker-files**|array|Another way to input protected apps through xml files|protected_app_locker_files|protectedAppLockerFiles|

### devicescorpmgt update-mobile-app

update-mobile-app a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-mobile-app|UpdateMobileApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the app was created.|created_date_time|createdDateTime|
|**--description**|string|The description of the app.|description|description|
|**--developer**|string|The developer of the app.|developer|developer|
|**--display-name**|string|The admin provided or imported title of the app.|display_name|displayName|
|**--information-url**|string|The more information Url.|information_url|informationUrl|
|**--is-featured**|boolean|The value indicating whether the app is marked as featured by the admin.|is_featured|isFeatured|
|**--large-icon**|object|Contains properties for a generic mime content.|large_icon|largeIcon|
|**--last-modified-date-time**|date-time|The date and time the app was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--notes**|string|Notes for the app.|notes|notes|
|**--owner**|string|The owner of the app.|owner|owner|
|**--privacy-information-url**|string|The privacy statement Url.|privacy_information_url|privacyInformationUrl|
|**--publisher**|string|The publisher of the app.|publisher|publisher|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--assignments**|array|The list of group assignments for this mobile app.|assignments|assignments|
|**--categories**|array|The list of categories for this app.|categories|categories|

### devicescorpmgt update-mobile-app-category

update-mobile-app-category a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-mobile-app-category|UpdateMobileAppCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-category-id**|string|key: id of mobileAppCategory|mobile_app_category_id|mobileAppCategory-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the app category.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time the mobileAppCategory was last modified.|last_modified_date_time|lastModifiedDateTime|

### devicescorpmgt update-mobile-app-configuration

update-mobile-app-configuration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-mobile-app-configuration|UpdateMobileAppConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|DateTime the object was created.|created_date_time|createdDateTime|
|**--description**|string|Admin provided description of the Device Configuration.|description|description|
|**--display-name**|string|Admin provided name of the device configuration.|display_name|displayName|
|**--last-modified-date-time**|date-time|DateTime the object was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--targeted-mobile-apps**|array|the associated app.|targeted_mobile_apps|targetedMobileApps|
|**--version**|integer|Version of the device configuration.|version|version|
|**--assignments**|array|The list of group assignemenets for app configration.|assignments|assignments|
|**--device-statuses**|array|List of ManagedDeviceMobileAppConfigurationDeviceStatus.|device_statuses|deviceStatuses|
|**--device-status-summary**|object|Contains properties, inherited properties and actions for an MDM mobile app configuration device status summary.|device_status_summary|deviceStatusSummary|
|**--user-statuses**|array|List of ManagedDeviceMobileAppConfigurationUserStatus.|user_statuses|userStatuses|
|**--user-status-summary**|object|Contains properties, inherited properties and actions for an MDM mobile app configuration user status summary.|user_status_summary|userStatusSummary|

### devicescorpmgt update-operation

update-operation a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedAppRegistrations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-operation|UpdateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-operation-id**|string|key: id of managedAppOperation|managed_app_operation_id|managedAppOperation-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The operation name.|display_name|displayName|
|**--last-modified-date-time**|date-time|The last time the app operation was modified.|last_modified_date_time|lastModifiedDateTime|
|**--state**|string|The current state of the operation|state|state|
|**--version**|string|Version of the entity.|version|version|

### devicescorpmgt update-targeted-managed-app-configuration

update-targeted-managed-app-configuration a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-targeted-managed-app-configuration|UpdateTargetedManagedAppConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--custom-settings**|array|A set of string key and string value pairs to be sent to apps for users to whom the configuration is scoped, unalterned by this service|custom_settings|customSettings|
|**--deployed-app-count**|integer|Count of apps to which the current policy is deployed.|deployed_app_count|deployedAppCount|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--apps**|array|List of apps to which the policy is deployed.|apps|apps|
|**--assignments**|array|Navigation property to list of inclusion and exclusion groups to which the policy is deployed.|assignments|assignments|
|**--deployment-summary-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--deployment-summary-configuration-deployed-user-count**|integer|Not yet documented|configuration_deployed_user_count|configurationDeployedUserCount|
|**--deployment-summary-configuration-deployment-summary-per-app**|array|Not yet documented|configuration_deployment_summary_per_app|configurationDeploymentSummaryPerApp|
|**--deployment-summary-display-name**|string|Not yet documented|microsoft_graph_managed_app_policy_deployment_summary_display_name|displayName|
|**--deployment-summary-last-refresh-time**|date-time|Not yet documented|last_refresh_time|lastRefreshTime|
|**--deployment-summary-version**|string|Version of the entity.|microsoft_graph_managed_app_policy_deployment_summary_version|version|

### devicescorpmgt update-user-state-summary

update-user-state-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.managedEBooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user-state-summary|UpdateUserStateSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--id**|string|Read-only.|id|id|
|**--failed-device-count**|integer|Failed Device Count.|failed_device_count|failedDeviceCount|
|**--installed-device-count**|integer|Installed Device Count.|installed_device_count|installedDeviceCount|
|**--not-installed-device-count**|integer|Not installed device count.|not_installed_device_count|notInstalledDeviceCount|
|**--user-name**|string|User name.|user_name|userName|
|**--device-states**|array|The install state of the eBook.|device_states|deviceStates|

### devicescorpmgt update-user-status-summary

update-user-status-summary a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user-status-summary|UpdateUserStatusSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--configuration-version**|integer|Version of the policy for that overview|configuration_version|configurationVersion|
|**--error-count**|integer|Number of error Users|error_count|errorCount|
|**--failed-count**|integer|Number of failed Users|failed_count|failedCount|
|**--last-update-date-time**|date-time|Last update time|last_update_date_time|lastUpdateDateTime|
|**--not-applicable-count**|integer|Number of not applicable users|not_applicable_count|notApplicableCount|
|**--pending-count**|integer|Number of pending Users|pending_count|pendingCount|
|**--success-count**|integer|Number of succeeded Users|success_count|successCount|

### devicescorpmgt update-user-statuses

update-user-statuses a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement.mobileAppConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user-statuses|UpdateUserStatuses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-user-status-id**|string|key: id of managedDeviceMobileAppConfigurationUserStatus|managed_device_mobile_app_configuration_user_status_id|managedDeviceMobileAppConfigurationUserStatus-id|
|**--id**|string|Read-only.|id|id|
|**--devices-count**|integer|Devices count for that user.|devices_count|devicesCount|
|**--last-reported-date-time**|date-time|Last modified date time of the policy report.|last_reported_date_time|lastReportedDateTime|
|**--status**|choice||status|status|
|**--user-display-name**|string|User name of the DevicePolicyStatus.|user_display_name|userDisplayName|
|**--user-principal-name**|string|UserPrincipalName.|user_principal_name|userPrincipalName|

### devicescorpmgt update-vpp-token

update-vpp-token a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-vpp-token|UpdateVppTokens|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vpp-token-id**|string|key: id of vppToken|vpp_token_id|vppToken-id|
|**--id**|string|Read-only.|id|id|
|**--apple-id**|string|The apple Id associated with the given Apple Volume Purchase Program Token.|apple_id|appleId|
|**--automatically-update-apps**|boolean|Whether or not apps for the VPP token will be automatically updated.|automatically_update_apps|automaticallyUpdateApps|
|**--country-or-region**|string|Whether or not apps for the VPP token will be automatically updated.|country_or_region|countryOrRegion|
|**--expiration-date-time**|date-time|The expiration date time of the Apple Volume Purchase Program Token.|expiration_date_time|expirationDateTime|
|**--last-modified-date-time**|date-time|Last modification date time associated with the Apple Volume Purchase Program Token.|last_modified_date_time|lastModifiedDateTime|
|**--last-sync-date-time**|date-time|The last time when an application sync was done with the Apple volume purchase program service using the Apple Volume Purchase Program Token.|last_sync_date_time|lastSyncDateTime|
|**--last-sync-status**|choice||last_sync_status|lastSyncStatus|
|**--organization-name**|string|The organization associated with the Apple Volume Purchase Program Token|organization_name|organizationName|
|**--state**|choice||state|state|
|**--token**|string|The Apple Volume Purchase Program Token string downloaded from the Apple Volume Purchase Program.|token|token|
|**--vpp-token-account-type**|choice||vpp_token_account_type|vppTokenAccountType|

### devicescorpmgt update-window-information-protection-policy

update-window-information-protection-policy a devicescorpmgt.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescorpmgt|deviceAppManagement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-window-information-protection-policy|UpdateWindowsInformationProtectionPolicies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--windows-information-protection-policy-id**|string|key: id of windowsInformationProtectionPolicy|windows_information_protection_policy_id|windowsInformationProtectionPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--azure-rights-management-services-allowed**|boolean|Specifies whether to allow Azure RMS encryption for WIP|azure_rights_management_services_allowed|azureRightsManagementServicesAllowed|
|**--data-recovery-certificate**|object|Windows Information Protection DataRecoveryCertificate|data_recovery_certificate|dataRecoveryCertificate|
|**--enforcement-level**|choice||enforcement_level|enforcementLevel|
|**--enterprise-domain**|string|Primary enterprise domain|enterprise_domain|enterpriseDomain|
|**--enterprise-internal-proxy-servers**|array|This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies|enterprise_internal_proxy_servers|enterpriseInternalProxyServers|
|**--enterprise-ip-ranges**|array|Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to|enterprise_ip_ranges|enterpriseIPRanges|
|**--enterprise-ip-ranges-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false|enterprise_ip_ranges_are_authoritative|enterpriseIPRangesAreAuthoritative|
|**--enterprise-network-domain-names**|array|This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to|enterprise_network_domain_names|enterpriseNetworkDomainNames|
|**--enterprise-protected-domain-names**|array|List of enterprise domains to be protected|enterprise_protected_domain_names|enterpriseProtectedDomainNames|
|**--enterprise-proxied-domains**|array|Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy|enterprise_proxied_domains|enterpriseProxiedDomains|
|**--enterprise-proxy-servers**|array|This is a list of proxy servers. Any server not on this list is considered non-enterprise|enterprise_proxy_servers|enterpriseProxyServers|
|**--enterprise-proxy-servers-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false|enterprise_proxy_servers_are_authoritative|enterpriseProxyServersAreAuthoritative|
|**--exempt-apps**|array|Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.|exempt_apps|exemptApps|
|**--icons-visible**|boolean|Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app|icons_visible|iconsVisible|
|**--indexing-encrypted-stores-or-items-blocked**|boolean|This switch is for the Windows Search Indexer, to allow or disallow indexing of items|indexing_encrypted_stores_or_items_blocked|indexingEncryptedStoresOrItemsBlocked|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--neutral-domain-resources**|array|List of domain names that can used for work or personal resource|neutral_domain_resources|neutralDomainResources|
|**--protected-apps**|array|Protected applications can access enterprise data and the data handled by those applications are protected with encryption|protected_apps|protectedApps|
|**--protection-under-lock-config-required**|boolean|Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured|protection_under_lock_config_required|protectionUnderLockConfigRequired|
|**--revoke-on-unenroll-disabled**|boolean|This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.|revoke_on_unenroll_disabled|revokeOnUnenrollDisabled|
|**--rights-management-services-template-id**|uuid|TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access|rights_management_services_template_id|rightsManagementServicesTemplateId|
|**--smb-auto-encrypted-file-extensions**|array|Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary|smb_auto_encrypted_file_extensions|smbAutoEncryptedFileExtensions|
|**--assignments**|array|Navigation property to list of security groups targeted for policy.|assignments|assignments|
|**--exempt-app-locker-files**|array|Another way to input exempt apps through xml files|exempt_app_locker_files|exemptAppLockerFiles|
|**--protected-app-locker-files**|array|Another way to input protected apps through xml files|protected_app_locker_files|protectedAppLockerFiles|
|**--days-without-contact-before-unenroll**|integer|Offline interval before app data is wiped (days)|days_without_contact_before_unenroll|daysWithoutContactBeforeUnenroll|
|**--mdm-enrollment-url**|string|Enrollment url for the MDM|mdm_enrollment_url|mdmEnrollmentUrl|
|**--minutes-of-inactivity-before-device-lock**|integer|Specifies the maximum amount of time (in minutes) allowed after the device is idle that will cause the device to become PIN or password locked.   Range is an integer X where 0 <= X <= 999.|minutes_of_inactivity_before_device_lock|minutesOfInactivityBeforeDeviceLock|
|**--number-of-past-pins-remembered**|integer|Integer value that specifies the number of past PINs that can be associated to a user account that can't be reused. The largest number you can configure for this policy setting is 50. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then storage of previous PINs is not required. This node was added in Windows 10, version 1511. Default is 0.|number_of_past_pins_remembered|numberOfPastPinsRemembered|
|**--password-maximum-attempt-count**|integer|The number of authentication failures allowed before the device will be wiped. A value of 0 disables device wipe functionality. Range is an integer X where 4 <= X <= 16 for desktop and 0 <= X <= 999 for mobile devices.|password_maximum_attempt_count|passwordMaximumAttemptCount|
|**--pin-expiration-days**|integer|Integer value specifies the period of time (in days) that a PIN can be used before the system requires the user to change it. The largest number you can configure for this policy setting is 730. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then the user's PIN will never expire. This node was added in Windows 10, version 1511. Default is 0.|pin_expiration_days|pinExpirationDays|
|**--pin-lowercase-letters**|choice||pin_lowercase_letters|pinLowercaseLetters|
|**--pin-minimum-length**|integer|Integer value that sets the minimum number of characters required for the PIN. Default value is 4. The lowest number you can configure for this policy setting is 4. The largest number you can configure must be less than the number configured in the Maximum PIN length policy setting or the number 127, whichever is the lowest.|pin_minimum_length|pinMinimumLength|
|**--pin-special-characters**|choice||pin_special_characters|pinSpecialCharacters|
|**--pin-uppercase-letters**|choice||pin_uppercase_letters|pinUppercaseLetters|
|**--revoke-on-mdm-handoff-disabled**|boolean|New property in RS2, pending documentation|revoke_on_mdm_handoff_disabled|revokeOnMdmHandoffDisabled|
|**--windows-hello-for-business-blocked**|boolean|Boolean value that sets Windows Hello for Business as a method for signing into Windows.|windows_hello_for_business_blocked|windowsHelloForBusinessBlocked|
