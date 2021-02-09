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
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--status**|object|signInStatus|status|status|
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
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--status**|object|signInStatus|status|status|
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
|delete|DeleteRestrictedSignIns|
|delete|DeleteSignIns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-audit-id**|string|key: id of directoryAudit|directory_audit_id|directoryAudit-id|
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
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--status**|object|signInStatus|status|status|
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
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--status**|object|signInStatus|status|status|
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
|**--restricted-sign-ins**|array||restricted_sign_ins|restrictedSignIns|
|**--sign-ins**|array|Read-only. Nullable.|sign_ins|signIns|

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
