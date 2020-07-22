# Azure CLI Module Creation Report

### places create-place

create-place a places.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|places|places.place|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-place|CreatePlace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--geo-coordinates**|object|outlookGeoCoordinates|geo_coordinates|geoCoordinates|
|**--phone**|string||phone|phone|
|**--address**|object|physicalAddress|address|address|

### places delete

delete a places.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|places|places.place|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePlace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--place-id**|string|key: place-id of place|place_id|place-id|
|**--if-match**|string|ETag|if_match|If-Match|

### places get-place

get-place a places.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|places|places.place|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-place|GetPlace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--place-id**|string|key: place-id of place|place_id|place-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### places list-place

list-place a places.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|places|places.place|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-place|ListPlace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### places update

update a places.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|places|places.place|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePlace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--place-id**|string|key: place-id of place|place_id|place-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--geo-coordinates**|object|outlookGeoCoordinates|geo_coordinates|geoCoordinates|
|**--phone**|string||phone|phone|
|**--address**|object|physicalAddress|address|address|
