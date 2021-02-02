# Azure CLI Module Creation Report

### people user create-person

create-person a people user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-person|CreatePeople|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--birthday**|string|The person's birthday.|birthday|birthday|
|**--company-name**|string|The name of the person's company.|company_name|companyName|
|**--department**|string|The person's department.|department|department|
|**--display-name**|string|The person's display name.|display_name|displayName|
|**--email-addresses**|array||email_addresses|emailAddresses|
|**--given-name**|string|The person's given name.|given_name|givenName|
|**--is-favorite**|boolean|true if the user has flagged this person as a favorite.|is_favorite|isFavorite|
|**--mailbox-type**|string||mailbox_type|mailboxType|
|**--office-location**|string|The location of the person's office.|office_location|officeLocation|
|**--person-notes**|string|Free-form notes that the user has taken about this person.|person_notes|personNotes|
|**--person-type**|string|The type of person.|person_type|personType|
|**--phones**|array|The person's phone numbers.|phones|phones|
|**--postal-addresses**|array|The person's addresses.|postal_addresses|postalAddresses|
|**--profession**|string|The person's profession.|profession|profession|
|**--sources**|array||sources|sources|
|**--surname**|string|The person's surname.|surname|surname|
|**--title**|string||title|title|
|**--user-principal-name**|string|The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.|user_principal_name|userPrincipalName|
|**--websites**|array|The person's websites.|websites|websites|
|**--yomi-company**|string|The phonetic Japanese name of the person's company.|yomi_company|yomiCompany|

### people user delete

delete a people user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePeople|
|delete|DeleteAnalytics|
|delete|DeleteProfile|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-id**|string|key: id of person|person_id|person-id|
|**--if-match**|string|ETag|if_match|If-Match|

### people user get-analytic

get-analytic a people user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-analytic|GetAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user get-person

get-person a people user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-person|GetPeople|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-id**|string|key: id of person|person_id|person-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user get-profile

get-profile a people user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-profile|GetProfile|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user list-person

list-person a people user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-person|ListPeople|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user update-analytic

update-analytic a people user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-analytic|UpdateAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--settings**|object|settings|settings|settings|
|**--activity-statistics**|array||activity_statistics|activityStatistics|

### people user update-person

update-person a people user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-person|UpdatePeople|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-id**|string|key: id of person|person_id|person-id|
|**--id**|string|Read-only.|id|id|
|**--birthday**|string|The person's birthday.|birthday|birthday|
|**--company-name**|string|The name of the person's company.|company_name|companyName|
|**--department**|string|The person's department.|department|department|
|**--display-name**|string|The person's display name.|display_name|displayName|
|**--email-addresses**|array||email_addresses|emailAddresses|
|**--given-name**|string|The person's given name.|given_name|givenName|
|**--is-favorite**|boolean|true if the user has flagged this person as a favorite.|is_favorite|isFavorite|
|**--mailbox-type**|string||mailbox_type|mailboxType|
|**--office-location**|string|The location of the person's office.|office_location|officeLocation|
|**--person-notes**|string|Free-form notes that the user has taken about this person.|person_notes|personNotes|
|**--person-type**|string|The type of person.|person_type|personType|
|**--phones**|array|The person's phone numbers.|phones|phones|
|**--postal-addresses**|array|The person's addresses.|postal_addresses|postalAddresses|
|**--profession**|string|The person's profession.|profession|profession|
|**--sources**|array||sources|sources|
|**--surname**|string|The person's surname.|surname|surname|
|**--title**|string||title|title|
|**--user-principal-name**|string|The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.|user_principal_name|userPrincipalName|
|**--websites**|array|The person's websites.|websites|websites|
|**--yomi-company**|string|The phonetic Japanese name of the person's company.|yomi_company|yomiCompany|

### people user update-profile

update-profile a people user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-profile|UpdateProfile|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--account**|array||account|account|
|**--addresses**|array||addresses|addresses|
|**--anniversaries**|array||anniversaries|anniversaries|
|**--awards**|array||awards|awards|
|**--certifications**|array||certifications|certifications|
|**--educational-activities**|array||educational_activities|educationalActivities|
|**--emails**|array||emails|emails|
|**--interests**|array||interests|interests|
|**--languages**|array||languages|languages|
|**--names**|array||names|names|
|**--notes**|array||notes|notes|
|**--patents**|array||patents|patents|
|**--phones**|array||phones|phones|
|**--positions**|array||positions|positions|
|**--projects**|array||projects|projects|
|**--publications**|array||publications|publications|
|**--skills**|array||skills|skills|
|**--web-accounts**|array||web_accounts|webAccounts|
|**--websites**|array||websites|websites|

### people user-analytic create-activity-statistics

create-activity-statistics a people user-analytic.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-analytic|users.analytics|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity-statistics|CreateActivityStatistics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|choice||activity|activity|
|**--duration**|duration||duration|duration|
|**--end-date**|date||end_date|endDate|
|**--start-date**|date||start_date|startDate|
|**--time-zone-used**|string||time_zone_used|timeZoneUsed|

### people user-analytic delete

delete a people user-analytic.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-analytic|users.analytics|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteActivityStatistics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--activity-statistics-id**|string|key: id of activityStatistics|activity_statistics_id|activityStatistics-id|
|**--if-match**|string|ETag|if_match|If-Match|

### people user-analytic get-activity-statistics

get-activity-statistics a people user-analytic.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-analytic|users.analytics|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-statistics|GetActivityStatistics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--activity-statistics-id**|string|key: id of activityStatistics|activity_statistics_id|activityStatistics-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-analytic list-activity-statistics

list-activity-statistics a people user-analytic.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-analytic|users.analytics|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity-statistics|ListActivityStatistics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-analytic update-activity-statistics

update-activity-statistics a people user-analytic.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-analytic|users.analytics|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-activity-statistics|UpdateActivityStatistics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--activity-statistics-id**|string|key: id of activityStatistics|activity_statistics_id|activityStatistics-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|choice||activity|activity|
|**--duration**|duration||duration|duration|
|**--end-date**|date||end_date|endDate|
|**--start-date**|date||start_date|startDate|
|**--time-zone-used**|string||time_zone_used|timeZoneUsed|

### people user-profile create-account

create-account a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-account|CreateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--age-group**|string||age_group|ageGroup|
|**--country-code**|string||country_code|countryCode|
|**--preferred-language-tag**|object|localeInfo|preferred_language_tag|preferredLanguageTag|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### people user-profile create-address

create-address a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-address|CreateAddresses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--detail**|object|physicalAddress|detail|detail|
|**--display-name**|string||display_name|displayName|
|**--geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

### people user-profile create-anniversary

create-anniversary a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-anniversary|CreateAnniversaries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--date**|date||date|date|
|**--type**|choice||type|type|

### people user-profile create-award

create-award a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-award|CreateAwards|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

### people user-profile create-certification

create-certification a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-certification|CreateCertifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--certification-id**|string||certification_id|certificationId|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--end-date**|date||end_date|endDate|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--issuing-company**|string||issuing_company|issuingCompany|
|**--start-date**|date||start_date|startDate|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

### people user-profile create-educational-activity

create-educational-activity a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-educational-activity|CreateEducationalActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|New navigation property|body|body|

### people user-profile create-email

create-email a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-email|CreateEmails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--address**|string||address|address|
|**--display-name**|string||display_name|displayName|
|**--type**|choice||type|type|

### people user-profile create-interest

create-interest a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-interest|CreateInterests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--web-url**|string||web_url|webUrl|

### people user-profile create-language

create-language a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-language|CreateLanguages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--proficiency**|choice||proficiency|proficiency|
|**--reading**|choice||reading|reading|
|**--spoken**|choice||spoken|spoken|
|**--tag**|string||tag|tag|
|**--written**|choice||written|written|

### people user-profile create-name

create-name a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-name|CreateNames|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--first**|string||first|first|
|**--initials**|string||initials|initials|
|**--language-tag**|string||language_tag|languageTag|
|**--last**|string||last|last|
|**--maiden**|string||maiden|maiden|
|**--middle**|string||middle|middle|
|**--nickname**|string||nickname|nickname|
|**--pronunciation**|object|yomiPersonName|pronunciation|pronunciation|
|**--suffix**|string||suffix|suffix|
|**--title**|string||title|title|

### people user-profile create-note

create-note a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-note|CreateNotes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--detail**|object|itemBody|detail|detail|
|**--display-name**|string||display_name|displayName|

### people user-profile create-patent

create-patent a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-patent|CreatePatents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-pending**|boolean||is_pending|isPending|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--number**|string||number|number|
|**--web-url**|string||web_url|webUrl|

### people user-profile create-phone

create-phone a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-phone|CreatePhones|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--number**|string||number|number|
|**--type**|choice||type|type|

### people user-profile create-position

create-position a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-position|CreatePositions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--colleagues**|array||colleagues|colleagues|
|**--is-current**|boolean||is_current|isCurrent|
|**--manager**|object|relatedPerson|manager|manager|
|**--detail-company**|object|companyDetail|company|company|
|**--detail-description**|string||description|description|
|**--detail-end-month-year**|date||end_month_year|endMonthYear|
|**--detail-job-title**|string||job_title|jobTitle|
|**--detail-role**|string||role|role|
|**--detail-start-month-year**|date||start_month_year|startMonthYear|
|**--detail-summary**|string||summary|summary|

### people user-profile create-project

create-project a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-project|CreateProjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--colleagues**|array||colleagues|colleagues|
|**--display-name**|string||display_name|displayName|
|**--sponsors**|array||sponsors|sponsors|
|**--detail-company**|object|companyDetail|company|company|
|**--detail-description**|string||description|description|
|**--detail-end-month-year**|date||end_month_year|endMonthYear|
|**--detail-job-title**|string||job_title|jobTitle|
|**--detail-role**|string||role|role|
|**--detail-start-month-year**|date||start_month_year|startMonthYear|
|**--detail-summary**|string||summary|summary|
|**--client-address**|object|physicalAddress|address|address|
|**--client-department**|string||department|department|
|**--client-display-name**|string||microsoft_graph_company_detail_display_name|displayName|
|**--client-office-location**|string||office_location|officeLocation|
|**--client-pronunciation**|string||pronunciation|pronunciation|
|**--client-web-url**|string||web_url|webUrl|

### people user-profile create-publication

create-publication a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-publication|CreatePublications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--published-date**|date||published_date|publishedDate|
|**--publisher**|string||publisher|publisher|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

### people user-profile create-skill

create-skill a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-skill|CreateSkills|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--display-name**|string||display_name|displayName|
|**--proficiency**|choice||proficiency|proficiency|
|**--web-url**|string||web_url|webUrl|

### people user-profile create-web-account

create-web-account a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-web-account|CreateWebAccounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--service**|object|serviceInformation|service|service|
|**--status-message**|string||status_message|statusMessage|
|**--microsoft-graph-web-account-user-id**|string||microsoft_graph_web_account_user_id|userId|
|**--web-url**|string||web_url|webUrl|

### people user-profile create-website

create-website a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-website|CreateWebsites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--web-url**|string||web_url|webUrl|

### people user-profile delete

delete a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccount|
|delete|DeleteAddresses|
|delete|DeleteAnniversaries|
|delete|DeleteAwards|
|delete|DeleteCertifications|
|delete|DeleteEducationalActivities|
|delete|DeleteEmails|
|delete|DeleteInterests|
|delete|DeleteLanguages|
|delete|DeleteNames|
|delete|DeleteNotes|
|delete|DeletePatents|
|delete|DeletePhones|
|delete|DeletePositions|
|delete|DeleteProjects|
|delete|DeletePublications|
|delete|DeleteSkills|
|delete|DeleteWebAccounts|
|delete|DeleteWebsites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-account-information-id**|string|key: id of userAccountInformation|user_account_information_id|userAccountInformation-id|
|**--item-address-id**|string|key: id of itemAddress|item_address_id|itemAddress-id|
|**--person-anniversary-id**|string|key: id of personAnniversary|person_anniversary_id|personAnniversary-id|
|**--person-award-id**|string|key: id of personAward|person_award_id|personAward-id|
|**--person-certification-id**|string|key: id of personCertification|person_certification_id|personCertification-id|
|**--educational-activity-id**|string|key: id of educationalActivity|educational_activity_id|educationalActivity-id|
|**--item-email-id**|string|key: id of itemEmail|item_email_id|itemEmail-id|
|**--person-interest-id**|string|key: id of personInterest|person_interest_id|personInterest-id|
|**--language-proficiency-id**|string|key: id of languageProficiency|language_proficiency_id|languageProficiency-id|
|**--person-name-id**|string|key: id of personName|person_name_id|personName-id|
|**--person-annotation-id**|string|key: id of personAnnotation|person_annotation_id|personAnnotation-id|
|**--item-patent-id**|string|key: id of itemPatent|item_patent_id|itemPatent-id|
|**--item-phone-id**|string|key: id of itemPhone|item_phone_id|itemPhone-id|
|**--work-position-id**|string|key: id of workPosition|work_position_id|workPosition-id|
|**--project-participation-id**|string|key: id of projectParticipation|project_participation_id|projectParticipation-id|
|**--item-publication-id**|string|key: id of itemPublication|item_publication_id|itemPublication-id|
|**--skill-proficiency-id**|string|key: id of skillProficiency|skill_proficiency_id|skillProficiency-id|
|**--web-account-id**|string|key: id of webAccount|web_account_id|webAccount-id|
|**--person-website-id**|string|key: id of personWebsite|person_website_id|personWebsite-id|
|**--if-match**|string|ETag|if_match|If-Match|

### people user-profile get-account

get-account a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-account|GetAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-account-information-id**|string|key: id of userAccountInformation|user_account_information_id|userAccountInformation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-address

get-address a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-address|GetAddresses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-address-id**|string|key: id of itemAddress|item_address_id|itemAddress-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-anniversary

get-anniversary a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-anniversary|GetAnniversaries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-anniversary-id**|string|key: id of personAnniversary|person_anniversary_id|personAnniversary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-award

get-award a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-award|GetAwards|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-award-id**|string|key: id of personAward|person_award_id|personAward-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-certification

get-certification a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-certification|GetCertifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-certification-id**|string|key: id of personCertification|person_certification_id|personCertification-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-educational-activity

get-educational-activity a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-educational-activity|GetEducationalActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--educational-activity-id**|string|key: id of educationalActivity|educational_activity_id|educationalActivity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-email

get-email a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email|GetEmails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-email-id**|string|key: id of itemEmail|item_email_id|itemEmail-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-interest

get-interest a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-interest|GetInterests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-interest-id**|string|key: id of personInterest|person_interest_id|personInterest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-language

get-language a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-language|GetLanguages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--language-proficiency-id**|string|key: id of languageProficiency|language_proficiency_id|languageProficiency-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-name

get-name a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-name|GetNames|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-name-id**|string|key: id of personName|person_name_id|personName-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-note

get-note a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-note|GetNotes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-annotation-id**|string|key: id of personAnnotation|person_annotation_id|personAnnotation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-patent

get-patent a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-patent|GetPatents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-patent-id**|string|key: id of itemPatent|item_patent_id|itemPatent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-phone

get-phone a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-phone|GetPhones|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-phone-id**|string|key: id of itemPhone|item_phone_id|itemPhone-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-position

get-position a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-position|GetPositions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--work-position-id**|string|key: id of workPosition|work_position_id|workPosition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-project

get-project a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-project|GetProjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--project-participation-id**|string|key: id of projectParticipation|project_participation_id|projectParticipation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-publication

get-publication a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-publication|GetPublications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-publication-id**|string|key: id of itemPublication|item_publication_id|itemPublication-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-skill

get-skill a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skill|GetSkills|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--skill-proficiency-id**|string|key: id of skillProficiency|skill_proficiency_id|skillProficiency-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-web-account

get-web-account a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-web-account|GetWebAccounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--web-account-id**|string|key: id of webAccount|web_account_id|webAccount-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile get-website

get-website a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-website|GetWebsites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-website-id**|string|key: id of personWebsite|person_website_id|personWebsite-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-account

list-account a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-account|ListAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-address

list-address a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-address|ListAddresses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-anniversary

list-anniversary a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-anniversary|ListAnniversaries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-award

list-award a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-award|ListAwards|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-certification

list-certification a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-certification|ListCertifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-educational-activity

list-educational-activity a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-educational-activity|ListEducationalActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-email

list-email a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-email|ListEmails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-interest

list-interest a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-interest|ListInterests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-language

list-language a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-language|ListLanguages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-name

list-name a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-name|ListNames|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-note

list-note a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-note|ListNotes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-patent

list-patent a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-patent|ListPatents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-phone

list-phone a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-phone|ListPhones|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-position

list-position a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-position|ListPositions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-project

list-project a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-project|ListProjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-publication

list-publication a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-publication|ListPublications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-skill

list-skill a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-skill|ListSkills|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-web-account

list-web-account a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-web-account|ListWebAccounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile list-website

list-website a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-website|ListWebsites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people user-profile update-account

update-account a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-account|UpdateAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-account-information-id**|string|key: id of userAccountInformation|user_account_information_id|userAccountInformation-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--age-group**|string||age_group|ageGroup|
|**--country-code**|string||country_code|countryCode|
|**--preferred-language-tag**|object|localeInfo|preferred_language_tag|preferredLanguageTag|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### people user-profile update-address

update-address a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-address|UpdateAddresses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-address-id**|string|key: id of itemAddress|item_address_id|itemAddress-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--detail**|object|physicalAddress|detail|detail|
|**--display-name**|string||display_name|displayName|
|**--geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

### people user-profile update-anniversary

update-anniversary a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-anniversary|UpdateAnniversaries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-anniversary-id**|string|key: id of personAnniversary|person_anniversary_id|personAnniversary-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--date**|date||date|date|
|**--type**|choice||type|type|

### people user-profile update-award

update-award a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-award|UpdateAwards|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-award-id**|string|key: id of personAward|person_award_id|personAward-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

### people user-profile update-certification

update-certification a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-certification|UpdateCertifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-certification-id**|string|key: id of personCertification|person_certification_id|personCertification-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--certification-id**|string||certification_id|certificationId|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--end-date**|date||end_date|endDate|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--issuing-company**|string||issuing_company|issuingCompany|
|**--start-date**|date||start_date|startDate|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

### people user-profile update-educational-activity

update-educational-activity a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-educational-activity|UpdateEducationalActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--educational-activity-id**|string|key: id of educationalActivity|educational_activity_id|educationalActivity-id|
|**--body**|object|New navigation property values|body|body|

### people user-profile update-email

update-email a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-email|UpdateEmails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-email-id**|string|key: id of itemEmail|item_email_id|itemEmail-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--address**|string||address|address|
|**--display-name**|string||display_name|displayName|
|**--type**|choice||type|type|

### people user-profile update-interest

update-interest a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-interest|UpdateInterests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-interest-id**|string|key: id of personInterest|person_interest_id|personInterest-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--web-url**|string||web_url|webUrl|

### people user-profile update-language

update-language a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-language|UpdateLanguages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--language-proficiency-id**|string|key: id of languageProficiency|language_proficiency_id|languageProficiency-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--proficiency**|choice||proficiency|proficiency|
|**--reading**|choice||reading|reading|
|**--spoken**|choice||spoken|spoken|
|**--tag**|string||tag|tag|
|**--written**|choice||written|written|

### people user-profile update-name

update-name a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-name|UpdateNames|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-name-id**|string|key: id of personName|person_name_id|personName-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--first**|string||first|first|
|**--initials**|string||initials|initials|
|**--language-tag**|string||language_tag|languageTag|
|**--last**|string||last|last|
|**--maiden**|string||maiden|maiden|
|**--middle**|string||middle|middle|
|**--nickname**|string||nickname|nickname|
|**--pronunciation**|object|yomiPersonName|pronunciation|pronunciation|
|**--suffix**|string||suffix|suffix|
|**--title**|string||title|title|

### people user-profile update-note

update-note a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-note|UpdateNotes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-annotation-id**|string|key: id of personAnnotation|person_annotation_id|personAnnotation-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--detail**|object|itemBody|detail|detail|
|**--display-name**|string||display_name|displayName|

### people user-profile update-patent

update-patent a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-patent|UpdatePatents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-patent-id**|string|key: id of itemPatent|item_patent_id|itemPatent-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-pending**|boolean||is_pending|isPending|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--number**|string||number|number|
|**--web-url**|string||web_url|webUrl|

### people user-profile update-phone

update-phone a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-phone|UpdatePhones|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-phone-id**|string|key: id of itemPhone|item_phone_id|itemPhone-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--number**|string||number|number|
|**--type**|choice||type|type|

### people user-profile update-position

update-position a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-position|UpdatePositions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--work-position-id**|string|key: id of workPosition|work_position_id|workPosition-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--colleagues**|array||colleagues|colleagues|
|**--is-current**|boolean||is_current|isCurrent|
|**--manager**|object|relatedPerson|manager|manager|
|**--detail-company**|object|companyDetail|company|company|
|**--detail-description**|string||description|description|
|**--detail-end-month-year**|date||end_month_year|endMonthYear|
|**--detail-job-title**|string||job_title|jobTitle|
|**--detail-role**|string||role|role|
|**--detail-start-month-year**|date||start_month_year|startMonthYear|
|**--detail-summary**|string||summary|summary|

### people user-profile update-project

update-project a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-project|UpdateProjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--project-participation-id**|string|key: id of projectParticipation|project_participation_id|projectParticipation-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--colleagues**|array||colleagues|colleagues|
|**--display-name**|string||display_name|displayName|
|**--sponsors**|array||sponsors|sponsors|
|**--detail-company**|object|companyDetail|company|company|
|**--detail-description**|string||description|description|
|**--detail-end-month-year**|date||end_month_year|endMonthYear|
|**--detail-job-title**|string||job_title|jobTitle|
|**--detail-role**|string||role|role|
|**--detail-start-month-year**|date||start_month_year|startMonthYear|
|**--detail-summary**|string||summary|summary|
|**--client-address**|object|physicalAddress|address|address|
|**--client-department**|string||department|department|
|**--client-display-name**|string||microsoft_graph_company_detail_display_name|displayName|
|**--client-office-location**|string||office_location|officeLocation|
|**--client-pronunciation**|string||pronunciation|pronunciation|
|**--client-web-url**|string||web_url|webUrl|

### people user-profile update-publication

update-publication a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-publication|UpdatePublications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-publication-id**|string|key: id of itemPublication|item_publication_id|itemPublication-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--published-date**|date||published_date|publishedDate|
|**--publisher**|string||publisher|publisher|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

### people user-profile update-skill

update-skill a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-skill|UpdateSkills|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--skill-proficiency-id**|string|key: id of skillProficiency|skill_proficiency_id|skillProficiency-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--display-name**|string||display_name|displayName|
|**--proficiency**|choice||proficiency|proficiency|
|**--web-url**|string||web_url|webUrl|

### people user-profile update-web-account

update-web-account a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-web-account|UpdateWebAccounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--web-account-id**|string|key: id of webAccount|web_account_id|webAccount-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--service**|object|serviceInformation|service|service|
|**--status-message**|string||status_message|statusMessage|
|**--microsoft-graph-web-account-user-id**|string||microsoft_graph_web_account_user_id|userId|
|**--web-url**|string||web_url|webUrl|

### people user-profile update-website

update-website a people user-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people user-profile|users.profile|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-website|UpdateWebsites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-website-id**|string|key: id of personWebsite|person_website_id|personWebsite-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--web-url**|string||web_url|webUrl|
