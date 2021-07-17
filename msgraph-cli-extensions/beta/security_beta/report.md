# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az security_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az security_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az security security|Security.security|[commands](#CommandsInSecurity.security)|
|az security security|Security|[commands](#CommandsInSecurity)|
|az security security-alert|Security.alerts|[commands](#CommandsInSecurity.alerts)|
|az security security-action|Security.securityActions|[commands](#CommandsInSecurity.securityActions)|
|az security security-ti-indicator|Security.tiIndicators|[commands](#CommandsInSecurity.tiIndicators)|

## COMMANDS
### <a name="CommandsInSecurity.security">Commands in `az security security` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az security security update](#Security.securityUpdateSecurity)|UpdateSecurity|[Parameters](#ParametersSecurity.securityUpdateSecurity)|Not Found|
|[az security security create-action](#Security.securityCreateSecurityActions)|CreateSecurityActions|[Parameters](#ParametersSecurity.securityCreateSecurityActions)|Not Found|
|[az security security list-action](#Security.securityListSecurityActions)|ListSecurityActions|[Parameters](#ParametersSecurity.securityListSecurityActions)|Not Found|
|[az security security show-security](#Security.securityGetSecurity)|GetSecurity|[Parameters](#ParametersSecurity.securityGetSecurity)|Not Found|
|[az security security update-action](#Security.securityUpdateSecurityActions)|UpdateSecurityActions|[Parameters](#ParametersSecurity.securityUpdateSecurityActions)|Not Found|

### <a name="CommandsInSecurity">Commands in `az security security` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az security security create-alert](#SecurityCreateAlerts)|CreateAlerts|[Parameters](#ParametersSecurityCreateAlerts)|Not Found|
|[az security security create-cloud-app-security-profile](#SecurityCreateCloudAppSecurityProfiles)|CreateCloudAppSecurityProfiles|[Parameters](#ParametersSecurityCreateCloudAppSecurityProfiles)|Not Found|
|[az security security create-domain-security-profile](#SecurityCreateDomainSecurityProfiles)|CreateDomainSecurityProfiles|[Parameters](#ParametersSecurityCreateDomainSecurityProfiles)|Not Found|
|[az security security create-file-security-profile](#SecurityCreateFileSecurityProfiles)|CreateFileSecurityProfiles|[Parameters](#ParametersSecurityCreateFileSecurityProfiles)|Not Found|
|[az security security create-host-security-profile](#SecurityCreateHostSecurityProfiles)|CreateHostSecurityProfiles|[Parameters](#ParametersSecurityCreateHostSecurityProfiles)|Not Found|
|[az security security create-ip-security-profile](#SecurityCreateIpSecurityProfiles)|CreateIpSecurityProfiles|[Parameters](#ParametersSecurityCreateIpSecurityProfiles)|Not Found|
|[az security security create-provider-tenant-setting](#SecurityCreateProviderTenantSettings)|CreateProviderTenantSettings|[Parameters](#ParametersSecurityCreateProviderTenantSettings)|Not Found|
|[az security security create-secure-score](#SecurityCreateSecureScores)|CreateSecureScores|[Parameters](#ParametersSecurityCreateSecureScores)|Not Found|
|[az security security create-secure-score-control-profile](#SecurityCreateSecureScoreControlProfiles)|CreateSecureScoreControlProfiles|[Parameters](#ParametersSecurityCreateSecureScoreControlProfiles)|Not Found|
|[az security security create-ti-indicator](#SecurityCreateTiIndicators)|CreateTiIndicators|[Parameters](#ParametersSecurityCreateTiIndicators)|Not Found|
|[az security security create-user-security-profile](#SecurityCreateUserSecurityProfiles)|CreateUserSecurityProfiles|[Parameters](#ParametersSecurityCreateUserSecurityProfiles)|Not Found|
|[az security security delete-alert](#SecurityDeleteAlerts)|DeleteAlerts|[Parameters](#ParametersSecurityDeleteAlerts)|Not Found|
|[az security security delete-cloud-app-security-profile](#SecurityDeleteCloudAppSecurityProfiles)|DeleteCloudAppSecurityProfiles|[Parameters](#ParametersSecurityDeleteCloudAppSecurityProfiles)|Not Found|
|[az security security delete-domain-security-profile](#SecurityDeleteDomainSecurityProfiles)|DeleteDomainSecurityProfiles|[Parameters](#ParametersSecurityDeleteDomainSecurityProfiles)|Not Found|
|[az security security delete-file-security-profile](#SecurityDeleteFileSecurityProfiles)|DeleteFileSecurityProfiles|[Parameters](#ParametersSecurityDeleteFileSecurityProfiles)|Not Found|
|[az security security delete-host-security-profile](#SecurityDeleteHostSecurityProfiles)|DeleteHostSecurityProfiles|[Parameters](#ParametersSecurityDeleteHostSecurityProfiles)|Not Found|
|[az security security delete-ip-security-profile](#SecurityDeleteIpSecurityProfiles)|DeleteIpSecurityProfiles|[Parameters](#ParametersSecurityDeleteIpSecurityProfiles)|Not Found|
|[az security security delete-provider-tenant-setting](#SecurityDeleteProviderTenantSettings)|DeleteProviderTenantSettings|[Parameters](#ParametersSecurityDeleteProviderTenantSettings)|Not Found|
|[az security security delete-secure-score](#SecurityDeleteSecureScores)|DeleteSecureScores|[Parameters](#ParametersSecurityDeleteSecureScores)|Not Found|
|[az security security delete-secure-score-control-profile](#SecurityDeleteSecureScoreControlProfiles)|DeleteSecureScoreControlProfiles|[Parameters](#ParametersSecurityDeleteSecureScoreControlProfiles)|Not Found|
|[az security security delete-security-action](#SecurityDeleteSecurityActions)|DeleteSecurityActions|[Parameters](#ParametersSecurityDeleteSecurityActions)|Not Found|
|[az security security delete-ti-indicator](#SecurityDeleteTiIndicators)|DeleteTiIndicators|[Parameters](#ParametersSecurityDeleteTiIndicators)|Not Found|
|[az security security delete-user-security-profile](#SecurityDeleteUserSecurityProfiles)|DeleteUserSecurityProfiles|[Parameters](#ParametersSecurityDeleteUserSecurityProfiles)|Not Found|
|[az security security list-alert](#SecurityListAlerts)|ListAlerts|[Parameters](#ParametersSecurityListAlerts)|Not Found|
|[az security security list-cloud-app-security-profile](#SecurityListCloudAppSecurityProfiles)|ListCloudAppSecurityProfiles|[Parameters](#ParametersSecurityListCloudAppSecurityProfiles)|Not Found|
|[az security security list-domain-security-profile](#SecurityListDomainSecurityProfiles)|ListDomainSecurityProfiles|[Parameters](#ParametersSecurityListDomainSecurityProfiles)|Not Found|
|[az security security list-file-security-profile](#SecurityListFileSecurityProfiles)|ListFileSecurityProfiles|[Parameters](#ParametersSecurityListFileSecurityProfiles)|Not Found|
|[az security security list-host-security-profile](#SecurityListHostSecurityProfiles)|ListHostSecurityProfiles|[Parameters](#ParametersSecurityListHostSecurityProfiles)|Not Found|
|[az security security list-ip-security-profile](#SecurityListIpSecurityProfiles)|ListIpSecurityProfiles|[Parameters](#ParametersSecurityListIpSecurityProfiles)|Not Found|
|[az security security list-provider-tenant-setting](#SecurityListProviderTenantSettings)|ListProviderTenantSettings|[Parameters](#ParametersSecurityListProviderTenantSettings)|Not Found|
|[az security security list-secure-score](#SecurityListSecureScores)|ListSecureScores|[Parameters](#ParametersSecurityListSecureScores)|Not Found|
|[az security security list-secure-score-control-profile](#SecurityListSecureScoreControlProfiles)|ListSecureScoreControlProfiles|[Parameters](#ParametersSecurityListSecureScoreControlProfiles)|Not Found|
|[az security security list-ti-indicator](#SecurityListTiIndicators)|ListTiIndicators|[Parameters](#ParametersSecurityListTiIndicators)|Not Found|
|[az security security list-user-security-profile](#SecurityListUserSecurityProfiles)|ListUserSecurityProfiles|[Parameters](#ParametersSecurityListUserSecurityProfiles)|Not Found|
|[az security security show-alert](#SecurityGetAlerts)|GetAlerts|[Parameters](#ParametersSecurityGetAlerts)|Not Found|
|[az security security show-cloud-app-security-profile](#SecurityGetCloudAppSecurityProfiles)|GetCloudAppSecurityProfiles|[Parameters](#ParametersSecurityGetCloudAppSecurityProfiles)|Not Found|
|[az security security show-domain-security-profile](#SecurityGetDomainSecurityProfiles)|GetDomainSecurityProfiles|[Parameters](#ParametersSecurityGetDomainSecurityProfiles)|Not Found|
|[az security security show-file-security-profile](#SecurityGetFileSecurityProfiles)|GetFileSecurityProfiles|[Parameters](#ParametersSecurityGetFileSecurityProfiles)|Not Found|
|[az security security show-host-security-profile](#SecurityGetHostSecurityProfiles)|GetHostSecurityProfiles|[Parameters](#ParametersSecurityGetHostSecurityProfiles)|Not Found|
|[az security security show-ip-security-profile](#SecurityGetIpSecurityProfiles)|GetIpSecurityProfiles|[Parameters](#ParametersSecurityGetIpSecurityProfiles)|Not Found|
|[az security security show-provider-tenant-setting](#SecurityGetProviderTenantSettings)|GetProviderTenantSettings|[Parameters](#ParametersSecurityGetProviderTenantSettings)|Not Found|
|[az security security show-secure-score](#SecurityGetSecureScores)|GetSecureScores|[Parameters](#ParametersSecurityGetSecureScores)|Not Found|
|[az security security show-secure-score-control-profile](#SecurityGetSecureScoreControlProfiles)|GetSecureScoreControlProfiles|[Parameters](#ParametersSecurityGetSecureScoreControlProfiles)|Not Found|
|[az security security show-security-action](#SecurityGetSecurityActions)|GetSecurityActions|[Parameters](#ParametersSecurityGetSecurityActions)|Not Found|
|[az security security show-ti-indicator](#SecurityGetTiIndicators)|GetTiIndicators|[Parameters](#ParametersSecurityGetTiIndicators)|Not Found|
|[az security security show-user-security-profile](#SecurityGetUserSecurityProfiles)|GetUserSecurityProfiles|[Parameters](#ParametersSecurityGetUserSecurityProfiles)|Not Found|
|[az security security update-alert](#SecurityUpdateAlerts)|UpdateAlerts|[Parameters](#ParametersSecurityUpdateAlerts)|Not Found|
|[az security security update-cloud-app-security-profile](#SecurityUpdateCloudAppSecurityProfiles)|UpdateCloudAppSecurityProfiles|[Parameters](#ParametersSecurityUpdateCloudAppSecurityProfiles)|Not Found|
|[az security security update-domain-security-profile](#SecurityUpdateDomainSecurityProfiles)|UpdateDomainSecurityProfiles|[Parameters](#ParametersSecurityUpdateDomainSecurityProfiles)|Not Found|
|[az security security update-file-security-profile](#SecurityUpdateFileSecurityProfiles)|UpdateFileSecurityProfiles|[Parameters](#ParametersSecurityUpdateFileSecurityProfiles)|Not Found|
|[az security security update-host-security-profile](#SecurityUpdateHostSecurityProfiles)|UpdateHostSecurityProfiles|[Parameters](#ParametersSecurityUpdateHostSecurityProfiles)|Not Found|
|[az security security update-ip-security-profile](#SecurityUpdateIpSecurityProfiles)|UpdateIpSecurityProfiles|[Parameters](#ParametersSecurityUpdateIpSecurityProfiles)|Not Found|
|[az security security update-provider-tenant-setting](#SecurityUpdateProviderTenantSettings)|UpdateProviderTenantSettings|[Parameters](#ParametersSecurityUpdateProviderTenantSettings)|Not Found|
|[az security security update-secure-score](#SecurityUpdateSecureScores)|UpdateSecureScores|[Parameters](#ParametersSecurityUpdateSecureScores)|Not Found|
|[az security security update-secure-score-control-profile](#SecurityUpdateSecureScoreControlProfiles)|UpdateSecureScoreControlProfiles|[Parameters](#ParametersSecurityUpdateSecureScoreControlProfiles)|Not Found|
|[az security security update-ti-indicator](#SecurityUpdateTiIndicators)|UpdateTiIndicators|[Parameters](#ParametersSecurityUpdateTiIndicators)|Not Found|
|[az security security update-user-security-profile](#SecurityUpdateUserSecurityProfiles)|UpdateUserSecurityProfiles|[Parameters](#ParametersSecurityUpdateUserSecurityProfiles)|Not Found|

### <a name="CommandsInSecurity.securityActions">Commands in `az security security-action` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az security security-action cancel-security-action](#Security.securityActionscancelSecurityAction)|cancelSecurityAction|[Parameters](#ParametersSecurity.securityActionscancelSecurityAction)|Not Found|

### <a name="CommandsInSecurity.alerts">Commands in `az security security-alert` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az security security-alert update-alert](#Security.alertsupdateAlerts)|updateAlerts|[Parameters](#ParametersSecurity.alertsupdateAlerts)|Not Found|

### <a name="CommandsInSecurity.tiIndicators">Commands in `az security security-ti-indicator` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az security security-ti-indicator delete-ti-indicator](#Security.tiIndicatorsdeleteTiIndicators)|deleteTiIndicators|[Parameters](#ParametersSecurity.tiIndicatorsdeleteTiIndicators)|Not Found|
|[az security security-ti-indicator delete-ti-indicator-by-external-id](#Security.tiIndicatorsdeleteTiIndicatorsByExternalId)|deleteTiIndicatorsByExternalId|[Parameters](#ParametersSecurity.tiIndicatorsdeleteTiIndicatorsByExternalId)|Not Found|
|[az security security-ti-indicator submit-ti-indicator](#Security.tiIndicatorssubmitTiIndicators)|submitTiIndicators|[Parameters](#ParametersSecurity.tiIndicatorssubmitTiIndicators)|Not Found|
|[az security security-ti-indicator update-ti-indicator](#Security.tiIndicatorsupdateTiIndicators)|updateTiIndicators|[Parameters](#ParametersSecurity.tiIndicatorsupdateTiIndicators)|Not Found|


## COMMAND DETAILS

### group `az security security`
#### <a name="Security.securityUpdateSecurity">Command `az security security update`</a>

##### <a name="ParametersSecurity.securityUpdateSecurity">Parameters</a> 
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

#### <a name="Security.securityCreateSecurityActions">Command `az security security create-action`</a>

##### <a name="ParametersSecurity.securityCreateSecurityActions">Parameters</a> 
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

#### <a name="Security.securityListSecurityActions">Command `az security security list-action`</a>

##### <a name="ParametersSecurity.securityListSecurityActions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="Security.securityGetSecurity">Command `az security security show-security`</a>

##### <a name="ParametersSecurity.securityGetSecurity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="Security.securityUpdateSecurityActions">Command `az security security update-action`</a>

##### <a name="ParametersSecurity.securityUpdateSecurityActions">Parameters</a> 
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

### group `az security security`
#### <a name="SecurityCreateAlerts">Command `az security security create-alert`</a>

##### <a name="ParametersSecurityCreateAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-group-name**|string|Name or alias of the activity group (attacker) this alert is attributed to.|activity_group_name|activityGroupName|
|**--assigned-to**|string|Name of the analyst the alert is assigned to for triage, investigation, or remediation (supports update).|assigned_to|assignedTo|
|**--azure-subscription-id**|string|Azure subscription ID, present if this alert is related to an Azure resource.|azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string|Azure Active Directory tenant ID. Required.|azure_tenant_id|azureTenantId|
|**--category**|string|Category of the alert (for example, credentialTheft, ransomware, etc.).|category|category|
|**--closed-date-time**|date-time|Time at which the alert was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z' (supports update).|closed_date_time|closedDateTime|
|**--cloud-app-states**|array|Security-related stateful information generated by the provider about the cloud application/s related to this alert.|cloud_app_states|cloudAppStates|
|**--comments**|array|Customer-provided comments on alert (for customer alert management) (supports update).|comments|comments|
|**--confidence**|integer|Confidence of the detection logic (percentage between 1-100).|confidence|confidence|
|**--created-date-time**|date-time|Time at which the alert was created by the alert provider. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Required.|created_date_time|createdDateTime|
|**--description**|string|Alert description.|description|description|
|**--detection-ids**|array|Set of alerts related to this alert entity (each alert is pushed to the SIEM as a separate record).|detection_ids|detectionIds|
|**--event-date-time**|date-time|Time at which the event(s) that served as the trigger(s) to generate the alert occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Required.|event_date_time|eventDateTime|
|**--feedback**|choice||feedback|feedback|
|**--file-states**|array|Security-related stateful information generated by the provider about the file(s) related to this alert.|file_states|fileStates|
|**--history-states**|array||history_states|historyStates|
|**--host-states**|array|Security-related stateful information generated by the provider about the host(s) related to this alert.|host_states|hostStates|
|**--incident-ids**|array|IDs of incidents related to current alert.|incident_ids|incidentIds|
|**--last-modified-date-time**|date-time|Time at which the alert entity was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|last_modified_date_time|lastModifiedDateTime|
|**--malware-states**|array|Threat Intelligence pertaining to malware related to this alert.|malware_states|malwareStates|
|**--network-connections**|array|Security-related stateful information generated by the provider about the network connection(s) related to this alert.|network_connections|networkConnections|
|**--processes**|array|Security-related stateful information generated by the provider about the process or processes related to this alert.|processes|processes|
|**--recommended-actions**|array|Vendor/provider recommended action(s) to take as a result of the alert (for example, isolate machine, enforce2FA, reimage host).|recommended_actions|recommendedActions|
|**--registry-key-states**|array|Security-related stateful information generated by the provider about the registry keys related to this alert.|registry_key_states|registryKeyStates|
|**--security-resources**|array|Resources related to current alert. For example, for some alerts this can have the Azure Resource value.|security_resources|securityResources|
|**--severity**|choice||severity|severity|
|**--source-materials**|array|Hyperlinks (URIs) to the source material related to the alert, for example, provider's user interface for alerts or log search, etc.|source_materials|sourceMaterials|
|**--status**|choice||status|status|
|**--tags**|array|User-definable labels that can be applied to an alert and can serve as filter conditions (for example 'HVA', 'SAW', etc.) (supports update).|tags|tags|
|**--title**|string|Alert title. Required.|title|title|
|**--triggers**|array|Security-related information about the specific properties that triggered the alert (properties appearing in the alert). Alerts might contain information about multiple users, hosts, files, ip addresses. This field indicates which properties triggered the alert generation.|triggers|triggers|
|**--user-states**|array|Security-related stateful information generated by the provider about the user accounts related to this alert.|user_states|userStates|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|
|**--vulnerability-states**|array|Threat intelligence pertaining to one or more vulnerabilities related to this alert.|vulnerability_states|vulnerabilityStates|

#### <a name="SecurityCreateCloudAppSecurityProfiles">Command `az security security create-cloud-app-security-profile`</a>

##### <a name="ParametersSecurityCreateCloudAppSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityCreateDomainSecurityProfiles">Command `az security security create-domain-security-profile`</a>

##### <a name="ParametersSecurityCreateDomainSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityCreateFileSecurityProfiles">Command `az security security create-file-security-profile`</a>

##### <a name="ParametersSecurityCreateFileSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityCreateHostSecurityProfiles">Command `az security security create-host-security-profile`</a>

##### <a name="ParametersSecurityCreateHostSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityCreateIpSecurityProfiles">Command `az security security create-ip-security-profile`</a>

##### <a name="ParametersSecurityCreateIpSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityCreateProviderTenantSettings">Command `az security security create-provider-tenant-setting`</a>

##### <a name="ParametersSecurityCreateProviderTenantSettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--enabled**|boolean||enabled|enabled|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--provider**|string||provider|provider|
|**--vendor**|string||vendor|vendor|

#### <a name="SecurityCreateSecureScores">Command `az security security create-secure-score`</a>

##### <a name="ParametersSecurityCreateSecureScores">Parameters</a> 
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

#### <a name="SecurityCreateSecureScoreControlProfiles">Command `az security security create-secure-score-control-profile`</a>

##### <a name="ParametersSecurityCreateSecureScoreControlProfiles">Parameters</a> 
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

#### <a name="SecurityCreateTiIndicators">Command `az security security create-ti-indicator`</a>

##### <a name="ParametersSecurityCreateTiIndicators">Parameters</a> 
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

#### <a name="SecurityCreateUserSecurityProfiles">Command `az security security create-user-security-profile`</a>

##### <a name="ParametersSecurityCreateUserSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityDeleteAlerts">Command `az security security delete-alert`</a>

##### <a name="ParametersSecurityDeleteAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alert-id**|string|key: id of alert|alert_id|alert-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteCloudAppSecurityProfiles">Command `az security security delete-cloud-app-security-profile`</a>

##### <a name="ParametersSecurityDeleteCloudAppSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--cloud-app-security-profile-id**|string|key: id of cloudAppSecurityProfile|cloud_app_security_profile_id|cloudAppSecurityProfile-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteDomainSecurityProfiles">Command `az security security delete-domain-security-profile`</a>

##### <a name="ParametersSecurityDeleteDomainSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-security-profile-id**|string|key: id of domainSecurityProfile|domain_security_profile_id|domainSecurityProfile-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteFileSecurityProfiles">Command `az security security delete-file-security-profile`</a>

##### <a name="ParametersSecurityDeleteFileSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--file-security-profile-id**|string|key: id of fileSecurityProfile|file_security_profile_id|fileSecurityProfile-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteHostSecurityProfiles">Command `az security security delete-host-security-profile`</a>

##### <a name="ParametersSecurityDeleteHostSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--host-security-profile-id**|string|key: id of hostSecurityProfile|host_security_profile_id|hostSecurityProfile-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteIpSecurityProfiles">Command `az security security delete-ip-security-profile`</a>

##### <a name="ParametersSecurityDeleteIpSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ip-security-profile-id**|string|key: id of ipSecurityProfile|ip_security_profile_id|ipSecurityProfile-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteProviderTenantSettings">Command `az security security delete-provider-tenant-setting`</a>

##### <a name="ParametersSecurityDeleteProviderTenantSettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provider-tenant-setting-id**|string|key: id of providerTenantSetting|provider_tenant_setting_id|providerTenantSetting-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteSecureScores">Command `az security security delete-secure-score`</a>

##### <a name="ParametersSecurityDeleteSecureScores">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--secure-score-id**|string|key: id of secureScore|secure_score_id|secureScore-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteSecureScoreControlProfiles">Command `az security security delete-secure-score-control-profile`</a>

##### <a name="ParametersSecurityDeleteSecureScoreControlProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--secure-score-control-profile-id**|string|key: id of secureScoreControlProfile|secure_score_control_profile_id|secureScoreControlProfile-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteSecurityActions">Command `az security security delete-security-action`</a>

##### <a name="ParametersSecurityDeleteSecurityActions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--security-action-id**|string|key: id of securityAction|security_action_id|securityAction-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteTiIndicators">Command `az security security delete-ti-indicator`</a>

##### <a name="ParametersSecurityDeleteTiIndicators">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ti-indicator-id**|string|key: id of tiIndicator|ti_indicator_id|tiIndicator-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteUserSecurityProfiles">Command `az security security delete-user-security-profile`</a>

##### <a name="ParametersSecurityDeleteUserSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-security-profile-id**|string|key: id of userSecurityProfile|user_security_profile_id|userSecurityProfile-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityListAlerts">Command `az security security list-alert`</a>

##### <a name="ParametersSecurityListAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityListCloudAppSecurityProfiles">Command `az security security list-cloud-app-security-profile`</a>

##### <a name="ParametersSecurityListCloudAppSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityListDomainSecurityProfiles">Command `az security security list-domain-security-profile`</a>

##### <a name="ParametersSecurityListDomainSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityListFileSecurityProfiles">Command `az security security list-file-security-profile`</a>

##### <a name="ParametersSecurityListFileSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityListHostSecurityProfiles">Command `az security security list-host-security-profile`</a>

##### <a name="ParametersSecurityListHostSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityListIpSecurityProfiles">Command `az security security list-ip-security-profile`</a>

##### <a name="ParametersSecurityListIpSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityListProviderTenantSettings">Command `az security security list-provider-tenant-setting`</a>

##### <a name="ParametersSecurityListProviderTenantSettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityListSecureScores">Command `az security security list-secure-score`</a>

##### <a name="ParametersSecurityListSecureScores">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityListSecureScoreControlProfiles">Command `az security security list-secure-score-control-profile`</a>

##### <a name="ParametersSecurityListSecureScoreControlProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityListTiIndicators">Command `az security security list-ti-indicator`</a>

##### <a name="ParametersSecurityListTiIndicators">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityListUserSecurityProfiles">Command `az security security list-user-security-profile`</a>

##### <a name="ParametersSecurityListUserSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetAlerts">Command `az security security show-alert`</a>

##### <a name="ParametersSecurityGetAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alert-id**|string|key: id of alert|alert_id|alert-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetCloudAppSecurityProfiles">Command `az security security show-cloud-app-security-profile`</a>

##### <a name="ParametersSecurityGetCloudAppSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--cloud-app-security-profile-id**|string|key: id of cloudAppSecurityProfile|cloud_app_security_profile_id|cloudAppSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetDomainSecurityProfiles">Command `az security security show-domain-security-profile`</a>

##### <a name="ParametersSecurityGetDomainSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-security-profile-id**|string|key: id of domainSecurityProfile|domain_security_profile_id|domainSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetFileSecurityProfiles">Command `az security security show-file-security-profile`</a>

##### <a name="ParametersSecurityGetFileSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--file-security-profile-id**|string|key: id of fileSecurityProfile|file_security_profile_id|fileSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetHostSecurityProfiles">Command `az security security show-host-security-profile`</a>

##### <a name="ParametersSecurityGetHostSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--host-security-profile-id**|string|key: id of hostSecurityProfile|host_security_profile_id|hostSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetIpSecurityProfiles">Command `az security security show-ip-security-profile`</a>

##### <a name="ParametersSecurityGetIpSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ip-security-profile-id**|string|key: id of ipSecurityProfile|ip_security_profile_id|ipSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetProviderTenantSettings">Command `az security security show-provider-tenant-setting`</a>

##### <a name="ParametersSecurityGetProviderTenantSettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provider-tenant-setting-id**|string|key: id of providerTenantSetting|provider_tenant_setting_id|providerTenantSetting-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetSecureScores">Command `az security security show-secure-score`</a>

##### <a name="ParametersSecurityGetSecureScores">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--secure-score-id**|string|key: id of secureScore|secure_score_id|secureScore-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetSecureScoreControlProfiles">Command `az security security show-secure-score-control-profile`</a>

##### <a name="ParametersSecurityGetSecureScoreControlProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--secure-score-control-profile-id**|string|key: id of secureScoreControlProfile|secure_score_control_profile_id|secureScoreControlProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetSecurityActions">Command `az security security show-security-action`</a>

##### <a name="ParametersSecurityGetSecurityActions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--security-action-id**|string|key: id of securityAction|security_action_id|securityAction-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetTiIndicators">Command `az security security show-ti-indicator`</a>

##### <a name="ParametersSecurityGetTiIndicators">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ti-indicator-id**|string|key: id of tiIndicator|ti_indicator_id|tiIndicator-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityGetUserSecurityProfiles">Command `az security security show-user-security-profile`</a>

##### <a name="ParametersSecurityGetUserSecurityProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-security-profile-id**|string|key: id of userSecurityProfile|user_security_profile_id|userSecurityProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="SecurityUpdateAlerts">Command `az security security update-alert`</a>

##### <a name="ParametersSecurityUpdateAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alert-id**|string|key: id of alert|alert_id|alert-id|
|**--id**|string|Read-only.|id|id|
|**--activity-group-name**|string|Name or alias of the activity group (attacker) this alert is attributed to.|activity_group_name|activityGroupName|
|**--assigned-to**|string|Name of the analyst the alert is assigned to for triage, investigation, or remediation (supports update).|assigned_to|assignedTo|
|**--azure-subscription-id**|string|Azure subscription ID, present if this alert is related to an Azure resource.|azure_subscription_id|azureSubscriptionId|
|**--azure-tenant-id**|string|Azure Active Directory tenant ID. Required.|azure_tenant_id|azureTenantId|
|**--category**|string|Category of the alert (for example, credentialTheft, ransomware, etc.).|category|category|
|**--closed-date-time**|date-time|Time at which the alert was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z' (supports update).|closed_date_time|closedDateTime|
|**--cloud-app-states**|array|Security-related stateful information generated by the provider about the cloud application/s related to this alert.|cloud_app_states|cloudAppStates|
|**--comments**|array|Customer-provided comments on alert (for customer alert management) (supports update).|comments|comments|
|**--confidence**|integer|Confidence of the detection logic (percentage between 1-100).|confidence|confidence|
|**--created-date-time**|date-time|Time at which the alert was created by the alert provider. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Required.|created_date_time|createdDateTime|
|**--description**|string|Alert description.|description|description|
|**--detection-ids**|array|Set of alerts related to this alert entity (each alert is pushed to the SIEM as a separate record).|detection_ids|detectionIds|
|**--event-date-time**|date-time|Time at which the event(s) that served as the trigger(s) to generate the alert occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Required.|event_date_time|eventDateTime|
|**--feedback**|choice||feedback|feedback|
|**--file-states**|array|Security-related stateful information generated by the provider about the file(s) related to this alert.|file_states|fileStates|
|**--history-states**|array||history_states|historyStates|
|**--host-states**|array|Security-related stateful information generated by the provider about the host(s) related to this alert.|host_states|hostStates|
|**--incident-ids**|array|IDs of incidents related to current alert.|incident_ids|incidentIds|
|**--last-modified-date-time**|date-time|Time at which the alert entity was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|last_modified_date_time|lastModifiedDateTime|
|**--malware-states**|array|Threat Intelligence pertaining to malware related to this alert.|malware_states|malwareStates|
|**--network-connections**|array|Security-related stateful information generated by the provider about the network connection(s) related to this alert.|network_connections|networkConnections|
|**--processes**|array|Security-related stateful information generated by the provider about the process or processes related to this alert.|processes|processes|
|**--recommended-actions**|array|Vendor/provider recommended action(s) to take as a result of the alert (for example, isolate machine, enforce2FA, reimage host).|recommended_actions|recommendedActions|
|**--registry-key-states**|array|Security-related stateful information generated by the provider about the registry keys related to this alert.|registry_key_states|registryKeyStates|
|**--security-resources**|array|Resources related to current alert. For example, for some alerts this can have the Azure Resource value.|security_resources|securityResources|
|**--severity**|choice||severity|severity|
|**--source-materials**|array|Hyperlinks (URIs) to the source material related to the alert, for example, provider's user interface for alerts or log search, etc.|source_materials|sourceMaterials|
|**--status**|choice||status|status|
|**--tags**|array|User-definable labels that can be applied to an alert and can serve as filter conditions (for example 'HVA', 'SAW', etc.) (supports update).|tags|tags|
|**--title**|string|Alert title. Required.|title|title|
|**--triggers**|array|Security-related information about the specific properties that triggered the alert (properties appearing in the alert). Alerts might contain information about multiple users, hosts, files, ip addresses. This field indicates which properties triggered the alert generation.|triggers|triggers|
|**--user-states**|array|Security-related stateful information generated by the provider about the user accounts related to this alert.|user_states|userStates|
|**--vendor-information**|object|securityVendorInformation|vendor_information|vendorInformation|
|**--vulnerability-states**|array|Threat intelligence pertaining to one or more vulnerabilities related to this alert.|vulnerability_states|vulnerabilityStates|

#### <a name="SecurityUpdateCloudAppSecurityProfiles">Command `az security security update-cloud-app-security-profile`</a>

##### <a name="ParametersSecurityUpdateCloudAppSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityUpdateDomainSecurityProfiles">Command `az security security update-domain-security-profile`</a>

##### <a name="ParametersSecurityUpdateDomainSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityUpdateFileSecurityProfiles">Command `az security security update-file-security-profile`</a>

##### <a name="ParametersSecurityUpdateFileSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityUpdateHostSecurityProfiles">Command `az security security update-host-security-profile`</a>

##### <a name="ParametersSecurityUpdateHostSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityUpdateIpSecurityProfiles">Command `az security security update-ip-security-profile`</a>

##### <a name="ParametersSecurityUpdateIpSecurityProfiles">Parameters</a> 
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

#### <a name="SecurityUpdateProviderTenantSettings">Command `az security security update-provider-tenant-setting`</a>

##### <a name="ParametersSecurityUpdateProviderTenantSettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provider-tenant-setting-id**|string|key: id of providerTenantSetting|provider_tenant_setting_id|providerTenantSetting-id|
|**--id**|string|Read-only.|id|id|
|**--azure-tenant-id**|string||azure_tenant_id|azureTenantId|
|**--enabled**|boolean||enabled|enabled|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--provider**|string||provider|provider|
|**--vendor**|string||vendor|vendor|

#### <a name="SecurityUpdateSecureScores">Command `az security security update-secure-score`</a>

##### <a name="ParametersSecurityUpdateSecureScores">Parameters</a> 
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

#### <a name="SecurityUpdateSecureScoreControlProfiles">Command `az security security update-secure-score-control-profile`</a>

##### <a name="ParametersSecurityUpdateSecureScoreControlProfiles">Parameters</a> 
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

#### <a name="SecurityUpdateTiIndicators">Command `az security security update-ti-indicator`</a>

##### <a name="ParametersSecurityUpdateTiIndicators">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ti-indicator-id**|string|key: id of tiIndicator|ti_indicator_id|tiIndicator-id|
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

#### <a name="SecurityUpdateUserSecurityProfiles">Command `az security security update-user-security-profile`</a>

##### <a name="ParametersSecurityUpdateUserSecurityProfiles">Parameters</a> 
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

### group `az security security-action`
#### <a name="Security.securityActionscancelSecurityAction">Command `az security security-action cancel-security-action`</a>

##### <a name="ParametersSecurity.securityActionscancelSecurityAction">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--security-action-id**|string|key: id of securityAction|security_action_id|securityAction-id|

### group `az security security-alert`
#### <a name="Security.alertsupdateAlerts">Command `az security security-alert update-alert`</a>

##### <a name="ParametersSecurity.alertsupdateAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

### group `az security security-ti-indicator`
#### <a name="Security.tiIndicatorsdeleteTiIndicators">Command `az security security-ti-indicator delete-ti-indicator`</a>

##### <a name="ParametersSecurity.tiIndicatorsdeleteTiIndicators">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

#### <a name="Security.tiIndicatorsdeleteTiIndicatorsByExternalId">Command `az security security-ti-indicator delete-ti-indicator-by-external-id`</a>

##### <a name="ParametersSecurity.tiIndicatorsdeleteTiIndicatorsByExternalId">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

#### <a name="Security.tiIndicatorssubmitTiIndicators">Command `az security security-ti-indicator submit-ti-indicator`</a>

##### <a name="ParametersSecurity.tiIndicatorssubmitTiIndicators">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

#### <a name="Security.tiIndicatorsupdateTiIndicators">Command `az security security-ti-indicator update-ti-indicator`</a>

##### <a name="ParametersSecurity.tiIndicatorsupdateTiIndicators">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|
