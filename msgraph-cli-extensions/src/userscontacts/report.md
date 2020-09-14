# Azure CLI Module Creation Report

### userscontacts create-child-folder

create-child-folder a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-child-folder|CreateChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|contactFolder-id|
|**--id**|string|Read-only.|id|id|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|

### userscontacts create-contact

create-contact a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-contact|CreateContacts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|contactFolder-id|
|**--body**|object|New navigation property|body|body|

### userscontacts create-contact-folder

create-contact-folder a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-contact-folder|CreateContactFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|

### userscontacts create-extension

create-extension a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|

### userscontacts create-multi-value-extended-property

create-multi-value-extended-property a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### userscontacts create-single-value-extended-property

create-single-value-extended-property a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### userscontacts get-child-folder

get-child-folder a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-child-folder|GetChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-folder-id1**|string|key: contactFolder-id of contactFolder|contact_folder_id1|contactFolder-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts get-contact

get-contact a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-contact|GetContacts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts get-contact-folder

get-contact-folder a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-contact-folder|GetContactFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|contactFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts get-extension

get-extension a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--extension-id**|string|key: extension-id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts get-multi-value-extended-property

get-multi-value-extended-property a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts get-photo

get-photo a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-photo|GetPhoto|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts get-single-value-extended-property

get-single-value-extended-property a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts list-child-folder

list-child-folder a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-child-folder|ListChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|contactFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts list-contact

list-contact a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-contact|ListContacts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|contactFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts list-contact-folder

list-contact-folder a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-contact-folder|ListContactFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts list-extension

list-extension a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts list-multi-value-extended-property

list-multi-value-extended-property a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts list-single-value-extended-property

list-single-value-extended-property a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userscontacts update-child-folder

update-child-folder a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-child-folder|UpdateChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-folder-id1**|string|key: contactFolder-id of contactFolder|contact_folder_id1|contactFolder-id1|
|**--id**|string|Read-only.|id|id|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|

### userscontacts update-contact

update-contact a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contactFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-contact|UpdateContacts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--body**|object|New navigation property values|body|body|

### userscontacts update-contact-folder

update-contact-folder a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-contact-folder|UpdateContactFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|contactFolder-id|
|**--id**|string|Read-only.|id|id|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|

### userscontacts update-extension

update-extension a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--extension-id**|string|key: extension-id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### userscontacts update-multi-value-extended-property

update-multi-value-extended-property a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### userscontacts update-photo

update-photo a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-photo|UpdatePhoto|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

### userscontacts update-single-value-extended-property

update-single-value-extended-property a userscontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userscontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--contact-id**|string|key: contact-id of contact|contact_id|contact-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|
