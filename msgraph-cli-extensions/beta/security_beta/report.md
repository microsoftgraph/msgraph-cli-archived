# Azure CLI Module Creation Report

### security cancel-security-action

cancel-security-action a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security.securityActions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel-security-action|cancelSecurityAction|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--security-action-id**|string|key: id of securityAction|security_action_id|securityAction-id|

### security create-alert

create-alert a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-alert|CreateAlerts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

### security create-cloud-app-security-profile

create-cloud-app-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-cloud-app-security-profile|CreateCloudAppSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--deployment-package-url**|string||deployment_package_url|deploymentPackageUrl|
|**--destination-service-name**|string||destination_service_name|destinationServiceName|
|**--is-signed**|boolean||is_signed|isSigned|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--manifest**|string||manifest|manifest|
|**--name**|string||name|name|
|**--permissions-required**|choice||permissions_required|permissionsRequired|
|**--platform**|string||platform|platform|
|**--policy-name**|string||policy_name|policyName|
|**--publisher**|string||publisher|publisher|
|**--risk-score**|string||risk_score|riskScore|
|**--tags**|array||tags|tags|
|**--type**|string||type|type|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security create-domain-security-profile

create-domain-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-domain-security-profile|CreateDomainSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-group-names**|array||activity_group_names|activityGroupNames|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--count-hits**|integer||count_hits|countHits|
|**--count-in-org**|integer||count_in_org|countInOrg|
|**--domain-categories**|array||domain_categories|domainCategories|
|**--domain-registered-date-time**|date-time||domain_registered_date_time|domainRegisteredDateTime|
|**--first-seen-date-time**|date-time||first_seen_date_time|firstSeenDateTime|
|**--last-seen-date-time**|date-time||last_seen_date_time|lastSeenDateTime|
|**--name**|string||name|name|
|**--registrant**|object|domainRegistrant|registrant|registrant|
|**--risk-score**|string||risk_score|riskScore|
|**--tags**|array||tags|tags|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security create-file-security-profile

create-file-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-file-security-profile|CreateFileSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-group-names**|array||activity_group_names|activityGroupNames|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--certificate-thumbprint**|string||certificate_thumbprint|certificateThumbprint|
|**--extensions**|array||extensions|extensions|
|**--file-type**|string||file_type|fileType|
|**--first-seen-date-time**|date-time||first_seen_date_time|firstSeenDateTime|
|**--hashes**|array||hashes|hashes|
|**--last-seen-date-time**|date-time||last_seen_date_time|lastSeenDateTime|
|**--malware-states**|array||malware_states|malwareStates|
|**--names**|array||names|names|
|**--risk-score**|string||risk_score|riskScore|
|**--size**|integer||size|size|
|**--tags**|array||tags|tags|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|
|**--vulnerability-states**|array||vulnerability_states|vulnerabilityStates|

### security create-host-security-profile

create-host-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-host-security-profile|CreateHostSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--first-seen-date-time**|date-time||first_seen_date_time|firstSeenDateTime|
|**--fqdn**|string||fqdn|fqdn|
|**--is-azure-ad-joined**|boolean||is_azure_ad_joined|isAzureAdJoined|
|**--is-azure-ad-registered**|boolean||is_azure_ad_registered|isAzureAdRegistered|
|**--is-hybrid-azure-domain-joined**|boolean||is_hybrid_azure_domain_joined|isHybridAzureDomainJoined|
|**--last-seen-date-time**|date-time||last_seen_date_time|lastSeenDateTime|
|**--logon-users**|array||logon_users|logonUsers|
|**--net-bios-name**|string||net_bios_name|netBiosName|
|**--network-interfaces**|array||network_interfaces|networkInterfaces|
|**--os**|string||os|os|
|**--os-version**|string||os_version|osVersion|
|**--parent-host**|string||parent_host|parentHost|
|**--related-host-ids**|array||related_host_ids|relatedHostIds|
|**--risk-score**|string||risk_score|riskScore|
|**--tags**|array||tags|tags|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security create-ip-security-profile

create-ip-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ip-security-profile|CreateIpSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-group-names**|array||activity_group_names|activityGroupNames|
|**--address**|string||address|address|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--count-hits**|integer||count_hits|countHits|
|**--count-hosts**|integer||count_hosts|countHosts|
|**--first-seen-date-time**|date-time||first_seen_date_time|firstSeenDateTime|
|**--ip-categories**|array||ip_categories|ipCategories|
|**--ip-reference-data**|array||ip_reference_data|ipReferenceData|
|**--last-seen-date-time**|date-time||last_seen_date_time|lastSeenDateTime|
|**--risk-score**|string||risk_score|riskScore|
|**--tags**|array||tags|tags|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security create-provider-tenant-setting

create-provider-tenant-setting a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-provider-tenant-setting|CreateProviderTenantSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--enabled**|boolean||enabled|enabled|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--provider**|string||provider|provider|
|**--vendor**|string||vendor|vendor|

### security create-secure-score

create-secure-score a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-secure-score|CreateSecureScores|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--active-user-count**|integer|Active user count of the given tenant.|active_user_count|activeUserCount|
|**--average-comparative-scores**|array|Average score by different scopes (for example, average by industry, average by seating) and control category (Identity, Data, Device, Apps, Infrastructure) within the scope.|average_comparative_scores|averageComparativeScores|
|**--azure-tenant-id**|string|GUID string for tenant ID.|azure_tenant_id|azureTenantId|
|**--control-scores**|array|Contains tenant scores for a set of controls.|control_scores|controlScores|
|**--created-date-time**|date-time|The date when the entity is created.|created_date_time|createdDateTime|
|**--current-score**|number|Tenant current attained score on specified date.|current_score|currentScore|
|**--enabled-services**|array|Microsoft-provided services for the tenant (for example, Exchange online, Skype, Sharepoint).|enabled_services|enabledServices|
|**--licensed-user-count**|integer|Licensed user count of the given tenant.|licensed_user_count|licensedUserCount|
|**--max-score**|number|Tenant maximum possible score on specified date.|max_score|maxScore|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security create-secure-score-control-profile

create-secure-score-control-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-secure-score-control-profile|CreateSecureScoreControlProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--action-type**|string|Control action type (Config, Review, Behavior).|action_type|actionType|
|**--action-url**|string|URL to where the control can be actioned.|action_url|actionUrl|
|**--azure-tenant-id**|string|GUID string for tenant ID.|azure_tenant_id|azureTenantId|
|**--compliance-information**|array||compliance_information|complianceInformation|
|**--control-category**|string|Control action category (Identity, Data, Device, Apps, Infrastructure).|control_category|controlCategory|
|**--control-state-updates**|array||control_state_updates|controlStateUpdates|
|**--deprecated**|boolean|Flag to indicate if a control is depreciated.|deprecated|deprecated|
|**--implementation-cost**|string|Resource cost of implemmentating control (low, moderate, high).|implementation_cost|implementationCost|
|**--last-modified-date-time**|date-time|Time at which the control profile entity was last modified. The Timestamp type represents date and time|last_modified_date_time|lastModifiedDateTime|
|**--max-score**|number|max attainable score for the control.|max_score|maxScore|
|**--rank**|integer|Microsoft's stack ranking of control.|rank|rank|
|**--remediation**|string|Description of what the control will help remediate.|remediation|remediation|
|**--remediation-impact**|string|Description of the impact on users of the remediation.|remediation_impact|remediationImpact|
|**--service**|string|Service that owns the control (Exchange, Sharepoint, Azure AD).|service|service|
|**--threats**|array|List of threats the control mitigates (accountBreach,dataDeletion,dataExfiltration,dataSpillage,|threats|threats|
|**--tier**|string||tier|tier|
|**--title**|string|Title of the control.|title|title|
|**--user-impact**|string||user_impact|userImpact|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security create-security-action

create-security-action a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-security-action|CreateSecurityActions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--action-reason**|string||action_reason|actionReason|
|**--app-id**|string||app_id|appId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--client-context**|string||client_context|clientContext|
|**--completed-date-time**|date-time||completed_date_time|completedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--error-info**|object|ResultInfo|error_info|errorInfo|
|**--last-action-date-time**|date-time||last_action_date_time|lastActionDateTime|
|**--name**|string||name|name|
|**--parameters**|array||parameters|parameters|
|**--states**|array||states|states|
|**--status**|choice||status|status|
|**--user**|string||user|user|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security create-ti-indicator

create-ti-indicator a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ti-indicator|CreateTiIndicators|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--action**|choice||action|action|
|**--activity-group-names**|array||activity_group_names|activityGroupNames|
|**--additional-information**|string||additional_information|additionalInformation|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--confidence**|integer||confidence|confidence|
|**--description**|string||description|description|
|**--diamond-model**|choice||diamond_model|diamondModel|
|**--domain-name**|string||domain_name|domainName|
|**--email-encoding**|string||email_encoding|emailEncoding|
|**--email-language**|string||email_language|emailLanguage|
|**--email-recipient**|string||email_recipient|emailRecipient|
|**--email-sender-address**|string||email_sender_address|emailSenderAddress|
|**--email-sender-name**|string||email_sender_name|emailSenderName|
|**--email-source-domain**|string||email_source_domain|emailSourceDomain|
|**--email-source-ip-address**|string||email_source_ip_address|emailSourceIpAddress|
|**--email-subject**|string||email_subject|emailSubject|
|**--email-x-mailer**|string||email_x_mailer|emailXMailer|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--external-id**|string||external_id|externalId|
|**--file-compile-date-time**|date-time||file_compile_date_time|fileCompileDateTime|
|**--file-created-date-time**|date-time||file_created_date_time|fileCreatedDateTime|
|**--file-hash-type**|choice||file_hash_type|fileHashType|
|**--file-hash-value**|string||file_hash_value|fileHashValue|
|**--file-mutex-name**|string||file_mutex_name|fileMutexName|
|**--file-name**|string||file_name|fileName|
|**--file-packer**|string||file_packer|filePacker|
|**--file-path**|string||file_path|filePath|
|**--file-size**|integer||file_size|fileSize|
|**--file-type**|string||file_type|fileType|
|**--ingested-date-time**|date-time||ingested_date_time|ingestedDateTime|
|**--is-active**|boolean||is_active|isActive|
|**--kill-chain**|array||kill_chain|killChain|
|**--known-false-positives**|string||known_false_positives|knownFalsePositives|
|**--last-reported-date-time**|date-time||last_reported_date_time|lastReportedDateTime|
|**--malware-family-names**|array||malware_family_names|malwareFamilyNames|
|**--network-cidr-block**|string||network_cidr_block|networkCidrBlock|
|**--network-destination-asn**|integer||network_destination_asn|networkDestinationAsn|
|**--network-destination-cidr-block**|string||network_destination_cidr_block|networkDestinationCidrBlock|
|**--network-destination-i-pv4**|string||network_destination_i_pv4|networkDestinationIPv4|
|**--network-destination-i-pv6**|string||network_destination_i_pv6|networkDestinationIPv6|
|**--network-destination-port**|integer||network_destination_port|networkDestinationPort|
|**--network-i-pv4**|string||network_i_pv4|networkIPv4|
|**--network-i-pv6**|string||network_i_pv6|networkIPv6|
|**--network-port**|integer||network_port|networkPort|
|**--network-protocol**|integer||network_protocol|networkProtocol|
|**--network-source-asn**|integer||network_source_asn|networkSourceAsn|
|**--network-source-cidr-block**|string||network_source_cidr_block|networkSourceCidrBlock|
|**--network-source-i-pv4**|string||network_source_i_pv4|networkSourceIPv4|
|**--network-source-i-pv6**|string||network_source_i_pv6|networkSourceIPv6|
|**--network-source-port**|integer||network_source_port|networkSourcePort|
|**--passive-only**|boolean||passive_only|passiveOnly|
|**--severity**|integer||severity|severity|
|**--tags**|array||tags|tags|
|**--target-product**|string||target_product|targetProduct|
|**--threat-type**|string||threat_type|threatType|
|**--tlp-level**|choice||tlp_level|tlpLevel|
|**--url**|string||url|url|
|**--user-agent**|string||user_agent|userAgent|

### security create-user-security-profile

create-user-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user-security-profile|CreateUserSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--accounts**|array||accounts|accounts|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--risk-score**|string||risk_score|riskScore|
|**--tags**|array||tags|tags|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security delete

delete a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAlerts|
|delete|DeleteCloudAppSecurityProfiles|
|delete|DeleteDomainSecurityProfiles|
|delete|DeleteFileSecurityProfiles|
|delete|DeleteHostSecurityProfiles|
|delete|DeleteIpSecurityProfiles|
|delete|DeleteProviderTenantSettings|
|delete|DeleteSecureScoreControlProfiles|
|delete|DeleteSecureScores|
|delete|DeleteSecurityActions|
|delete|DeleteTiIndicators|
|delete|DeleteUserSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alert-id**|string|key: id of alert|alert_id|alert-id|
|**--cloud-app-security-profile-id**|string|key: id of cloudAppSecurityProfile|cloud_app_security_profile_id|cloudAppSecurityProfile-id|
|**--domain-security-profile-id**|string|key: id of domainSecurityProfile|domain_security_profile_id|domainSecurityProfile-id|
|**--file-security-profile-id**|string|key: id of fileSecurityProfile|file_security_profile_id|fileSecurityProfile-id|
|**--host-security-profile-id**|string|key: id of hostSecurityProfile|host_security_profile_id|hostSecurityProfile-id|
|**--ip-security-profile-id**|string|key: id of ipSecurityProfile|ip_security_profile_id|ipSecurityProfile-id|
|**--provider-tenant-setting-id**|string|key: id of providerTenantSetting|provider_tenant_setting_id|providerTenantSetting-id|
|**--secure-score-control-profile-id**|string|key: id of secureScoreControlProfile|secure_score_control_profile_id|secureScoreControlProfile-id|
|**--secure-score-id**|string|key: id of secureScore|secure_score_id|secureScore-id|
|**--security-action-id**|string|key: id of securityAction|security_action_id|securityAction-id|
|**--ti-indicator-id**|string|key: id of tiIndicator|ti_indicator_id|tiIndicator-id|
|**--user-security-profile-id**|string|key: id of userSecurityProfile|user_security_profile_id|userSecurityProfile-id|
|**--if-match**|string|ETag|if_match|If-Match|

### security delete-ti-indicator

delete-ti-indicator a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security.tiIndicators|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete-ti-indicator|deleteTiIndicators|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

### security delete-ti-indicator-by-external-id

delete-ti-indicator-by-external-id a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security.tiIndicators|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete-ti-indicator-by-external-id|deleteTiIndicatorsByExternalId|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

### security get-alert

get-alert a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-alert|GetAlerts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alert-id**|string|key: id of alert|alert_id|alert-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-cloud-app-security-profile

get-cloud-app-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-cloud-app-security-profile|GetCloudAppSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--cloud-app-security-profile-id**|string|key: id of cloudAppSecurityProfile|cloud_app_security_profile_id|cloudAppSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-domain-security-profile

get-domain-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-domain-security-profile|GetDomainSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-security-profile-id**|string|key: id of domainSecurityProfile|domain_security_profile_id|domainSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-file-security-profile

get-file-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-file-security-profile|GetFileSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--file-security-profile-id**|string|key: id of fileSecurityProfile|file_security_profile_id|fileSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-host-security-profile

get-host-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-host-security-profile|GetHostSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--host-security-profile-id**|string|key: id of hostSecurityProfile|host_security_profile_id|hostSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-ip-security-profile

get-ip-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ip-security-profile|GetIpSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ip-security-profile-id**|string|key: id of ipSecurityProfile|ip_security_profile_id|ipSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-provider-tenant-setting

get-provider-tenant-setting a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-provider-tenant-setting|GetProviderTenantSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provider-tenant-setting-id**|string|key: id of providerTenantSetting|provider_tenant_setting_id|providerTenantSetting-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-secure-score

get-secure-score a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-secure-score|GetSecureScores|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--secure-score-id**|string|key: id of secureScore|secure_score_id|secureScore-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-secure-score-control-profile

get-secure-score-control-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-secure-score-control-profile|GetSecureScoreControlProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--secure-score-control-profile-id**|string|key: id of secureScoreControlProfile|secure_score_control_profile_id|secureScoreControlProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-security

get-security a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security.security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-security|GetSecurity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-security-action

get-security-action a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-security-action|GetSecurityActions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--security-action-id**|string|key: id of securityAction|security_action_id|securityAction-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-ti-indicator

get-ti-indicator a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ti-indicator|GetTiIndicators|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ti-indicator-id**|string|key: id of tiIndicator|ti_indicator_id|tiIndicator-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security get-user-security-profile

get-user-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-security-profile|GetUserSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-security-profile-id**|string|key: id of userSecurityProfile|user_security_profile_id|userSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-alert

list-alert a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-alert|ListAlerts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-cloud-app-security-profile

list-cloud-app-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-cloud-app-security-profile|ListCloudAppSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-domain-security-profile

list-domain-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-domain-security-profile|ListDomainSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-file-security-profile

list-file-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-file-security-profile|ListFileSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-host-security-profile

list-host-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-host-security-profile|ListHostSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-ip-security-profile

list-ip-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ip-security-profile|ListIpSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-provider-tenant-setting

list-provider-tenant-setting a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-provider-tenant-setting|ListProviderTenantSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-secure-score

list-secure-score a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-secure-score|ListSecureScores|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-secure-score-control-profile

list-secure-score-control-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-secure-score-control-profile|ListSecureScoreControlProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-security-action

list-security-action a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-security-action|ListSecurityActions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-ti-indicator

list-ti-indicator a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ti-indicator|ListTiIndicators|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security list-user-security-profile

list-user-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user-security-profile|ListUserSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### security submit-ti-indicator

submit-ti-indicator a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security.tiIndicators|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|submit-ti-indicator|submitTiIndicators|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

### security update-alert

update-alert a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security.alerts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-alert|updateAlerts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

### security update-cloud-app-security-profile

update-cloud-app-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-cloud-app-security-profile|UpdateCloudAppSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--cloud-app-security-profile-id**|string|key: id of cloudAppSecurityProfile|cloud_app_security_profile_id|cloudAppSecurityProfile-id|
|**--id**|string|Read-only.|id|id|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--deployment-package-url**|string||deployment_package_url|deploymentPackageUrl|
|**--destination-service-name**|string||destination_service_name|destinationServiceName|
|**--is-signed**|boolean||is_signed|isSigned|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--manifest**|string||manifest|manifest|
|**--name**|string||name|name|
|**--permissions-required**|choice||permissions_required|permissionsRequired|
|**--platform**|string||platform|platform|
|**--policy-name**|string||policy_name|policyName|
|**--publisher**|string||publisher|publisher|
|**--risk-score**|string||risk_score|riskScore|
|**--tags**|array||tags|tags|
|**--type**|string||type|type|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security update-domain-security-profile

update-domain-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-domain-security-profile|UpdateDomainSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-security-profile-id**|string|key: id of domainSecurityProfile|domain_security_profile_id|domainSecurityProfile-id|
|**--id**|string|Read-only.|id|id|
|**--activity-group-names**|array||activity_group_names|activityGroupNames|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--count-hits**|integer||count_hits|countHits|
|**--count-in-org**|integer||count_in_org|countInOrg|
|**--domain-categories**|array||domain_categories|domainCategories|
|**--domain-registered-date-time**|date-time||domain_registered_date_time|domainRegisteredDateTime|
|**--first-seen-date-time**|date-time||first_seen_date_time|firstSeenDateTime|
|**--last-seen-date-time**|date-time||last_seen_date_time|lastSeenDateTime|
|**--name**|string||name|name|
|**--registrant**|object|domainRegistrant|registrant|registrant|
|**--risk-score**|string||risk_score|riskScore|
|**--tags**|array||tags|tags|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security update-file-security-profile

update-file-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-file-security-profile|UpdateFileSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--file-security-profile-id**|string|key: id of fileSecurityProfile|file_security_profile_id|fileSecurityProfile-id|
|**--id**|string|Read-only.|id|id|
|**--activity-group-names**|array||activity_group_names|activityGroupNames|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--certificate-thumbprint**|string||certificate_thumbprint|certificateThumbprint|
|**--extensions**|array||extensions|extensions|
|**--file-type**|string||file_type|fileType|
|**--first-seen-date-time**|date-time||first_seen_date_time|firstSeenDateTime|
|**--hashes**|array||hashes|hashes|
|**--last-seen-date-time**|date-time||last_seen_date_time|lastSeenDateTime|
|**--malware-states**|array||malware_states|malwareStates|
|**--names**|array||names|names|
|**--risk-score**|string||risk_score|riskScore|
|**--size**|integer||size|size|
|**--tags**|array||tags|tags|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|
|**--vulnerability-states**|array||vulnerability_states|vulnerabilityStates|

### security update-host-security-profile

update-host-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-host-security-profile|UpdateHostSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--host-security-profile-id**|string|key: id of hostSecurityProfile|host_security_profile_id|hostSecurityProfile-id|
|**--id**|string|Read-only.|id|id|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--first-seen-date-time**|date-time||first_seen_date_time|firstSeenDateTime|
|**--fqdn**|string||fqdn|fqdn|
|**--is-azure-ad-joined**|boolean||is_azure_ad_joined|isAzureAdJoined|
|**--is-azure-ad-registered**|boolean||is_azure_ad_registered|isAzureAdRegistered|
|**--is-hybrid-azure-domain-joined**|boolean||is_hybrid_azure_domain_joined|isHybridAzureDomainJoined|
|**--last-seen-date-time**|date-time||last_seen_date_time|lastSeenDateTime|
|**--logon-users**|array||logon_users|logonUsers|
|**--net-bios-name**|string||net_bios_name|netBiosName|
|**--network-interfaces**|array||network_interfaces|networkInterfaces|
|**--os**|string||os|os|
|**--os-version**|string||os_version|osVersion|
|**--parent-host**|string||parent_host|parentHost|
|**--related-host-ids**|array||related_host_ids|relatedHostIds|
|**--risk-score**|string||risk_score|riskScore|
|**--tags**|array||tags|tags|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security update-ip-security-profile

update-ip-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-ip-security-profile|UpdateIpSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ip-security-profile-id**|string|key: id of ipSecurityProfile|ip_security_profile_id|ipSecurityProfile-id|
|**--id**|string|Read-only.|id|id|
|**--activity-group-names**|array||activity_group_names|activityGroupNames|
|**--address**|string||address|address|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--count-hits**|integer||count_hits|countHits|
|**--count-hosts**|integer||count_hosts|countHosts|
|**--first-seen-date-time**|date-time||first_seen_date_time|firstSeenDateTime|
|**--ip-categories**|array||ip_categories|ipCategories|
|**--ip-reference-data**|array||ip_reference_data|ipReferenceData|
|**--last-seen-date-time**|date-time||last_seen_date_time|lastSeenDateTime|
|**--risk-score**|string||risk_score|riskScore|
|**--tags**|array||tags|tags|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security update-provider-tenant-setting

update-provider-tenant-setting a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-provider-tenant-setting|UpdateProviderTenantSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provider-tenant-setting-id**|string|key: id of providerTenantSetting|provider_tenant_setting_id|providerTenantSetting-id|
|**--id**|string|Read-only.|id|id|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--enabled**|boolean||enabled|enabled|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--provider**|string||provider|provider|
|**--vendor**|string||vendor|vendor|

### security update-secure-score

update-secure-score a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-secure-score|UpdateSecureScores|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--secure-score-id**|string|key: id of secureScore|secure_score_id|secureScore-id|
|**--id**|string|Read-only.|id|id|
|**--active-user-count**|integer|Active user count of the given tenant.|active_user_count|activeUserCount|
|**--average-comparative-scores**|array|Average score by different scopes (for example, average by industry, average by seating) and control category (Identity, Data, Device, Apps, Infrastructure) within the scope.|average_comparative_scores|averageComparativeScores|
|**--azure-tenant-id**|string|GUID string for tenant ID.|azure_tenant_id|azureTenantId|
|**--control-scores**|array|Contains tenant scores for a set of controls.|control_scores|controlScores|
|**--created-date-time**|date-time|The date when the entity is created.|created_date_time|createdDateTime|
|**--current-score**|number|Tenant current attained score on specified date.|current_score|currentScore|
|**--enabled-services**|array|Microsoft-provided services for the tenant (for example, Exchange online, Skype, Sharepoint).|enabled_services|enabledServices|
|**--licensed-user-count**|integer|Licensed user count of the given tenant.|licensed_user_count|licensedUserCount|
|**--max-score**|number|Tenant maximum possible score on specified date.|max_score|maxScore|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security update-secure-score-control-profile

update-secure-score-control-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-secure-score-control-profile|UpdateSecureScoreControlProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--secure-score-control-profile-id**|string|key: id of secureScoreControlProfile|secure_score_control_profile_id|secureScoreControlProfile-id|
|**--id**|string|Read-only.|id|id|
|**--action-type**|string|Control action type (Config, Review, Behavior).|action_type|actionType|
|**--action-url**|string|URL to where the control can be actioned.|action_url|actionUrl|
|**--azure-tenant-id**|string|GUID string for tenant ID.|azure_tenant_id|azureTenantId|
|**--compliance-information**|array||compliance_information|complianceInformation|
|**--control-category**|string|Control action category (Identity, Data, Device, Apps, Infrastructure).|control_category|controlCategory|
|**--control-state-updates**|array||control_state_updates|controlStateUpdates|
|**--deprecated**|boolean|Flag to indicate if a control is depreciated.|deprecated|deprecated|
|**--implementation-cost**|string|Resource cost of implemmentating control (low, moderate, high).|implementation_cost|implementationCost|
|**--last-modified-date-time**|date-time|Time at which the control profile entity was last modified. The Timestamp type represents date and time|last_modified_date_time|lastModifiedDateTime|
|**--max-score**|number|max attainable score for the control.|max_score|maxScore|
|**--rank**|integer|Microsoft's stack ranking of control.|rank|rank|
|**--remediation**|string|Description of what the control will help remediate.|remediation|remediation|
|**--remediation-impact**|string|Description of the impact on users of the remediation.|remediation_impact|remediationImpact|
|**--service**|string|Service that owns the control (Exchange, Sharepoint, Azure AD).|service|service|
|**--threats**|array|List of threats the control mitigates (accountBreach,dataDeletion,dataExfiltration,dataSpillage,|threats|threats|
|**--tier**|string||tier|tier|
|**--title**|string|Title of the control.|title|title|
|**--user-impact**|string||user_impact|userImpact|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security update-security

update-security a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security.security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-security|UpdateSecurity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--provider-status**|array||provider_status|providerStatus|
|**--alerts**|array|Read-only. Nullable.|alerts|alerts|
|**--cloud-app-security-profiles**|array||cloud_app_security_profiles|cloudAppSecurityProfiles|
|**--domain-security-profiles**|array||domain_security_profiles|domainSecurityProfiles|
|**--file-security-profiles**|array||file_security_profiles|fileSecurityProfiles|
|**--host-security-profiles**|array||host_security_profiles|hostSecurityProfiles|
|**--ip-security-profiles**|array||ip_security_profiles|ipSecurityProfiles|
|**--provider-tenant-settings**|array||provider_tenant_settings|providerTenantSettings|
|**--secure-score-control-profiles**|array||secure_score_control_profiles|secureScoreControlProfiles|
|**--secure-scores**|array||secure_scores|secureScores|
|**--security-actions**|array||security_actions|securityActions|
|**--ti-indicators**|array||ti_indicators|tiIndicators|
|**--user-security-profiles**|array||user_security_profiles|userSecurityProfiles|

### security update-security-action

update-security-action a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-security-action|UpdateSecurityActions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--security-action-id**|string|key: id of securityAction|security_action_id|securityAction-id|
|**--id**|string|Read-only.|id|id|
|**--action-reason**|string||action_reason|actionReason|
|**--app-id**|string||app_id|appId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--client-context**|string||client_context|clientContext|
|**--completed-date-time**|date-time||completed_date_time|completedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--error-info**|object|ResultInfo|error_info|errorInfo|
|**--last-action-date-time**|date-time||last_action_date_time|lastActionDateTime|
|**--name**|string||name|name|
|**--parameters**|array||parameters|parameters|
|**--states**|array||states|states|
|**--status**|choice||status|status|
|**--user**|string||user|user|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|

### security update-ti-indicator

update-ti-indicator a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security.tiIndicators|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-ti-indicator|updateTiIndicators|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

### security update-user-security-profile

update-user-security-profile a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user-security-profile|UpdateUserSecurityProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-security-profile-id**|string|key: id of userSecurityProfile|user_security_profile_id|userSecurityProfile-id|
|**--id**|string|Read-only.|id|id|
|**--accounts**|array||accounts|accounts|
|**--azure-subscription-id**|string||azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--risk-score**|string||risk_score|riskScore|
|**--tags**|array||tags|tags|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|
