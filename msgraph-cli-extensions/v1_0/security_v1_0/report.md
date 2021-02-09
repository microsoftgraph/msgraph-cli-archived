# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az security_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az security_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az security security|Security.security|[commands](#CommandsInSecurity.security)|
|az security security|Security|[commands](#CommandsInSecurity)|

## COMMANDS
### <a name="CommandsInSecurity.security">Commands in `az security security` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az security security update](#Security.securityUpdateSecurity)|UpdateSecurity|[Parameters](#ParametersSecurity.securityUpdateSecurity)|Not Found|
|[az security security show-security](#Security.securityGetSecurity)|GetSecurity|[Parameters](#ParametersSecurity.securityGetSecurity)|Not Found|

### <a name="CommandsInSecurity">Commands in `az security security` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az security security delete](#SecurityDeleteAlerts)|DeleteAlerts|[Parameters](#ParametersSecurityDeleteAlerts)|Not Found|
|[az security security delete](#SecurityDeleteSecureScoreControlProfiles)|DeleteSecureScoreControlProfiles|[Parameters](#ParametersSecurityDeleteSecureScoreControlProfiles)|Not Found|
|[az security security delete](#SecurityDeleteSecureScores)|DeleteSecureScores|[Parameters](#ParametersSecurityDeleteSecureScores)|Not Found|
|[az security security create-alert](#SecurityCreateAlerts)|CreateAlerts|[Parameters](#ParametersSecurityCreateAlerts)|Not Found|
|[az security security create-secure-score](#SecurityCreateSecureScores)|CreateSecureScores|[Parameters](#ParametersSecurityCreateSecureScores)|Not Found|
|[az security security create-secure-score-control-profile](#SecurityCreateSecureScoreControlProfiles)|CreateSecureScoreControlProfiles|[Parameters](#ParametersSecurityCreateSecureScoreControlProfiles)|Not Found|
|[az security security list-alert](#SecurityListAlerts)|ListAlerts|[Parameters](#ParametersSecurityListAlerts)|Not Found|
|[az security security list-secure-score](#SecurityListSecureScores)|ListSecureScores|[Parameters](#ParametersSecurityListSecureScores)|Not Found|
|[az security security list-secure-score-control-profile](#SecurityListSecureScoreControlProfiles)|ListSecureScoreControlProfiles|[Parameters](#ParametersSecurityListSecureScoreControlProfiles)|Not Found|
|[az security security show-alert](#SecurityGetAlerts)|GetAlerts|[Parameters](#ParametersSecurityGetAlerts)|Not Found|
|[az security security show-secure-score](#SecurityGetSecureScores)|GetSecureScores|[Parameters](#ParametersSecurityGetSecureScores)|Not Found|
|[az security security show-secure-score-control-profile](#SecurityGetSecureScoreControlProfiles)|GetSecureScoreControlProfiles|[Parameters](#ParametersSecurityGetSecureScoreControlProfiles)|Not Found|
|[az security security update-alert](#SecurityUpdateAlerts)|UpdateAlerts|[Parameters](#ParametersSecurityUpdateAlerts)|Not Found|
|[az security security update-secure-score](#SecurityUpdateSecureScores)|UpdateSecureScores|[Parameters](#ParametersSecurityUpdateSecureScores)|Not Found|
|[az security security update-secure-score-control-profile](#SecurityUpdateSecureScoreControlProfiles)|UpdateSecureScoreControlProfiles|[Parameters](#ParametersSecurityUpdateSecureScoreControlProfiles)|Not Found|


## COMMAND DETAILS

### group `az security security`
#### <a name="Security.securityUpdateSecurity">Command `az security security update`</a>

##### <a name="ParametersSecurity.securityUpdateSecurity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--alerts**|array|Read-only. Nullable.|alerts|alerts|
|**--secure-score-control-profiles**|array||secure_score_control_profiles|secureScoreControlProfiles|
|**--secure-scores**|array||secure_scores|secureScores|

#### <a name="Security.securityGetSecurity">Command `az security security show-security`</a>

##### <a name="ParametersSecurity.securityGetSecurity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az security security`
#### <a name="SecurityDeleteAlerts">Command `az security security delete`</a>

##### <a name="ParametersSecurityDeleteAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alert-id**|string|key: id of alert|alert_id|alert-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="SecurityDeleteSecureScoreControlProfiles">Command `az security security delete`</a>

##### <a name="ParametersSecurityDeleteSecureScoreControlProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--secure-score-control-profile-id**|string|key: id of secureScoreControlProfile|secure_score_control_profile_id|secureScoreControlProfile-id|

#### <a name="SecurityDeleteSecureScores">Command `az security security delete`</a>

##### <a name="ParametersSecurityDeleteSecureScores">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--secure-score-id**|string|key: id of secureScore|secure_score_id|secureScore-id|

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

#### <a name="SecurityListAlerts">Command `az security security list-alert`</a>

##### <a name="ParametersSecurityListAlerts">Parameters</a> 
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

#### <a name="SecurityGetAlerts">Command `az security security show-alert`</a>

##### <a name="ParametersSecurityGetAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alert-id**|string|key: id of alert|alert_id|alert-id|
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
