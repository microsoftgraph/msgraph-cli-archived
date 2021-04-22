# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az personalcontacts_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az personalcontacts_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az personalcontacts user|users|[commands](#CommandsInusers)|
|az personalcontacts user-contact-folder|users.contactFolders|[commands](#CommandsInusers.contactFolders)|
|az personalcontacts user-contact-folder-contact|users.contactFolders.contacts|[commands](#CommandsInusers.contactFolders.contacts)|
|az personalcontacts user-contact|users.contacts|[commands](#CommandsInusers.contacts)|

## COMMANDS
### <a name="CommandsInusers">Commands in `az personalcontacts user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az personalcontacts user create-contact](#usersCreateContacts)|CreateContacts|[Parameters](#ParametersusersCreateContacts)|Not Found|
|[az personalcontacts user create-contact-folder](#usersCreateContactFolders)|CreateContactFolders|[Parameters](#ParametersusersCreateContactFolders)|Not Found|
|[az personalcontacts user delete-contact](#usersDeleteContacts)|DeleteContacts|[Parameters](#ParametersusersDeleteContacts)|Not Found|
|[az personalcontacts user delete-contact-folder](#usersDeleteContactFolders)|DeleteContactFolders|[Parameters](#ParametersusersDeleteContactFolders)|Not Found|
|[az personalcontacts user list-contact](#usersListContacts)|ListContacts|[Parameters](#ParametersusersListContacts)|Not Found|
|[az personalcontacts user list-contact-folder](#usersListContactFolders)|ListContactFolders|[Parameters](#ParametersusersListContactFolders)|Not Found|
|[az personalcontacts user show-contact](#usersGetContacts)|GetContacts|[Parameters](#ParametersusersGetContacts)|Not Found|
|[az personalcontacts user show-contact-folder](#usersGetContactFolders)|GetContactFolders|[Parameters](#ParametersusersGetContactFolders)|Not Found|
|[az personalcontacts user update-contact](#usersUpdateContacts)|UpdateContacts|[Parameters](#ParametersusersUpdateContacts)|Not Found|
|[az personalcontacts user update-contact-folder](#usersUpdateContactFolders)|UpdateContactFolders|[Parameters](#ParametersusersUpdateContactFolders)|Not Found|

### <a name="CommandsInusers.contacts">Commands in `az personalcontacts user-contact` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az personalcontacts user-contact create-extension](#users.contactsCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.contactsCreateExtensions)|Not Found|
|[az personalcontacts user-contact create-multi-value-extended-property](#users.contactsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.contactsCreateMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact create-single-value-extended-property](#users.contactsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.contactsCreateSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact delete-extension](#users.contactsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.contactsDeleteExtensions)|Not Found|
|[az personalcontacts user-contact delete-multi-value-extended-property](#users.contactsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.contactsDeleteMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact delete-photo](#users.contactsDeletePhoto)|DeletePhoto|[Parameters](#Parametersusers.contactsDeletePhoto)|Not Found|
|[az personalcontacts user-contact delete-single-value-extended-property](#users.contactsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.contactsDeleteSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact list-extension](#users.contactsListExtensions)|ListExtensions|[Parameters](#Parametersusers.contactsListExtensions)|Not Found|
|[az personalcontacts user-contact list-multi-value-extended-property](#users.contactsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.contactsListMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact list-single-value-extended-property](#users.contactsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.contactsListSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact set-photo-content](#users.contactsSetPhotoContent)|SetPhotoContent|[Parameters](#Parametersusers.contactsSetPhotoContent)|Not Found|
|[az personalcontacts user-contact show-extension](#users.contactsGetExtensions)|GetExtensions|[Parameters](#Parametersusers.contactsGetExtensions)|Not Found|
|[az personalcontacts user-contact show-multi-value-extended-property](#users.contactsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.contactsGetMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact show-photo](#users.contactsGetPhoto)|GetPhoto|[Parameters](#Parametersusers.contactsGetPhoto)|Not Found|
|[az personalcontacts user-contact show-photo-content](#users.contactsGetPhotoContent)|GetPhotoContent|[Parameters](#Parametersusers.contactsGetPhotoContent)|Not Found|
|[az personalcontacts user-contact show-single-value-extended-property](#users.contactsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.contactsGetSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact update-extension](#users.contactsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.contactsUpdateExtensions)|Not Found|
|[az personalcontacts user-contact update-multi-value-extended-property](#users.contactsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.contactsUpdateMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact update-photo](#users.contactsUpdatePhoto)|UpdatePhoto|[Parameters](#Parametersusers.contactsUpdatePhoto)|Not Found|
|[az personalcontacts user-contact update-single-value-extended-property](#users.contactsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.contactsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.contactFolders">Commands in `az personalcontacts user-contact-folder` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az personalcontacts user-contact-folder create-child-folder](#users.contactFoldersCreateChildFolders)|CreateChildFolders|[Parameters](#Parametersusers.contactFoldersCreateChildFolders)|Not Found|
|[az personalcontacts user-contact-folder create-contact](#users.contactFoldersCreateContacts)|CreateContacts|[Parameters](#Parametersusers.contactFoldersCreateContacts)|Not Found|
|[az personalcontacts user-contact-folder create-multi-value-extended-property](#users.contactFoldersCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.contactFoldersCreateMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder create-single-value-extended-property](#users.contactFoldersCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.contactFoldersCreateSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder delete-child-folder](#users.contactFoldersDeleteChildFolders)|DeleteChildFolders|[Parameters](#Parametersusers.contactFoldersDeleteChildFolders)|Not Found|
|[az personalcontacts user-contact-folder delete-contact](#users.contactFoldersDeleteContacts)|DeleteContacts|[Parameters](#Parametersusers.contactFoldersDeleteContacts)|Not Found|
|[az personalcontacts user-contact-folder delete-multi-value-extended-property](#users.contactFoldersDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.contactFoldersDeleteMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder delete-single-value-extended-property](#users.contactFoldersDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.contactFoldersDeleteSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder list-child-folder](#users.contactFoldersListChildFolders)|ListChildFolders|[Parameters](#Parametersusers.contactFoldersListChildFolders)|Not Found|
|[az personalcontacts user-contact-folder list-contact](#users.contactFoldersListContacts)|ListContacts|[Parameters](#Parametersusers.contactFoldersListContacts)|Not Found|
|[az personalcontacts user-contact-folder list-multi-value-extended-property](#users.contactFoldersListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.contactFoldersListMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder list-single-value-extended-property](#users.contactFoldersListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.contactFoldersListSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder show-child-folder](#users.contactFoldersGetChildFolders)|GetChildFolders|[Parameters](#Parametersusers.contactFoldersGetChildFolders)|Not Found|
|[az personalcontacts user-contact-folder show-contact](#users.contactFoldersGetContacts)|GetContacts|[Parameters](#Parametersusers.contactFoldersGetContacts)|Not Found|
|[az personalcontacts user-contact-folder show-multi-value-extended-property](#users.contactFoldersGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.contactFoldersGetMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder show-single-value-extended-property](#users.contactFoldersGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.contactFoldersGetSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder update-child-folder](#users.contactFoldersUpdateChildFolders)|UpdateChildFolders|[Parameters](#Parametersusers.contactFoldersUpdateChildFolders)|Not Found|
|[az personalcontacts user-contact-folder update-contact](#users.contactFoldersUpdateContacts)|UpdateContacts|[Parameters](#Parametersusers.contactFoldersUpdateContacts)|Not Found|
|[az personalcontacts user-contact-folder update-multi-value-extended-property](#users.contactFoldersUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.contactFoldersUpdateMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder update-single-value-extended-property](#users.contactFoldersUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.contactFoldersUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.contactFolders.contacts">Commands in `az personalcontacts user-contact-folder-contact` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az personalcontacts user-contact-folder-contact create-extension](#users.contactFolders.contactsCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.contactFolders.contactsCreateExtensions)|Not Found|
|[az personalcontacts user-contact-folder-contact create-multi-value-extended-property](#users.contactFolders.contactsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.contactFolders.contactsCreateMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder-contact create-single-value-extended-property](#users.contactFolders.contactsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.contactFolders.contactsCreateSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder-contact delete-extension](#users.contactFolders.contactsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.contactFolders.contactsDeleteExtensions)|Not Found|
|[az personalcontacts user-contact-folder-contact delete-multi-value-extended-property](#users.contactFolders.contactsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.contactFolders.contactsDeleteMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder-contact delete-photo](#users.contactFolders.contactsDeletePhoto)|DeletePhoto|[Parameters](#Parametersusers.contactFolders.contactsDeletePhoto)|Not Found|
|[az personalcontacts user-contact-folder-contact delete-single-value-extended-property](#users.contactFolders.contactsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.contactFolders.contactsDeleteSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder-contact list-extension](#users.contactFolders.contactsListExtensions)|ListExtensions|[Parameters](#Parametersusers.contactFolders.contactsListExtensions)|Not Found|
|[az personalcontacts user-contact-folder-contact list-multi-value-extended-property](#users.contactFolders.contactsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.contactFolders.contactsListMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder-contact list-single-value-extended-property](#users.contactFolders.contactsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.contactFolders.contactsListSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder-contact set-photo-content](#users.contactFolders.contactsSetPhotoContent)|SetPhotoContent|[Parameters](#Parametersusers.contactFolders.contactsSetPhotoContent)|Not Found|
|[az personalcontacts user-contact-folder-contact show-extension](#users.contactFolders.contactsGetExtensions)|GetExtensions|[Parameters](#Parametersusers.contactFolders.contactsGetExtensions)|Not Found|
|[az personalcontacts user-contact-folder-contact show-multi-value-extended-property](#users.contactFolders.contactsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.contactFolders.contactsGetMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder-contact show-photo](#users.contactFolders.contactsGetPhoto)|GetPhoto|[Parameters](#Parametersusers.contactFolders.contactsGetPhoto)|Not Found|
|[az personalcontacts user-contact-folder-contact show-photo-content](#users.contactFolders.contactsGetPhotoContent)|GetPhotoContent|[Parameters](#Parametersusers.contactFolders.contactsGetPhotoContent)|Not Found|
|[az personalcontacts user-contact-folder-contact show-single-value-extended-property](#users.contactFolders.contactsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.contactFolders.contactsGetSingleValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder-contact update-extension](#users.contactFolders.contactsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.contactFolders.contactsUpdateExtensions)|Not Found|
|[az personalcontacts user-contact-folder-contact update-multi-value-extended-property](#users.contactFolders.contactsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.contactFolders.contactsUpdateMultiValueExtendedProperties)|Not Found|
|[az personalcontacts user-contact-folder-contact update-photo](#users.contactFolders.contactsUpdatePhoto)|UpdatePhoto|[Parameters](#Parametersusers.contactFolders.contactsUpdatePhoto)|Not Found|
|[az personalcontacts user-contact-folder-contact update-single-value-extended-property](#users.contactFolders.contactsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.contactFolders.contactsUpdateSingleValueExtendedProperties)|Not Found|


## COMMAND DETAILS

### group `az personalcontacts user`
#### <a name="usersCreateContacts">Command `az personalcontacts user create-contact`</a>

##### <a name="ParametersusersCreateContacts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assistant-name**|string|The name of the contact's assistant.|assistant_name|assistantName|
|**--birthday**|date-time|The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|birthday|birthday|
|**--children**|array|The names of the contact's children.|children|children|
|**--company-name**|string|The name of the contact's company.|company_name|companyName|
|**--department**|string|The contact's department.|department|department|
|**--display-name**|string|The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.|display_name|displayName|
|**--email-addresses**|array|The contact's email addresses.|email_addresses|emailAddresses|
|**--file-as**|string|The name the contact is filed under.|file_as|fileAs|
|**--gender**|string||gender|gender|
|**--generation**|string|The contact's generation.|generation|generation|
|**--given-name**|string|The contact's given name.|given_name|givenName|
|**--im-addresses**|array|The contact's instant messaging (IM) addresses.|im_addresses|imAddresses|
|**--initials**|string|The contact's initials.|initials|initials|
|**--is-favorite**|boolean||is_favorite|isFavorite|
|**--job-title**|string|The contact’s job title.|job_title|jobTitle|
|**--manager**|string|The name of the contact's manager.|manager|manager|
|**--middle-name**|string|The contact's middle name.|middle_name|middleName|
|**--nick-name**|string|The contact's nickname.|nick_name|nickName|
|**--office-location**|string|The location of the contact's office.|office_location|officeLocation|
|**--parent-folder-id**|string|The ID of the contact's parent folder.|parent_folder_id|parentFolderId|
|**--personal-notes**|string|The user's notes about the contact.|personal_notes|personalNotes|
|**--phones**|array||phones|phones|
|**--postal-addresses**|array||postal_addresses|postalAddresses|
|**--profession**|string|The contact's profession.|profession|profession|
|**--spouse-name**|string|The name of the contact's spouse/partner.|spouse_name|spouseName|
|**--surname**|string|The contact's surname.|surname|surname|
|**--title**|string|The contact's title.|title|title|
|**--websites**|array||websites|websites|
|**--wedding-anniversary**|date||wedding_anniversary|weddingAnniversary|
|**--yomi-company-name**|string|The phonetic Japanese company name of the contact.|yomi_company_name|yomiCompanyName|
|**--yomi-given-name**|string|The phonetic Japanese given name (first name) of the contact.|yomi_given_name|yomiGivenName|
|**--yomi-surname**|string|The phonetic Japanese surname (last name)  of the contact.|yomi_surname|yomiSurname|
|**--extensions**|array|The collection of open extensions defined for the contact. Read-only. Nullable.|extensions|extensions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contact. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--photo**|object|profilePhoto|photo|photo|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contact. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-status**|choice||flag_status|flagStatus|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

#### <a name="usersCreateContactFolders">Command `az personalcontacts user create-contact-folder`</a>

##### <a name="ParametersusersCreateContactFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="usersDeleteContacts">Command `az personalcontacts user delete-contact`</a>

##### <a name="ParametersusersDeleteContacts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteContactFolders">Command `az personalcontacts user delete-contact-folder`</a>

##### <a name="ParametersusersDeleteContactFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListContacts">Command `az personalcontacts user list-contact`</a>

##### <a name="ParametersusersListContacts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListContactFolders">Command `az personalcontacts user list-contact-folder`</a>

##### <a name="ParametersusersListContactFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetContacts">Command `az personalcontacts user show-contact`</a>

##### <a name="ParametersusersGetContacts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetContactFolders">Command `az personalcontacts user show-contact-folder`</a>

##### <a name="ParametersusersGetContactFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateContacts">Command `az personalcontacts user update-contact`</a>

##### <a name="ParametersusersUpdateContacts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assistant-name**|string|The name of the contact's assistant.|assistant_name|assistantName|
|**--birthday**|date-time|The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|birthday|birthday|
|**--children**|array|The names of the contact's children.|children|children|
|**--company-name**|string|The name of the contact's company.|company_name|companyName|
|**--department**|string|The contact's department.|department|department|
|**--display-name**|string|The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.|display_name|displayName|
|**--email-addresses**|array|The contact's email addresses.|email_addresses|emailAddresses|
|**--file-as**|string|The name the contact is filed under.|file_as|fileAs|
|**--gender**|string||gender|gender|
|**--generation**|string|The contact's generation.|generation|generation|
|**--given-name**|string|The contact's given name.|given_name|givenName|
|**--im-addresses**|array|The contact's instant messaging (IM) addresses.|im_addresses|imAddresses|
|**--initials**|string|The contact's initials.|initials|initials|
|**--is-favorite**|boolean||is_favorite|isFavorite|
|**--job-title**|string|The contact’s job title.|job_title|jobTitle|
|**--manager**|string|The name of the contact's manager.|manager|manager|
|**--middle-name**|string|The contact's middle name.|middle_name|middleName|
|**--nick-name**|string|The contact's nickname.|nick_name|nickName|
|**--office-location**|string|The location of the contact's office.|office_location|officeLocation|
|**--parent-folder-id**|string|The ID of the contact's parent folder.|parent_folder_id|parentFolderId|
|**--personal-notes**|string|The user's notes about the contact.|personal_notes|personalNotes|
|**--phones**|array||phones|phones|
|**--postal-addresses**|array||postal_addresses|postalAddresses|
|**--profession**|string|The contact's profession.|profession|profession|
|**--spouse-name**|string|The name of the contact's spouse/partner.|spouse_name|spouseName|
|**--surname**|string|The contact's surname.|surname|surname|
|**--title**|string|The contact's title.|title|title|
|**--websites**|array||websites|websites|
|**--wedding-anniversary**|date||wedding_anniversary|weddingAnniversary|
|**--yomi-company-name**|string|The phonetic Japanese company name of the contact.|yomi_company_name|yomiCompanyName|
|**--yomi-given-name**|string|The phonetic Japanese given name (first name) of the contact.|yomi_given_name|yomiGivenName|
|**--yomi-surname**|string|The phonetic Japanese surname (last name)  of the contact.|yomi_surname|yomiSurname|
|**--extensions**|array|The collection of open extensions defined for the contact. Read-only. Nullable.|extensions|extensions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contact. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--photo**|object|profilePhoto|photo|photo|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contact. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-status**|choice||flag_status|flagStatus|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

#### <a name="usersUpdateContactFolders">Command `az personalcontacts user update-contact-folder`</a>

##### <a name="ParametersusersUpdateContactFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### group `az personalcontacts user-contact`
#### <a name="users.contactsCreateExtensions">Command `az personalcontacts user-contact create-extension`</a>

##### <a name="Parametersusers.contactsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.contactsCreateMultiValueExtendedProperties">Command `az personalcontacts user-contact create-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.contactsCreateSingleValueExtendedProperties">Command `az personalcontacts user-contact create-single-value-extended-property`</a>

##### <a name="Parametersusers.contactsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.contactsDeleteExtensions">Command `az personalcontacts user-contact delete-extension`</a>

##### <a name="Parametersusers.contactsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactsDeleteMultiValueExtendedProperties">Command `az personalcontacts user-contact delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactsDeletePhoto">Command `az personalcontacts user-contact delete-photo`</a>

##### <a name="Parametersusers.contactsDeletePhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactsDeleteSingleValueExtendedProperties">Command `az personalcontacts user-contact delete-single-value-extended-property`</a>

##### <a name="Parametersusers.contactsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactsListExtensions">Command `az personalcontacts user-contact list-extension`</a>

##### <a name="Parametersusers.contactsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactsListMultiValueExtendedProperties">Command `az personalcontacts user-contact list-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactsListSingleValueExtendedProperties">Command `az personalcontacts user-contact list-single-value-extended-property`</a>

##### <a name="Parametersusers.contactsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactsSetPhotoContent">Command `az personalcontacts user-contact set-photo-content`</a>

##### <a name="Parametersusers.contactsSetPhotoContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--data**|binary|New media content.|data|data|

#### <a name="users.contactsGetExtensions">Command `az personalcontacts user-contact show-extension`</a>

##### <a name="Parametersusers.contactsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactsGetMultiValueExtendedProperties">Command `az personalcontacts user-contact show-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactsGetPhoto">Command `az personalcontacts user-contact show-photo`</a>

##### <a name="Parametersusers.contactsGetPhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactsGetPhotoContent">Command `az personalcontacts user-contact show-photo-content`</a>

##### <a name="Parametersusers.contactsGetPhotoContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|

#### <a name="users.contactsGetSingleValueExtendedProperties">Command `az personalcontacts user-contact show-single-value-extended-property`</a>

##### <a name="Parametersusers.contactsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactsUpdateExtensions">Command `az personalcontacts user-contact update-extension`</a>

##### <a name="Parametersusers.contactsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.contactsUpdateMultiValueExtendedProperties">Command `az personalcontacts user-contact update-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.contactsUpdatePhoto">Command `az personalcontacts user-contact update-photo`</a>

##### <a name="Parametersusers.contactsUpdatePhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

#### <a name="users.contactsUpdateSingleValueExtendedProperties">Command `az personalcontacts user-contact update-single-value-extended-property`</a>

##### <a name="Parametersusers.contactsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az personalcontacts user-contact-folder`
#### <a name="users.contactFoldersCreateChildFolders">Command `az personalcontacts user-contact-folder create-child-folder`</a>

##### <a name="Parametersusers.contactFoldersCreateChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.contactFoldersCreateContacts">Command `az personalcontacts user-contact-folder create-contact`</a>

##### <a name="Parametersusers.contactFoldersCreateContacts">Parameters</a> 
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
|**--children**|array|The names of the contact's children.|children|children|
|**--company-name**|string|The name of the contact's company.|company_name|companyName|
|**--department**|string|The contact's department.|department|department|
|**--display-name**|string|The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.|display_name|displayName|
|**--email-addresses**|array|The contact's email addresses.|email_addresses|emailAddresses|
|**--file-as**|string|The name the contact is filed under.|file_as|fileAs|
|**--gender**|string||gender|gender|
|**--generation**|string|The contact's generation.|generation|generation|
|**--given-name**|string|The contact's given name.|given_name|givenName|
|**--im-addresses**|array|The contact's instant messaging (IM) addresses.|im_addresses|imAddresses|
|**--initials**|string|The contact's initials.|initials|initials|
|**--is-favorite**|boolean||is_favorite|isFavorite|
|**--job-title**|string|The contact’s job title.|job_title|jobTitle|
|**--manager**|string|The name of the contact's manager.|manager|manager|
|**--middle-name**|string|The contact's middle name.|middle_name|middleName|
|**--nick-name**|string|The contact's nickname.|nick_name|nickName|
|**--office-location**|string|The location of the contact's office.|office_location|officeLocation|
|**--parent-folder-id**|string|The ID of the contact's parent folder.|parent_folder_id|parentFolderId|
|**--personal-notes**|string|The user's notes about the contact.|personal_notes|personalNotes|
|**--phones**|array||phones|phones|
|**--postal-addresses**|array||postal_addresses|postalAddresses|
|**--profession**|string|The contact's profession.|profession|profession|
|**--spouse-name**|string|The name of the contact's spouse/partner.|spouse_name|spouseName|
|**--surname**|string|The contact's surname.|surname|surname|
|**--title**|string|The contact's title.|title|title|
|**--websites**|array||websites|websites|
|**--wedding-anniversary**|date||wedding_anniversary|weddingAnniversary|
|**--yomi-company-name**|string|The phonetic Japanese company name of the contact.|yomi_company_name|yomiCompanyName|
|**--yomi-given-name**|string|The phonetic Japanese given name (first name) of the contact.|yomi_given_name|yomiGivenName|
|**--yomi-surname**|string|The phonetic Japanese surname (last name)  of the contact.|yomi_surname|yomiSurname|
|**--extensions**|array|The collection of open extensions defined for the contact. Read-only. Nullable.|extensions|extensions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contact. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--photo**|object|profilePhoto|photo|photo|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contact. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-status**|choice||flag_status|flagStatus|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

#### <a name="users.contactFoldersCreateMultiValueExtendedProperties">Command `az personalcontacts user-contact-folder create-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactFoldersCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.contactFoldersCreateSingleValueExtendedProperties">Command `az personalcontacts user-contact-folder create-single-value-extended-property`</a>

##### <a name="Parametersusers.contactFoldersCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.contactFoldersDeleteChildFolders">Command `az personalcontacts user-contact-folder delete-child-folder`</a>

##### <a name="Parametersusers.contactFoldersDeleteChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-folder-id1**|string|key: id of contactFolder|contact_folder_id1|contactFolder-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactFoldersDeleteContacts">Command `az personalcontacts user-contact-folder delete-contact`</a>

##### <a name="Parametersusers.contactFoldersDeleteContacts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactFoldersDeleteMultiValueExtendedProperties">Command `az personalcontacts user-contact-folder delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactFoldersDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactFoldersDeleteSingleValueExtendedProperties">Command `az personalcontacts user-contact-folder delete-single-value-extended-property`</a>

##### <a name="Parametersusers.contactFoldersDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactFoldersListChildFolders">Command `az personalcontacts user-contact-folder list-child-folder`</a>

##### <a name="Parametersusers.contactFoldersListChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFoldersListContacts">Command `az personalcontacts user-contact-folder list-contact`</a>

##### <a name="Parametersusers.contactFoldersListContacts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFoldersListMultiValueExtendedProperties">Command `az personalcontacts user-contact-folder list-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactFoldersListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFoldersListSingleValueExtendedProperties">Command `az personalcontacts user-contact-folder list-single-value-extended-property`</a>

##### <a name="Parametersusers.contactFoldersListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFoldersGetChildFolders">Command `az personalcontacts user-contact-folder show-child-folder`</a>

##### <a name="Parametersusers.contactFoldersGetChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-folder-id1**|string|key: id of contactFolder|contact_folder_id1|contactFolder-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFoldersGetContacts">Command `az personalcontacts user-contact-folder show-contact`</a>

##### <a name="Parametersusers.contactFoldersGetContacts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFoldersGetMultiValueExtendedProperties">Command `az personalcontacts user-contact-folder show-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactFoldersGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFoldersGetSingleValueExtendedProperties">Command `az personalcontacts user-contact-folder show-single-value-extended-property`</a>

##### <a name="Parametersusers.contactFoldersGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFoldersUpdateChildFolders">Command `az personalcontacts user-contact-folder update-child-folder`</a>

##### <a name="Parametersusers.contactFoldersUpdateChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-folder-id1**|string|key: id of contactFolder|contact_folder_id1|contactFolder-id1|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The folder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The ID of the folder's parent folder.|parent_folder_id|parentFolderId|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--child-folders**|array|The collection of child folders in the folder. Navigation property. Read-only. Nullable.|child_folders|childFolders|
|**--contacts**|array|The contacts in the folder. Navigation property. Read-only. Nullable.|contacts|contacts|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.contactFoldersUpdateContacts">Command `az personalcontacts user-contact-folder update-contact`</a>

##### <a name="Parametersusers.contactFoldersUpdateContacts">Parameters</a> 
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
|**--children**|array|The names of the contact's children.|children|children|
|**--company-name**|string|The name of the contact's company.|company_name|companyName|
|**--department**|string|The contact's department.|department|department|
|**--display-name**|string|The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.|display_name|displayName|
|**--email-addresses**|array|The contact's email addresses.|email_addresses|emailAddresses|
|**--file-as**|string|The name the contact is filed under.|file_as|fileAs|
|**--gender**|string||gender|gender|
|**--generation**|string|The contact's generation.|generation|generation|
|**--given-name**|string|The contact's given name.|given_name|givenName|
|**--im-addresses**|array|The contact's instant messaging (IM) addresses.|im_addresses|imAddresses|
|**--initials**|string|The contact's initials.|initials|initials|
|**--is-favorite**|boolean||is_favorite|isFavorite|
|**--job-title**|string|The contact’s job title.|job_title|jobTitle|
|**--manager**|string|The name of the contact's manager.|manager|manager|
|**--middle-name**|string|The contact's middle name.|middle_name|middleName|
|**--nick-name**|string|The contact's nickname.|nick_name|nickName|
|**--office-location**|string|The location of the contact's office.|office_location|officeLocation|
|**--parent-folder-id**|string|The ID of the contact's parent folder.|parent_folder_id|parentFolderId|
|**--personal-notes**|string|The user's notes about the contact.|personal_notes|personalNotes|
|**--phones**|array||phones|phones|
|**--postal-addresses**|array||postal_addresses|postalAddresses|
|**--profession**|string|The contact's profession.|profession|profession|
|**--spouse-name**|string|The name of the contact's spouse/partner.|spouse_name|spouseName|
|**--surname**|string|The contact's surname.|surname|surname|
|**--title**|string|The contact's title.|title|title|
|**--websites**|array||websites|websites|
|**--wedding-anniversary**|date||wedding_anniversary|weddingAnniversary|
|**--yomi-company-name**|string|The phonetic Japanese company name of the contact.|yomi_company_name|yomiCompanyName|
|**--yomi-given-name**|string|The phonetic Japanese given name (first name) of the contact.|yomi_given_name|yomiGivenName|
|**--yomi-surname**|string|The phonetic Japanese surname (last name)  of the contact.|yomi_surname|yomiSurname|
|**--extensions**|array|The collection of open extensions defined for the contact. Read-only. Nullable.|extensions|extensions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the contact. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--photo**|object|profilePhoto|photo|photo|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the contact. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-status**|choice||flag_status|flagStatus|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

#### <a name="users.contactFoldersUpdateMultiValueExtendedProperties">Command `az personalcontacts user-contact-folder update-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactFoldersUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.contactFoldersUpdateSingleValueExtendedProperties">Command `az personalcontacts user-contact-folder update-single-value-extended-property`</a>

##### <a name="Parametersusers.contactFoldersUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az personalcontacts user-contact-folder-contact`
#### <a name="users.contactFolders.contactsCreateExtensions">Command `az personalcontacts user-contact-folder-contact create-extension`</a>

##### <a name="Parametersusers.contactFolders.contactsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.contactFolders.contactsCreateMultiValueExtendedProperties">Command `az personalcontacts user-contact-folder-contact create-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactFolders.contactsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.contactFolders.contactsCreateSingleValueExtendedProperties">Command `az personalcontacts user-contact-folder-contact create-single-value-extended-property`</a>

##### <a name="Parametersusers.contactFolders.contactsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.contactFolders.contactsDeleteExtensions">Command `az personalcontacts user-contact-folder-contact delete-extension`</a>

##### <a name="Parametersusers.contactFolders.contactsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactFolders.contactsDeleteMultiValueExtendedProperties">Command `az personalcontacts user-contact-folder-contact delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactFolders.contactsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactFolders.contactsDeletePhoto">Command `az personalcontacts user-contact-folder-contact delete-photo`</a>

##### <a name="Parametersusers.contactFolders.contactsDeletePhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactFolders.contactsDeleteSingleValueExtendedProperties">Command `az personalcontacts user-contact-folder-contact delete-single-value-extended-property`</a>

##### <a name="Parametersusers.contactFolders.contactsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.contactFolders.contactsListExtensions">Command `az personalcontacts user-contact-folder-contact list-extension`</a>

##### <a name="Parametersusers.contactFolders.contactsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFolders.contactsListMultiValueExtendedProperties">Command `az personalcontacts user-contact-folder-contact list-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactFolders.contactsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFolders.contactsListSingleValueExtendedProperties">Command `az personalcontacts user-contact-folder-contact list-single-value-extended-property`</a>

##### <a name="Parametersusers.contactFolders.contactsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFolders.contactsSetPhotoContent">Command `az personalcontacts user-contact-folder-contact set-photo-content`</a>

##### <a name="Parametersusers.contactFolders.contactsSetPhotoContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--data**|binary|New media content.|data|data|

#### <a name="users.contactFolders.contactsGetExtensions">Command `az personalcontacts user-contact-folder-contact show-extension`</a>

##### <a name="Parametersusers.contactFolders.contactsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFolders.contactsGetMultiValueExtendedProperties">Command `az personalcontacts user-contact-folder-contact show-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactFolders.contactsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFolders.contactsGetPhoto">Command `az personalcontacts user-contact-folder-contact show-photo`</a>

##### <a name="Parametersusers.contactFolders.contactsGetPhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFolders.contactsGetPhotoContent">Command `az personalcontacts user-contact-folder-contact show-photo-content`</a>

##### <a name="Parametersusers.contactFolders.contactsGetPhotoContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|

#### <a name="users.contactFolders.contactsGetSingleValueExtendedProperties">Command `az personalcontacts user-contact-folder-contact show-single-value-extended-property`</a>

##### <a name="Parametersusers.contactFolders.contactsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.contactFolders.contactsUpdateExtensions">Command `az personalcontacts user-contact-folder-contact update-extension`</a>

##### <a name="Parametersusers.contactFolders.contactsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.contactFolders.contactsUpdateMultiValueExtendedProperties">Command `az personalcontacts user-contact-folder-contact update-multi-value-extended-property`</a>

##### <a name="Parametersusers.contactFolders.contactsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.contactFolders.contactsUpdatePhoto">Command `az personalcontacts user-contact-folder-contact update-photo`</a>

##### <a name="Parametersusers.contactFolders.contactsUpdatePhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

#### <a name="users.contactFolders.contactsUpdateSingleValueExtendedProperties">Command `az personalcontacts user-contact-folder-contact update-single-value-extended-property`</a>

##### <a name="Parametersusers.contactFolders.contactsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--contact-folder-id**|string|key: id of contactFolder|contact_folder_id|contactFolder-id|
|**--contact-id**|string|key: id of contact|contact_id|contact-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|
