# Azure CLI Module Creation Report

### usersmail create-attachment

create-attachment a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--size**|integer|The length of the attachment in bytes.|size|size|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|

### usersmail create-child-folder

create-child-folder a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-child-folder|CreateChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The mailFolder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The unique identifier for the mailFolder's parent mailFolder.|parent_folder_id|parentFolderId|
|**--child-folder-count**|integer|The number of immediate child mailFolders in the current mailFolder.|child_folder_count|childFolderCount|
|**--unread-item-count**|integer|The number of items in the mailFolder marked as unread.|unread_item_count|unreadItemCount|
|**--total-item-count**|integer|The number of items in the mailFolder.|total_item_count|totalItemCount|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--messages**|array|The collection of messages in the mailFolder.|messages|messages|
|**--message-rules**|array|The collection of rules that apply to the user's Inbox folder.|message_rules|messageRules|
|**--child-folders**|array|The collection of child folders in the mailFolder.|child_folders|childFolders|
|**--user-configurations**|array||user_configurations|userConfigurations|

### usersmail create-extension

create-extension a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|

### usersmail create-mail-folder

create-mail-folder a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-mail-folder|CreateMailFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The mailFolder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The unique identifier for the mailFolder's parent mailFolder.|parent_folder_id|parentFolderId|
|**--child-folder-count**|integer|The number of immediate child mailFolders in the current mailFolder.|child_folder_count|childFolderCount|
|**--unread-item-count**|integer|The number of items in the mailFolder marked as unread.|unread_item_count|unreadItemCount|
|**--total-item-count**|integer|The number of items in the mailFolder.|total_item_count|totalItemCount|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--messages**|array|The collection of messages in the mailFolder.|messages|messages|
|**--message-rules**|array|The collection of rules that apply to the user's Inbox folder.|message_rules|messageRules|
|**--child-folders**|array|The collection of child folders in the mailFolder.|child_folders|childFolders|
|**--user-configurations**|array||user_configurations|userConfigurations|

### usersmail create-mention

create-mention a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-mention|CreateMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--mentioned**|object|emailAddress|mentioned|mentioned|
|**--mention-text**|string||mention_text|mentionText|
|**--client-reference**|string||client_reference|clientReference|
|**--created-by**|object|emailAddress|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--server-created-date-time**|date-time||server_created_date_time|serverCreatedDateTime|
|**--deep-link**|string||deep_link|deepLink|
|**--application**|string||application|application|

### usersmail create-message

create-message a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-message|CreateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--body**|object|New navigation property|body|body|

### usersmail create-message-rule

create-message-rule a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-message-rule|CreateMessageRules|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--body**|object|New navigation property|body|body|

### usersmail create-multi-value-extended-property

create-multi-value-extended-property a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### usersmail create-override

create-override a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.inferenceClassification|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-override|CreateOverrides|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--classify-as**|choice||classify_as|classifyAs|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|

### usersmail create-single-value-extended-property

create-single-value-extended-property a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### usersmail create-user-configuration

create-user-configuration a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user-configuration|CreateUserConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--binary-data**|byte-array||binary_data|binaryData|

### usersmail get-attachment

get-attachment a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--attachment-id**|string|key: attachment-id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-child-folder

get-child-folder a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-child-folder|GetChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: mailFolder-id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-extension

get-extension a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--extension-id**|string|key: extension-id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-inference-classification

get-inference-classification a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-inference-classification|GetInferenceClassification|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-mail-folder

get-mail-folder a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mail-folder|GetMailFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-mention

get-mention a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mention|GetMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--mention-id**|string|key: mention-id of mention|mention_id|mention-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-message

get-message a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-message|GetMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-message-rule

get-message-rule a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-message-rule|GetMessageRules|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-rule-id**|string|key: messageRule-id of messageRule|message_rule_id|messageRule-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-multi-value-extended-property

get-multi-value-extended-property a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-override

get-override a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.inferenceClassification|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-override|GetOverrides|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: inferenceClassificationOverride-id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-single-value-extended-property

get-single-value-extended-property a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail get-user-configuration

get-user-configuration a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-configuration|GetUserConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--user-configuration-id**|string|key: userConfiguration-id of userConfiguration|user_configuration_id|userConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-attachment

list-attachment a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-child-folder

list-child-folder a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-child-folder|ListChildFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-extension

list-extension a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-mail-folder

list-mail-folder a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-mail-folder|ListMailFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-mention

list-mention a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-mention|ListMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-message

list-message a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-message|ListMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-message-rule

list-message-rule a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-message-rule|ListMessageRules|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-multi-value-extended-property

list-multi-value-extended-property a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-override

list-override a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.inferenceClassification|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-override|ListOverrides|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-single-value-extended-property

list-single-value-extended-property a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail list-user-configuration

list-user-configuration a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user-configuration|ListUserConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersmail update

update a usersmail.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersmail|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAttachments|
|update|UpdateExtensions|
|update|UpdateMentions|
|update|UpdateMultiValueExtendedProperties|
|update|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--attachment-id**|string|key: attachment-id of attachment|attachment_id|attachment-id|
|**--extension-id**|string|key: extension-id of extension|extension_id|extension-id|
|**--mention-id**|string|key: mention-id of mention|mention_id|mention-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--size**|integer|The length of the attachment in bytes.|size|size|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--mentioned**|object|emailAddress|mentioned|mentioned|
|**--mention-text**|string||mention_text|mentionText|
|**--client-reference**|string||client_reference|clientReference|
|**--created-by**|object|emailAddress|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--server-created-date-time**|date-time||server_created_date_time|serverCreatedDateTime|
|**--deep-link**|string||deep_link|deepLink|
|**--application**|string||application|application|
|**--value**|array|A collection of property values.|value|value|
