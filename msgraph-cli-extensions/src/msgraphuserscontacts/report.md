# Azure CLI Module Creation Report

### msgraphuserscontacts user create-contact

create-contact a msgraphuserscontacts user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--body**|object|New navigation property|body|
### msgraphuserscontacts user create-contact-folder

create-contact-folder a msgraphuserscontacts user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--id**|string|Read-only.|id|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|
|**--display-name**|string|The folder's display name.|display_name|
|**--well-known-name**|string||well_known_name|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|
### msgraphuserscontacts user get-contact

get-contact a msgraphuserscontacts user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user get-contact-folder

get-contact-folder a msgraphuserscontacts user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user list-contact

list-contact a msgraphuserscontacts user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user list-contact-folder

list-contact-folder a msgraphuserscontacts user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user update

update a msgraphuserscontacts user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--body**|object|New navigation property values|body|
|**--id**|string|Read-only.|id|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|
|**--display-name**|string|The folder's display name.|display_name|
|**--well-known-name**|string||well_known_name|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|
### msgraphuserscontacts user-contact create-extension

create-extension a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--id**|string|Read-only.|id|
### msgraphuserscontacts user-contact create-multi-value-extended-property

create-multi-value-extended-property a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--id**|string|Read-only.|id|
|**--value**|array|A collection of property values.|value|
### msgraphuserscontacts user-contact create-single-value-extended-property

create-single-value-extended-property a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--id**|string|Read-only.|id|
|**--value**|string|A property value.|value|
### msgraphuserscontacts user-contact get-extension

get-extension a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--extension-id**|string|key: extension-id of extension|extension_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact get-multi-value-extended-property

get-multi-value-extended-property a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact get-photo

get-photo a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact get-single-value-extended-property

get-single-value-extended-property a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact list-extension

list-extension a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact list-multi-value-extended-property

list-multi-value-extended-property a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact list-single-value-extended-property

list-single-value-extended-property a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact update

update a msgraphuserscontacts user-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--extension-id**|string|key: extension-id of extension|extension_id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|
|**--id**|string|Read-only.|id|
|**--value**|array|A collection of property values.|value|
|**--height**|integer|The height of the photo. Read-only.|height|
|**--width**|integer|The width of the photo. Read-only.|width|
### msgraphuserscontacts user-contact-folder create-child-folder

create-child-folder a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--id**|string|Read-only.|id|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|
|**--display-name**|string|The folder's display name.|display_name|
|**--well-known-name**|string||well_known_name|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|
### msgraphuserscontacts user-contact-folder create-contact

create-contact a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--body**|object|New navigation property|body|
### msgraphuserscontacts user-contact-folder create-multi-value-extended-property

create-multi-value-extended-property a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--id**|string|Read-only.|id|
|**--value**|array|A collection of property values.|value|
### msgraphuserscontacts user-contact-folder create-single-value-extended-property

create-single-value-extended-property a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--id**|string|Read-only.|id|
|**--value**|string|A property value.|value|
### msgraphuserscontacts user-contact-folder get-child-folder

get-child-folder a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-folder-id1**|string|key: contactFolder-id of contactFolder|contact_folder_id1|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder get-contact

get-contact a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder get-multi-value-extended-property

get-multi-value-extended-property a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder get-single-value-extended-property

get-single-value-extended-property a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder list-child-folder

list-child-folder a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder list-contact

list-contact a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder list-multi-value-extended-property

list-multi-value-extended-property a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder list-single-value-extended-property

list-single-value-extended-property a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder update

update a msgraphuserscontacts user-contact-folder.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-folder-id1**|string|key: contactFolder-id of contactFolder|contact_folder_id1|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--body**|object|New navigation property values|body|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|
|**--id**|string|Read-only.|id|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|
|**--display-name**|string|The folder's display name.|display_name|
|**--well-known-name**|string||well_known_name|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|
|**--value**|array|A collection of property values.|value|
### msgraphuserscontacts user-contact-folder-contact create-extension

create-extension a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--id**|string|Read-only.|id|
### msgraphuserscontacts user-contact-folder-contact create-multi-value-extended-property

create-multi-value-extended-property a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--id**|string|Read-only.|id|
|**--value**|array|A collection of property values.|value|
### msgraphuserscontacts user-contact-folder-contact create-single-value-extended-property

create-single-value-extended-property a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--id**|string|Read-only.|id|
|**--value**|string|A property value.|value|
### msgraphuserscontacts user-contact-folder-contact get-extension

get-extension a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--extension-id**|string|key: extension-id of extension|extension_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder-contact get-multi-value-extended-property

get-multi-value-extended-property a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder-contact get-photo

get-photo a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder-contact get-single-value-extended-property

get-single-value-extended-property a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder-contact list-extension

list-extension a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder-contact list-multi-value-extended-property

list-multi-value-extended-property a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder-contact list-single-value-extended-property

list-single-value-extended-property a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--Sort**|array|Order items by property values|Sort|
|**--Property**|array|Select properties to be returned|Property|
|**--ExpandProperty**|array|Expand related entities|ExpandProperty|
### msgraphuserscontacts user-contact-folder-contact update

update a msgraphuserscontacts user-contact-folder-contact.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--user-id**|string|key: user-id of user|user_id|
|**--contact-folder-id**|string|key: contactFolder-id of contactFolder|contact_folder_id|
|**--contact-id**|string|key: contact-id of contact|contact_id|
|**--extension-id**|string|key: extension-id of extension|extension_id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|
|**--id**|string|Read-only.|id|
|**--value**|array|A collection of property values.|value|
|**--height**|integer|The height of the photo. Read-only.|height|
|**--width**|integer|The width of the photo. Read-only.|width|