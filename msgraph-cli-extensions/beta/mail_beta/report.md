# Azure CLI Module Creation Report

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--inference-classification**|choice||inference_classification|inferenceClassification|
|**--internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--subject**|string|The subject of the message.|subject|subject|
|**--to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--unique-body**|object|itemBody|unique_body|uniqueBody|
|**--unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--mentions**|array||mentions|mentions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|
|**--mentions-preview-is-mentioned**|boolean||is_mentioned|isMentioned|
|**--from-email-address-address**|string|The email address of the person or entity.|microsoft_graph_email_address|address|
|**--from-email-address-name**|string|The display name of the person or entity.|microsoft_graph_email_address_name|name|
|**--flag-completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--flag-due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-flag-status**|choice||flag_status|flagStatus|
|**--flag-start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

### mail user createl-folder

createl-folder a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|createl-folder|CreateMailFolders|

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
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--child-folders**|array|The collection of child folders in the mailFolder.|child_folders|childFolders|
|**--message-rules**|array|The collection of rules that apply to the user's Inbox folder.|message_rules|messageRules|
|**--messages**|array|The collection of messages in the mailFolder.|messages|messages|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--user-configurations**|array||user_configurations|userConfigurations|

### mail user delete

delete a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteMailFolders|
|delete|DeleteMessages|
|delete|DeleteInferenceClassification|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--user-id**|string|key: id of user|user_id|user-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user get-message-content

get-message-content a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-message-content|GetMessagesContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|

### mail user getl-folder

getl-folder a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|getl-folder|GetMailFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user listl-folder

listl-folder a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|listl-folder|ListMailFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user set-message-content

set-message-content a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-message-content|SetMessagesContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--data**|binary|New media content.|data|data|

### mail user update-inference-classification

update-inference-classification a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

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

### mail user update-message

update-message a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-message|UpdateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--inference-classification**|choice||inference_classification|inferenceClassification|
|**--internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--subject**|string|The subject of the message.|subject|subject|
|**--to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--unique-body**|object|itemBody|unique_body|uniqueBody|
|**--unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--mentions**|array||mentions|mentions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|
|**--mentions-preview-is-mentioned**|boolean||is_mentioned|isMentioned|
|**--from-email-address-address**|string|The email address of the person or entity.|microsoft_graph_email_address|address|
|**--from-email-address-name**|string|The display name of the person or entity.|microsoft_graph_email_address_name|name|
|**--flag-completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--flag-due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-flag-status**|choice||flag_status|flagStatus|
|**--flag-start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

### mail user updatel-folder

updatel-folder a mail user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|updatel-folder|UpdateMailFolders|

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
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--child-folders**|array|The collection of child folders in the mailFolder.|child_folders|childFolders|
|**--message-rules**|array|The collection of rules that apply to the user's Inbox folder.|message_rules|messageRules|
|**--messages**|array|The collection of messages in the mailFolder.|messages|messages|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--user-configurations**|array||user_configurations|userConfigurations|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--classify-as**|choice||classify_as|classifyAs|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|

### mail user-inference-classification delete

delete a mail user-inference-classification.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-inference-classification|users.inferenceClassification|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteOverrides|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-inference-classification update-override

update-override a mail user-inference-classification.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-inference-classification|users.inferenceClassification|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--child-folder-count**|integer|The number of immediate child mailFolders in the current mailFolder.|child_folder_count|childFolderCount|
|**--display-name**|string|The mailFolder's display name.|display_name|displayName|
|**--parent-folder-id**|string|The unique identifier for the mailFolder's parent mailFolder.|parent_folder_id|parentFolderId|
|**--total-item-count**|integer|The number of items in the mailFolder.|total_item_count|totalItemCount|
|**--unread-item-count**|integer|The number of items in the mailFolder marked as unread.|unread_item_count|unreadItemCount|
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--child-folders**|array|The collection of child folders in the mailFolder.|child_folders|childFolders|
|**--message-rules**|array|The collection of rules that apply to the user's Inbox folder.|message_rules|messageRules|
|**--messages**|array|The collection of messages in the mailFolder.|messages|messages|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--inference-classification**|choice||inference_classification|inferenceClassification|
|**--internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--subject**|string|The subject of the message.|subject|subject|
|**--to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--unique-body**|object|itemBody|unique_body|uniqueBody|
|**--unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--mentions**|array||mentions|mentions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|
|**--mentions-preview-is-mentioned**|boolean||is_mentioned|isMentioned|
|**--from-email-address-address**|string|The email address of the person or entity.|microsoft_graph_email_address|address|
|**--from-email-address-name**|string|The display name of the person or entity.|microsoft_graph_email_address_name|name|
|**--flag-completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--flag-due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-flag-status**|choice||flag_status|flagStatus|
|**--flag-start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--binary-data**|byte-array||binary_data|binaryData|

### mail user-mail-folder delete

delete a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteChildFolders|
|delete|DeleteMessageRules|
|delete|DeleteMessages|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteUserConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--message-rule-id**|string|key: id of messageRule|message_rule_id|messageRule-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--user-configuration-id**|string|key: id of userConfiguration|user_configuration_id|userConfiguration-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: id of mailFolder|mail_folder_id1|mailFolder-id1|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder get-message-content

get-message-content a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-message-content|GetMessagesContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-rule-id**|string|key: id of messageRule|message_rule_id|messageRule-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--user-configuration-id**|string|key: id of userConfiguration|user_configuration_id|userConfiguration-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder set-message-content

set-message-content a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-message-content|SetMessagesContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--data**|binary|New media content.|data|data|

### mail user-mail-folder update-child-folder

update-child-folder a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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
|**--well-known-name**|string||well_known_name|wellKnownName|
|**--child-folders**|array|The collection of child folders in the mailFolder.|child_folders|childFolders|
|**--message-rules**|array|The collection of rules that apply to the user's Inbox folder.|message_rules|messageRules|
|**--messages**|array|The collection of messages in the mailFolder.|messages|messages|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--user-configurations**|array||user_configurations|userConfigurations|

### mail user-mail-folder update-message

update-message a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--inference-classification**|choice||inference_classification|inferenceClassification|
|**--internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--subject**|string|The subject of the message.|subject|subject|
|**--to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--unique-body**|object|itemBody|unique_body|uniqueBody|
|**--unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--mentions**|array||mentions|mentions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|
|**--mentions-preview-is-mentioned**|boolean||is_mentioned|isMentioned|
|**--from-email-address-address**|string|The email address of the person or entity.|microsoft_graph_email_address|address|
|**--from-email-address-name**|string|The display name of the person or entity.|microsoft_graph_email_address_name|name|
|**--flag-completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--flag-due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-flag-status**|choice||flag_status|flagStatus|
|**--flag-start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

### mail user-mail-folder update-message-rule

update-message-rule a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

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

### mail user-mail-folder update-multi-value-extended-property

update-multi-value-extended-property a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### mail user-mail-folder update-single-value-extended-property

update-single-value-extended-property a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### mail user-mail-folder update-user-configuration

update-user-configuration a mail user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user-configuration|UpdateUserConfigurations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--user-configuration-id**|string|key: id of userConfiguration|user_configuration_id|userConfiguration-id|
|**--id**|string|Read-only.|id|id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--application**|string||application|application|
|**--client-reference**|string||client_reference|clientReference|
|**--created-by**|object|emailAddress|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--deep-link**|string||deep_link|deepLink|
|**--mentioned**|object|emailAddress|mentioned|mentioned|
|**--mention-text**|string||mention_text|mentionText|
|**--server-created-date-time**|date-time||server_created_date_time|serverCreatedDateTime|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### mail user-mail-folder-message delete

delete a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExtensions|
|delete|DeleteMentions|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--mention-id**|string|key: id of mention|mention_id|mention-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--mention-id**|string|key: id of mention|mention_id|mention-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-mail-folder-message update-attachment

update-attachment a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### mail user-mail-folder-message update-extension

update-extension a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### mail user-mail-folder-message update-mention

update-mention a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-mention|UpdateMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--mention-id**|string|key: id of mention|mention_id|mention-id|
|**--id**|string|Read-only.|id|id|
|**--application**|string||application|application|
|**--client-reference**|string||client_reference|clientReference|
|**--created-by**|object|emailAddress|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--deep-link**|string||deep_link|deepLink|
|**--mentioned**|object|emailAddress|mentioned|mentioned|
|**--mention-text**|string||mention_text|mentionText|
|**--server-created-date-time**|date-time||server_created_date_time|serverCreatedDateTime|

### mail user-mail-folder-message update-multi-value-extended-property

update-multi-value-extended-property a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### mail user-mail-folder-message update-single-value-extended-property

update-single-value-extended-property a mail user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--application**|string||application|application|
|**--client-reference**|string||client_reference|clientReference|
|**--created-by**|object|emailAddress|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--deep-link**|string||deep_link|deepLink|
|**--mentioned**|object|emailAddress|mentioned|mentioned|
|**--mention-text**|string||mention_text|mentionText|
|**--server-created-date-time**|date-time||server_created_date_time|serverCreatedDateTime|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### mail user-message delete

delete a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExtensions|
|delete|DeleteMentions|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--mention-id**|string|key: id of mention|mention_id|mention-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--mention-id**|string|key: id of mention|mention_id|mention-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
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
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### mail user-message update-attachment

update-attachment a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message update-extension

update-extension a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message update-mention

update-mention a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-mention|UpdateMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--mention-id**|string|key: id of mention|mention_id|mention-id|
|**--id**|string|Read-only.|id|id|
|**--application**|string||application|application|
|**--client-reference**|string||client_reference|clientReference|
|**--created-by**|object|emailAddress|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--deep-link**|string||deep_link|deepLink|
|**--mentioned**|object|emailAddress|mentioned|mentioned|
|**--mention-text**|string||mention_text|mentionText|
|**--server-created-date-time**|date-time||server_created_date_time|serverCreatedDateTime|

### mail user-message update-multi-value-extended-property

update-multi-value-extended-property a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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

### mail user-message update-single-value-extended-property

update-single-value-extended-property a mail user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|mail user-message|users.messages|

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
