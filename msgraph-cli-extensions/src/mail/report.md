# Azure CLI Module Creation Report

### mail user create-mail-folder

create-mail-folder a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

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

### mail user create-message

create-message a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-message|CreateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--body**|object|New navigation property|body|body|

### mail user get-inference-classification

get-inference-classification a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

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

### mail user get-mail-folder

get-mail-folder a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

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

### mail user get-message

get-message a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-message|GetMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user list-mail-folder

list-mail-folder a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

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

### mail user list-message

list-message a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-message|ListMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user update

update a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateMailFolders|
|update|UpdateMessages|
|update|UpdateInferenceClassification|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--body**|object|New navigation property values|body|body|
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
|**--overrides**|array|A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.|overrides|overrides|

### mail user-inference-classification create-override

create-override a mail user-inference-classification.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-inference-classification|users.inferenceClassification|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-override|CreateOverrides|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--classify-as**|choice|inferenceClassificationType|classify_as|classifyAs|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|

### mail user-inference-classification get-override

get-override a mail user-inference-classification.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-inference-classification|users.inferenceClassification|

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

### mail user-inference-classification list-override

list-override a mail user-inference-classification.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-inference-classification|users.inferenceClassification|

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

### mail user-inference-classification update

update a mail user-inference-classification.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-inference-classification|users.inferenceClassification|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateOverrides|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: inferenceClassificationOverride-id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--id**|string|Read-only.|id|id|
|**--classify-as**|choice|inferenceClassificationType|classify_as|classifyAs|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|

### mail user-mail-folder create-child-folder

create-child-folder a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder create-message

create-message a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder create-message-rule

create-message-rule a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder create-multi-value-extended-property

create-multi-value-extended-property a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### mail user-mail-folder create-single-value-extended-property

create-single-value-extended-property a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### mail user-mail-folder create-user-configuration

create-user-configuration a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder get-child-folder

get-child-folder a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder get-message

get-message a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder get-message-rule

get-message-rule a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder get-multi-value-extended-property

get-multi-value-extended-property a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder get-single-value-extended-property

get-single-value-extended-property a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder get-user-configuration

get-user-configuration a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder list-child-folder

list-child-folder a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder list-message

list-message a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder list-message-rule

list-message-rule a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder list-multi-value-extended-property

list-multi-value-extended-property a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder list-single-value-extended-property

list-single-value-extended-property a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder list-user-configuration

list-user-configuration a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder update

update a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateChildFolders|
|update|UpdateMessageRules|
|update|UpdateMessages|
|update|UpdateMultiValueExtendedProperties|
|update|UpdateSingleValueExtendedProperties|
|update|UpdateUserConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: mailFolder-id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--message-rule-id**|string|key: messageRule-id of messageRule|message_rule_id|messageRule-id|
|**--body**|object|New navigation property values|body|body|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--user-configuration-id**|string|key: userConfiguration-id of userConfiguration|user_configuration_id|userConfiguration-id|
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
|**--value**|array|A collection of property values.|value|value|
|**--binary-data**|byte-array||binary_data|binaryData|

### mail user-mail-folder-message create-attachment

create-attachment a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--size**|integer|The length of the attachment in bytes.|size|size|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|

### mail user-mail-folder-message create-extension

create-extension a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|

### mail user-mail-folder-message create-mention

create-mention a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-mention|CreateMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
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

### mail user-mail-folder-message create-multi-value-extended-property

create-multi-value-extended-property a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### mail user-mail-folder-message create-single-value-extended-property

create-single-value-extended-property a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### mail user-mail-folder-message get-attachment

get-attachment a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--attachment-id**|string|key: attachment-id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message get-extension

get-extension a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--extension-id**|string|key: extension-id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message get-mention

get-mention a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mention|GetMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--mention-id**|string|key: mention-id of mention|mention_id|mention-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message get-multi-value-extended-property

get-multi-value-extended-property a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message get-single-value-extended-property

get-single-value-extended-property a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message list-attachment

list-attachment a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message list-extension

list-extension a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message list-mention

list-mention a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-mention|ListMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message list-multi-value-extended-property

list-multi-value-extended-property a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message list-single-value-extended-property

list-single-value-extended-property a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: message-id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message update

update a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

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
|**--mail-folder-id**|string|key: mailFolder-id of mailFolder|mail_folder_id|mailFolder-id|
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

### mail user-message create-attachment

create-attachment a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message create-extension

create-extension a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message create-mention

create-mention a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message create-multi-value-extended-property

create-multi-value-extended-property a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message create-single-value-extended-property

create-single-value-extended-property a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message get-attachment

get-attachment a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message get-extension

get-extension a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message get-mention

get-mention a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message get-multi-value-extended-property

get-multi-value-extended-property a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message get-single-value-extended-property

get-single-value-extended-property a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message list-attachment

list-attachment a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message list-extension

list-extension a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message list-mention

list-mention a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message list-multi-value-extended-property

list-multi-value-extended-property a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message list-single-value-extended-property

list-single-value-extended-property a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message update

update a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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
