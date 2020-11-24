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
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assistant-name**|string|The name of the contact's assistant.|assistant_name|assistantName|
|**--birthday**|date-time|The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|birthday|birthday|
|**--business-address**|object|physicalAddress|business_address|businessAddress|
|**--business-home-page**|string|The business home page of the contact.|business_home_page|businessHomePage|
|**--business-phones**|array|The contact's business phone numbers.|business_phones|businessPhones|
|**--children**|array|The names of the contact's children.|children|children|
|**--company-name**|string|The name of the contact's company.|company_name|companyName|
|**--department**|string|The contact's department.|department|department|
|**--display-name**|string|The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.|display_name|displayName|
|**--email-addresses**|array|The contact's email addresses.|email_addresses|emailAddresses|
|**--file-as**|string|The name the contact is filed under.|file_as|fileAs|
|**--generation**|string|The contact's generation.|generation|generation|
|**--given-name**|string|The contact's given name.|given_name|givenName|
|**--home-address**|object|physicalAddress|home_address|homeAddress|
|**--home-phones**|array|The contact's home phone numbers.|home_phones|homePhones|
|**--im-addresses**|array|The contact's instant messaging (IM) addresses.|im_addresses|imAddresses|
|**--initials**|string|The contact's initials.|initials|initials|
|**--job-title**|string|The contact’s job title.|job_title|jobTitle|
|**--manager**|string|The name of the contact's manager.|manager|manager|
|**--middle-name**|string|The contact's middle name.|middle_name|middleName|
|**--mobile-phone**|string|The contact's mobile phone number.|mobile_phone|mobilePhone|
|**--nick-name**|string|The contact's nickname.|nick_name|nickName|
|**--office-location**|string|The location of the contact's office.|office_location|officeLocation|
|**--other-address**|object|physicalAddress|other_address|otherAddress|
|**--parent-folder-id**|string|The ID of the contact's parent folder.|parent_folder_id|parentFolderId|
|**--personal-notes**|string|The user's notes about the contact.|personal_notes|personalNotes|
|**--profession**|string|The contact's profession.|profession|profession|
|**--spouse-name**|string|The name of the contact's spouse/partner.|spouse_name|spouseName|
|**--surname**|string|The contact's surname.|surname|surname|
|**--title**|string|The contact's title.|title|title|
|**--yomi-company-name**|string|The phonetic Japanese company name of the contact.|yomi_company_name|yomiCompanyName|
|**--yomi-given-name**|string|The phonetic Japanese given name (first name) of the contact.|yomi_given_name|yomiGivenName|
|**--yomi-surname**|string|The phonetic Japanese surname (last name)  of the contact.|yomi_surname|yomiSurname|
|**--extensions**|array|The collection of open extensions defined for the contact. Read-only. Nullable.|extensions|extensions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contact. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--photo**|object|profilePhoto|photo|photo|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contact. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

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

### personalcontacts get-photo-content

get-photo-content a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-photo-content|GetPhotoContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|

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

### personalcontacts set-photo-content

set-photo-content a personalcontacts.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|personalcontacts|users.contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-photo-content|SetPhotoContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--data**|binary|New media content.|data|data|

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
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assistant-name**|string|The name of the contact's assistant.|assistant_name|assistantName|
|**--birthday**|date-time|The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|birthday|birthday|
|**--business-address**|object|physicalAddress|business_address|businessAddress|
|**--business-home-page**|string|The business home page of the contact.|business_home_page|businessHomePage|
|**--business-phones**|array|The contact's business phone numbers.|business_phones|businessPhones|
|**--children**|array|The names of the contact's children.|children|children|
|**--company-name**|string|The name of the contact's company.|company_name|companyName|
|**--department**|string|The contact's department.|department|department|
|**--display-name**|string|The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.|display_name|displayName|
|**--email-addresses**|array|The contact's email addresses.|email_addresses|emailAddresses|
|**--file-as**|string|The name the contact is filed under.|file_as|fileAs|
|**--generation**|string|The contact's generation.|generation|generation|
|**--given-name**|string|The contact's given name.|given_name|givenName|
|**--home-address**|object|physicalAddress|home_address|homeAddress|
|**--home-phones**|array|The contact's home phone numbers.|home_phones|homePhones|
|**--im-addresses**|array|The contact's instant messaging (IM) addresses.|im_addresses|imAddresses|
|**--initials**|string|The contact's initials.|initials|initials|
|**--job-title**|string|The contact’s job title.|job_title|jobTitle|
|**--manager**|string|The name of the contact's manager.|manager|manager|
|**--middle-name**|string|The contact's middle name.|middle_name|middleName|
|**--mobile-phone**|string|The contact's mobile phone number.|mobile_phone|mobilePhone|
|**--nick-name**|string|The contact's nickname.|nick_name|nickName|
|**--office-location**|string|The location of the contact's office.|office_location|officeLocation|
|**--other-address**|object|physicalAddress|other_address|otherAddress|
|**--parent-folder-id**|string|The ID of the contact's parent folder.|parent_folder_id|parentFolderId|
|**--personal-notes**|string|The user's notes about the contact.|personal_notes|personalNotes|
|**--profession**|string|The contact's profession.|profession|profession|
|**--spouse-name**|string|The name of the contact's spouse/partner.|spouse_name|spouseName|
|**--surname**|string|The contact's surname.|surname|surname|
|**--title**|string|The contact's title.|title|title|
|**--yomi-company-name**|string|The phonetic Japanese company name of the contact.|yomi_company_name|yomiCompanyName|
|**--yomi-given-name**|string|The phonetic Japanese given name (first name) of the contact.|yomi_given_name|yomiGivenName|
|**--yomi-surname**|string|The phonetic Japanese surname (last name)  of the contact.|yomi_surname|yomiSurname|
|**--extensions**|array|The collection of open extensions defined for the contact. Read-only. Nullable.|extensions|extensions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contact. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--photo**|object|profilePhoto|photo|photo|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contact. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

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
