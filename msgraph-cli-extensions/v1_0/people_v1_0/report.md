# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az people_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az people_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az people user|users|[commands](#CommandsInusers)|
|az people user-insight|users.insights|[commands](#CommandsInusers.insights)|
|az people user-insight-shared|users.insights.shared|[commands](#CommandsInusers.insights.shared)|
|az people user-insight-trending|users.insights.trending|[commands](#CommandsInusers.insights.trending)|
|az people user-insight-used|users.insights.used|[commands](#CommandsInusers.insights.used)|

## COMMANDS
### <a name="CommandsInusers">Commands in `az people user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az people user delete](#usersDeletePeople)|DeletePeople|[Parameters](#ParametersusersDeletePeople)|Not Found|
|[az people user delete](#usersDeleteInsights)|DeleteInsights|[Parameters](#ParametersusersDeleteInsights)|Not Found|
|[az people user create-person](#usersCreatePeople)|CreatePeople|[Parameters](#ParametersusersCreatePeople)|Not Found|
|[az people user list-person](#usersListPeople)|ListPeople|[Parameters](#ParametersusersListPeople)|Not Found|
|[az people user show-insight](#usersGetInsights)|GetInsights|[Parameters](#ParametersusersGetInsights)|Not Found|
|[az people user show-person](#usersGetPeople)|GetPeople|[Parameters](#ParametersusersGetPeople)|Not Found|
|[az people user update-insight](#usersUpdateInsights)|UpdateInsights|[Parameters](#ParametersusersUpdateInsights)|Not Found|
|[az people user update-person](#usersUpdatePeople)|UpdatePeople|[Parameters](#ParametersusersUpdatePeople)|Not Found|

### <a name="CommandsInusers.insights">Commands in `az people user-insight` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az people user-insight delete](#users.insightsDeleteShared)|DeleteShared|[Parameters](#Parametersusers.insightsDeleteShared)|Not Found|
|[az people user-insight delete](#users.insightsDeleteTrending)|DeleteTrending|[Parameters](#Parametersusers.insightsDeleteTrending)|Not Found|
|[az people user-insight delete](#users.insightsDeleteUsed)|DeleteUsed|[Parameters](#Parametersusers.insightsDeleteUsed)|Not Found|
|[az people user-insight create-shared](#users.insightsCreateShared)|CreateShared|[Parameters](#Parametersusers.insightsCreateShared)|Not Found|
|[az people user-insight create-trending](#users.insightsCreateTrending)|CreateTrending|[Parameters](#Parametersusers.insightsCreateTrending)|Not Found|
|[az people user-insight create-used](#users.insightsCreateUsed)|CreateUsed|[Parameters](#Parametersusers.insightsCreateUsed)|Not Found|
|[az people user-insight list-shared](#users.insightsListShared)|ListShared|[Parameters](#Parametersusers.insightsListShared)|Not Found|
|[az people user-insight list-trending](#users.insightsListTrending)|ListTrending|[Parameters](#Parametersusers.insightsListTrending)|Not Found|
|[az people user-insight list-used](#users.insightsListUsed)|ListUsed|[Parameters](#Parametersusers.insightsListUsed)|Not Found|
|[az people user-insight show-shared](#users.insightsGetShared)|GetShared|[Parameters](#Parametersusers.insightsGetShared)|Not Found|
|[az people user-insight show-trending](#users.insightsGetTrending)|GetTrending|[Parameters](#Parametersusers.insightsGetTrending)|Not Found|
|[az people user-insight show-used](#users.insightsGetUsed)|GetUsed|[Parameters](#Parametersusers.insightsGetUsed)|Not Found|
|[az people user-insight update-shared](#users.insightsUpdateShared)|UpdateShared|[Parameters](#Parametersusers.insightsUpdateShared)|Not Found|
|[az people user-insight update-trending](#users.insightsUpdateTrending)|UpdateTrending|[Parameters](#Parametersusers.insightsUpdateTrending)|Not Found|
|[az people user-insight update-used](#users.insightsUpdateUsed)|UpdateUsed|[Parameters](#Parametersusers.insightsUpdateUsed)|Not Found|

### <a name="CommandsInusers.insights.shared">Commands in `az people user-insight-shared` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az people user-insight-shared delete](#users.insights.sharedDeleteRefLastSharedMethod)|DeleteRefLastSharedMethod|[Parameters](#Parametersusers.insights.sharedDeleteRefLastSharedMethod)|Not Found|
|[az people user-insight-shared delete](#users.insights.sharedDeleteRefResource)|DeleteRefResource|[Parameters](#Parametersusers.insights.sharedDeleteRefResource)|Not Found|
|[az people user-insight-shared set-ref-last-shared-method](#users.insights.sharedSetRefLastSharedMethod)|SetRefLastSharedMethod|[Parameters](#Parametersusers.insights.sharedSetRefLastSharedMethod)|Not Found|
|[az people user-insight-shared set-ref-resource](#users.insights.sharedSetRefResource)|SetRefResource|[Parameters](#Parametersusers.insights.sharedSetRefResource)|Not Found|
|[az people user-insight-shared show-last-shared-method](#users.insights.sharedGetLastSharedMethod)|GetLastSharedMethod|[Parameters](#Parametersusers.insights.sharedGetLastSharedMethod)|Not Found|
|[az people user-insight-shared show-ref-last-shared-method](#users.insights.sharedGetRefLastSharedMethod)|GetRefLastSharedMethod|[Parameters](#Parametersusers.insights.sharedGetRefLastSharedMethod)|Not Found|
|[az people user-insight-shared show-ref-resource](#users.insights.sharedGetRefResource)|GetRefResource|[Parameters](#Parametersusers.insights.sharedGetRefResource)|Not Found|
|[az people user-insight-shared show-resource](#users.insights.sharedGetResource)|GetResource|[Parameters](#Parametersusers.insights.sharedGetResource)|Not Found|

### <a name="CommandsInusers.insights.trending">Commands in `az people user-insight-trending` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az people user-insight-trending delete](#users.insights.trendingDeleteRefResource)|DeleteRefResource|[Parameters](#Parametersusers.insights.trendingDeleteRefResource)|Not Found|
|[az people user-insight-trending set-ref-resource](#users.insights.trendingSetRefResource)|SetRefResource|[Parameters](#Parametersusers.insights.trendingSetRefResource)|Not Found|
|[az people user-insight-trending show-ref-resource](#users.insights.trendingGetRefResource)|GetRefResource|[Parameters](#Parametersusers.insights.trendingGetRefResource)|Not Found|
|[az people user-insight-trending show-resource](#users.insights.trendingGetResource)|GetResource|[Parameters](#Parametersusers.insights.trendingGetResource)|Not Found|

### <a name="CommandsInusers.insights.used">Commands in `az people user-insight-used` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az people user-insight-used delete](#users.insights.usedDeleteRefResource)|DeleteRefResource|[Parameters](#Parametersusers.insights.usedDeleteRefResource)|Not Found|
|[az people user-insight-used set-ref-resource](#users.insights.usedSetRefResource)|SetRefResource|[Parameters](#Parametersusers.insights.usedSetRefResource)|Not Found|
|[az people user-insight-used show-ref-resource](#users.insights.usedGetRefResource)|GetRefResource|[Parameters](#Parametersusers.insights.usedGetRefResource)|Not Found|
|[az people user-insight-used show-resource](#users.insights.usedGetResource)|GetResource|[Parameters](#Parametersusers.insights.usedGetResource)|Not Found|


## COMMAND DETAILS

### group `az people user`
#### <a name="usersDeletePeople">Command `az people user delete`</a>

##### <a name="ParametersusersDeletePeople">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-id**|string|key: id of person|person_id|person-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteInsights">Command `az people user delete`</a>

##### <a name="ParametersusersDeleteInsights">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersCreatePeople">Command `az people user create-person`</a>

##### <a name="ParametersusersCreatePeople">Parameters</a> 
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

#### <a name="usersListPeople">Command `az people user list-person`</a>

##### <a name="ParametersusersListPeople">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetInsights">Command `az people user show-insight`</a>

##### <a name="ParametersusersGetInsights">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetPeople">Command `az people user show-person`</a>

##### <a name="ParametersusersGetPeople">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-id**|string|key: id of person|person_id|person-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateInsights">Command `az people user update-insight`</a>

##### <a name="ParametersusersUpdateInsights">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--shared**|array|Calculated relationship identifying documents shared with or by the user. This includes URLs, file attachments, and reference attachments to OneDrive for Business and SharePoint files found in Outlook messages and meetings. This also includes URLs and reference attachments to Teams conversations. Ordered by recency of share.|shared|shared|
|**--trending**|array|Calculated relationship identifying documents trending around a user. Trending documents are calculated based on activity of the user's closest network of people and include files stored in OneDrive for Business and SharePoint. Trending insights help the user to discover potentially useful content that the user has access to, but has never viewed before.|trending|trending|
|**--used**|array|Calculated relationship identifying the latest documents viewed or modified by a user, including OneDrive for Business and SharePoint documents, ranked by recency of use.|used|used|

#### <a name="usersUpdatePeople">Command `az people user update-person`</a>

##### <a name="ParametersusersUpdatePeople">Parameters</a> 
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

### group `az people user-insight`
#### <a name="users.insightsDeleteShared">Command `az people user-insight delete`</a>

##### <a name="Parametersusers.insightsDeleteShared">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.insightsDeleteTrending">Command `az people user-insight delete`</a>

##### <a name="Parametersusers.insightsDeleteTrending">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trending-id**|string|key: id of trending|trending_id|trending-id|

#### <a name="users.insightsDeleteUsed">Command `az people user-insight delete`</a>

##### <a name="Parametersusers.insightsDeleteUsed">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|

#### <a name="users.insightsCreateShared">Command `az people user-insight create-shared`</a>

##### <a name="Parametersusers.insightsCreateShared">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--sharing-history**|array||sharing_history|sharingHistory|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--shared-by**|object|insightIdentity|shared_by|sharedBy|
|**--shared-date-time**|date-time|The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.|shared_date_time|sharedDateTime|
|**--sharing-reference**|object|resourceReference|sharing_reference|sharingReference|
|**--sharing-subject**|string|The subject with which the document was shared.|sharing_subject|sharingSubject|
|**--sharing-type**|string|Determines the way the document was shared, can be by a 'Link', 'Attachment', 'Group', 'Site'.|sharing_type|sharingType|

#### <a name="users.insightsCreateTrending">Command `az people user-insight create-trending`</a>

##### <a name="Parametersusers.insightsCreateTrending">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--weight**|number|Value indicating how much the document is currently trending. The larger the number, the more the document is currently trending around the user (the more relevant it is). Returned documents are sorted by this value.|weight|weight|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="users.insightsCreateUsed">Command `az people user-insight create-used`</a>

##### <a name="Parametersusers.insightsCreateUsed">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--last-used**|object|usageDetails|last_used|lastUsed|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="users.insightsListShared">Command `az people user-insight list-shared`</a>

##### <a name="Parametersusers.insightsListShared">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.insightsListTrending">Command `az people user-insight list-trending`</a>

##### <a name="Parametersusers.insightsListTrending">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.insightsListUsed">Command `az people user-insight list-used`</a>

##### <a name="Parametersusers.insightsListUsed">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.insightsGetShared">Command `az people user-insight show-shared`</a>

##### <a name="Parametersusers.insightsGetShared">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.insightsGetTrending">Command `az people user-insight show-trending`</a>

##### <a name="Parametersusers.insightsGetTrending">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--trending-id**|string|key: id of trending|trending_id|trending-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.insightsGetUsed">Command `az people user-insight show-used`</a>

##### <a name="Parametersusers.insightsGetUsed">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.insightsUpdateShared">Command `az people user-insight update-shared`</a>

##### <a name="Parametersusers.insightsUpdateShared">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--id**|string|Read-only.|id|id|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--sharing-history**|array||sharing_history|sharingHistory|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--shared-by**|object|insightIdentity|shared_by|sharedBy|
|**--shared-date-time**|date-time|The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.|shared_date_time|sharedDateTime|
|**--sharing-reference**|object|resourceReference|sharing_reference|sharingReference|
|**--sharing-subject**|string|The subject with which the document was shared.|sharing_subject|sharingSubject|
|**--sharing-type**|string|Determines the way the document was shared, can be by a 'Link', 'Attachment', 'Group', 'Site'.|sharing_type|sharingType|

#### <a name="users.insightsUpdateTrending">Command `az people user-insight update-trending`</a>

##### <a name="Parametersusers.insightsUpdateTrending">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--trending-id**|string|key: id of trending|trending_id|trending-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--weight**|number|Value indicating how much the document is currently trending. The larger the number, the more the document is currently trending around the user (the more relevant it is). Returned documents are sorted by this value.|weight|weight|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="users.insightsUpdateUsed">Command `az people user-insight update-used`</a>

##### <a name="Parametersusers.insightsUpdateUsed">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|
|**--id**|string|Read-only.|id|id|
|**--last-used**|object|usageDetails|last_used|lastUsed|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

### group `az people user-insight-shared`
#### <a name="users.insights.sharedDeleteRefLastSharedMethod">Command `az people user-insight-shared delete`</a>

##### <a name="Parametersusers.insights.sharedDeleteRefLastSharedMethod">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.insights.sharedDeleteRefResource">Command `az people user-insight-shared delete`</a>

##### <a name="Parametersusers.insights.sharedDeleteRefResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="users.insights.sharedSetRefLastSharedMethod">Command `az people user-insight-shared set-ref-last-shared-method`</a>

##### <a name="Parametersusers.insights.sharedSetRefLastSharedMethod">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="users.insights.sharedSetRefResource">Command `az people user-insight-shared set-ref-resource`</a>

##### <a name="Parametersusers.insights.sharedSetRefResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="users.insights.sharedGetLastSharedMethod">Command `az people user-insight-shared show-last-shared-method`</a>

##### <a name="Parametersusers.insights.sharedGetLastSharedMethod">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.insights.sharedGetRefLastSharedMethod">Command `az people user-insight-shared show-ref-last-shared-method`</a>

##### <a name="Parametersusers.insights.sharedGetRefLastSharedMethod">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|

#### <a name="users.insights.sharedGetRefResource">Command `az people user-insight-shared show-ref-resource`</a>

##### <a name="Parametersusers.insights.sharedGetRefResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|

#### <a name="users.insights.sharedGetResource">Command `az people user-insight-shared show-resource`</a>

##### <a name="Parametersusers.insights.sharedGetResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--shared-insight-id**|string|key: id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az people user-insight-trending`
#### <a name="users.insights.trendingDeleteRefResource">Command `az people user-insight-trending delete`</a>

##### <a name="Parametersusers.insights.trendingDeleteRefResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--trending-id**|string|key: id of trending|trending_id|trending-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.insights.trendingSetRefResource">Command `az people user-insight-trending set-ref-resource`</a>

##### <a name="Parametersusers.insights.trendingSetRefResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--trending-id**|string|key: id of trending|trending_id|trending-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="users.insights.trendingGetRefResource">Command `az people user-insight-trending show-ref-resource`</a>

##### <a name="Parametersusers.insights.trendingGetRefResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--trending-id**|string|key: id of trending|trending_id|trending-id|

#### <a name="users.insights.trendingGetResource">Command `az people user-insight-trending show-resource`</a>

##### <a name="Parametersusers.insights.trendingGetResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--trending-id**|string|key: id of trending|trending_id|trending-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az people user-insight-used`
#### <a name="users.insights.usedDeleteRefResource">Command `az people user-insight-used delete`</a>

##### <a name="Parametersusers.insights.usedDeleteRefResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.insights.usedSetRefResource">Command `az people user-insight-used set-ref-resource`</a>

##### <a name="Parametersusers.insights.usedSetRefResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="users.insights.usedGetRefResource">Command `az people user-insight-used show-ref-resource`</a>

##### <a name="Parametersusers.insights.usedGetRefResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|

#### <a name="users.insights.usedGetResource">Command `az people user-insight-used show-resource`</a>

##### <a name="Parametersusers.insights.usedGetResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--used-insight-id**|string|key: id of usedInsight|used_insight_id|usedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|
