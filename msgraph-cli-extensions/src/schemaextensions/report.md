# Azure CLI Module Creation Report

### schemaextensions create-schema-extension

create-schema-extension a schemaextensions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|schemaextensions|schemaExtensions.schemaExtension|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-schema-extension|CreateSchemaExtension|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Description for the schema extension.|description|description|
|**--owner**|string|The appId of the application that is the owner of the schema extension. This property can be supplied on creation, to set the owner.  If not supplied, then the calling application's appId will be set as the owner. In either case, the signed-in user must be the owner of the application. Once set, this property is read-only and cannot be changed.|owner|owner|
|**--properties**|array|The collection of property names and types that make up the schema extension definition.|properties|properties|
|**--status**|string|The lifecycle state of the schema extension. Possible states are InDevelopment, Available, and Deprecated. Automatically set to InDevelopment on creation. Schema extensions provides more information on the possible state transitions and behaviors.|status|status|
|**--target-types**|array|Set of Microsoft Graph types (that can support extensions) that the schema extension can be applied to. Select from contact, device, event, group, message, organization, post, or user.|target_types|targetTypes|

### schemaextensions delete

delete a schemaextensions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|schemaextensions|schemaExtensions.schemaExtension|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSchemaExtension|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--schema-extension-id**|string|key: id of schemaExtension|schema_extension_id|schemaExtension-id|
|**--if-match**|string|ETag|if_match|If-Match|

### schemaextensions get-schema-extension

get-schema-extension a schemaextensions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|schemaextensions|schemaExtensions.schemaExtension|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schema-extension|GetSchemaExtension|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--schema-extension-id**|string|key: id of schemaExtension|schema_extension_id|schemaExtension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### schemaextensions list-schema-extension

list-schema-extension a schemaextensions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|schemaextensions|schemaExtensions.schemaExtension|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-schema-extension|ListSchemaExtension|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### schemaextensions update-schema-extension

update-schema-extension a schemaextensions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|schemaextensions|schemaExtensions.schemaExtension|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-schema-extension|UpdateSchemaExtension|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--schema-extension-id**|string|key: id of schemaExtension|schema_extension_id|schemaExtension-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Description for the schema extension.|description|description|
|**--owner**|string|The appId of the application that is the owner of the schema extension. This property can be supplied on creation, to set the owner.  If not supplied, then the calling application's appId will be set as the owner. In either case, the signed-in user must be the owner of the application. Once set, this property is read-only and cannot be changed.|owner|owner|
|**--properties**|array|The collection of property names and types that make up the schema extension definition.|properties|properties|
|**--status**|string|The lifecycle state of the schema extension. Possible states are InDevelopment, Available, and Deprecated. Automatically set to InDevelopment on creation. Schema extensions provides more information on the possible state transitions and behaviors.|status|status|
|**--target-types**|array|Set of Microsoft Graph types (that can support extensions) that the schema extension can be applied to. Select from contact, device, event, group, message, organization, post, or user.|target_types|targetTypes|
