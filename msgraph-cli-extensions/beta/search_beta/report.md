# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az search_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az search_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az search external-external|external.external|[commands](#CommandsInexternal.external)|
|az search external|external|[commands](#CommandsInexternal)|
|az search search-entity|search.searchEntity|[commands](#CommandsInsearch.searchEntity)|
|az search search|search|[commands](#CommandsInsearch)|

## COMMANDS
### <a name="CommandsInexternal">Commands in `az search external` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az search external delete](#externalDeleteConnections)|DeleteConnections|[Parameters](#ParametersexternalDeleteConnections)|Not Found|
|[az search external create-connection](#externalCreateConnections)|CreateConnections|[Parameters](#ParametersexternalCreateConnections)|Not Found|
|[az search external list-connection](#externalListConnections)|ListConnections|[Parameters](#ParametersexternalListConnections)|Not Found|
|[az search external show-connection](#externalGetConnections)|GetConnections|[Parameters](#ParametersexternalGetConnections)|Not Found|
|[az search external update-connection](#externalUpdateConnections)|UpdateConnections|[Parameters](#ParametersexternalUpdateConnections)|Not Found|

### <a name="CommandsInexternal.external">Commands in `az search external-external` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az search external-external show-external](#external.externalGetExternal)|GetExternal|[Parameters](#Parametersexternal.externalGetExternal)|Not Found|
|[az search external-external update-external](#external.externalUpdateExternal)|UpdateExternal|[Parameters](#Parametersexternal.externalUpdateExternal)|Not Found|

### <a name="CommandsInsearch">Commands in `az search search` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az search search query](#searchquery)|query|[Parameters](#Parameterssearchquery)|Not Found|

### <a name="CommandsInsearch.searchEntity">Commands in `az search search-entity` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az search search-entity show-search-entity](#search.searchEntityGetSearchEntity)|GetSearchEntity|[Parameters](#Parameterssearch.searchEntityGetSearchEntity)|Not Found|
|[az search search-entity update-search-entity](#search.searchEntityUpdateSearchEntity)|UpdateSearchEntity|[Parameters](#Parameterssearch.searchEntityUpdateSearchEntity)|Not Found|


## COMMAND DETAILS

### group `az search external`
#### <a name="externalDeleteConnections">Command `az search external delete`</a>

##### <a name="ParametersexternalDeleteConnections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--external-connection-id**|string|key: id of externalConnection|external_connection_id|externalConnection-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="externalCreateConnections">Command `az search external create-connection`</a>

##### <a name="ParametersexternalCreateConnections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|configuration|configuration|configuration|
|**--description**|string||description|description|
|**--name**|string||name|name|
|**--state**|choice||state|state|
|**--groups**|array||groups|groups|
|**--items**|array||items|items|
|**--operations**|array||operations|operations|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--base-type**|string||base_type|baseType|
|**--properties**|array||properties|properties|

#### <a name="externalListConnections">Command `az search external list-connection`</a>

##### <a name="ParametersexternalListConnections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="externalGetConnections">Command `az search external show-connection`</a>

##### <a name="ParametersexternalGetConnections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--external-connection-id**|string|key: id of externalConnection|external_connection_id|externalConnection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="externalUpdateConnections">Command `az search external update-connection`</a>

##### <a name="ParametersexternalUpdateConnections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--external-connection-id**|string|key: id of externalConnection|external_connection_id|externalConnection-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|configuration|configuration|configuration|
|**--description**|string||description|description|
|**--name**|string||name|name|
|**--state**|choice||state|state|
|**--groups**|array||groups|groups|
|**--items**|array||items|items|
|**--operations**|array||operations|operations|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--base-type**|string||base_type|baseType|
|**--properties**|array||properties|properties|

### group `az search external-external`
#### <a name="external.externalGetExternal">Command `az search external-external show-external`</a>

##### <a name="Parametersexternal.externalGetExternal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="external.externalUpdateExternal">Command `az search external-external update-external`</a>

##### <a name="Parametersexternal.externalUpdateExternal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--connections**|array||connections|connections|

### group `az search search`
#### <a name="searchquery">Command `az search search query`</a>

##### <a name="Parameterssearchquery">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--requests**|array||requests|requests|

### group `az search search-entity`
#### <a name="search.searchEntityGetSearchEntity">Command `az search search-entity show-search-entity`</a>

##### <a name="Parameterssearch.searchEntityGetSearchEntity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="search.searchEntityUpdateSearchEntity">Command `az search search-entity update-search-entity`</a>

##### <a name="Parameterssearch.searchEntityUpdateSearchEntity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
