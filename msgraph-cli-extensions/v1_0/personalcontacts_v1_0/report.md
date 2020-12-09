# Azure CLI Module Creation Report

### personalcontacts create-child-folder

create-child-folder a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-child-folder|CreateChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### personalcontacts create-contact

create-contact a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-contact|CreateContacts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--body**|object|New navigation property|body|body|

### personalcontacts create-contact-folder

create-contact-folder a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-contact-folder|CreateContactFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### personalcontacts create-extension

create-extension a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|

### personalcontacts create-multi-value-extended-property

create-multi-value-extended-property a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### personalcontacts create-single-value-extended-property

create-single-value-extended-property a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### personalcontacts delete

delete a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensions|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeletePhoto|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### personalcontacts get-child-folder

get-child-folder a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-child-folder|GetChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-folder-id1**|string|key: id of contactFolder|contact_folder_id1|contactFolder-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts get-contact

get-contact a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-contact|GetContacts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts get-contact-folder

get-contact-folder a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-contact-folder|GetContactFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts get-extension

get-extension a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts get-multi-value-extended-property

get-multi-value-extended-property a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts get-photo

get-photo a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-photo|GetPhoto|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts get-single-value-extended-property

get-single-value-extended-property a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts list-child-folder

list-child-folder a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-child-folder|ListChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts list-contact

list-contact a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-contact|ListContacts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts list-contact-folder

list-contact-folder a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-contact-folder|ListContactFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts list-extension

list-extension a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts list-multi-value-extended-property

list-multi-value-extended-property a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts list-single-value-extended-property

list-single-value-extended-property a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### personalcontacts update-child-folder

update-child-folder a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-child-folder|UpdateChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-folder-id1**|string|key: id of contactFolder|contact_folder_id1|contactFolder-id1|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### personalcontacts update-contact

update-contact a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-contact|UpdateContacts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--body**|object|New navigation property values|body|body|

### personalcontacts update-contact-folder

update-contact-folder a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-contact-folder|UpdateContactFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### personalcontacts update-extension

update-extension a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### personalcontacts update-multi-value-extended-property

update-multi-value-extended-property a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### personalcontacts update-photo

update-photo a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-photo|UpdatePhoto|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

### personalcontacts update-single-value-extended-property

update-single-value-extended-property a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|
