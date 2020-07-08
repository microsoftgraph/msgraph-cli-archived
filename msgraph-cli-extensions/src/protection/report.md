# Azure CLI Module Creation Report

### protection anonymou-ip-risk-event-anonymou-ip-risk-event create-anonymou-ip-risk-event

create-anonymou-ip-risk-event a protection anonymou-ip-risk-event-anonymou-ip-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection anonymou-ip-risk-event-anonymou-ip-risk-event|anonymousIpRiskEvents.anonymousIpRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-anonymou-ip-risk-event|CreateAnonymousIpRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|
|**--ip-address**|string||ip_address|ipAddress|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

### protection anonymou-ip-risk-event-anonymou-ip-risk-event delete

delete a protection anonymou-ip-risk-event-anonymou-ip-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection anonymou-ip-risk-event-anonymou-ip-risk-event|anonymousIpRiskEvents.anonymousIpRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAnonymousIpRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--anonymous-ip-risk-event-id**|string|key: anonymousIpRiskEvent-id of anonymousIpRiskEvent|anonymous_ip_risk_event_id|anonymousIpRiskEvent-id|
|**--if-match**|string|ETag|if_match|If-Match|

### protection anonymou-ip-risk-event-anonymou-ip-risk-event get-anonymou-ip-risk-event

get-anonymou-ip-risk-event a protection anonymou-ip-risk-event-anonymou-ip-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection anonymou-ip-risk-event-anonymou-ip-risk-event|anonymousIpRiskEvents.anonymousIpRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-anonymou-ip-risk-event|GetAnonymousIpRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--anonymous-ip-risk-event-id**|string|key: anonymousIpRiskEvent-id of anonymousIpRiskEvent|anonymous_ip_risk_event_id|anonymousIpRiskEvent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection anonymou-ip-risk-event-anonymou-ip-risk-event list-anonymou-ip-risk-event

list-anonymou-ip-risk-event a protection anonymou-ip-risk-event-anonymou-ip-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection anonymou-ip-risk-event-anonymou-ip-risk-event|anonymousIpRiskEvents.anonymousIpRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-anonymou-ip-risk-event|ListAnonymousIpRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection anonymou-ip-risk-event-anonymou-ip-risk-event update

update a protection anonymou-ip-risk-event-anonymou-ip-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection anonymou-ip-risk-event-anonymou-ip-risk-event|anonymousIpRiskEvents.anonymousIpRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAnonymousIpRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--anonymous-ip-risk-event-id**|string|key: anonymousIpRiskEvent-id of anonymousIpRiskEvent|anonymous_ip_risk_event_id|anonymousIpRiskEvent-id|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|
|**--ip-address**|string||ip_address|ipAddress|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

### protection identity-risk-event get-impacted-user

get-impacted-user a protection identity-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection identity-risk-event|identityRiskEvents|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-impacted-user|GetImpactedUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-risk-event-id**|string|key: identityRiskEvent-id of identityRiskEvent|identity_risk_event_id|identityRiskEvent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection identity-risk-event-identity-risk-event create-identity-risk-event

create-identity-risk-event a protection identity-risk-event-identity-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection identity-risk-event-identity-risk-event|identityRiskEvents.identityRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-identity-risk-event|CreateIdentityRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|

### protection identity-risk-event-identity-risk-event delete

delete a protection identity-risk-event-identity-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection identity-risk-event-identity-risk-event|identityRiskEvents.identityRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteIdentityRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-risk-event-id**|string|key: identityRiskEvent-id of identityRiskEvent|identity_risk_event_id|identityRiskEvent-id|
|**--if-match**|string|ETag|if_match|If-Match|

### protection identity-risk-event-identity-risk-event get-identity-risk-event

get-identity-risk-event a protection identity-risk-event-identity-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection identity-risk-event-identity-risk-event|identityRiskEvents.identityRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-identity-risk-event|GetIdentityRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-risk-event-id**|string|key: identityRiskEvent-id of identityRiskEvent|identity_risk_event_id|identityRiskEvent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection identity-risk-event-identity-risk-event list-identity-risk-event

list-identity-risk-event a protection identity-risk-event-identity-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection identity-risk-event-identity-risk-event|identityRiskEvents.identityRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-identity-risk-event|ListIdentityRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection identity-risk-event-identity-risk-event update

update a protection identity-risk-event-identity-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection identity-risk-event-identity-risk-event|identityRiskEvents.identityRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateIdentityRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-risk-event-id**|string|key: identityRiskEvent-id of identityRiskEvent|identity_risk_event_id|identityRiskEvent-id|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|

### protection impossible-travel-risk-event-impossible-travel-risk-event create-impossible-travel-risk-event

create-impossible-travel-risk-event a protection impossible-travel-risk-event-impossible-travel-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection impossible-travel-risk-event-impossible-travel-risk-event|impossibleTravelRiskEvents.impossibleTravelRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-impossible-travel-risk-event|CreateImpossibleTravelRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### protection impossible-travel-risk-event-impossible-travel-risk-event delete

delete a protection impossible-travel-risk-event-impossible-travel-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection impossible-travel-risk-event-impossible-travel-risk-event|impossibleTravelRiskEvents.impossibleTravelRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteImpossibleTravelRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--impossible-travel-risk-event-id**|string|key: impossibleTravelRiskEvent-id of impossibleTravelRiskEvent|impossible_travel_risk_event_id|impossibleTravelRiskEvent-id|
|**--if-match**|string|ETag|if_match|If-Match|

### protection impossible-travel-risk-event-impossible-travel-risk-event get-impossible-travel-risk-event

get-impossible-travel-risk-event a protection impossible-travel-risk-event-impossible-travel-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection impossible-travel-risk-event-impossible-travel-risk-event|impossibleTravelRiskEvents.impossibleTravelRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-impossible-travel-risk-event|GetImpossibleTravelRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--impossible-travel-risk-event-id**|string|key: impossibleTravelRiskEvent-id of impossibleTravelRiskEvent|impossible_travel_risk_event_id|impossibleTravelRiskEvent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection impossible-travel-risk-event-impossible-travel-risk-event list-impossible-travel-risk-event

list-impossible-travel-risk-event a protection impossible-travel-risk-event-impossible-travel-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection impossible-travel-risk-event-impossible-travel-risk-event|impossibleTravelRiskEvents.impossibleTravelRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-impossible-travel-risk-event|ListImpossibleTravelRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection impossible-travel-risk-event-impossible-travel-risk-event update

update a protection impossible-travel-risk-event-impossible-travel-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection impossible-travel-risk-event-impossible-travel-risk-event|impossibleTravelRiskEvents.impossibleTravelRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateImpossibleTravelRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--impossible-travel-risk-event-id**|string|key: impossibleTravelRiskEvent-id of impossibleTravelRiskEvent|impossible_travel_risk_event_id|impossibleTravelRiskEvent-id|
|**--body**|object|New property values|body|body|

### protection leaked-credentials-risk-event-leaked-credentials-risk-event create-leaked-credentials-risk-event

create-leaked-credentials-risk-event a protection leaked-credentials-risk-event-leaked-credentials-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection leaked-credentials-risk-event-leaked-credentials-risk-event|leakedCredentialsRiskEvents.leakedCredentialsRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-leaked-credentials-risk-event|CreateLeakedCredentialsRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|

### protection leaked-credentials-risk-event-leaked-credentials-risk-event delete

delete a protection leaked-credentials-risk-event-leaked-credentials-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection leaked-credentials-risk-event-leaked-credentials-risk-event|leakedCredentialsRiskEvents.leakedCredentialsRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteLeakedCredentialsRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--leaked-credentials-risk-event-id**|string|key: leakedCredentialsRiskEvent-id of leakedCredentialsRiskEvent|leaked_credentials_risk_event_id|leakedCredentialsRiskEvent-id|
|**--if-match**|string|ETag|if_match|If-Match|

### protection leaked-credentials-risk-event-leaked-credentials-risk-event get-leaked-credentials-risk-event

get-leaked-credentials-risk-event a protection leaked-credentials-risk-event-leaked-credentials-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection leaked-credentials-risk-event-leaked-credentials-risk-event|leakedCredentialsRiskEvents.leakedCredentialsRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-leaked-credentials-risk-event|GetLeakedCredentialsRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--leaked-credentials-risk-event-id**|string|key: leakedCredentialsRiskEvent-id of leakedCredentialsRiskEvent|leaked_credentials_risk_event_id|leakedCredentialsRiskEvent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection leaked-credentials-risk-event-leaked-credentials-risk-event list-leaked-credentials-risk-event

list-leaked-credentials-risk-event a protection leaked-credentials-risk-event-leaked-credentials-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection leaked-credentials-risk-event-leaked-credentials-risk-event|leakedCredentialsRiskEvents.leakedCredentialsRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-leaked-credentials-risk-event|ListLeakedCredentialsRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection leaked-credentials-risk-event-leaked-credentials-risk-event update

update a protection leaked-credentials-risk-event-leaked-credentials-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection leaked-credentials-risk-event-leaked-credentials-risk-event|leakedCredentialsRiskEvents.leakedCredentialsRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateLeakedCredentialsRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--leaked-credentials-risk-event-id**|string|key: leakedCredentialsRiskEvent-id of leakedCredentialsRiskEvent|leaked_credentials_risk_event_id|leakedCredentialsRiskEvent-id|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|

### protection malware-risk-event-malware-risk-event create-malware-risk-event

create-malware-risk-event a protection malware-risk-event-malware-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection malware-risk-event-malware-risk-event|malwareRiskEvents.malwareRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-malware-risk-event|CreateMalwareRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|
|**--ip-address**|string||ip_address|ipAddress|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--device-information**|string||device_information|deviceInformation|
|**--malware-name**|string||malware_name|malwareName|

### protection malware-risk-event-malware-risk-event delete

delete a protection malware-risk-event-malware-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection malware-risk-event-malware-risk-event|malwareRiskEvents.malwareRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteMalwareRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--malware-risk-event-id**|string|key: malwareRiskEvent-id of malwareRiskEvent|malware_risk_event_id|malwareRiskEvent-id|
|**--if-match**|string|ETag|if_match|If-Match|

### protection malware-risk-event-malware-risk-event get-malware-risk-event

get-malware-risk-event a protection malware-risk-event-malware-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection malware-risk-event-malware-risk-event|malwareRiskEvents.malwareRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-malware-risk-event|GetMalwareRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--malware-risk-event-id**|string|key: malwareRiskEvent-id of malwareRiskEvent|malware_risk_event_id|malwareRiskEvent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection malware-risk-event-malware-risk-event list-malware-risk-event

list-malware-risk-event a protection malware-risk-event-malware-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection malware-risk-event-malware-risk-event|malwareRiskEvents.malwareRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-malware-risk-event|ListMalwareRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection malware-risk-event-malware-risk-event update

update a protection malware-risk-event-malware-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection malware-risk-event-malware-risk-event|malwareRiskEvents.malwareRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateMalwareRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--malware-risk-event-id**|string|key: malwareRiskEvent-id of malwareRiskEvent|malware_risk_event_id|malwareRiskEvent-id|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|
|**--ip-address**|string||ip_address|ipAddress|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--device-information**|string||device_information|deviceInformation|
|**--malware-name**|string||malware_name|malwareName|

### protection risk-detection-risk-detection create-risk-detection

create-risk-detection a protection risk-detection-risk-detection.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risk-detection-risk-detection|riskDetections.riskDetection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-risk-detection|CreateRiskDetection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--request-id**|string||request_id|requestId|
|**--correlation-id**|string||correlation_id|correlationId|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-type**|choice|riskEventType|risk_type|riskType|
|**--risk-state**|choice|riskState|risk_state|riskState|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-detail**|choice|riskDetail|risk_detail|riskDetail|
|**--source**|string||source|source|
|**--detection-timing-type**|choice|riskDetectionTimingType|detection_timing_type|detectionTimingType|
|**--activity**|choice|activityType|activity|activity|
|**--token-issuer-type**|choice|tokenIssuerType|token_issuer_type|tokenIssuerType|
|**--ip-address**|string||ip_address|ipAddress|
|**--activity-date-time**|date-time||activity_date_time|activityDateTime|
|**--detected-date-time**|date-time||detected_date_time|detectedDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--user-id**|string||user_id|userId|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--additional-info**|string||additional_info|additionalInfo|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

### protection risk-detection-risk-detection delete

delete a protection risk-detection-risk-detection.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risk-detection-risk-detection|riskDetections.riskDetection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRiskDetection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risk-detection-id**|string|key: riskDetection-id of riskDetection|risk_detection_id|riskDetection-id|
|**--if-match**|string|ETag|if_match|If-Match|

### protection risk-detection-risk-detection get-risk-detection

get-risk-detection a protection risk-detection-risk-detection.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risk-detection-risk-detection|riskDetections.riskDetection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-risk-detection|GetRiskDetection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risk-detection-id**|string|key: riskDetection-id of riskDetection|risk_detection_id|riskDetection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection risk-detection-risk-detection list-risk-detection

list-risk-detection a protection risk-detection-risk-detection.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risk-detection-risk-detection|riskDetections.riskDetection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-risk-detection|ListRiskDetection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection risk-detection-risk-detection update

update a protection risk-detection-risk-detection.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risk-detection-risk-detection|riskDetections.riskDetection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateRiskDetection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risk-detection-id**|string|key: riskDetection-id of riskDetection|risk_detection_id|riskDetection-id|
|**--id**|string|Read-only.|id|id|
|**--request-id**|string||request_id|requestId|
|**--correlation-id**|string||correlation_id|correlationId|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-type**|choice|riskEventType|risk_type|riskType|
|**--risk-state**|choice|riskState|risk_state|riskState|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-detail**|choice|riskDetail|risk_detail|riskDetail|
|**--source**|string||source|source|
|**--detection-timing-type**|choice|riskDetectionTimingType|detection_timing_type|detectionTimingType|
|**--activity**|choice|activityType|activity|activity|
|**--token-issuer-type**|choice|tokenIssuerType|token_issuer_type|tokenIssuerType|
|**--ip-address**|string||ip_address|ipAddress|
|**--activity-date-time**|date-time||activity_date_time|activityDateTime|
|**--detected-date-time**|date-time||detected_date_time|detectedDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--user-id**|string||user_id|userId|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--additional-info**|string||additional_info|additionalInfo|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

### protection risky-user confirm-compromised

confirm-compromised a protection risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|confirm-compromised|confirmCompromised|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-ids**|array||user_ids|userIds|

### protection risky-user create-history

create-history a protection risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-history|CreateHistory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: riskyUser-id of riskyUser|risky_user_id|riskyUser-id|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean||is_deleted|isDeleted|
|**--is-guest**|boolean||is_guest|isGuest|
|**--is-processing**|boolean||is_processing|isProcessing|
|**--risk-last-updated-date-time**|date-time||risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-state**|choice|riskState|risk_state|riskState|
|**--risk-detail**|choice|riskDetail|risk_detail|riskDetail|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--history**|array||history|history|
|**--user-id**|string||user_id|userId|
|**--initiated-by**|string||initiated_by|initiatedBy|
|**--activity**|object|riskUserActivity|activity|activity|

### protection risky-user dismiss

dismiss a protection risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss|dismiss|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-ids**|array||user_ids|userIds|

### protection risky-user get-history

get-history a protection risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-history|GetHistory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: riskyUser-id of riskyUser|risky_user_id|riskyUser-id|
|**--risky-user-history-item-id**|string|key: riskyUserHistoryItem-id of riskyUserHistoryItem|risky_user_history_item_id|riskyUserHistoryItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection risky-user list-history

list-history a protection risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-history|ListHistory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: riskyUser-id of riskyUser|risky_user_id|riskyUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection risky-user update

update a protection risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user|riskyUsers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateHistory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: riskyUser-id of riskyUser|risky_user_id|riskyUser-id|
|**--risky-user-history-item-id**|string|key: riskyUserHistoryItem-id of riskyUserHistoryItem|risky_user_history_item_id|riskyUserHistoryItem-id|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean||is_deleted|isDeleted|
|**--is-guest**|boolean||is_guest|isGuest|
|**--is-processing**|boolean||is_processing|isProcessing|
|**--risk-last-updated-date-time**|date-time||risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-state**|choice|riskState|risk_state|riskState|
|**--risk-detail**|choice|riskDetail|risk_detail|riskDetail|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--history**|array||history|history|
|**--user-id**|string||user_id|userId|
|**--initiated-by**|string||initiated_by|initiatedBy|
|**--activity**|object|riskUserActivity|activity|activity|

### protection risky-user-risky-user create-risky-user

create-risky-user a protection risky-user-risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user-risky-user|riskyUsers.riskyUser|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-risky-user|CreateRiskyUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean||is_deleted|isDeleted|
|**--is-guest**|boolean||is_guest|isGuest|
|**--is-processing**|boolean||is_processing|isProcessing|
|**--risk-last-updated-date-time**|date-time||risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-state**|choice|riskState|risk_state|riskState|
|**--risk-detail**|choice|riskDetail|risk_detail|riskDetail|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--history**|array||history|history|

### protection risky-user-risky-user delete

delete a protection risky-user-risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user-risky-user|riskyUsers.riskyUser|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRiskyUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: riskyUser-id of riskyUser|risky_user_id|riskyUser-id|
|**--if-match**|string|ETag|if_match|If-Match|

### protection risky-user-risky-user get-risky-user

get-risky-user a protection risky-user-risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user-risky-user|riskyUsers.riskyUser|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-risky-user|GetRiskyUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: riskyUser-id of riskyUser|risky_user_id|riskyUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection risky-user-risky-user list-risky-user

list-risky-user a protection risky-user-risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user-risky-user|riskyUsers.riskyUser|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-risky-user|ListRiskyUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection risky-user-risky-user update

update a protection risky-user-risky-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection risky-user-risky-user|riskyUsers.riskyUser|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateRiskyUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: riskyUser-id of riskyUser|risky_user_id|riskyUser-id|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean||is_deleted|isDeleted|
|**--is-guest**|boolean||is_guest|isGuest|
|**--is-processing**|boolean||is_processing|isProcessing|
|**--risk-last-updated-date-time**|date-time||risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-state**|choice|riskState|risk_state|riskState|
|**--risk-detail**|choice|riskDetail|risk_detail|riskDetail|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--history**|array||history|history|

### protection suspiciou-ip-risk-event-suspiciou-ip-risk-event create-suspiciou-ip-risk-event

create-suspiciou-ip-risk-event a protection suspiciou-ip-risk-event-suspiciou-ip-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection suspiciou-ip-risk-event-suspiciou-ip-risk-event|suspiciousIpRiskEvents.suspiciousIpRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-suspiciou-ip-risk-event|CreateSuspiciousIpRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|
|**--ip-address**|string||ip_address|ipAddress|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

### protection suspiciou-ip-risk-event-suspiciou-ip-risk-event delete

delete a protection suspiciou-ip-risk-event-suspiciou-ip-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection suspiciou-ip-risk-event-suspiciou-ip-risk-event|suspiciousIpRiskEvents.suspiciousIpRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSuspiciousIpRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--suspicious-ip-risk-event-id**|string|key: suspiciousIpRiskEvent-id of suspiciousIpRiskEvent|suspicious_ip_risk_event_id|suspiciousIpRiskEvent-id|
|**--if-match**|string|ETag|if_match|If-Match|

### protection suspiciou-ip-risk-event-suspiciou-ip-risk-event get-suspiciou-ip-risk-event

get-suspiciou-ip-risk-event a protection suspiciou-ip-risk-event-suspiciou-ip-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection suspiciou-ip-risk-event-suspiciou-ip-risk-event|suspiciousIpRiskEvents.suspiciousIpRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-suspiciou-ip-risk-event|GetSuspiciousIpRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--suspicious-ip-risk-event-id**|string|key: suspiciousIpRiskEvent-id of suspiciousIpRiskEvent|suspicious_ip_risk_event_id|suspiciousIpRiskEvent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection suspiciou-ip-risk-event-suspiciou-ip-risk-event list-suspiciou-ip-risk-event

list-suspiciou-ip-risk-event a protection suspiciou-ip-risk-event-suspiciou-ip-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection suspiciou-ip-risk-event-suspiciou-ip-risk-event|suspiciousIpRiskEvents.suspiciousIpRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-suspiciou-ip-risk-event|ListSuspiciousIpRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection suspiciou-ip-risk-event-suspiciou-ip-risk-event update

update a protection suspiciou-ip-risk-event-suspiciou-ip-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection suspiciou-ip-risk-event-suspiciou-ip-risk-event|suspiciousIpRiskEvents.suspiciousIpRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSuspiciousIpRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--suspicious-ip-risk-event-id**|string|key: suspiciousIpRiskEvent-id of suspiciousIpRiskEvent|suspicious_ip_risk_event_id|suspiciousIpRiskEvent-id|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|
|**--ip-address**|string||ip_address|ipAddress|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

### protection unfamiliar-location-risk-event-unfamiliar-location-risk-event create-unfamiliar-location-risk-event

create-unfamiliar-location-risk-event a protection unfamiliar-location-risk-event-unfamiliar-location-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection unfamiliar-location-risk-event-unfamiliar-location-risk-event|unfamiliarLocationRiskEvents.unfamiliarLocationRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-unfamiliar-location-risk-event|CreateUnfamiliarLocationRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|
|**--ip-address**|string||ip_address|ipAddress|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

### protection unfamiliar-location-risk-event-unfamiliar-location-risk-event delete

delete a protection unfamiliar-location-risk-event-unfamiliar-location-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection unfamiliar-location-risk-event-unfamiliar-location-risk-event|unfamiliarLocationRiskEvents.unfamiliarLocationRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteUnfamiliarLocationRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--unfamiliar-location-risk-event-id**|string|key: unfamiliarLocationRiskEvent-id of unfamiliarLocationRiskEvent|unfamiliar_location_risk_event_id|unfamiliarLocationRiskEvent-id|
|**--if-match**|string|ETag|if_match|If-Match|

### protection unfamiliar-location-risk-event-unfamiliar-location-risk-event get-unfamiliar-location-risk-event

get-unfamiliar-location-risk-event a protection unfamiliar-location-risk-event-unfamiliar-location-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection unfamiliar-location-risk-event-unfamiliar-location-risk-event|unfamiliarLocationRiskEvents.unfamiliarLocationRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-unfamiliar-location-risk-event|GetUnfamiliarLocationRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--unfamiliar-location-risk-event-id**|string|key: unfamiliarLocationRiskEvent-id of unfamiliarLocationRiskEvent|unfamiliar_location_risk_event_id|unfamiliarLocationRiskEvent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection unfamiliar-location-risk-event-unfamiliar-location-risk-event list-unfamiliar-location-risk-event

list-unfamiliar-location-risk-event a protection unfamiliar-location-risk-event-unfamiliar-location-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection unfamiliar-location-risk-event-unfamiliar-location-risk-event|unfamiliarLocationRiskEvents.unfamiliarLocationRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-unfamiliar-location-risk-event|ListUnfamiliarLocationRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### protection unfamiliar-location-risk-event-unfamiliar-location-risk-event update

update a protection unfamiliar-location-risk-event-unfamiliar-location-risk-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|protection unfamiliar-location-risk-event-unfamiliar-location-risk-event|unfamiliarLocationRiskEvents.unfamiliarLocationRiskEvent|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateUnfamiliarLocationRiskEvent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--unfamiliar-location-risk-event-id**|string|key: unfamiliarLocationRiskEvent-id of unfamiliarLocationRiskEvent|unfamiliar_location_risk_event_id|unfamiliarLocationRiskEvent-id|
|**--id**|string|Read-only.|id|id|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--risk-event-date-time**|date-time||risk_event_date_time|riskEventDateTime|
|**--risk-event-type**|string||risk_event_type|riskEventType|
|**--risk-level**|choice|riskLevel|risk_level|riskLevel|
|**--risk-event-status**|choice|riskEventStatus|risk_event_status|riskEventStatus|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--user-id**|string||user_id|userId|
|**--impacted-user**|object|Represents an Azure Active Directory user object.|impacted_user|impactedUser|
|**--ip-address**|string||ip_address|ipAddress|
|**--location-city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--location-state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--location-country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--location-geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
