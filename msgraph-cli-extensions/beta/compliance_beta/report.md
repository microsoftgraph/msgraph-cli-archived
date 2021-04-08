# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az compliance_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az compliance_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az compliance compliance|compliance.compliance|[commands](#CommandsIncompliance.compliance)|
|az compliance compliance|compliance|[commands](#CommandsIncompliance)|
|az compliance compliance-ediscovery|compliance.ediscovery|[commands](#CommandsIncompliance.ediscovery)|
|az compliance compliance-ediscovery-case|compliance.ediscovery.cases|[commands](#CommandsIncompliance.ediscovery.cases)|
|az compliance compliance-ediscovery-case-custodian|compliance.ediscovery.cases.custodians|[commands](#CommandsIncompliance.ediscovery.cases.custodians)|
|az compliance compliance-ediscovery-case-custodian-site-source|compliance.ediscovery.cases.custodians.siteSources|[commands](#CommandsIncompliance.ediscovery.cases.custodians.siteSources)|
|az compliance compliance-ediscovery-case-custodian-unified-group-source|compliance.ediscovery.cases.custodians.unifiedGroupSources|[commands](#CommandsIncompliance.ediscovery.cases.custodians.unifiedGroupSources)|
|az compliance compliance-ediscovery-case-review-set|compliance.ediscovery.cases.reviewSets|[commands](#CommandsIncompliance.ediscovery.cases.reviewSets)|

## COMMANDS
### <a name="CommandsIncompliance.compliance">Commands in `az compliance compliance` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az compliance compliance create](#compliance.complianceUpdateCompliance)|UpdateCompliance|[Parameters](#Parameterscompliance.complianceUpdateCompliance)|Not Found|
|[az compliance compliance show-compliance](#compliance.complianceGetCompliance)|GetCompliance|[Parameters](#Parameterscompliance.complianceGetCompliance)|Not Found|

### <a name="CommandsIncompliance">Commands in `az compliance compliance` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az compliance compliance delete-ediscovery](#complianceDeleteEdiscovery)|DeleteEdiscovery|[Parameters](#ParameterscomplianceDeleteEdiscovery)|Not Found|
|[az compliance compliance show-ediscovery](#complianceGetEdiscovery)|GetEdiscovery|[Parameters](#ParameterscomplianceGetEdiscovery)|Not Found|
|[az compliance compliance update-ediscovery](#complianceUpdateEdiscovery)|UpdateEdiscovery|[Parameters](#ParameterscomplianceUpdateEdiscovery)|Not Found|

### <a name="CommandsIncompliance.ediscovery">Commands in `az compliance compliance-ediscovery` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az compliance compliance-ediscovery create-case](#compliance.ediscoveryCreateCases)|CreateCases|[Parameters](#Parameterscompliance.ediscoveryCreateCases)|Not Found|
|[az compliance compliance-ediscovery delete-case](#compliance.ediscoveryDeleteCases)|DeleteCases|[Parameters](#Parameterscompliance.ediscoveryDeleteCases)|Not Found|
|[az compliance compliance-ediscovery list-case](#compliance.ediscoveryListCases)|ListCases|[Parameters](#Parameterscompliance.ediscoveryListCases)|Not Found|
|[az compliance compliance-ediscovery show-case](#compliance.ediscoveryGetCases)|GetCases|[Parameters](#Parameterscompliance.ediscoveryGetCases)|Not Found|
|[az compliance compliance-ediscovery update-case](#compliance.ediscoveryUpdateCases)|UpdateCases|[Parameters](#Parameterscompliance.ediscoveryUpdateCases)|Not Found|

### <a name="CommandsIncompliance.ediscovery.cases">Commands in `az compliance compliance-ediscovery-case` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az compliance compliance-ediscovery-case close](#compliance.ediscovery.casesclose)|close|[Parameters](#Parameterscompliance.ediscovery.casesclose)|Not Found|
|[az compliance compliance-ediscovery-case create-custodian](#compliance.ediscovery.casesCreateCustodians)|CreateCustodians|[Parameters](#Parameterscompliance.ediscovery.casesCreateCustodians)|Not Found|
|[az compliance compliance-ediscovery-case create-review-set](#compliance.ediscovery.casesCreateReviewSets)|CreateReviewSets|[Parameters](#Parameterscompliance.ediscovery.casesCreateReviewSets)|Not Found|
|[az compliance compliance-ediscovery-case delete-custodian](#compliance.ediscovery.casesDeleteCustodians)|DeleteCustodians|[Parameters](#Parameterscompliance.ediscovery.casesDeleteCustodians)|Not Found|
|[az compliance compliance-ediscovery-case delete-review-set](#compliance.ediscovery.casesDeleteReviewSets)|DeleteReviewSets|[Parameters](#Parameterscompliance.ediscovery.casesDeleteReviewSets)|Not Found|
|[az compliance compliance-ediscovery-case list-custodian](#compliance.ediscovery.casesListCustodians)|ListCustodians|[Parameters](#Parameterscompliance.ediscovery.casesListCustodians)|Not Found|
|[az compliance compliance-ediscovery-case list-review-set](#compliance.ediscovery.casesListReviewSets)|ListReviewSets|[Parameters](#Parameterscompliance.ediscovery.casesListReviewSets)|Not Found|
|[az compliance compliance-ediscovery-case reopen](#compliance.ediscovery.casesreopen)|reopen|[Parameters](#Parameterscompliance.ediscovery.casesreopen)|Not Found|
|[az compliance compliance-ediscovery-case show-custodian](#compliance.ediscovery.casesGetCustodians)|GetCustodians|[Parameters](#Parameterscompliance.ediscovery.casesGetCustodians)|Not Found|
|[az compliance compliance-ediscovery-case show-review-set](#compliance.ediscovery.casesGetReviewSets)|GetReviewSets|[Parameters](#Parameterscompliance.ediscovery.casesGetReviewSets)|Not Found|
|[az compliance compliance-ediscovery-case update-custodian](#compliance.ediscovery.casesUpdateCustodians)|UpdateCustodians|[Parameters](#Parameterscompliance.ediscovery.casesUpdateCustodians)|Not Found|
|[az compliance compliance-ediscovery-case update-review-set](#compliance.ediscovery.casesUpdateReviewSets)|UpdateReviewSets|[Parameters](#Parameterscompliance.ediscovery.casesUpdateReviewSets)|Not Found|

### <a name="CommandsIncompliance.ediscovery.cases.custodians">Commands in `az compliance compliance-ediscovery-case-custodian` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az compliance compliance-ediscovery-case-custodian activate](#compliance.ediscovery.cases.custodiansactivate)|activate|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansactivate)|Not Found|
|[az compliance compliance-ediscovery-case-custodian create-site-source](#compliance.ediscovery.cases.custodiansCreateSiteSources)|CreateSiteSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansCreateSiteSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian create-unified-group-source](#compliance.ediscovery.cases.custodiansCreateUnifiedGroupSources)|CreateUnifiedGroupSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansCreateUnifiedGroupSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian create-user-source](#compliance.ediscovery.cases.custodiansCreateUserSources)|CreateUserSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansCreateUserSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian delete-ref-last-index-operation](#compliance.ediscovery.cases.custodiansDeleteRefLastIndexOperation)|DeleteRefLastIndexOperation|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansDeleteRefLastIndexOperation)|Not Found|
|[az compliance compliance-ediscovery-case-custodian delete-site-source](#compliance.ediscovery.cases.custodiansDeleteSiteSources)|DeleteSiteSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansDeleteSiteSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian delete-unified-group-source](#compliance.ediscovery.cases.custodiansDeleteUnifiedGroupSources)|DeleteUnifiedGroupSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansDeleteUnifiedGroupSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian delete-user-source](#compliance.ediscovery.cases.custodiansDeleteUserSources)|DeleteUserSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansDeleteUserSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian list-site-source](#compliance.ediscovery.cases.custodiansListSiteSources)|ListSiteSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansListSiteSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian list-unified-group-source](#compliance.ediscovery.cases.custodiansListUnifiedGroupSources)|ListUnifiedGroupSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansListUnifiedGroupSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian list-user-source](#compliance.ediscovery.cases.custodiansListUserSources)|ListUserSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansListUserSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian release](#compliance.ediscovery.cases.custodiansrelease)|release|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansrelease)|Not Found|
|[az compliance compliance-ediscovery-case-custodian set-ref-last-index-operation](#compliance.ediscovery.cases.custodiansSetRefLastIndexOperation)|SetRefLastIndexOperation|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansSetRefLastIndexOperation)|Not Found|
|[az compliance compliance-ediscovery-case-custodian show-last-index-operation](#compliance.ediscovery.cases.custodiansGetLastIndexOperation)|GetLastIndexOperation|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansGetLastIndexOperation)|Not Found|
|[az compliance compliance-ediscovery-case-custodian show-ref-last-index-operation](#compliance.ediscovery.cases.custodiansGetRefLastIndexOperation)|GetRefLastIndexOperation|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansGetRefLastIndexOperation)|Not Found|
|[az compliance compliance-ediscovery-case-custodian show-site-source](#compliance.ediscovery.cases.custodiansGetSiteSources)|GetSiteSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansGetSiteSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian show-unified-group-source](#compliance.ediscovery.cases.custodiansGetUnifiedGroupSources)|GetUnifiedGroupSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansGetUnifiedGroupSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian show-user-source](#compliance.ediscovery.cases.custodiansGetUserSources)|GetUserSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansGetUserSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian update-index](#compliance.ediscovery.cases.custodiansupdateIndex)|updateIndex|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansupdateIndex)|Not Found|
|[az compliance compliance-ediscovery-case-custodian update-site-source](#compliance.ediscovery.cases.custodiansUpdateSiteSources)|UpdateSiteSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansUpdateSiteSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian update-unified-group-source](#compliance.ediscovery.cases.custodiansUpdateUnifiedGroupSources)|UpdateUnifiedGroupSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansUpdateUnifiedGroupSources)|Not Found|
|[az compliance compliance-ediscovery-case-custodian update-user-source](#compliance.ediscovery.cases.custodiansUpdateUserSources)|UpdateUserSources|[Parameters](#Parameterscompliance.ediscovery.cases.custodiansUpdateUserSources)|Not Found|

### <a name="CommandsIncompliance.ediscovery.cases.custodians.siteSources">Commands in `az compliance compliance-ediscovery-case-custodian-site-source` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az compliance compliance-ediscovery-case-custodian-site-source delete-ref-site](#compliance.ediscovery.cases.custodians.siteSourcesDeleteRefSite)|DeleteRefSite|[Parameters](#Parameterscompliance.ediscovery.cases.custodians.siteSourcesDeleteRefSite)|Not Found|
|[az compliance compliance-ediscovery-case-custodian-site-source set-ref-site](#compliance.ediscovery.cases.custodians.siteSourcesSetRefSite)|SetRefSite|[Parameters](#Parameterscompliance.ediscovery.cases.custodians.siteSourcesSetRefSite)|Not Found|
|[az compliance compliance-ediscovery-case-custodian-site-source show-ref-site](#compliance.ediscovery.cases.custodians.siteSourcesGetRefSite)|GetRefSite|[Parameters](#Parameterscompliance.ediscovery.cases.custodians.siteSourcesGetRefSite)|Not Found|
|[az compliance compliance-ediscovery-case-custodian-site-source show-site](#compliance.ediscovery.cases.custodians.siteSourcesGetSite)|GetSite|[Parameters](#Parameterscompliance.ediscovery.cases.custodians.siteSourcesGetSite)|Not Found|

### <a name="CommandsIncompliance.ediscovery.cases.custodians.unifiedGroupSources">Commands in `az compliance compliance-ediscovery-case-custodian-unified-group-source` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az compliance compliance-ediscovery-case-custodian-unified-group-source delete-ref-group](#compliance.ediscovery.cases.custodians.unifiedGroupSourcesDeleteRefGroup)|DeleteRefGroup|[Parameters](#Parameterscompliance.ediscovery.cases.custodians.unifiedGroupSourcesDeleteRefGroup)|Not Found|
|[az compliance compliance-ediscovery-case-custodian-unified-group-source set-ref-group](#compliance.ediscovery.cases.custodians.unifiedGroupSourcesSetRefGroup)|SetRefGroup|[Parameters](#Parameterscompliance.ediscovery.cases.custodians.unifiedGroupSourcesSetRefGroup)|Not Found|
|[az compliance compliance-ediscovery-case-custodian-unified-group-source show-group](#compliance.ediscovery.cases.custodians.unifiedGroupSourcesGetGroup)|GetGroup|[Parameters](#Parameterscompliance.ediscovery.cases.custodians.unifiedGroupSourcesGetGroup)|Not Found|
|[az compliance compliance-ediscovery-case-custodian-unified-group-source show-ref-group](#compliance.ediscovery.cases.custodians.unifiedGroupSourcesGetRefGroup)|GetRefGroup|[Parameters](#Parameterscompliance.ediscovery.cases.custodians.unifiedGroupSourcesGetRefGroup)|Not Found|

### <a name="CommandsIncompliance.ediscovery.cases.reviewSets">Commands in `az compliance compliance-ediscovery-case-review-set` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az compliance compliance-ediscovery-case-review-set create-query](#compliance.ediscovery.cases.reviewSetsCreateQueries)|CreateQueries|[Parameters](#Parameterscompliance.ediscovery.cases.reviewSetsCreateQueries)|Not Found|
|[az compliance compliance-ediscovery-case-review-set delete-query](#compliance.ediscovery.cases.reviewSetsDeleteQueries)|DeleteQueries|[Parameters](#Parameterscompliance.ediscovery.cases.reviewSetsDeleteQueries)|Not Found|
|[az compliance compliance-ediscovery-case-review-set list-query](#compliance.ediscovery.cases.reviewSetsListQueries)|ListQueries|[Parameters](#Parameterscompliance.ediscovery.cases.reviewSetsListQueries)|Not Found|
|[az compliance compliance-ediscovery-case-review-set show-query](#compliance.ediscovery.cases.reviewSetsGetQueries)|GetQueries|[Parameters](#Parameterscompliance.ediscovery.cases.reviewSetsGetQueries)|Not Found|
|[az compliance compliance-ediscovery-case-review-set update-query](#compliance.ediscovery.cases.reviewSetsUpdateQueries)|UpdateQueries|[Parameters](#Parameterscompliance.ediscovery.cases.reviewSetsUpdateQueries)|Not Found|


## COMMAND DETAILS

### group `az compliance compliance`
#### <a name="compliance.complianceUpdateCompliance">Command `az compliance compliance create`</a>

##### <a name="Parameterscompliance.complianceUpdateCompliance">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--cases**|array||cases|cases|

#### <a name="compliance.complianceGetCompliance">Command `az compliance compliance show-compliance`</a>

##### <a name="Parameterscompliance.complianceGetCompliance">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az compliance compliance`
#### <a name="complianceDeleteEdiscovery">Command `az compliance compliance delete-ediscovery`</a>

##### <a name="ParameterscomplianceDeleteEdiscovery">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="complianceGetEdiscovery">Command `az compliance compliance show-ediscovery`</a>

##### <a name="ParameterscomplianceGetEdiscovery">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="complianceUpdateEdiscovery">Command `az compliance compliance update-ediscovery`</a>

##### <a name="ParameterscomplianceUpdateEdiscovery">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--cases**|array||cases|cases|

### group `az compliance compliance-ediscovery`
#### <a name="compliance.ediscoveryCreateCases">Command `az compliance compliance-ediscovery create-case`</a>

##### <a name="Parameterscompliance.ediscoveryCreateCases">Parameters</a> 
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="compliance.ediscoveryDeleteCases">Command `az compliance compliance-ediscovery delete-case`</a>

##### <a name="Parameterscompliance.ediscoveryDeleteCases">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="compliance.ediscoveryListCases">Command `az compliance compliance-ediscovery list-case`</a>

##### <a name="Parameterscompliance.ediscoveryListCases">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscoveryGetCases">Command `az compliance compliance-ediscovery show-case`</a>

##### <a name="Parameterscompliance.ediscoveryGetCases">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscoveryUpdateCases">Command `az compliance compliance-ediscovery update-case`</a>

##### <a name="Parameterscompliance.ediscoveryUpdateCases">Parameters</a> 
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az compliance compliance-ediscovery-case`
#### <a name="compliance.ediscovery.casesclose">Command `az compliance compliance-ediscovery-case close`</a>

##### <a name="Parameterscompliance.ediscovery.casesclose">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|

#### <a name="compliance.ediscovery.casesCreateCustodians">Command `az compliance compliance-ediscovery-case create-custodian`</a>

##### <a name="Parameterscompliance.ediscovery.casesCreateCustodians">Parameters</a> 
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

#### <a name="compliance.ediscovery.casesCreateReviewSets">Command `az compliance compliance-ediscovery-case create-review-set`</a>

##### <a name="Parameterscompliance.ediscovery.casesCreateReviewSets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--queries**|array||queries|queries|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="compliance.ediscovery.casesDeleteCustodians">Command `az compliance compliance-ediscovery-case delete-custodian`</a>

##### <a name="Parameterscompliance.ediscovery.casesDeleteCustodians">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="compliance.ediscovery.casesDeleteReviewSets">Command `az compliance compliance-ediscovery-case delete-review-set`</a>

##### <a name="Parameterscompliance.ediscovery.casesDeleteReviewSets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="compliance.ediscovery.casesListCustodians">Command `az compliance compliance-ediscovery-case list-custodian`</a>

##### <a name="Parameterscompliance.ediscovery.casesListCustodians">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.casesListReviewSets">Command `az compliance compliance-ediscovery-case list-review-set`</a>

##### <a name="Parameterscompliance.ediscovery.casesListReviewSets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.casesreopen">Command `az compliance compliance-ediscovery-case reopen`</a>

##### <a name="Parameterscompliance.ediscovery.casesreopen">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|

#### <a name="compliance.ediscovery.casesGetCustodians">Command `az compliance compliance-ediscovery-case show-custodian`</a>

##### <a name="Parameterscompliance.ediscovery.casesGetCustodians">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.casesGetReviewSets">Command `az compliance compliance-ediscovery-case show-review-set`</a>

##### <a name="Parameterscompliance.ediscovery.casesGetReviewSets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.casesUpdateCustodians">Command `az compliance compliance-ediscovery-case update-custodian`</a>

##### <a name="Parameterscompliance.ediscovery.casesUpdateCustodians">Parameters</a> 
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

#### <a name="compliance.ediscovery.casesUpdateReviewSets">Command `az compliance compliance-ediscovery-case update-review-set`</a>

##### <a name="Parameterscompliance.ediscovery.casesUpdateReviewSets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--queries**|array||queries|queries|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

### group `az compliance compliance-ediscovery-case-custodian`
#### <a name="compliance.ediscovery.cases.custodiansactivate">Command `az compliance compliance-ediscovery-case-custodian activate`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansactivate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|

#### <a name="compliance.ediscovery.cases.custodiansCreateSiteSources">Command `az compliance compliance-ediscovery-case-custodian create-site-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansCreateSiteSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--site**|object|site|site|site|

#### <a name="compliance.ediscovery.cases.custodiansCreateUnifiedGroupSources">Command `az compliance compliance-ediscovery-case-custodian create-unified-group-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansCreateUnifiedGroupSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--included-sources**|choice||included_sources|includedSources|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|

#### <a name="compliance.ediscovery.cases.custodiansCreateUserSources">Command `az compliance compliance-ediscovery-case-custodian create-user-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansCreateUserSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--email**|string||email|email|
|**--included-sources**|choice||included_sources|includedSources|

#### <a name="compliance.ediscovery.cases.custodiansDeleteRefLastIndexOperation">Command `az compliance compliance-ediscovery-case-custodian delete-ref-last-index-operation`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansDeleteRefLastIndexOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="compliance.ediscovery.cases.custodiansDeleteSiteSources">Command `az compliance compliance-ediscovery-case-custodian delete-site-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansDeleteSiteSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="compliance.ediscovery.cases.custodiansDeleteUnifiedGroupSources">Command `az compliance compliance-ediscovery-case-custodian delete-unified-group-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansDeleteUnifiedGroupSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="compliance.ediscovery.cases.custodiansDeleteUserSources">Command `az compliance compliance-ediscovery-case-custodian delete-user-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansDeleteUserSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--user-source-id**|string|key: id of userSource|user_source_id|userSource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="compliance.ediscovery.cases.custodiansListSiteSources">Command `az compliance compliance-ediscovery-case-custodian list-site-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansListSiteSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.cases.custodiansListUnifiedGroupSources">Command `az compliance compliance-ediscovery-case-custodian list-unified-group-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansListUnifiedGroupSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.cases.custodiansListUserSources">Command `az compliance compliance-ediscovery-case-custodian list-user-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansListUserSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.cases.custodiansrelease">Command `az compliance compliance-ediscovery-case-custodian release`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansrelease">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|

#### <a name="compliance.ediscovery.cases.custodiansSetRefLastIndexOperation">Command `az compliance compliance-ediscovery-case-custodian set-ref-last-index-operation`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansSetRefLastIndexOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="compliance.ediscovery.cases.custodiansGetLastIndexOperation">Command `az compliance compliance-ediscovery-case-custodian show-last-index-operation`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansGetLastIndexOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.cases.custodiansGetRefLastIndexOperation">Command `az compliance compliance-ediscovery-case-custodian show-ref-last-index-operation`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansGetRefLastIndexOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|

#### <a name="compliance.ediscovery.cases.custodiansGetSiteSources">Command `az compliance compliance-ediscovery-case-custodian show-site-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansGetSiteSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.cases.custodiansGetUnifiedGroupSources">Command `az compliance compliance-ediscovery-case-custodian show-unified-group-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansGetUnifiedGroupSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.cases.custodiansGetUserSources">Command `az compliance compliance-ediscovery-case-custodian show-user-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansGetUserSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--user-source-id**|string|key: id of userSource|user_source_id|userSource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.cases.custodiansupdateIndex">Command `az compliance compliance-ediscovery-case-custodian update-index`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansupdateIndex">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|

#### <a name="compliance.ediscovery.cases.custodiansUpdateSiteSources">Command `az compliance compliance-ediscovery-case-custodian update-site-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansUpdateSiteSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--site**|object|site|site|site|

#### <a name="compliance.ediscovery.cases.custodiansUpdateUnifiedGroupSources">Command `az compliance compliance-ediscovery-case-custodian update-unified-group-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansUpdateUnifiedGroupSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--included-sources**|choice||included_sources|includedSources|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|

#### <a name="compliance.ediscovery.cases.custodiansUpdateUserSources">Command `az compliance compliance-ediscovery-case-custodian update-user-source`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodiansUpdateUserSources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--user-source-id**|string|key: id of userSource|user_source_id|userSource-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--email**|string||email|email|
|**--included-sources**|choice||included_sources|includedSources|

### group `az compliance compliance-ediscovery-case-custodian-site-source`
#### <a name="compliance.ediscovery.cases.custodians.siteSourcesDeleteRefSite">Command `az compliance compliance-ediscovery-case-custodian-site-source delete-ref-site`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodians.siteSourcesDeleteRefSite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="compliance.ediscovery.cases.custodians.siteSourcesSetRefSite">Command `az compliance compliance-ediscovery-case-custodian-site-source set-ref-site`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodians.siteSourcesSetRefSite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="compliance.ediscovery.cases.custodians.siteSourcesGetRefSite">Command `az compliance compliance-ediscovery-case-custodian-site-source show-ref-site`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodians.siteSourcesGetRefSite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|

#### <a name="compliance.ediscovery.cases.custodians.siteSourcesGetSite">Command `az compliance compliance-ediscovery-case-custodian-site-source show-site`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodians.siteSourcesGetSite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--site-source-id**|string|key: id of siteSource|site_source_id|siteSource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az compliance compliance-ediscovery-case-custodian-unified-group-source`
#### <a name="compliance.ediscovery.cases.custodians.unifiedGroupSourcesDeleteRefGroup">Command `az compliance compliance-ediscovery-case-custodian-unified-group-source delete-ref-group`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodians.unifiedGroupSourcesDeleteRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="compliance.ediscovery.cases.custodians.unifiedGroupSourcesSetRefGroup">Command `az compliance compliance-ediscovery-case-custodian-unified-group-source set-ref-group`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodians.unifiedGroupSourcesSetRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="compliance.ediscovery.cases.custodians.unifiedGroupSourcesGetGroup">Command `az compliance compliance-ediscovery-case-custodian-unified-group-source show-group`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodians.unifiedGroupSourcesGetGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.cases.custodians.unifiedGroupSourcesGetRefGroup">Command `az compliance compliance-ediscovery-case-custodian-unified-group-source show-ref-group`</a>

##### <a name="Parameterscompliance.ediscovery.cases.custodians.unifiedGroupSourcesGetRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--custodian-id**|string|key: id of custodian|custodian_id|custodian-id|
|**--unified-group-source-id**|string|key: id of unifiedGroupSource|unified_group_source_id|unifiedGroupSource-id|

### group `az compliance compliance-ediscovery-case-review-set`
#### <a name="compliance.ediscovery.cases.reviewSetsCreateQueries">Command `az compliance compliance-ediscovery-case-review-set create-query`</a>

##### <a name="Parameterscompliance.ediscovery.cases.reviewSetsCreateQueries">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--query**|string||query|query|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="compliance.ediscovery.cases.reviewSetsDeleteQueries">Command `az compliance compliance-ediscovery-case-review-set delete-query`</a>

##### <a name="Parameterscompliance.ediscovery.cases.reviewSetsDeleteQueries">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--review-set-query-id**|string|key: id of reviewSetQuery|review_set_query_id|reviewSetQuery-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="compliance.ediscovery.cases.reviewSetsListQueries">Command `az compliance compliance-ediscovery-case-review-set list-query`</a>

##### <a name="Parameterscompliance.ediscovery.cases.reviewSetsListQueries">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.cases.reviewSetsGetQueries">Command `az compliance compliance-ediscovery-case-review-set show-query`</a>

##### <a name="Parameterscompliance.ediscovery.cases.reviewSetsGetQueries">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ediscovery-case-id**|string|key: id of ediscoveryCase|ediscovery_case_id|ediscoveryCase-id|
|**--review-set-id**|string|key: id of reviewSet|review_set_id|reviewSet-id|
|**--review-set-query-id**|string|key: id of reviewSetQuery|review_set_query_id|reviewSetQuery-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="compliance.ediscovery.cases.reviewSetsUpdateQueries">Command `az compliance compliance-ediscovery-case-review-set update-query`</a>

##### <a name="Parameterscompliance.ediscovery.cases.reviewSetsUpdateQueries">Parameters</a> 
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
