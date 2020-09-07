# Azure CLI Module Creation Report

### analytics create-activity-statistics

create-activity-statistics a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.analytics|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity-statistics|CreateActivityStatistics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|choice||activity|activity|
|**--start-date**|date||start_date|startDate|
|**--end-date**|date||end_date|endDate|
|**--time-zone-used**|string||time_zone_used|timeZoneUsed|
|**--duration**|duration||duration|duration|

### analytics create-shared

create-shared a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-shared|CreateShared|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--sharing-history**|array||sharing_history|sharingHistory|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--last-shared-method-id**|string|Read-only.|id1|id|
|**--last-shared-shared-by**|object|insightIdentity|shared_by|sharedBy|
|**--last-shared-shared-date-time**|date-time|The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.|shared_date_time|sharedDateTime|
|**--last-shared-sharing-subject**|string|The subject with which the document was shared.|sharing_subject|sharingSubject|
|**--last-shared-sharing-type**|string|Determines the way the document was shared, can be by a 'Link', 'Attachment', 'Group', 'Site'.|sharing_type|sharingType|
|**--last-shared-sharing-reference**|object|resourceReference|sharing_reference|sharingReference|

### analytics create-trending

create-trending a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-trending|CreateTrending|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--weight**|number|Value indicating how much the document is currently trending. The larger the number, the more the document is currently trending around the user (the more relevant it is). Returned documents are sorted by this value.|weight|weight|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|

### analytics create-used

create-used a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-used|CreateUsed|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--last-used**|object|usageDetails|last_used|lastUsed|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|

### analytics delete

delete a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|activitystatistics.activityStatistics|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteActivityStatistics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--activity-statistics-id**|string|key: activityStatistics-id of activityStatistics|activity_statistics_id|activityStatistics-id|
|**--if-match**|string|ETag|if_match|If-Match|

### analytics get-activity-statistics

get-activity-statistics a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.analytics|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-statistics|GetActivityStatistics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--activity-statistics-id**|string|key: activityStatistics-id of activityStatistics|activity_statistics_id|activityStatistics-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics get-analytic

get-analytic a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-analytic|GetAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics get-insight

get-insight a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-insight|GetInsights|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics get-last-shared-method

get-last-shared-method a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights.shared|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-last-shared-method|GetLastSharedMethod|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--shared-insight-id**|string|key: sharedInsight-id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics get-resource

get-resource a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights.used|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResource|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--used-insight-id**|string|key: usedInsight-id of usedInsight|used_insight_id|usedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics get-shared

get-shared a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shared|GetShared|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--shared-insight-id**|string|key: sharedInsight-id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics get-trending

get-trending a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-trending|GetTrending|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--trending-id**|string|key: trending-id of trending|trending_id|trending-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics get-used

get-used a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-used|GetUsed|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--used-insight-id**|string|key: usedInsight-id of usedInsight|used_insight_id|usedInsight-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics list-activity-statistics

list-activity-statistics a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.analytics|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity-statistics|ListActivityStatistics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics list-shared

list-shared a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-shared|ListShared|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics list-trending

list-trending a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-trending|ListTrending|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics list-used

list-used a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-used|ListUsed|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### analytics update-activity-statistics

update-activity-statistics a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.analytics|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-activity-statistics|UpdateActivityStatistics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--activity-statistics-id**|string|key: activityStatistics-id of activityStatistics|activity_statistics_id|activityStatistics-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|choice||activity|activity|
|**--start-date**|date||start_date|startDate|
|**--end-date**|date||end_date|endDate|
|**--time-zone-used**|string||time_zone_used|timeZoneUsed|
|**--duration**|duration||duration|duration|

### analytics update-analytic

update-analytic a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-analytic|UpdateAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--settings**|object|settings|settings|settings|
|**--activity-statistics**|array||activity_statistics|activityStatistics|

### analytics update-insight

update-insight a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-insight|UpdateInsights|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--trending**|array|Calculated relationship identifying trending documents. Trending documents can be stored in OneDrive or in SharePoint sites.|trending|trending|
|**--shared**|array|Calculated relationship identifying documents shared with a user. Documents can be shared as email attachments or as OneDrive for Business links sent in emails.|shared|shared|
|**--used**|array|Calculated relationship identifying documents viewed and modified by a user. Includes documents the user used in OneDrive for Business, SharePoint, opened as email attachments, and as link attachments from sources like Box, DropBox and Google Drive.|used|used|

### analytics update-shared

update-shared a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shared|UpdateShared|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--shared-insight-id**|string|key: sharedInsight-id of sharedInsight|shared_insight_id|sharedInsight-id|
|**--id**|string|Read-only.|id|id|
|**--sharing-history**|array||sharing_history|sharingHistory|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--last-shared-method-id**|string|Read-only.|id1|id|
|**--last-shared-shared-by**|object|insightIdentity|shared_by|sharedBy|
|**--last-shared-shared-date-time**|date-time|The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.|shared_date_time|sharedDateTime|
|**--last-shared-sharing-subject**|string|The subject with which the document was shared.|sharing_subject|sharingSubject|
|**--last-shared-sharing-type**|string|Determines the way the document was shared, can be by a 'Link', 'Attachment', 'Group', 'Site'.|sharing_type|sharingType|
|**--last-shared-sharing-reference**|object|resourceReference|sharing_reference|sharingReference|

### analytics update-trending

update-trending a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-trending|UpdateTrending|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--trending-id**|string|key: trending-id of trending|trending_id|trending-id|
|**--id**|string|Read-only.|id|id|
|**--weight**|number|Value indicating how much the document is currently trending. The larger the number, the more the document is currently trending around the user (the more relevant it is). Returned documents are sorted by this value.|weight|weight|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|

### analytics update-used

update-used a analytics.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|analytics|users.insights|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-used|UpdateUsed|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--used-insight-id**|string|key: usedInsight-id of usedInsight|used_insight_id|usedInsight-id|
|**--id**|string|Read-only.|id|id|
|**--last-used**|object|usageDetails|last_used|lastUsed|
|**--resource-visualization**|object|resourceVisualization|resource_visualization|resourceVisualization|
|**--resource-reference**|object|resourceReference|resource_reference|resourceReference|
|**--resource-id**|string|Read-only.|microsoft_graph_entity_id|id|
