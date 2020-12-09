# Azure CLI Module Creation Report

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
|delete|DeleteSecureScoreControlProfiles|
|delete|DeleteSecureScores|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alert-id**|string|key: id of alert|alert_id|alert-id|
|**--secure-score-control-profile-id**|string|key: id of secureScoreControlProfile|secure_score_control_profile_id|secureScoreControlProfile-id|
|**--secure-score-id**|string|key: id of secureScore|secure_score_id|secureScore-id|
|**--if-match**|string|ETag|if_match|If-Match|

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

### security update-alert

update-alert a security.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|security|Security|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-alert|UpdateAlerts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alert-id**|string|key: id of alert|alert_id|alert-id|
|**--body**|object|New navigation property values|body|body|

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
|**--alerts**|array|Read-only. Nullable.|alerts|alerts|
|**--secure-score-control-profiles**|array||secure_score_control_profiles|secureScoreControlProfiles|
|**--secure-scores**|array||secure_scores|secureScores|
