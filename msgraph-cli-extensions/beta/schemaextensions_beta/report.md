# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az schemaextensions_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az schemaextensions_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az schemaextensions schemaextensionsschemaextension|schemaExtensions.schemaExtension|[commands](#CommandsInschemaExtensions.schemaExtension)|

## COMMANDS
### <a name="CommandsInschemaExtensions.schemaExtension">Commands in `az schemaextensions schemaextensionsschemaextension` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az schemaextensions schemaextensionsschemaextension create-schema-extension](#schemaExtensions.schemaExtensionCreateSchemaExtension)|CreateSchemaExtension|[Parameters](#ParametersschemaExtensions.schemaExtensionCreateSchemaExtension)|Not Found|
|[az schemaextensions schemaextensionsschemaextension delete-schema-extension](#schemaExtensions.schemaExtensionDeleteSchemaExtension)|DeleteSchemaExtension|[Parameters](#ParametersschemaExtensions.schemaExtensionDeleteSchemaExtension)|Not Found|
|[az schemaextensions schemaextensionsschemaextension list-schema-extension](#schemaExtensions.schemaExtensionListSchemaExtension)|ListSchemaExtension|[Parameters](#ParametersschemaExtensions.schemaExtensionListSchemaExtension)|Not Found|
|[az schemaextensions schemaextensionsschemaextension show-schema-extension](#schemaExtensions.schemaExtensionGetSchemaExtension)|GetSchemaExtension|[Parameters](#ParametersschemaExtensions.schemaExtensionGetSchemaExtension)|Not Found|
|[az schemaextensions schemaextensionsschemaextension update-schema-extension](#schemaExtensions.schemaExtensionUpdateSchemaExtension)|UpdateSchemaExtension|[Parameters](#ParametersschemaExtensions.schemaExtensionUpdateSchemaExtension)|Not Found|


## COMMAND DETAILS

### group `az schemaextensions schemaextensionsschemaextension`
#### <a name="schemaExtensions.schemaExtensionCreateSchemaExtension">Command `az schemaextensions schemaextensionsschemaextension create-schema-extension`</a>

##### <a name="ParametersschemaExtensions.schemaExtensionCreateSchemaExtension">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Description for the schema extension.|description|description|
|**--owner**|string|The appId of the application that is the owner of the schema extension. This property can be supplied on creation, to set the owner.  If not supplied, then the calling application's appId will be set as the owner. In either case, the signed-in user must be the owner of the application. Once set, this property is read-only and cannot be changed.|owner|owner|
|**--properties**|array|The collection of property names and types that make up the schema extension definition.|properties|properties|
|**--status**|string|The lifecycle state of the schema extension. Possible states are InDevelopment, Available, and Deprecated. Automatically set to InDevelopment on creation. Schema extensions provides more information on the possible state transitions and behaviors.|status|status|
|**--target-types**|array|Set of Microsoft Graph types (that can support extensions) that the schema extension can be applied to. Select from contact, device, event, group, message, organization, post, or user.|target_types|targetTypes|

#### <a name="schemaExtensions.schemaExtensionDeleteSchemaExtension">Command `az schemaextensions schemaextensionsschemaextension delete-schema-extension`</a>

##### <a name="ParametersschemaExtensions.schemaExtensionDeleteSchemaExtension">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--schema-extension-id**|string|key: id of schemaExtension|schema_extension_id|schemaExtension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="schemaExtensions.schemaExtensionListSchemaExtension">Command `az schemaextensions schemaextensionsschemaextension list-schema-extension`</a>

##### <a name="ParametersschemaExtensions.schemaExtensionListSchemaExtension">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="schemaExtensions.schemaExtensionGetSchemaExtension">Command `az schemaextensions schemaextensionsschemaextension show-schema-extension`</a>

##### <a name="ParametersschemaExtensions.schemaExtensionGetSchemaExtension">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--schema-extension-id**|string|key: id of schemaExtension|schema_extension_id|schemaExtension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="schemaExtensions.schemaExtensionUpdateSchemaExtension">Command `az schemaextensions schemaextensionsschemaextension update-schema-extension`</a>

##### <a name="ParametersschemaExtensions.schemaExtensionUpdateSchemaExtension">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--schema-extension-id**|string|key: id of schemaExtension|schema_extension_id|schemaExtension-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Description for the schema extension.|description|description|
|**--owner**|string|The appId of the application that is the owner of the schema extension. This property can be supplied on creation, to set the owner.  If not supplied, then the calling application's appId will be set as the owner. In either case, the signed-in user must be the owner of the application. Once set, this property is read-only and cannot be changed.|owner|owner|
|**--properties**|array|The collection of property names and types that make up the schema extension definition.|properties|properties|
|**--status**|string|The lifecycle state of the schema extension. Possible states are InDevelopment, Available, and Deprecated. Automatically set to InDevelopment on creation. Schema extensions provides more information on the possible state transitions and behaviors.|status|status|
|**--target-types**|array|Set of Microsoft Graph types (that can support extensions) that the schema extension can be applied to. Select from contact, device, event, group, message, organization, post, or user.|target_types|targetTypes|
