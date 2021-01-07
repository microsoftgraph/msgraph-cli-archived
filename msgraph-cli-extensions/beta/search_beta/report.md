# Azure CLI Module Creation Report

### search create-connection

create-connection a search.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|search|external|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-connection|CreateConnections|

#### Parameters
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
|**--schema-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--schema-base-type**|string||base_type|baseType|
|**--schema-properties**|array||properties|properties|

### search delete

delete a search.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|search|external|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteConnections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--external-connection-id**|string|key: id of externalConnection|external_connection_id|externalConnection-id|
|**--if-match**|string|ETag|if_match|If-Match|

### search get-connection

get-connection a search.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|search|external|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-connection|GetConnections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--external-connection-id**|string|key: id of externalConnection|external_connection_id|externalConnection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### search get-external

get-external a search.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|search|external.external|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-external|GetExternal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### search get-search-entity

get-search-entity a search.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|search|search.searchEntity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-search-entity|GetSearchEntity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### search list-connection

list-connection a search.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|search|external|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-connection|ListConnections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### search query

query a search.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|search|search|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|query|query|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--requests**|array||requests|requests|

### search update-connection

update-connection a search.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|search|external|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-connection|UpdateConnections|

#### Parameters
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
|**--schema-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--schema-base-type**|string||base_type|baseType|
|**--schema-properties**|array||properties|properties|

### search update-external

update-external a search.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|search|external.external|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-external|UpdateExternal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--connections**|array||connections|connections|

### search update-search-entity

update-search-entity a search.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|search|search.searchEntity|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-search-entity|UpdateSearchEntity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
