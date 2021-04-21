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
|[az security security show-security](#Security.securityGetSecurity)|GetSecurity|[Parameters](#ParametersSecurity.securityGetSecurity)|Not Found|
|[az security security update-security](#Security.securityUpdateSecurity)|UpdateSecurity|[Parameters](#ParametersSecurity.securityUpdateSecurity)|Not Found|

### <a name="CommandsInSecurity">Commands in `az security security` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az security security create-alert](#SecurityCreateAlerts)|CreateAlerts|[Parameters](#ParametersSecurityCreateAlerts)|Not Found|
|[az security security create-secure-score](#SecurityCreateSecureScores)|CreateSecureScores|[Parameters](#ParametersSecurityCreateSecureScores)|Not Found|
|[az security security create-secure-score-control-profile](#SecurityCreateSecureScoreControlProfiles)|CreateSecureScoreControlProfiles|[Parameters](#ParametersSecurityCreateSecureScoreControlProfiles)|Not Found|
|[az security security delete-alert](#SecurityDeleteAlerts)|DeleteAlerts|[Parameters](#ParametersSecurityDeleteAlerts)|Not Found|
|[az security security delete-secure-score](#SecurityDeleteSecureScores)|DeleteSecureScores|[Parameters](#ParametersSecurityDeleteSecureScores)|Not Found|
|[az security security delete-secure-score-control-profile](#SecurityDeleteSecureScoreControlProfiles)|DeleteSecureScoreControlProfiles|[Parameters](#ParametersSecurityDeleteSecureScoreControlProfiles)|Not Found|
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
#### <a name="Security.securityGetSecurity">Command `az security security show-security`</a>

##### <a name="ParametersSecurity.securityGetSecurity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="Security.securityUpdateSecurity">Command `az security security update-security`</a>

##### <a name="ParametersSecurity.securityUpdateSecurity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--alerts**|array|Read-only. Nullable.|alerts|alerts|
|**--secure-score-control-profiles**|array||secure_score_control_profiles|secureScoreControlProfiles|
|**--secure-scores**|array||secure_scores|secureScores|

### group `az security security`
#### <a name="SecurityCreateAlerts">Command `az security security create-alert`</a>

##### <a name="ParametersSecurityCreateAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

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

#### <a name="SecurityDeleteAlerts">Command `az security security delete-alert`</a>

##### <a name="ParametersSecurityDeleteAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alert-id**|string|key: id of alert|alert_id|alert-id|
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
|**--body**|object|New navigation property values|body|body|

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
