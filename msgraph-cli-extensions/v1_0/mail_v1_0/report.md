# Azure CLI Module Creation Report

### mail create-attachment

create-attachment a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### mail create-child-folder

create-child-folder a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-child-folder|CreateChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--child-folder-count**|integer|The number of immediate child mailFolders in the current mailFolder.|child_folder_count|childFolderCount|
|**--display-name**|string|The mailFolder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The unique identifier for the mailFolder's parent mailFolder.|parent_folder_id|parentFolderId|
|**--total-item-count**|integer|The number of items in the mailFolder.|total_item_count|totalItemCount|
|**--unread-item-count**|integer|The number of items in the mailFolder marked as unread.|unread_item_count|unreadItemCount|
|**--child-folders**|array|The collection of child folders in the mailFolder.|child_folders|childFolders|
|**--message-rules**|array|The collection of rules that apply to the user's Inbox folder.|message_rules|messageRules|
|**--messages**|array|The collection of messages in the mailFolder.|messages|messages|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### mail create-extension

create-extension a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|

### mail create-mail-folder

create-mail-folder a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-mail-folder|CreateMailFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--child-folder-count**|integer|The number of immediate child mailFolders in the current mailFolder.|child_folder_count|childFolderCount|
|**--display-name**|string|The mailFolder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The unique identifier for the mailFolder's parent mailFolder.|parent_folder_id|parentFolderId|
|**--total-item-count**|integer|The number of items in the mailFolder.|total_item_count|totalItemCount|
|**--unread-item-count**|integer|The number of items in the mailFolder marked as unread.|unread_item_count|unreadItemCount|
|**--child-folders**|array|The collection of child folders in the mailFolder.|child_folders|childFolders|
|**--message-rules**|array|The collection of rules that apply to the user's Inbox folder.|message_rules|messageRules|
|**--messages**|array|The collection of messages in the mailFolder.|messages|messages|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### mail create-message

create-message a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-message|CreateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--body**|object|New navigation property|body|body|

### mail create-message-rule

create-message-rule a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-message-rule|CreateMessageRules|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--body**|object|New navigation property|body|body|

### mail create-multi-value-extended-property

create-multi-value-extended-property a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### mail create-override

create-override a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.inferenceClassification|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-override|CreateOverrides|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--classify-as**|choice||classify_as|classifyAs|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|

### mail create-single-value-extended-property

create-single-value-extended-property a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### mail delete

delete a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExtensions|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### mail get-attachment

get-attachment a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail get-child-folder

get-child-folder a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-child-folder|GetChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail get-extension

get-extension a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail get-inference-classification

get-inference-classification a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-inference-classification|GetInferenceClassification|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail get-mail-folder

get-mail-folder a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mail-folder|GetMailFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail get-message

get-message a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-message|GetMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail get-message-rule

get-message-rule a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-message-rule|GetMessageRules|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-rule-id**|string|key: id of messageRule|message_rule_id|messageRule-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail get-multi-value-extended-property

get-multi-value-extended-property a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail get-override

get-override a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.inferenceClassification|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-override|GetOverrides|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail get-single-value-extended-property

get-single-value-extended-property a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail list-attachment

list-attachment a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail list-child-folder

list-child-folder a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-child-folder|ListChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail list-extension

list-extension a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail list-mail-folder

list-mail-folder a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-mail-folder|ListMailFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail list-message

list-message a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-message|ListMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail list-message-rule

list-message-rule a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-message-rule|ListMessageRules|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail list-multi-value-extended-property

list-multi-value-extended-property a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail list-override

list-override a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.inferenceClassification|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-override|ListOverrides|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail list-single-value-extended-property

list-single-value-extended-property a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail update-attachment

update-attachment a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### mail update-child-folder

update-child-folder a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-child-folder|UpdateChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--id**|string|Read-only.|id|id|
|**--child-folder-count**|integer|The number of immediate child mailFolders in the current mailFolder.|child_folder_count|childFolderCount|
|**--display-name**|string|The mailFolder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The unique identifier for the mailFolder's parent mailFolder.|parent_folder_id|parentFolderId|
|**--total-item-count**|integer|The number of items in the mailFolder.|total_item_count|totalItemCount|
|**--unread-item-count**|integer|The number of items in the mailFolder marked as unread.|unread_item_count|unreadItemCount|
|**--child-folders**|array|The collection of child folders in the mailFolder.|child_folders|childFolders|
|**--message-rules**|array|The collection of rules that apply to the user's Inbox folder.|message_rules|messageRules|
|**--messages**|array|The collection of messages in the mailFolder.|messages|messages|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### mail update-extension

update-extension a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### mail update-inference-classification

update-inference-classification a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-inference-classification|UpdateInferenceClassification|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--overrides**|array|A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.|overrides|overrides|

### mail update-mail-folder

update-mail-folder a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-mail-folder|UpdateMailFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--child-folder-count**|integer|The number of immediate child mailFolders in the current mailFolder.|child_folder_count|childFolderCount|
|**--display-name**|string|The mailFolder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The unique identifier for the mailFolder's parent mailFolder.|parent_folder_id|parentFolderId|
|**--total-item-count**|integer|The number of items in the mailFolder.|total_item_count|totalItemCount|
|**--unread-item-count**|integer|The number of items in the mailFolder marked as unread.|unread_item_count|unreadItemCount|
|**--child-folders**|array|The collection of child folders in the mailFolder.|child_folders|childFolders|
|**--message-rules**|array|The collection of rules that apply to the user's Inbox folder.|message_rules|messageRules|
|**--messages**|array|The collection of messages in the mailFolder.|messages|messages|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### mail update-message

update-message a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-message|UpdateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--body**|object|New navigation property values|body|body|

### mail update-message-rule

update-message-rule a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-message-rule|UpdateMessageRules|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-rule-id**|string|key: id of messageRule|message_rule_id|messageRule-id|
|**--body**|object|New navigation property values|body|body|

### mail update-multi-value-extended-property

update-multi-value-extended-property a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### mail update-override

update-override a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.inferenceClassification|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-override|UpdateOverrides|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--id**|string|Read-only.|id|id|
|**--classify-as**|choice||classify_as|classifyAs|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|

### mail update-single-value-extended-property

update-single-value-extended-property a mail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|
