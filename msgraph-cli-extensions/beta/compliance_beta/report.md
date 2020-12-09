# Azure CLI Module Creation Report

### compliance activate

activate a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|activate|activate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|

### compliance close

close a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|close|close|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|

### compliance create-case

create-case a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-case|CreateCases|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--external-id**|string||external_id|externalId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--status**|choice||status|status|
|**--custodians**|array||custodians|custodians|
|**--review-sets**|array||review_sets|reviewSets|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--closed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--closed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--closed-by-user**|object|identity|microsoft_graph_identity_user|user|

### compliance create-custodian

create-custodian a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-custodian|CreateCustodians|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--id**|string|Read-only.|id|id|
|**--acknowledged-date-time**|date-time||acknowledged_date_time|acknowledgedDateTime|
|**--apply-hold-to-sources**|boolean||apply_hold_to_sources|applyHoldToSources|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--released-date-time**|date-time||released_date_time|releasedDateTime|
|**--status**|choice||status|status|
|**--last-index-operation**|object|caseIndexOperation|last_index_operation|lastIndexOperation|
|**--site-sources**|array||site_sources|siteSources|
|**--unified-group-sources**|array||unified_group_sources|unifiedGroupSources|
|**--user-sources**|array||user_sources|userSources|

### compliance create-query

create-query a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.reviewSets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-query|CreateQueries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--query**|string||query|query|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|

### compliance create-review-set

create-review-set a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-review-set|CreateReviewSets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--queries**|array||queries|queries|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### compliance create-site-source

create-site-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-site-source|CreateSiteSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--site**|object|site|site|site|

### compliance create-unified-group-source

create-unified-group-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-unified-group-source|CreateUnifiedGroupSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--included-sources**|choice||included_sources|includedSources|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|

### compliance create-user-source

create-user-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user-source|CreateUserSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--email**|string||email|email|
|**--included-sources**|choice||included_sources|includedSources|

### compliance delete

delete a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.reviewSets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteQueries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--review-set-query-id**|string|key: id of reviewSetQuery|review_set_query_id|reviewSetQuery-id|
|**--if-match**|string|ETag|if_match|If-Match|

### compliance get-case

get-case a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-case|GetCases|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-compliance

get-compliance a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.compliance|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-compliance|GetCompliance|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-custodian

get-custodian a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-custodian|GetCustodians|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-ediscovery

get-ediscovery a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ediscovery|GetEdiscovery|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-group

get-group a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians.unifiedGroupSources|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-group|GetGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-last-index-operation

get-last-index-operation a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-last-index-operation|GetLastIndexOperation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-query

get-query a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.reviewSets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-query|GetQueries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--review-set-query-id**|string|key: id of reviewSetQuery|review_set_query_id|reviewSetQuery-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-ref-group

get-ref-group a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians.unifiedGroupSources|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-group|GetRefGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|

### compliance get-ref-last-index-operation

get-ref-last-index-operation a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-last-index-operation|GetRefLastIndexOperation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|

### compliance get-ref-site

get-ref-site a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians.siteSources|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-site|GetRefSite|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|

### compliance get-review-set

get-review-set a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-review-set|GetReviewSets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-site

get-site a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians.siteSources|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-site|GetSite|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-site-source

get-site-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-site-source|GetSiteSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-unified-group-source

get-unified-group-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-unified-group-source|GetUnifiedGroupSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance get-user-source

get-user-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-source|GetUserSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--user-source-id**|string|key: id of userSource|user_source_id|userSource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance list-case

list-case a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-case|ListCases|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance list-custodian

list-custodian a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-custodian|ListCustodians|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance list-query

list-query a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.reviewSets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-query|ListQueries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance list-review-set

list-review-set a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-review-set|ListReviewSets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance list-site-source

list-site-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-site-source|ListSiteSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance list-unified-group-source

list-unified-group-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-unified-group-source|ListUnifiedGroupSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance list-user-source

list-user-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user-source|ListUserSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### compliance release

release a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|release|release|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|

### compliance reopen

reopen a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reopen|reopen|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|

### compliance set-ref-group

set-ref-group a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians.unifiedGroupSources|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-group|SetRefGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### compliance set-ref-last-index-operation

set-ref-last-index-operation a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-last-index-operation|SetRefLastIndexOperation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### compliance set-ref-site

set-ref-site a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians.siteSources|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-site|SetRefSite|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### compliance update-case

update-case a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-case|UpdateCases|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--id**|string|Read-only.|id|id|
|**--closed-date-time**|date-time||closed_date_time|closedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--external-id**|string||external_id|externalId|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--status**|choice||status|status|
|**--custodians**|array||custodians|custodians|
|**--review-sets**|array||review_sets|reviewSets|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--closed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--closed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--closed-by-user**|object|identity|microsoft_graph_identity_user|user|

### compliance update-compliance

update-compliance a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.compliance|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-compliance|UpdateCompliance|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-id**|string|Read-only.|id|id|
|**--ediscovery-cases**|array||cases|cases|

### compliance update-custodian

update-custodian a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-custodian|UpdateCustodians|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--id**|string|Read-only.|id|id|
|**--acknowledged-date-time**|date-time||acknowledged_date_time|acknowledgedDateTime|
|**--apply-hold-to-sources**|boolean||apply_hold_to_sources|applyHoldToSources|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--email**|string||email|email|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--released-date-time**|date-time||released_date_time|releasedDateTime|
|**--status**|choice||status|status|
|**--last-index-operation**|object|caseIndexOperation|last_index_operation|lastIndexOperation|
|**--site-sources**|array||site_sources|siteSources|
|**--unified-group-sources**|array||unified_group_sources|unifiedGroupSources|
|**--user-sources**|array||user_sources|userSources|

### compliance update-ediscovery

update-ediscovery a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-ediscovery|UpdateEdiscovery|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--cases**|array||cases|cases|

### compliance update-index

update-index a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-index|updateIndex|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|

### compliance update-query

update-query a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.reviewSets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-query|UpdateQueries|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--review-set-query-id**|string|key: id of reviewSetQuery|review_set_query_id|reviewSetQuery-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--query**|string||query|query|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|

### compliance update-review-set

update-review-set a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-review-set|UpdateReviewSets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--queries**|array||queries|queries|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### compliance update-site-source

update-site-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-site-source|UpdateSiteSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--site**|object|site|site|site|

### compliance update-unified-group-source

update-unified-group-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-unified-group-source|UpdateUnifiedGroupSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--included-sources**|choice||included_sources|includedSources|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|

### compliance update-user-source

update-user-source a compliance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|compliance|compliance.ediscovery.cases.custodians|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user-source|UpdateUserSources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--user-source-id**|string|key: id of userSource|user_source_id|userSource-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--email**|string||email|email|
|**--included-sources**|choice||included_sources|includedSources|
