# Azure CLI Module Creation Report

### people create-person

create-person a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users|

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
|**--given-name**|string|The person's given name.|given_name|givenName|
|**--im-address**|string|The instant message voice over IP (VOIP) session initiation protocol (SIP) address for the user. Read-only.|im_address|imAddress|
|**--is-favorite**|boolean|true if the user has flagged this person as a favorite.|is_favorite|isFavorite|
|**--job-title**|string|The person's job title.|job_title|jobTitle|
|**--office-location**|string|The location of the person's office.|office_location|officeLocation|
|**--person-notes**|string|Free-form notes that the user has taken about this person.|person_notes|personNotes|
|**--person-type**|object|personType|person_type|personType|
|**--phones**|array|The person's phone numbers.|phones|phones|
|**--postal-addresses**|array|The person's addresses.|postal_addresses|postalAddresses|
|**--profession**|string|The person's profession.|profession|profession|
|**--scored-email-addresses**|array|The person's email addresses.|scored_email_addresses|scoredEmailAddresses|
|**--surname**|string|The person's surname.|surname|surname|
|**--user-principal-name**|string|The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.|user_principal_name|userPrincipalName|
|**--websites**|array|The person's websites.|websites|websites|
|**--yomi-company**|string|The phonetic Japanese name of the person's company.|yomi_company|yomiCompany|

### people create-shared

create-shared a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-shared|CreateShared|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--sharing-history**|array||sharing_history|sharingHistory|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--last-shared-method-id**|string|Read-only.|id1|id|
|**--last-shared-shared-by**|object|insightIdentity|shared_by|sharedBy|
|**--last-shared-shared-date-time**|date-time|The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.|shared_date_time|sharedDateTime|
|**--last-shared-sharing-reference**|object|resourceReference|sharing_reference|sharingReference|
|**--last-shared-sharing-subject**|string|The subject with which the document was shared.|sharing_subject|sharingSubject|
|**--last-shared-sharing-type**|string|Determines the way the document was shared, can be by a 'Link', 'Attachment', 'Group', 'Site'.|sharing_type|sharingType|

### people create-trending

create-trending a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-trending|CreateTrending|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--weight**|number|Value indicating how much the document is currently trending. The larger the number, the more the document is currently trending around the user (the more relevant it is). Returned documents are sorted by this value.|weight|weight|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|

### people create-used

create-used a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-used|CreateUsed|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--last-used**|object|usageDetails|last_used|lastUsed|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|

### people delete

delete a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights.used|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefResource|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|
|**--if-match**|string|ETag|if_match|If-Match|

### people get-insight

get-insight a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-insight|GetInsights|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people get-last-shared-method

get-last-shared-method a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights.shared|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-last-shared-method|GetLastSharedMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people get-person

get-person a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users|

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

### people get-ref-last-shared-method

get-ref-last-shared-method a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights.shared|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-last-shared-method|GetRefLastSharedMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|

### people get-ref-resource

get-ref-resource a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights.used|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-resource|GetRefResource|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|

### people get-resource

get-resource a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights.used|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResource|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people get-shared

get-shared a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shared|GetShared|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people get-trending

get-trending a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-trending|GetTrending|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--trending-id**|string|key: id of trending|trending_id|trending-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people get-used

get-used a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-used|GetUsed|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people list-person

list-person a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users|

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

### people list-shared

list-shared a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-shared|ListShared|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people list-trending

list-trending a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-trending|ListTrending|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people list-used

list-used a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-used|ListUsed|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### people set-ref-last-shared-method

set-ref-last-shared-method a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights.shared|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-last-shared-method|SetRefLastSharedMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### people set-ref-resource

set-ref-resource a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights.used|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-resource|SetRefResource|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### people update-insight

update-insight a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-insight|UpdateInsights|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--shared**|array|Calculated relationship identifying documents shared with or by the user. This includes URLs, file attachments, and reference attachments to OneDrive for Business and SharePoint files found in Outlook messages and meetings. This also includes URLs and reference attachments to Teams conversations. Ordered by recency of share.|shared|shared|
|**--trending**|array|Calculated relationship identifying documents trending around a user. Trending documents are calculated based on activity of the user's closest network of people and include files stored in OneDrive for Business and SharePoint. Trending insights help the user to discover potentially useful content that the user has access to, but has never viewed before.|trending|trending|
|**--used**|array|Calculated relationship identifying the latest documents viewed or modified by a user, including OneDrive for Business and SharePoint documents, ranked by recency of use.|used|used|

### people update-person

update-person a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users|

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
|**--given-name**|string|The person's given name.|given_name|givenName|
|**--im-address**|string|The instant message voice over IP (VOIP) session initiation protocol (SIP) address for the user. Read-only.|im_address|imAddress|
|**--is-favorite**|boolean|true if the user has flagged this person as a favorite.|is_favorite|isFavorite|
|**--job-title**|string|The person's job title.|job_title|jobTitle|
|**--office-location**|string|The location of the person's office.|office_location|officeLocation|
|**--person-notes**|string|Free-form notes that the user has taken about this person.|person_notes|personNotes|
|**--person-type**|object|personType|person_type|personType|
|**--phones**|array|The person's phone numbers.|phones|phones|
|**--postal-addresses**|array|The person's addresses.|postal_addresses|postalAddresses|
|**--profession**|string|The person's profession.|profession|profession|
|**--scored-email-addresses**|array|The person's email addresses.|scored_email_addresses|scoredEmailAddresses|
|**--surname**|string|The person's surname.|surname|surname|
|**--user-principal-name**|string|The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.|user_principal_name|userPrincipalName|
|**--websites**|array|The person's websites.|websites|websites|
|**--yomi-company**|string|The phonetic Japanese name of the person's company.|yomi_company|yomiCompany|

### people update-shared

update-shared a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shared|UpdateShared|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--id**|string|Read-only.|id|id|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--sharing-history**|array||sharing_history|sharingHistory|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--last-shared-method-id**|string|Read-only.|id1|id|
|**--last-shared-shared-by**|object|insightIdentity|shared_by|sharedBy|
|**--last-shared-shared-date-time**|date-time|The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.|shared_date_time|sharedDateTime|
|**--last-shared-sharing-reference**|object|resourceReference|sharing_reference|sharingReference|
|**--last-shared-sharing-subject**|string|The subject with which the document was shared.|sharing_subject|sharingSubject|
|**--last-shared-sharing-type**|string|Determines the way the document was shared, can be by a 'Link', 'Attachment', 'Group', 'Site'.|sharing_type|sharingType|

### people update-trending

update-trending a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-trending|UpdateTrending|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--trending-id**|string|key: id of trending|trending_id|trending-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--weight**|number|Value indicating how much the document is currently trending. The larger the number, the more the document is currently trending around the user (the more relevant it is). Returned documents are sorted by this value.|weight|weight|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|

### people update-used

update-used a people.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|people|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-used|UpdateUsed|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|
|**--id**|string|Read-only.|id|id|
|**--last-used**|object|usageDetails|last_used|lastUsed|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|
