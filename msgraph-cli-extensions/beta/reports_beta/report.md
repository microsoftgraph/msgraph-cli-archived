# Azure CLI Module Creation Report

### reports audit-log create-directory-audit

create-directory-audit a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-audit|CreateDirectoryAudits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-date-time**|date-time|Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|activity_date_time|activityDateTime|
|**--activity-display-name**|string|Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For full list, see Azure AD activity list.|activity_display_name|activityDisplayName|
|**--additional-details**|array|Indicates additional details on the activity.|additional_details|additionalDetails|
|**--category**|string|Indicates which resource category that's targeted by the activity. (For example: User Management, Group Management etc..)|category|category|
|**--correlation-id**|string|Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.|correlation_id|correlationId|
|**--logged-by-service**|string|Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.|logged_by_service|loggedByService|
|**--operation-type**|string||operation_type|operationType|
|**--result**|choice||result|result|
|**--result-reason**|string|Describes cause of 'failure' or 'timeout' results.|result_reason|resultReason|
|**--target-resources**|array|Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other.|target_resources|targetResources|
|**--initiated-by-app**|object|appIdentity|app|app|
|**--initiated-by-user**|object|userIdentity|user|user|

### reports audit-log create-directory-provisioning

create-directory-provisioning a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-provisioning|CreateDirectoryProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--action**|string||action|action|
|**--activity-date-time**|date-time||activity_date_time|activityDateTime|
|**--change-id**|string||change_id|changeId|
|**--cycle-id**|string||cycle_id|cycleId|
|**--duration-in-milliseconds**|integer||duration_in_milliseconds|durationInMilliseconds|
|**--initiated-by**|object|initiator|initiated_by|initiatedBy|
|**--job-id**|string||job_id|jobId|
|**--modified-properties**|array||modified_properties|modifiedProperties|
|**--provisioning-steps**|array||provisioning_steps|provisioningSteps|
|**--service-principal**|object|provisioningServicePrincipal|service_principal|servicePrincipal|
|**--tenant-id**|string||tenant_id|tenantId|
|**--target-system-details**|dictionary|detailsInfo|details|details|
|**--target-system-display-name**|string||display_name|displayName|
|**--target-system-id**|string||microsoft_graph_provisioning_system_details_id|id|
|**--target-identity-details**|dictionary|detailsInfo|microsoft_graph_details_info_details|details|
|**--target-identity-display-name**|string||microsoft_graph_provisioned_identity_display_name|displayName|
|**--target-identity-id**|string||microsoft_graph_provisioned_identity_id|id|
|**--target-identity-identity-type**|string||identity_type|identityType|
|**--status-info-status**|choice||status|status|
|**--source-system-details**|dictionary|detailsInfo|details1|details|
|**--source-system-display-name**|string||microsoft_graph_provisioning_system_details_display_name|displayName|
|**--source-system-id**|string||id1|id|
|**--source-identity-details**|dictionary|detailsInfo|details2|details|
|**--source-identity-display-name**|string||display_name1|displayName|
|**--source-identity-id**|string||id2|id|
|**--source-identity-identity-type**|string||microsoft_graph_provisioned_identity_type|identityType|

### reports audit-log create-provisioning

create-provisioning a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-provisioning|CreateProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--action**|string||action|action|
|**--activity-date-time**|date-time||activity_date_time|activityDateTime|
|**--change-id**|string||change_id|changeId|
|**--cycle-id**|string||cycle_id|cycleId|
|**--duration-in-milliseconds**|integer||duration_in_milliseconds|durationInMilliseconds|
|**--initiated-by**|object|initiator|initiated_by|initiatedBy|
|**--job-id**|string||job_id|jobId|
|**--modified-properties**|array||modified_properties|modifiedProperties|
|**--provisioning-steps**|array||provisioning_steps|provisioningSteps|
|**--service-principal**|object|provisioningServicePrincipal|service_principal|servicePrincipal|
|**--tenant-id**|string||tenant_id|tenantId|
|**--target-system-details**|dictionary|detailsInfo|details|details|
|**--target-system-display-name**|string||display_name|displayName|
|**--target-system-id**|string||microsoft_graph_provisioning_system_details_id|id|
|**--target-identity-details**|dictionary|detailsInfo|microsoft_graph_details_info_details|details|
|**--target-identity-display-name**|string||microsoft_graph_provisioned_identity_display_name|displayName|
|**--target-identity-id**|string||microsoft_graph_provisioned_identity_id|id|
|**--target-identity-identity-type**|string||identity_type|identityType|
|**--status-info-status**|choice||status|status|
|**--source-system-details**|dictionary|detailsInfo|details1|details|
|**--source-system-display-name**|string||microsoft_graph_provisioning_system_details_display_name|displayName|
|**--source-system-id**|string||id1|id|
|**--source-identity-details**|dictionary|detailsInfo|details2|details|
|**--source-identity-display-name**|string||display_name1|displayName|
|**--source-identity-id**|string||id2|id|
|**--source-identity-identity-type**|string||microsoft_graph_provisioned_identity_type|identityType|

### reports audit-log create-restricted-sign-in

create-restricted-sign-in a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-restricted-sign-in|CreateRestrictedSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--alternate-sign-in-name**|string||alternate_sign_in_name|alternateSignInName|
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--authentication-details**|array||authentication_details|authenticationDetails|
|**--authentication-methods-used**|array||authentication_methods_used|authenticationMethodsUsed|
|**--authentication-processing-details**|array||authentication_processing_details|authenticationProcessingDetails|
|**--authentication-requirement**|string||authentication_requirement|authenticationRequirement|
|**--authentication-requirement-policies**|array||authentication_requirement_policies|authenticationRequirementPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--mfa-detail**|object|mfaDetail|mfa_detail|mfaDetail|
|**--network-location-details**|array||network_location_details|networkLocationDetails|
|**--original-request-id**|string||original_request_id|originalRequestId|
|**--processing-time-in-milliseconds**|integer||processing_time_in_milliseconds|processingTimeInMilliseconds|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--resource-tenant-id**|string||resource_tenant_id|resourceTenantId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--service-principal-id**|string||service_principal_id|servicePrincipalId|
|**--service-principal-name**|string||service_principal_name|servicePrincipalName|
|**--sign-in-event-types**|array||sign_in_event_types|signInEventTypes|
|**--status**|object|signInStatus|status|status|
|**--token-issuer-name**|string||token_issuer_name|tokenIssuerName|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-agent**|string||user_agent|userAgent|
|**--user-display-name**|string|Display name of the user that initiated the sign-in.|user_display_name|userDisplayName|
|**--user-id**|string|ID of the user that initiated the sign-in.|user_id|userId|
|**--user-principal-name**|string|User principal name of the user that initiated the sign-in.|user_principal_name|userPrincipalName|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--target-tenant-id**|uuid||target_tenant_id|targetTenantId|

### reports audit-log create-sign-in

create-sign-in a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sign-in|CreateSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--alternate-sign-in-name**|string||alternate_sign_in_name|alternateSignInName|
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--authentication-details**|array||authentication_details|authenticationDetails|
|**--authentication-methods-used**|array||authentication_methods_used|authenticationMethodsUsed|
|**--authentication-processing-details**|array||authentication_processing_details|authenticationProcessingDetails|
|**--authentication-requirement**|string||authentication_requirement|authenticationRequirement|
|**--authentication-requirement-policies**|array||authentication_requirement_policies|authenticationRequirementPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--mfa-detail**|object|mfaDetail|mfa_detail|mfaDetail|
|**--network-location-details**|array||network_location_details|networkLocationDetails|
|**--original-request-id**|string||original_request_id|originalRequestId|
|**--processing-time-in-milliseconds**|integer||processing_time_in_milliseconds|processingTimeInMilliseconds|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--resource-tenant-id**|string||resource_tenant_id|resourceTenantId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--service-principal-id**|string||service_principal_id|servicePrincipalId|
|**--service-principal-name**|string||service_principal_name|servicePrincipalName|
|**--sign-in-event-types**|array||sign_in_event_types|signInEventTypes|
|**--status**|object|signInStatus|status|status|
|**--token-issuer-name**|string||token_issuer_name|tokenIssuerName|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-agent**|string||user_agent|userAgent|
|**--user-display-name**|string|Display name of the user that initiated the sign-in.|user_display_name|userDisplayName|
|**--user-id**|string|ID of the user that initiated the sign-in.|user_id|userId|
|**--user-principal-name**|string|User principal name of the user that initiated the sign-in.|user_principal_name|userPrincipalName|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|

### reports audit-log delete

delete a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDirectoryAudits|
|delete|DeleteDirectoryProvisioning|
|delete|DeleteProvisioning|
|delete|DeleteRestrictedSignIns|
|delete|DeleteSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-audit-id**|string|key: id of directoryAudit|directory_audit_id|directoryAudit-id|
|**--provisioning-object-summary-id**|string|key: id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--restricted-sign-in-id**|string|key: id of restrictedSignIn|restricted_sign_in_id|restrictedSignIn-id|
|**--sign-in-id**|string|key: id of signIn|sign_in_id|signIn-id|
|**--if-match**|string|ETag|if_match|If-Match|

### reports audit-log get-directory-audit

get-directory-audit a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-audit|GetDirectoryAudits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-audit-id**|string|key: id of directoryAudit|directory_audit_id|directoryAudit-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log get-directory-provisioning

get-directory-provisioning a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-provisioning|GetDirectoryProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log get-provisioning

get-provisioning a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-provisioning|GetProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log get-restricted-sign-in

get-restricted-sign-in a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-restricted-sign-in|GetRestrictedSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--restricted-sign-in-id**|string|key: id of restrictedSignIn|restricted_sign_in_id|restrictedSignIn-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log get-sign-in

get-sign-in a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sign-in|GetSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sign-in-id**|string|key: id of signIn|sign_in_id|signIn-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log list-directory-audit

list-directory-audit a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-directory-audit|ListDirectoryAudits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log list-directory-provisioning

list-directory-provisioning a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-directory-provisioning|ListDirectoryProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log list-provisioning

list-provisioning a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-provisioning|ListProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log list-restricted-sign-in

list-restricted-sign-in a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-restricted-sign-in|ListRestrictedSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log list-sign-in

list-sign-in a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-sign-in|ListSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log update-directory-audit

update-directory-audit a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory-audit|UpdateDirectoryAudits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-audit-id**|string|key: id of directoryAudit|directory_audit_id|directoryAudit-id|
|**--id**|string|Read-only.|id|id|
|**--activity-date-time**|date-time|Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|activity_date_time|activityDateTime|
|**--activity-display-name**|string|Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For full list, see Azure AD activity list.|activity_display_name|activityDisplayName|
|**--additional-details**|array|Indicates additional details on the activity.|additional_details|additionalDetails|
|**--category**|string|Indicates which resource category that's targeted by the activity. (For example: User Management, Group Management etc..)|category|category|
|**--correlation-id**|string|Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.|correlation_id|correlationId|
|**--logged-by-service**|string|Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.|logged_by_service|loggedByService|
|**--operation-type**|string||operation_type|operationType|
|**--result**|choice||result|result|
|**--result-reason**|string|Describes cause of 'failure' or 'timeout' results.|result_reason|resultReason|
|**--target-resources**|array|Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other.|target_resources|targetResources|
|**--initiated-by-app**|object|appIdentity|app|app|
|**--initiated-by-user**|object|userIdentity|user|user|

### reports audit-log update-directory-provisioning

update-directory-provisioning a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory-provisioning|UpdateDirectoryProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--id**|string|Read-only.|id|id|
|**--action**|string||action|action|
|**--activity-date-time**|date-time||activity_date_time|activityDateTime|
|**--change-id**|string||change_id|changeId|
|**--cycle-id**|string||cycle_id|cycleId|
|**--duration-in-milliseconds**|integer||duration_in_milliseconds|durationInMilliseconds|
|**--initiated-by**|object|initiator|initiated_by|initiatedBy|
|**--job-id**|string||job_id|jobId|
|**--modified-properties**|array||modified_properties|modifiedProperties|
|**--provisioning-steps**|array||provisioning_steps|provisioningSteps|
|**--service-principal**|object|provisioningServicePrincipal|service_principal|servicePrincipal|
|**--tenant-id**|string||tenant_id|tenantId|
|**--target-system-details**|dictionary|detailsInfo|details|details|
|**--target-system-display-name**|string||display_name|displayName|
|**--target-system-id**|string||microsoft_graph_provisioning_system_details_id|id|
|**--target-identity-details**|dictionary|detailsInfo|microsoft_graph_details_info_details|details|
|**--target-identity-display-name**|string||microsoft_graph_provisioned_identity_display_name|displayName|
|**--target-identity-id**|string||microsoft_graph_provisioned_identity_id|id|
|**--target-identity-identity-type**|string||identity_type|identityType|
|**--status-info-status**|choice||status|status|
|**--source-system-details**|dictionary|detailsInfo|details1|details|
|**--source-system-display-name**|string||microsoft_graph_provisioning_system_details_display_name|displayName|
|**--source-system-id**|string||id1|id|
|**--source-identity-details**|dictionary|detailsInfo|details2|details|
|**--source-identity-display-name**|string||display_name1|displayName|
|**--source-identity-id**|string||id2|id|
|**--source-identity-identity-type**|string||microsoft_graph_provisioned_identity_type|identityType|

### reports audit-log update-provisioning

update-provisioning a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-provisioning|UpdateProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--id**|string|Read-only.|id|id|
|**--action**|string||action|action|
|**--activity-date-time**|date-time||activity_date_time|activityDateTime|
|**--change-id**|string||change_id|changeId|
|**--cycle-id**|string||cycle_id|cycleId|
|**--duration-in-milliseconds**|integer||duration_in_milliseconds|durationInMilliseconds|
|**--initiated-by**|object|initiator|initiated_by|initiatedBy|
|**--job-id**|string||job_id|jobId|
|**--modified-properties**|array||modified_properties|modifiedProperties|
|**--provisioning-steps**|array||provisioning_steps|provisioningSteps|
|**--service-principal**|object|provisioningServicePrincipal|service_principal|servicePrincipal|
|**--tenant-id**|string||tenant_id|tenantId|
|**--target-system-details**|dictionary|detailsInfo|details|details|
|**--target-system-display-name**|string||display_name|displayName|
|**--target-system-id**|string||microsoft_graph_provisioning_system_details_id|id|
|**--target-identity-details**|dictionary|detailsInfo|microsoft_graph_details_info_details|details|
|**--target-identity-display-name**|string||microsoft_graph_provisioned_identity_display_name|displayName|
|**--target-identity-id**|string||microsoft_graph_provisioned_identity_id|id|
|**--target-identity-identity-type**|string||identity_type|identityType|
|**--status-info-status**|choice||status|status|
|**--source-system-details**|dictionary|detailsInfo|details1|details|
|**--source-system-display-name**|string||microsoft_graph_provisioning_system_details_display_name|displayName|
|**--source-system-id**|string||id1|id|
|**--source-identity-details**|dictionary|detailsInfo|details2|details|
|**--source-identity-display-name**|string||display_name1|displayName|
|**--source-identity-id**|string||id2|id|
|**--source-identity-identity-type**|string||microsoft_graph_provisioned_identity_type|identityType|

### reports audit-log update-restricted-sign-in

update-restricted-sign-in a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-restricted-sign-in|UpdateRestrictedSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--restricted-sign-in-id**|string|key: id of restrictedSignIn|restricted_sign_in_id|restrictedSignIn-id|
|**--id**|string|Read-only.|id|id|
|**--alternate-sign-in-name**|string||alternate_sign_in_name|alternateSignInName|
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--authentication-details**|array||authentication_details|authenticationDetails|
|**--authentication-methods-used**|array||authentication_methods_used|authenticationMethodsUsed|
|**--authentication-processing-details**|array||authentication_processing_details|authenticationProcessingDetails|
|**--authentication-requirement**|string||authentication_requirement|authenticationRequirement|
|**--authentication-requirement-policies**|array||authentication_requirement_policies|authenticationRequirementPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--mfa-detail**|object|mfaDetail|mfa_detail|mfaDetail|
|**--network-location-details**|array||network_location_details|networkLocationDetails|
|**--original-request-id**|string||original_request_id|originalRequestId|
|**--processing-time-in-milliseconds**|integer||processing_time_in_milliseconds|processingTimeInMilliseconds|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--resource-tenant-id**|string||resource_tenant_id|resourceTenantId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--service-principal-id**|string||service_principal_id|servicePrincipalId|
|**--service-principal-name**|string||service_principal_name|servicePrincipalName|
|**--sign-in-event-types**|array||sign_in_event_types|signInEventTypes|
|**--status**|object|signInStatus|status|status|
|**--token-issuer-name**|string||token_issuer_name|tokenIssuerName|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-agent**|string||user_agent|userAgent|
|**--user-display-name**|string|Display name of the user that initiated the sign-in.|user_display_name|userDisplayName|
|**--user-id**|string|ID of the user that initiated the sign-in.|user_id|userId|
|**--user-principal-name**|string|User principal name of the user that initiated the sign-in.|user_principal_name|userPrincipalName|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--target-tenant-id**|uuid||target_tenant_id|targetTenantId|

### reports audit-log update-sign-in

update-sign-in a reports audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-sign-in|UpdateSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sign-in-id**|string|key: id of signIn|sign_in_id|signIn-id|
|**--id**|string|Read-only.|id|id|
|**--alternate-sign-in-name**|string||alternate_sign_in_name|alternateSignInName|
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--authentication-details**|array||authentication_details|authenticationDetails|
|**--authentication-methods-used**|array||authentication_methods_used|authenticationMethodsUsed|
|**--authentication-processing-details**|array||authentication_processing_details|authenticationProcessingDetails|
|**--authentication-requirement**|string||authentication_requirement|authenticationRequirement|
|**--authentication-requirement-policies**|array||authentication_requirement_policies|authenticationRequirementPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--mfa-detail**|object|mfaDetail|mfa_detail|mfaDetail|
|**--network-location-details**|array||network_location_details|networkLocationDetails|
|**--original-request-id**|string||original_request_id|originalRequestId|
|**--processing-time-in-milliseconds**|integer||processing_time_in_milliseconds|processingTimeInMilliseconds|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--resource-tenant-id**|string||resource_tenant_id|resourceTenantId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--service-principal-id**|string||service_principal_id|servicePrincipalId|
|**--service-principal-name**|string||service_principal_name|servicePrincipalName|
|**--sign-in-event-types**|array||sign_in_event_types|signInEventTypes|
|**--status**|object|signInStatus|status|status|
|**--token-issuer-name**|string||token_issuer_name|tokenIssuerName|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-agent**|string||user_agent|userAgent|
|**--user-display-name**|string|Display name of the user that initiated the sign-in.|user_display_name|userDisplayName|
|**--user-id**|string|ID of the user that initiated the sign-in.|user_id|userId|
|**--user-principal-name**|string|User principal name of the user that initiated the sign-in.|user_principal_name|userPrincipalName|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|

### reports audit-log-audit-log-root get-audit-log-root

get-audit-log-root a reports audit-log-audit-log-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log-audit-log-root|auditLogs.auditLogRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-audit-log-root|GetAuditLogRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports audit-log-audit-log-root update-audit-log-root

update-audit-log-root a reports audit-log-audit-log-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports audit-log-audit-log-root|auditLogs.auditLogRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-audit-log-root|UpdateAuditLogRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--directory-audits**|array|Read-only. Nullable.|directory_audits|directoryAudits|
|**--directory-provisioning**|array||directory_provisioning|directoryProvisioning|
|**--provisioning**|array||provisioning|provisioning|
|**--restricted-sign-ins**|array||restricted_sign_ins|restrictedSignIns|
|**--sign-ins**|array|Read-only. Nullable.|sign_ins|signIns|

### reports report create-application-sign-in-detailed-summary

create-application-sign-in-detailed-summary a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-application-sign-in-detailed-summary|CreateApplicationSignInDetailedSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--aggregated-event-date-time**|date-time||aggregated_event_date_time|aggregatedEventDateTime|
|**--app-display-name**|string||app_display_name|appDisplayName|
|**--app-id**|string||app_id|appId|
|**--sign-in-count**|integer||sign_in_count|signInCount|
|**--status-additional-details**|string|Provides additional details on the sign-in activity|additional_details|additionalDetails|
|**--status-error-code**|integer|Provides the 5-6digit error code that's generated during a sign-in failure. Check out the list of error codes and messages.|error_code|errorCode|
|**--status-failure-reason**|string|Provides the error message or the reason for failure for the corresponding sign-in activity. Check out the list of error codes and messages.|failure_reason|failureReason|

### reports report create-credential-user-registration-detail

create-credential-user-registration-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-credential-user-registration-detail|CreateCredentialUserRegistrationDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--auth-methods**|array||auth_methods|authMethods|
|**--is-capable**|boolean||is_capable|isCapable|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--is-mfa-registered**|boolean||is_mfa_registered|isMfaRegistered|
|**--is-registered**|boolean||is_registered|isRegistered|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### reports report create-daily-print-usage-summary-by-printer

create-daily-print-usage-summary-by-printer a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-daily-print-usage-summary-by-printer|CreateDailyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|

### reports report create-daily-print-usage-summary-by-user

create-daily-print-usage-summary-by-user a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-daily-print-usage-summary-by-user|CreateDailyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--usage-date**|date||usage_date|usageDate|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### reports report create-monthly-print-usage-summary-by-printer

create-monthly-print-usage-summary-by-printer a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-monthly-print-usage-summary-by-printer|CreateMonthlyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|

### reports report create-monthly-print-usage-summary-by-user

create-monthly-print-usage-summary-by-user a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-monthly-print-usage-summary-by-user|CreateMonthlyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--usage-date**|date||usage_date|usageDate|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### reports report create-user-credential-usage-detail

create-user-credential-usage-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user-credential-usage-detail|CreateUserCredentialUsageDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--auth-method**|choice||auth_method|authMethod|
|**--event-date-time**|date-time||event_date_time|eventDateTime|
|**--failure-reason**|string||failure_reason|failureReason|
|**--feature**|choice||feature|feature|
|**--is-success**|boolean||is_success|isSuccess|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### reports report delete

delete a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteApplicationSignInDetailedSummary|
|delete|DeleteCredentialUserRegistrationDetails|
|delete|DeleteDailyPrintUsageSummariesByPrinter|
|delete|DeleteDailyPrintUsageSummariesByUser|
|delete|DeleteMonthlyPrintUsageSummariesByPrinter|
|delete|DeleteMonthlyPrintUsageSummariesByUser|
|delete|DeleteUserCredentialUsageDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-sign-in-detailed-summary-id**|string|key: id of applicationSignInDetailedSummary|application_sign_in_detailed_summary_id|applicationSignInDetailedSummary-id|
|**--credential-user-registration-details-id**|string|key: id of credentialUserRegistrationDetails|credential_user_registration_details_id|credentialUserRegistrationDetails-id|
|**--print-usage-summary-by-printer-id**|string|key: id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--print-usage-summary-by-user-id**|string|key: id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--user-credential-usage-details-id**|string|key: id of userCredentialUsageDetails|user_credential_usage_details_id|userCredentialUsageDetails-id|
|**--if-match**|string|ETag|if_match|If-Match|

### reports report device-configuration-device-activity

device-configuration-device-activity a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|device-configuration-device-activity|deviceConfigurationDeviceActivity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports report device-configuration-user-activity

device-configuration-user-activity a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|device-configuration-user-activity|deviceConfigurationUserActivity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports report get-application-sign-in-detailed-summary

get-application-sign-in-detailed-summary a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-application-sign-in-detailed-summary|GetApplicationSignInDetailedSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-sign-in-detailed-summary-id**|string|key: id of applicationSignInDetailedSummary|application_sign_in_detailed_summary_id|applicationSignInDetailedSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report get-azure-ad-application-sign-in-summary

get-azure-ad-application-sign-in-summary a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-azure-ad-application-sign-in-summary|getAzureADApplicationSignInSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-azure-ad-feature-usage

get-azure-ad-feature-usage a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-azure-ad-feature-usage|getAzureADFeatureUsage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-azure-ad-license-usage

get-azure-ad-license-usage a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-azure-ad-license-usage|getAzureADLicenseUsage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-azure-ad-user-feature-usage

get-azure-ad-user-feature-usage a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-azure-ad-user-feature-usage|getAzureADUserFeatureUsage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports report get-credential-usage-summary

get-credential-usage-summary a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-credential-usage-summary|getCredentialUsageSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-credential-user-registration-count

get-credential-user-registration-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-credential-user-registration-count|getCredentialUserRegistrationCount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports report get-credential-user-registration-detail

get-credential-user-registration-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-credential-user-registration-detail|GetCredentialUserRegistrationDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--credential-user-registration-details-id**|string|key: id of credentialUserRegistrationDetails|credential_user_registration_details_id|credentialUserRegistrationDetails-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report get-daily-print-usage-summary-by-printer

get-daily-print-usage-summary-by-printer a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-daily-print-usage-summary-by-printer|GetDailyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report get-daily-print-usage-summary-by-user

get-daily-print-usage-summary-by-user a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-daily-print-usage-summary-by-user|GetDailyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report get-email-activity-count

get-email-activity-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-activity-count|getEmailActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-email-activity-user-count

get-email-activity-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-activity-user-count|getEmailActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-email-activity-user-detail-ddb2

get-email-activity-user-detail-ddb2 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-activity-user-detail-ddb2|getEmailActivityUserDetail-ddb2|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-email-activity-user-detail-fe32

get-email-activity-user-detail-fe32 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-activity-user-detail-fe32|getEmailActivityUserDetail-fe32|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-email-app-usage-app-user-count

get-email-app-usage-app-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-app-usage-app-user-count|getEmailAppUsageAppsUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-email-app-usage-user-count

get-email-app-usage-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-app-usage-user-count|getEmailAppUsageUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-email-app-usage-user-detail546-b

get-email-app-usage-user-detail546-b a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-app-usage-user-detail546-b|getEmailAppUsageUserDetail-546b|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-email-app-usage-user-detail62-ec

get-email-app-usage-user-detail62-ec a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-app-usage-user-detail62-ec|getEmailAppUsageUserDetail-62ec|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-email-app-usage-version-user-count

get-email-app-usage-version-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-app-usage-version-user-count|getEmailAppUsageVersionsUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-m365-app-platform-user-count

get-m365-app-platform-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-m365-app-platform-user-count|getM365AppPlatformUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-m365-app-user-count

get-m365-app-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-m365-app-user-count|getM365AppUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-m365-app-user-detail-c8-df

get-m365-app-user-detail-c8-df a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-m365-app-user-detail-c8-df|getM365AppUserDetail-c8df|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-m365-app-user-detail2-b20

get-m365-app-user-detail2-b20 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-m365-app-user-detail2-b20|getM365AppUserDetail-2b20|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-mailbox-usage-detail

get-mailbox-usage-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mailbox-usage-detail|getMailboxUsageDetail|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-mailbox-usage-mailbox-count

get-mailbox-usage-mailbox-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mailbox-usage-mailbox-count|getMailboxUsageMailboxCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-mailbox-usage-quota-status-mailbox-count

get-mailbox-usage-quota-status-mailbox-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mailbox-usage-quota-status-mailbox-count|getMailboxUsageQuotaStatusMailboxCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-mailbox-usage-storage

get-mailbox-usage-storage a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mailbox-usage-storage|getMailboxUsageStorage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-monthly-print-usage-summary-by-printer

get-monthly-print-usage-summary-by-printer a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-monthly-print-usage-summary-by-printer|GetMonthlyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report get-monthly-print-usage-summary-by-user

get-monthly-print-usage-summary-by-user a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-monthly-print-usage-summary-by-user|GetMonthlyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report get-office365-activation-count

get-office365-activation-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-activation-count|getOffice365ActivationCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports report get-office365-activation-user-count

get-office365-activation-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-activation-user-count|getOffice365ActivationsUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports report get-office365-activation-user-detail

get-office365-activation-user-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-activation-user-detail|getOffice365ActivationsUserDetail|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports report get-office365-active-user-count

get-office365-active-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-active-user-count|getOffice365ActiveUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-office365-active-user-detail-d389

get-office365-active-user-detail-d389 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-active-user-detail-d389|getOffice365ActiveUserDetail-d389|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-office365-active-user-detail68-ad

get-office365-active-user-detail68-ad a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-active-user-detail68-ad|getOffice365ActiveUserDetail-68ad|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-office365-group-activity-count

get-office365-group-activity-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-count|getOffice365GroupsActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-office365-group-activity-detail38-f6

get-office365-group-activity-detail38-f6 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-detail38-f6|getOffice365GroupsActivityDetail-38f6|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-office365-group-activity-detail81-cc

get-office365-group-activity-detail81-cc a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-detail81-cc|getOffice365GroupsActivityDetail-81cc|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-office365-group-activity-file-count

get-office365-group-activity-file-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-file-count|getOffice365GroupsActivityFileCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-office365-group-activity-group-count

get-office365-group-activity-group-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-group-count|getOffice365GroupsActivityGroupCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-office365-group-activity-storage

get-office365-group-activity-storage a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-storage|getOffice365GroupsActivityStorage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-office365-service-user-count

get-office365-service-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-service-user-count|getOffice365ServicesUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-one-drive-activity-file-count

get-one-drive-activity-file-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-activity-file-count|getOneDriveActivityFileCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-one-drive-activity-user-count

get-one-drive-activity-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-activity-user-count|getOneDriveActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-one-drive-activity-user-detail-c424

get-one-drive-activity-user-detail-c424 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-activity-user-detail-c424|getOneDriveActivityUserDetail-c424|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-one-drive-activity-user-detail05-f1

get-one-drive-activity-user-detail05-f1 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-activity-user-detail05-f1|getOneDriveActivityUserDetail-05f1|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-one-drive-usage-account-count

get-one-drive-usage-account-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-usage-account-count|getOneDriveUsageAccountCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-one-drive-usage-account-detail-dd7-f

get-one-drive-usage-account-detail-dd7-f a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-usage-account-detail-dd7-f|getOneDriveUsageAccountDetail-dd7f|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-one-drive-usage-account-detail-e827

get-one-drive-usage-account-detail-e827 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-usage-account-detail-e827|getOneDriveUsageAccountDetail-e827|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-one-drive-usage-file-count

get-one-drive-usage-file-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-usage-file-count|getOneDriveUsageFileCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-one-drive-usage-storage

get-one-drive-usage-storage a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-usage-storage|getOneDriveUsageStorage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-relying-party-detailed-summary

get-relying-party-detailed-summary a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-relying-party-detailed-summary|getRelyingPartyDetailedSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-share-point-activity-file-count

get-share-point-activity-file-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-activity-file-count|getSharePointActivityFileCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-share-point-activity-page

get-share-point-activity-page a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-activity-page|getSharePointActivityPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-share-point-activity-user-count

get-share-point-activity-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-activity-user-count|getSharePointActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-share-point-activity-user-detail-b778

get-share-point-activity-user-detail-b778 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-activity-user-detail-b778|getSharePointActivityUserDetail-b778|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-share-point-activity-user-detail-f3-be

get-share-point-activity-user-detail-f3-be a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-activity-user-detail-f3-be|getSharePointActivityUserDetail-f3be|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-share-point-site-usage-detail-d27-a

get-share-point-site-usage-detail-d27-a a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-detail-d27-a|getSharePointSiteUsageDetail-d27a|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-share-point-site-usage-detail204-b

get-share-point-site-usage-detail204-b a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-detail204-b|getSharePointSiteUsageDetail-204b|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-share-point-site-usage-file-count

get-share-point-site-usage-file-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-file-count|getSharePointSiteUsageFileCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-share-point-site-usage-page

get-share-point-site-usage-page a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-page|getSharePointSiteUsagePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-share-point-site-usage-site-count

get-share-point-site-usage-site-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-site-count|getSharePointSiteUsageSiteCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-share-point-site-usage-storage

get-share-point-site-usage-storage a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-storage|getSharePointSiteUsageStorage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-activity-count

get-skype-for-business-activity-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-activity-count|getSkypeForBusinessActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-activity-user-count

get-skype-for-business-activity-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-activity-user-count|getSkypeForBusinessActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-activity-user-detail-e4-c9

get-skype-for-business-activity-user-detail-e4-c9 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-activity-user-detail-e4-c9|getSkypeForBusinessActivityUserDetail-e4c9|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-skype-for-business-activity-user-detail744-e

get-skype-for-business-activity-user-detail744-e a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-activity-user-detail744-e|getSkypeForBusinessActivityUserDetail-744e|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-device-usage-distribution-user-count

get-skype-for-business-device-usage-distribution-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-device-usage-distribution-user-count|getSkypeForBusinessDeviceUsageDistributionUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-device-usage-user-count

get-skype-for-business-device-usage-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-device-usage-user-count|getSkypeForBusinessDeviceUsageUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-device-usage-user-detail-a692

get-skype-for-business-device-usage-user-detail-a692 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-device-usage-user-detail-a692|getSkypeForBusinessDeviceUsageUserDetail-a692|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-skype-for-business-device-usage-user-detail-e753

get-skype-for-business-device-usage-user-detail-e753 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-device-usage-user-detail-e753|getSkypeForBusinessDeviceUsageUserDetail-e753|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-organizer-activity-count

get-skype-for-business-organizer-activity-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-organizer-activity-count|getSkypeForBusinessOrganizerActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-organizer-activity-minute-count

get-skype-for-business-organizer-activity-minute-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-organizer-activity-minute-count|getSkypeForBusinessOrganizerActivityMinuteCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-organizer-activity-user-count

get-skype-for-business-organizer-activity-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-organizer-activity-user-count|getSkypeForBusinessOrganizerActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-participant-activity-count

get-skype-for-business-participant-activity-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-participant-activity-count|getSkypeForBusinessParticipantActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-participant-activity-minute-count

get-skype-for-business-participant-activity-minute-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-participant-activity-minute-count|getSkypeForBusinessParticipantActivityMinuteCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-participant-activity-user-count

get-skype-for-business-participant-activity-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-participant-activity-user-count|getSkypeForBusinessParticipantActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-peer-to-peer-activity-count

get-skype-for-business-peer-to-peer-activity-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-peer-to-peer-activity-count|getSkypeForBusinessPeerToPeerActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-peer-to-peer-activity-minute-count

get-skype-for-business-peer-to-peer-activity-minute-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-peer-to-peer-activity-minute-count|getSkypeForBusinessPeerToPeerActivityMinuteCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-skype-for-business-peer-to-peer-activity-user-count

get-skype-for-business-peer-to-peer-activity-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-peer-to-peer-activity-user-count|getSkypeForBusinessPeerToPeerActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-team-device-usage-distribution-user-count

get-team-device-usage-distribution-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-device-usage-distribution-user-count|getTeamsDeviceUsageDistributionUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-team-device-usage-user-count

get-team-device-usage-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-device-usage-user-count|getTeamsDeviceUsageUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-team-device-usage-user-detail7148

get-team-device-usage-user-detail7148 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-device-usage-user-detail7148|getTeamsDeviceUsageUserDetail-7148|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-team-device-usage-user-detail7565

get-team-device-usage-user-detail7565 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-device-usage-user-detail7565|getTeamsDeviceUsageUserDetail-7565|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-team-user-activity-count

get-team-user-activity-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-user-activity-count|getTeamsUserActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-team-user-activity-user-count

get-team-user-activity-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-user-activity-user-count|getTeamsUserActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-team-user-activity-user-detail-a3-f1

get-team-user-activity-user-detail-a3-f1 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-user-activity-user-detail-a3-f1|getTeamsUserActivityUserDetail-a3f1|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-team-user-activity-user-detail-eb13

get-team-user-activity-user-detail-eb13 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-user-activity-user-detail-eb13|getTeamsUserActivityUserDetail-eb13|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-tenant-secure-score

get-tenant-secure-score a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-tenant-secure-score|getTenantSecureScores|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|integer||period|period|

### reports report get-user-credential-usage-detail

get-user-credential-usage-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-credential-usage-detail|GetUserCredentialUsageDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-credential-usage-details-id**|string|key: id of userCredentialUsageDetails|user_credential_usage_details_id|userCredentialUsageDetails-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report get-yammer-activity-count

get-yammer-activity-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-activity-count|getYammerActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-yammer-activity-user-count

get-yammer-activity-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-activity-user-count|getYammerActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-yammer-activity-user-detail-ac30

get-yammer-activity-user-detail-ac30 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-activity-user-detail-ac30|getYammerActivityUserDetail-ac30|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-yammer-activity-user-detail15-a5

get-yammer-activity-user-detail15-a5 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-activity-user-detail15-a5|getYammerActivityUserDetail-15a5|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-yammer-device-usage-distribution-user-count

get-yammer-device-usage-distribution-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-device-usage-distribution-user-count|getYammerDeviceUsageDistributionUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-yammer-device-usage-user-count

get-yammer-device-usage-user-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-device-usage-user-count|getYammerDeviceUsageUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-yammer-device-usage-user-detail-cfad

get-yammer-device-usage-user-detail-cfad a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-device-usage-user-detail-cfad|getYammerDeviceUsageUserDetail-cfad|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-yammer-device-usage-user-detail-d0-ac

get-yammer-device-usage-user-detail-d0-ac a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-device-usage-user-detail-d0-ac|getYammerDeviceUsageUserDetail-d0ac|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-yammer-group-activity-count

get-yammer-group-activity-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-group-activity-count|getYammerGroupsActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-yammer-group-activity-detail-da9-a

get-yammer-group-activity-detail-da9-a a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-group-activity-detail-da9-a|getYammerGroupsActivityDetail-da9a|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports report get-yammer-group-activity-detail0-d7-d

get-yammer-group-activity-detail0-d7-d a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-group-activity-detail0-d7-d|getYammerGroupsActivityDetail-0d7d|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report get-yammer-group-activity-group-count

get-yammer-group-activity-group-count a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-group-activity-group-count|getYammerGroupsActivityGroupCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report list-application-sign-in-detailed-summary

list-application-sign-in-detailed-summary a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-application-sign-in-detailed-summary|ListApplicationSignInDetailedSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report list-credential-user-registration-detail

list-credential-user-registration-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-credential-user-registration-detail|ListCredentialUserRegistrationDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report list-daily-print-usage-summary

list-daily-print-usage-summary a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-daily-print-usage-summary|ListDailyPrintUsageSummariesByPrinter|
|list-daily-print-usage-summary|ListDailyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report list-monthly-print-usage-summary

list-monthly-print-usage-summary a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-monthly-print-usage-summary|ListMonthlyPrintUsageSummariesByPrinter|
|list-monthly-print-usage-summary|ListMonthlyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report list-user-credential-usage-detail

list-user-credential-usage-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user-credential-usage-detail|ListUserCredentialUsageDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report managed-device-enrollment-abandonment-detail

managed-device-enrollment-abandonment-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-abandonment-detail|managedDeviceEnrollmentAbandonmentDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip**|integer||skip|skip|
|**--top**|integer||top|top|
|**--filter**|string||filter|filter|
|**--skip-token**|string||skip_token|skipToken|

### reports report managed-device-enrollment-abandonment-summary

managed-device-enrollment-abandonment-summary a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-abandonment-summary|managedDeviceEnrollmentAbandonmentSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip**|integer||skip|skip|
|**--top**|integer||top|top|
|**--filter**|string||filter|filter|
|**--skip-token**|string||skip_token|skipToken|

### reports report managed-device-enrollment-failure-details027-e

managed-device-enrollment-failure-details027-e a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-failure-details027-e|managedDeviceEnrollmentFailureDetails-027e|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports report managed-device-enrollment-failure-details2-b3-d

managed-device-enrollment-failure-details2-b3-d a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-failure-details2-b3-d|managedDeviceEnrollmentFailureDetails-2b3d|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip**|integer||skip|skip|
|**--top**|integer||top|top|
|**--filter**|string||filter|filter|
|**--skip-token**|string||skip_token|skipToken|

### reports report managed-device-enrollment-failure-trend

managed-device-enrollment-failure-trend a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-failure-trend|managedDeviceEnrollmentFailureTrends|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports report managed-device-enrollment-top-failure-afd1

managed-device-enrollment-top-failure-afd1 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-top-failure-afd1|managedDeviceEnrollmentTopFailures-afd1|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports report managed-device-enrollment-top-failures4669

managed-device-enrollment-top-failures4669 a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-top-failures4669|managedDeviceEnrollmentTopFailures-4669|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports report update-application-sign-in-detailed-summary

update-application-sign-in-detailed-summary a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-application-sign-in-detailed-summary|UpdateApplicationSignInDetailedSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-sign-in-detailed-summary-id**|string|key: id of applicationSignInDetailedSummary|application_sign_in_detailed_summary_id|applicationSignInDetailedSummary-id|
|**--id**|string|Read-only.|id|id|
|**--aggregated-event-date-time**|date-time||aggregated_event_date_time|aggregatedEventDateTime|
|**--app-display-name**|string||app_display_name|appDisplayName|
|**--app-id**|string||app_id|appId|
|**--sign-in-count**|integer||sign_in_count|signInCount|
|**--status-additional-details**|string|Provides additional details on the sign-in activity|additional_details|additionalDetails|
|**--status-error-code**|integer|Provides the 5-6digit error code that's generated during a sign-in failure. Check out the list of error codes and messages.|error_code|errorCode|
|**--status-failure-reason**|string|Provides the error message or the reason for failure for the corresponding sign-in activity. Check out the list of error codes and messages.|failure_reason|failureReason|

### reports report update-credential-user-registration-detail

update-credential-user-registration-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-credential-user-registration-detail|UpdateCredentialUserRegistrationDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--credential-user-registration-details-id**|string|key: id of credentialUserRegistrationDetails|credential_user_registration_details_id|credentialUserRegistrationDetails-id|
|**--id**|string|Read-only.|id|id|
|**--auth-methods**|array||auth_methods|authMethods|
|**--is-capable**|boolean||is_capable|isCapable|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--is-mfa-registered**|boolean||is_mfa_registered|isMfaRegistered|
|**--is-registered**|boolean||is_registered|isRegistered|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### reports report update-daily-print-usage-summary-by-printer

update-daily-print-usage-summary-by-printer a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-daily-print-usage-summary-by-printer|UpdateDailyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|

### reports report update-daily-print-usage-summary-by-user

update-daily-print-usage-summary-by-user a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-daily-print-usage-summary-by-user|UpdateDailyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--usage-date**|date||usage_date|usageDate|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### reports report update-monthly-print-usage-summary-by-printer

update-monthly-print-usage-summary-by-printer a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-monthly-print-usage-summary-by-printer|UpdateMonthlyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|

### reports report update-monthly-print-usage-summary-by-user

update-monthly-print-usage-summary-by-user a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-monthly-print-usage-summary-by-user|UpdateMonthlyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--usage-date**|date||usage_date|usageDate|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### reports report update-user-credential-usage-detail

update-user-credential-usage-detail a reports report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user-credential-usage-detail|UpdateUserCredentialUsageDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-credential-usage-details-id**|string|key: id of userCredentialUsageDetails|user_credential_usage_details_id|userCredentialUsageDetails-id|
|**--id**|string|Read-only.|id|id|
|**--auth-method**|choice||auth_method|authMethod|
|**--event-date-time**|date-time||event_date_time|eventDateTime|
|**--failure-reason**|string||failure_reason|failureReason|
|**--feature**|choice||feature|feature|
|**--is-success**|boolean||is_success|isSuccess|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### reports report-root get-root

get-root a reports report-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report-root|reports.reportRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-root|GetReportRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports report-root update-root

update-root a reports report-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports report-root|reports.reportRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-root|UpdateReportRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--application-sign-in-detailed-summary**|array||application_sign_in_detailed_summary|applicationSignInDetailedSummary|
|**--credential-user-registration-details**|array||credential_user_registration_details|credentialUserRegistrationDetails|
|**--user-credential-usage-details**|array||user_credential_usage_details|userCredentialUsageDetails|
|**--daily-print-usage-summaries-by-printer**|array||daily_print_usage_summaries_by_printer|dailyPrintUsageSummariesByPrinter|
|**--daily-print-usage-summaries-by-user**|array||daily_print_usage_summaries_by_user|dailyPrintUsageSummariesByUser|
|**--monthly-print-usage-summaries-by-printer**|array||monthly_print_usage_summaries_by_printer|monthlyPrintUsageSummariesByPrinter|
|**--monthly-print-usage-summaries-by-user**|array||monthly_print_usage_summaries_by_user|monthlyPrintUsageSummariesByUser|
