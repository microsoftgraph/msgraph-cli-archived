# Azure CLI Module Creation Report

### auditlogs audit-log create-directory-audit

create-directory-audit a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-audit|CreateDirectoryAudits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--category**|string|Indicates which resource category that's targeted by the activity. (For example: User Management, Group Management etc..)|category|category|
|**--correlation-id**|string|Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.|correlation_id|correlationId|
|**--result**|choice|operationResult|result|result|
|**--result-reason**|string|Describes cause of 'failure' or 'timeout' results.|result_reason|resultReason|
|**--activity-display-name**|string|Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For full list, see Azure AD activity list.|activity_display_name|activityDisplayName|
|**--activity-date-time**|date-time|Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|activity_date_time|activityDateTime|
|**--logged-by-service**|string|Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.|logged_by_service|loggedByService|
|**--operation-type**|string||operation_type|operationType|
|**--target-resources**|array|Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other.|target_resources|targetResources|
|**--additional-details**|array|Indicates additional details on the activity.|additional_details|additionalDetails|
|**--initiated-by-user**|object|userIdentity|user|user|
|**--initiated-by-app**|object|appIdentity|app|app|

### auditlogs audit-log create-directory-provisioning

create-directory-provisioning a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-provisioning|CreateDirectoryProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-date-time**|date-time||activity_date_time|activityDateTime|
|**--tenant-id**|string||tenant_id|tenantId|
|**--job-id**|string||job_id|jobId|
|**--cycle-id**|string||cycle_id|cycleId|
|**--change-id**|string||change_id|changeId|
|**--action**|string||action|action|
|**--duration-in-milliseconds**|integer||duration_in_milliseconds|durationInMilliseconds|
|**--service-principal**|object|identity|service_principal|servicePrincipal|
|**--initiated-by**|object|initiator|initiated_by|initiatedBy|
|**--provisioning-steps**|array||provisioning_steps|provisioningSteps|
|**--modified-properties**|array||modified_properties|modifiedProperties|
|**--status-info-status**|choice|provisioningResult|status|status|
|**--target-identity-id**|string||microsoft_graph_provisioned_identity_id|id|
|**--target-identity-display-name**|string||display_name|displayName|
|**--target-identity-identity-type**|string||identity_type|identityType|
|**--target-identity-details**|any|Any object|details|details|
|**--source-identity-id**|string||id1|id|
|**--source-identity-display-name**|string||microsoft_graph_provisioned_identity_display_name|displayName|
|**--source-identity-identity-type**|string||microsoft_graph_provisioned_identity_type|identityType|
|**--source-identity-details**|any|Any object|any_details|details|
|**--target-system-id**|string||microsoft_graph_provisioning_system_details_id|id|
|**--target-system-display-name**|string||microsoft_graph_provisioning_system_details_display_name|displayName|
|**--target-system-details**|any|Any object|details1|details|
|**--source-system-id**|string||id2|id|
|**--source-system-display-name**|string||display_name1|displayName|
|**--source-system-details**|any|Any object|details2|details|

### auditlogs audit-log create-provisioning

create-provisioning a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-provisioning|CreateProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-date-time**|date-time||activity_date_time|activityDateTime|
|**--tenant-id**|string||tenant_id|tenantId|
|**--job-id**|string||job_id|jobId|
|**--cycle-id**|string||cycle_id|cycleId|
|**--change-id**|string||change_id|changeId|
|**--action**|string||action|action|
|**--duration-in-milliseconds**|integer||duration_in_milliseconds|durationInMilliseconds|
|**--service-principal**|object|identity|service_principal|servicePrincipal|
|**--initiated-by**|object|initiator|initiated_by|initiatedBy|
|**--provisioning-steps**|array||provisioning_steps|provisioningSteps|
|**--modified-properties**|array||modified_properties|modifiedProperties|
|**--status-info-status**|choice|provisioningResult|status|status|
|**--target-identity-id**|string||microsoft_graph_provisioned_identity_id|id|
|**--target-identity-display-name**|string||display_name|displayName|
|**--target-identity-identity-type**|string||identity_type|identityType|
|**--target-identity-details**|any|Any object|details|details|
|**--source-identity-id**|string||id1|id|
|**--source-identity-display-name**|string||microsoft_graph_provisioned_identity_display_name|displayName|
|**--source-identity-identity-type**|string||microsoft_graph_provisioned_identity_type|identityType|
|**--source-identity-details**|any|Any object|any_details|details|
|**--target-system-id**|string||microsoft_graph_provisioning_system_details_id|id|
|**--target-system-display-name**|string||microsoft_graph_provisioning_system_details_display_name|displayName|
|**--target-system-details**|any|Any object|details1|details|
|**--source-system-id**|string||id2|id|
|**--source-system-display-name**|string||display_name1|displayName|
|**--source-system-details**|any|Any object|details2|details|

### auditlogs audit-log create-restricted-sign-in

create-restricted-sign-in a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

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
|**--conditional-access-status**|choice|conditionalAccessStatus|conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--mfa-detail**|object|mfaDetail|mfa_detail|mfaDetail|
|**--network-location-details**|array||network_location_details|networkLocationDetails|
|**--original-request-id**|string||original_request_id|originalRequestId|
|**--processing-time-in-milliseconds**|integer||processing_time_in_milliseconds|processingTimeInMilliseconds|
|**--risk-detail**|choice|riskDetail|risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice|riskLevel|risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice|riskLevel|risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice|riskState|risk_state|riskState|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--service-principal-id**|string||service_principal_id|servicePrincipalId|
|**--service-principal-name**|string||service_principal_name|servicePrincipalName|
|**--status**|object|signInStatus|status|status|
|**--token-issuer-name**|string||token_issuer_name|tokenIssuerName|
|**--token-issuer-type**|choice|tokenIssuerType|token_issuer_type|tokenIssuerType|
|**--user-agent**|string||user_agent|userAgent|
|**--user-display-name**|string|Display name of the user that initiated the sign-in.|user_display_name|userDisplayName|
|**--user-id**|string|ID of the user that initiated the sign-in.|user_id|userId|
|**--user-principal-name**|string|User principal name of the user that initiated the sign-in.|user_principal_name|userPrincipalName|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--target-tenant-id**|uuid||target_tenant_id|targetTenantId|

### auditlogs audit-log create-sign-in

create-sign-in a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-sign-in|CreateSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

### auditlogs audit-log get-directory-audit

get-directory-audit a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-audit|GetDirectoryAudits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-audit-id**|string|key: directoryAudit-id of directoryAudit|directory_audit_id|directoryAudit-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### auditlogs audit-log get-directory-provisioning

get-directory-provisioning a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-provisioning|GetDirectoryProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: provisioningObjectSummary-id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### auditlogs audit-log get-provisioning

get-provisioning a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-provisioning|GetProvisioning|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: provisioningObjectSummary-id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### auditlogs audit-log get-restricted-sign-in

get-restricted-sign-in a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-restricted-sign-in|GetRestrictedSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--restricted-sign-in-id**|string|key: restrictedSignIn-id of restrictedSignIn|restricted_sign_in_id|restrictedSignIn-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### auditlogs audit-log get-sign-in

get-sign-in a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-sign-in|GetSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sign-in-id**|string|key: signIn-id of signIn|sign_in_id|signIn-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### auditlogs audit-log list-directory-audit

list-directory-audit a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

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

### auditlogs audit-log list-directory-provisioning

list-directory-provisioning a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

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

### auditlogs audit-log list-provisioning

list-provisioning a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

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

### auditlogs audit-log list-restricted-sign-in

list-restricted-sign-in a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

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

### auditlogs audit-log list-sign-in

list-sign-in a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

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

### auditlogs audit-log update

update a auditlogs audit-log.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log|auditLogs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateDirectoryAudits|
|update|UpdateDirectoryProvisioning|
|update|UpdateProvisioning|
|update|UpdateRestrictedSignIns|
|update|UpdateSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-audit-id**|string|key: directoryAudit-id of directoryAudit|directory_audit_id|directoryAudit-id|
|**--provisioning-object-summary-id**|string|key: provisioningObjectSummary-id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--restricted-sign-in-id**|string|key: restrictedSignIn-id of restrictedSignIn|restricted_sign_in_id|restrictedSignIn-id|
|**--sign-in-id**|string|key: signIn-id of signIn|sign_in_id|signIn-id|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--category**|string|Indicates which resource category that's targeted by the activity. (For example: User Management, Group Management etc..)|category|category|
|**--correlation-id**|string|Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.|correlation_id|correlationId|
|**--result**|choice|operationResult|result|result|
|**--result-reason**|string|Describes cause of 'failure' or 'timeout' results.|result_reason|resultReason|
|**--activity-display-name**|string|Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For full list, see Azure AD activity list.|activity_display_name|activityDisplayName|
|**--activity-date-time**|date-time|Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|activity_date_time|activityDateTime|
|**--logged-by-service**|string|Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.|logged_by_service|loggedByService|
|**--operation-type**|string||operation_type|operationType|
|**--target-resources**|array|Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other.|target_resources|targetResources|
|**--additional-details**|array|Indicates additional details on the activity.|additional_details|additionalDetails|
|**--initiated-by-user**|object|userIdentity|user|user|
|**--initiated-by-app**|object|appIdentity|app|app|
|**--tenant-id**|string||tenant_id|tenantId|
|**--job-id**|string||job_id|jobId|
|**--cycle-id**|string||cycle_id|cycleId|
|**--change-id**|string||change_id|changeId|
|**--action**|string||action|action|
|**--duration-in-milliseconds**|integer||duration_in_milliseconds|durationInMilliseconds|
|**--service-principal**|object|identity|service_principal|servicePrincipal|
|**--initiated-by**|object|initiator|initiated_by|initiatedBy|
|**--provisioning-steps**|array||provisioning_steps|provisioningSteps|
|**--modified-properties**|array||modified_properties|modifiedProperties|
|**--status-info-status**|choice|provisioningResult|status|status|
|**--target-identity-id**|string||microsoft_graph_provisioned_identity_id|id|
|**--target-identity-display-name**|string||display_name|displayName|
|**--target-identity-identity-type**|string||identity_type|identityType|
|**--target-identity-details**|any|Any object|details|details|
|**--source-identity-id**|string||id1|id|
|**--source-identity-display-name**|string||microsoft_graph_provisioned_identity_display_name|displayName|
|**--source-identity-identity-type**|string||microsoft_graph_provisioned_identity_type|identityType|
|**--source-identity-details**|any|Any object|any_details|details|
|**--target-system-id**|string||microsoft_graph_provisioning_system_details_id|id|
|**--target-system-display-name**|string||microsoft_graph_provisioning_system_details_display_name|displayName|
|**--target-system-details**|any|Any object|details1|details|
|**--source-system-id**|string||id2|id|
|**--source-system-display-name**|string||display_name1|displayName|
|**--source-system-details**|any|Any object|details2|details|
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
|**--conditional-access-status**|choice|conditionalAccessStatus|conditional_access_status|conditionalAccessStatus|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--mfa-detail**|object|mfaDetail|mfa_detail|mfaDetail|
|**--network-location-details**|array||network_location_details|networkLocationDetails|
|**--original-request-id**|string||original_request_id|originalRequestId|
|**--processing-time-in-milliseconds**|integer||processing_time_in_milliseconds|processingTimeInMilliseconds|
|**--risk-detail**|choice|riskDetail|risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice|riskLevel|risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice|riskLevel|risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice|riskState|risk_state|riskState|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--service-principal-id**|string||service_principal_id|servicePrincipalId|
|**--service-principal-name**|string||service_principal_name|servicePrincipalName|
|**--status**|object|signInStatus|status|status|
|**--token-issuer-name**|string||token_issuer_name|tokenIssuerName|
|**--token-issuer-type**|choice|tokenIssuerType|token_issuer_type|tokenIssuerType|
|**--user-agent**|string||user_agent|userAgent|
|**--user-display-name**|string|Display name of the user that initiated the sign-in.|user_display_name|userDisplayName|
|**--user-id**|string|ID of the user that initiated the sign-in.|user_id|userId|
|**--user-principal-name**|string|User principal name of the user that initiated the sign-in.|user_principal_name|userPrincipalName|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--target-tenant-id**|uuid||target_tenant_id|targetTenantId|

### auditlogs audit-log-audit-log-root get-audit-log-root

get-audit-log-root a auditlogs audit-log-audit-log-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log-audit-log-root|auditLogs.auditLogRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-audit-log-root|GetAuditLogRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### auditlogs audit-log-audit-log-root update

update a auditlogs audit-log-audit-log-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|auditlogs audit-log-audit-log-root|auditLogs.auditLogRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAuditLogRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--sign-ins**|array|Read-only. Nullable.|sign_ins|signIns|
|**--directory-audits**|array|Read-only. Nullable.|directory_audits|directoryAudits|
|**--restricted-sign-ins**|array||restricted_sign_ins|restrictedSignIns|
|**--directory-provisioning**|array||directory_provisioning|directoryProvisioning|
|**--provisioning**|array||provisioning|provisioning|
