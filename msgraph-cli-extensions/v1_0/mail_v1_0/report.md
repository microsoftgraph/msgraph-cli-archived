# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az mail_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az mail_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az mail user|users|[commands](#CommandsInusers)|
|az mail user-inference-classification|users.inferenceClassification|[commands](#CommandsInusers.inferenceClassification)|
|az mail user-mail-folder|users.mailFolders|[commands](#CommandsInusers.mailFolders)|
|az mail user-mail-folder-message|users.mailFolders.messages|[commands](#CommandsInusers.mailFolders.messages)|
|az mail user-message|users.messages|[commands](#CommandsInusers.messages)|

## COMMANDS
### <a name="CommandsInusers">Commands in `az mail user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az mail user create-mail-folder](#usersCreateMailFolders)|CreateMailFolders|[Parameters](#ParametersusersCreateMailFolders)|Not Found|
|[az mail user create-message](#usersCreateMessages)|CreateMessages|[Parameters](#ParametersusersCreateMessages)|Not Found|
|[az mail user delete-inference-classification](#usersDeleteInferenceClassification)|DeleteInferenceClassification|[Parameters](#ParametersusersDeleteInferenceClassification)|Not Found|
|[az mail user delete-mail-folder](#usersDeleteMailFolders)|DeleteMailFolders|[Parameters](#ParametersusersDeleteMailFolders)|Not Found|
|[az mail user delete-message](#usersDeleteMessages)|DeleteMessages|[Parameters](#ParametersusersDeleteMessages)|Not Found|
|[az mail user list-mail-folder](#usersListMailFolders)|ListMailFolders|[Parameters](#ParametersusersListMailFolders)|Not Found|
|[az mail user list-message](#usersListMessages)|ListMessages|[Parameters](#ParametersusersListMessages)|Not Found|
|[az mail user show-inference-classification](#usersGetInferenceClassification)|GetInferenceClassification|[Parameters](#ParametersusersGetInferenceClassification)|Not Found|
|[az mail user show-mail-folder](#usersGetMailFolders)|GetMailFolders|[Parameters](#ParametersusersGetMailFolders)|Not Found|
|[az mail user show-message](#usersGetMessages)|GetMessages|[Parameters](#ParametersusersGetMessages)|Not Found|
|[az mail user update-inference-classification](#usersUpdateInferenceClassification)|UpdateInferenceClassification|[Parameters](#ParametersusersUpdateInferenceClassification)|Not Found|
|[az mail user update-mail-folder](#usersUpdateMailFolders)|UpdateMailFolders|[Parameters](#ParametersusersUpdateMailFolders)|Not Found|
|[az mail user update-message](#usersUpdateMessages)|UpdateMessages|[Parameters](#ParametersusersUpdateMessages)|Not Found|

### <a name="CommandsInusers.inferenceClassification">Commands in `az mail user-inference-classification` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az mail user-inference-classification create-override](#users.inferenceClassificationCreateOverrides)|CreateOverrides|[Parameters](#Parametersusers.inferenceClassificationCreateOverrides)|Not Found|
|[az mail user-inference-classification delete-override](#users.inferenceClassificationDeleteOverrides)|DeleteOverrides|[Parameters](#Parametersusers.inferenceClassificationDeleteOverrides)|Not Found|
|[az mail user-inference-classification list-override](#users.inferenceClassificationListOverrides)|ListOverrides|[Parameters](#Parametersusers.inferenceClassificationListOverrides)|Not Found|
|[az mail user-inference-classification show-override](#users.inferenceClassificationGetOverrides)|GetOverrides|[Parameters](#Parametersusers.inferenceClassificationGetOverrides)|Not Found|
|[az mail user-inference-classification update-override](#users.inferenceClassificationUpdateOverrides)|UpdateOverrides|[Parameters](#Parametersusers.inferenceClassificationUpdateOverrides)|Not Found|

### <a name="CommandsInusers.mailFolders">Commands in `az mail user-mail-folder` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az mail user-mail-folder create-child-folder](#users.mailFoldersCreateChildFolders)|CreateChildFolders|[Parameters](#Parametersusers.mailFoldersCreateChildFolders)|Not Found|
|[az mail user-mail-folder create-message](#users.mailFoldersCreateMessages)|CreateMessages|[Parameters](#Parametersusers.mailFoldersCreateMessages)|Not Found|
|[az mail user-mail-folder create-message-rule](#users.mailFoldersCreateMessageRules)|CreateMessageRules|[Parameters](#Parametersusers.mailFoldersCreateMessageRules)|Not Found|
|[az mail user-mail-folder create-multi-value-extended-property](#users.mailFoldersCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersCreateMultiValueExtendedProperties)|Not Found|
|[az mail user-mail-folder create-single-value-extended-property](#users.mailFoldersCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersCreateSingleValueExtendedProperties)|Not Found|
|[az mail user-mail-folder delete-child-folder](#users.mailFoldersDeleteChildFolders)|DeleteChildFolders|[Parameters](#Parametersusers.mailFoldersDeleteChildFolders)|Not Found|
|[az mail user-mail-folder delete-message](#users.mailFoldersDeleteMessages)|DeleteMessages|[Parameters](#Parametersusers.mailFoldersDeleteMessages)|Not Found|
|[az mail user-mail-folder delete-message-rule](#users.mailFoldersDeleteMessageRules)|DeleteMessageRules|[Parameters](#Parametersusers.mailFoldersDeleteMessageRules)|Not Found|
|[az mail user-mail-folder delete-multi-value-extended-property](#users.mailFoldersDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersDeleteMultiValueExtendedProperties)|Not Found|
|[az mail user-mail-folder delete-single-value-extended-property](#users.mailFoldersDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersDeleteSingleValueExtendedProperties)|Not Found|
|[az mail user-mail-folder list-child-folder](#users.mailFoldersListChildFolders)|ListChildFolders|[Parameters](#Parametersusers.mailFoldersListChildFolders)|Not Found|
|[az mail user-mail-folder list-message](#users.mailFoldersListMessages)|ListMessages|[Parameters](#Parametersusers.mailFoldersListMessages)|Not Found|
|[az mail user-mail-folder list-message-rule](#users.mailFoldersListMessageRules)|ListMessageRules|[Parameters](#Parametersusers.mailFoldersListMessageRules)|Not Found|
|[az mail user-mail-folder list-multi-value-extended-property](#users.mailFoldersListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersListMultiValueExtendedProperties)|Not Found|
|[az mail user-mail-folder list-single-value-extended-property](#users.mailFoldersListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersListSingleValueExtendedProperties)|Not Found|
|[az mail user-mail-folder show-child-folder](#users.mailFoldersGetChildFolders)|GetChildFolders|[Parameters](#Parametersusers.mailFoldersGetChildFolders)|Not Found|
|[az mail user-mail-folder show-message](#users.mailFoldersGetMessages)|GetMessages|[Parameters](#Parametersusers.mailFoldersGetMessages)|Not Found|
|[az mail user-mail-folder show-message-rule](#users.mailFoldersGetMessageRules)|GetMessageRules|[Parameters](#Parametersusers.mailFoldersGetMessageRules)|Not Found|
|[az mail user-mail-folder show-multi-value-extended-property](#users.mailFoldersGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersGetMultiValueExtendedProperties)|Not Found|
|[az mail user-mail-folder show-single-value-extended-property](#users.mailFoldersGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersGetSingleValueExtendedProperties)|Not Found|
|[az mail user-mail-folder update-child-folder](#users.mailFoldersUpdateChildFolders)|UpdateChildFolders|[Parameters](#Parametersusers.mailFoldersUpdateChildFolders)|Not Found|
|[az mail user-mail-folder update-message](#users.mailFoldersUpdateMessages)|UpdateMessages|[Parameters](#Parametersusers.mailFoldersUpdateMessages)|Not Found|
|[az mail user-mail-folder update-message-rule](#users.mailFoldersUpdateMessageRules)|UpdateMessageRules|[Parameters](#Parametersusers.mailFoldersUpdateMessageRules)|Not Found|
|[az mail user-mail-folder update-multi-value-extended-property](#users.mailFoldersUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersUpdateMultiValueExtendedProperties)|Not Found|
|[az mail user-mail-folder update-single-value-extended-property](#users.mailFoldersUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.mailFolders.messages">Commands in `az mail user-mail-folder-message` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az mail user-mail-folder-message create-attachment](#users.mailFolders.messagesCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.mailFolders.messagesCreateAttachments)|Not Found|
|[az mail user-mail-folder-message create-extension](#users.mailFolders.messagesCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.mailFolders.messagesCreateExtensions)|Not Found|
|[az mail user-mail-folder-message create-multi-value-extended-property](#users.mailFolders.messagesCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesCreateMultiValueExtendedProperties)|Not Found|
|[az mail user-mail-folder-message create-single-value-extended-property](#users.mailFolders.messagesCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesCreateSingleValueExtendedProperties)|Not Found|
|[az mail user-mail-folder-message delete-attachment](#users.mailFolders.messagesDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.mailFolders.messagesDeleteAttachments)|Not Found|
|[az mail user-mail-folder-message delete-extension](#users.mailFolders.messagesDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.mailFolders.messagesDeleteExtensions)|Not Found|
|[az mail user-mail-folder-message delete-multi-value-extended-property](#users.mailFolders.messagesDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesDeleteMultiValueExtendedProperties)|Not Found|
|[az mail user-mail-folder-message delete-single-value-extended-property](#users.mailFolders.messagesDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesDeleteSingleValueExtendedProperties)|Not Found|
|[az mail user-mail-folder-message list-attachment](#users.mailFolders.messagesListAttachments)|ListAttachments|[Parameters](#Parametersusers.mailFolders.messagesListAttachments)|Not Found|
|[az mail user-mail-folder-message list-extension](#users.mailFolders.messagesListExtensions)|ListExtensions|[Parameters](#Parametersusers.mailFolders.messagesListExtensions)|Not Found|
|[az mail user-mail-folder-message list-multi-value-extended-property](#users.mailFolders.messagesListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesListMultiValueExtendedProperties)|Not Found|
|[az mail user-mail-folder-message list-single-value-extended-property](#users.mailFolders.messagesListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesListSingleValueExtendedProperties)|Not Found|
|[az mail user-mail-folder-message show-attachment](#users.mailFolders.messagesGetAttachments)|GetAttachments|[Parameters](#Parametersusers.mailFolders.messagesGetAttachments)|Not Found|
|[az mail user-mail-folder-message show-extension](#users.mailFolders.messagesGetExtensions)|GetExtensions|[Parameters](#Parametersusers.mailFolders.messagesGetExtensions)|Not Found|
|[az mail user-mail-folder-message show-multi-value-extended-property](#users.mailFolders.messagesGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesGetMultiValueExtendedProperties)|Not Found|
|[az mail user-mail-folder-message show-single-value-extended-property](#users.mailFolders.messagesGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesGetSingleValueExtendedProperties)|Not Found|
|[az mail user-mail-folder-message update-attachment](#users.mailFolders.messagesUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.mailFolders.messagesUpdateAttachments)|Not Found|
|[az mail user-mail-folder-message update-extension](#users.mailFolders.messagesUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.mailFolders.messagesUpdateExtensions)|Not Found|
|[az mail user-mail-folder-message update-multi-value-extended-property](#users.mailFolders.messagesUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesUpdateMultiValueExtendedProperties)|Not Found|
|[az mail user-mail-folder-message update-single-value-extended-property](#users.mailFolders.messagesUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.messages">Commands in `az mail user-message` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az mail user-message create-attachment](#users.messagesCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.messagesCreateAttachments)|Not Found|
|[az mail user-message create-extension](#users.messagesCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.messagesCreateExtensions)|Not Found|
|[az mail user-message create-multi-value-extended-property](#users.messagesCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.messagesCreateMultiValueExtendedProperties)|Not Found|
|[az mail user-message create-single-value-extended-property](#users.messagesCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.messagesCreateSingleValueExtendedProperties)|Not Found|
|[az mail user-message delete-attachment](#users.messagesDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.messagesDeleteAttachments)|Not Found|
|[az mail user-message delete-extension](#users.messagesDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.messagesDeleteExtensions)|Not Found|
|[az mail user-message delete-multi-value-extended-property](#users.messagesDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.messagesDeleteMultiValueExtendedProperties)|Not Found|
|[az mail user-message delete-single-value-extended-property](#users.messagesDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.messagesDeleteSingleValueExtendedProperties)|Not Found|
|[az mail user-message list-attachment](#users.messagesListAttachments)|ListAttachments|[Parameters](#Parametersusers.messagesListAttachments)|Not Found|
|[az mail user-message list-extension](#users.messagesListExtensions)|ListExtensions|[Parameters](#Parametersusers.messagesListExtensions)|Not Found|
|[az mail user-message list-multi-value-extended-property](#users.messagesListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.messagesListMultiValueExtendedProperties)|Not Found|
|[az mail user-message list-single-value-extended-property](#users.messagesListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.messagesListSingleValueExtendedProperties)|Not Found|
|[az mail user-message show-attachment](#users.messagesGetAttachments)|GetAttachments|[Parameters](#Parametersusers.messagesGetAttachments)|Not Found|
|[az mail user-message show-extension](#users.messagesGetExtensions)|GetExtensions|[Parameters](#Parametersusers.messagesGetExtensions)|Not Found|
|[az mail user-message show-multi-value-extended-property](#users.messagesGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.messagesGetMultiValueExtendedProperties)|Not Found|
|[az mail user-message show-single-value-extended-property](#users.messagesGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.messagesGetSingleValueExtendedProperties)|Not Found|
|[az mail user-message update-attachment](#users.messagesUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.messagesUpdateAttachments)|Not Found|
|[az mail user-message update-extension](#users.messagesUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.messagesUpdateExtensions)|Not Found|
|[az mail user-message update-multi-value-extended-property](#users.messagesUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.messagesUpdateMultiValueExtendedProperties)|Not Found|
|[az mail user-message update-single-value-extended-property](#users.messagesUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.messagesUpdateSingleValueExtendedProperties)|Not Found|


## COMMAND DETAILS

### group `az mail user`
#### <a name="usersCreateMailFolders">Command `az mail user create-mail-folder`</a>

##### <a name="ParametersusersCreateMailFolders">Parameters</a> 
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

#### <a name="usersCreateMessages">Command `az mail user create-message`</a>

##### <a name="ParametersusersCreateMessages">Parameters</a> 
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
|**--web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--microsoft-graph-email-address**|object|emailAddress|microsoft_graph_email_address|emailAddress|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-status**|choice||flag_status|flagStatus|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

#### <a name="usersDeleteInferenceClassification">Command `az mail user delete-inference-classification`</a>

##### <a name="ParametersusersDeleteInferenceClassification">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteMailFolders">Command `az mail user delete-mail-folder`</a>

##### <a name="ParametersusersDeleteMailFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteMessages">Command `az mail user delete-message`</a>

##### <a name="ParametersusersDeleteMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListMailFolders">Command `az mail user list-mail-folder`</a>

##### <a name="ParametersusersListMailFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListMessages">Command `az mail user list-message`</a>

##### <a name="ParametersusersListMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetInferenceClassification">Command `az mail user show-inference-classification`</a>

##### <a name="ParametersusersGetInferenceClassification">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetMailFolders">Command `az mail user show-mail-folder`</a>

##### <a name="ParametersusersGetMailFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetMessages">Command `az mail user show-message`</a>

##### <a name="ParametersusersGetMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateInferenceClassification">Command `az mail user update-inference-classification`</a>

##### <a name="ParametersusersUpdateInferenceClassification">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--overrides**|array|A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.|overrides|overrides|

#### <a name="usersUpdateMailFolders">Command `az mail user update-mail-folder`</a>

##### <a name="ParametersusersUpdateMailFolders">Parameters</a> 
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

#### <a name="usersUpdateMessages">Command `az mail user update-message`</a>

##### <a name="ParametersusersUpdateMessages">Parameters</a> 
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
|**--web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--microsoft-graph-email-address**|object|emailAddress|microsoft_graph_email_address|emailAddress|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-status**|choice||flag_status|flagStatus|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

### group `az mail user-inference-classification`
#### <a name="users.inferenceClassificationCreateOverrides">Command `az mail user-inference-classification create-override`</a>

##### <a name="Parametersusers.inferenceClassificationCreateOverrides">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--classify-as**|choice||classify_as|classifyAs|
|**--sender-email-address**|object|emailAddress|sender_email_address|senderEmailAddress|

#### <a name="users.inferenceClassificationDeleteOverrides">Command `az mail user-inference-classification delete-override`</a>

##### <a name="Parametersusers.inferenceClassificationDeleteOverrides">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.inferenceClassificationListOverrides">Command `az mail user-inference-classification list-override`</a>

##### <a name="Parametersusers.inferenceClassificationListOverrides">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.inferenceClassificationGetOverrides">Command `az mail user-inference-classification show-override`</a>

##### <a name="Parametersusers.inferenceClassificationGetOverrides">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.inferenceClassificationUpdateOverrides">Command `az mail user-inference-classification update-override`</a>

##### <a name="Parametersusers.inferenceClassificationUpdateOverrides">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--id**|string|Read-only.|id|id|
|**--classify-as**|choice||classify_as|classifyAs|
|**--sender-email-address**|object|emailAddress|sender_email_address|senderEmailAddress|

### group `az mail user-mail-folder`
#### <a name="users.mailFoldersCreateChildFolders">Command `az mail user-mail-folder create-child-folder`</a>

##### <a name="Parametersusers.mailFoldersCreateChildFolders">Parameters</a> 
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

#### <a name="users.mailFoldersCreateMessages">Command `az mail user-mail-folder create-message`</a>

##### <a name="Parametersusers.mailFoldersCreateMessages">Parameters</a> 
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
|**--web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--microsoft-graph-email-address**|object|emailAddress|microsoft_graph_email_address|emailAddress|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-status**|choice||flag_status|flagStatus|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

#### <a name="users.mailFoldersCreateMessageRules">Command `az mail user-mail-folder create-message-rule`</a>

##### <a name="Parametersusers.mailFoldersCreateMessageRules">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the rule.|display_name|displayName|
|**--has-error**|boolean|Indicates whether the rule is in an error condition. Read-only.|has_error|hasError|
|**--is-enabled**|boolean|Indicates whether the rule is enabled to be applied to messages.|is_enabled|isEnabled|
|**--is-read-only**|boolean|Indicates if the rule is read-only and cannot be modified or deleted by the rules REST API.|is_read_only|isReadOnly|
|**--sequence**|integer|Indicates the order in which the rule is executed, among other rules.|sequence|sequence|
|**--body-contains**|array|Represents the strings that should appear in the body of an incoming message in order for the condition or exception to apply.|body_contains|bodyContains|
|**--body-or-subject-contains**|array|Represents the strings that should appear in the body or subject of an incoming message in order for the condition or exception to apply.|body_or_subject_contains|bodyOrSubjectContains|
|**--categories**|array|Represents the categories that an incoming message should be labeled with in order for the condition or exception to apply.|categories|categories|
|**--from-addresses**|array|Represents the specific sender email addresses of an incoming message in order for the condition or exception to apply.|from_addresses|fromAddresses|
|**--has-attachments**|boolean|Indicates whether an incoming message must have attachments in order for the condition or exception to apply.|has_attachments|hasAttachments|
|**--header-contains**|array|Represents the strings that appear in the headers of an incoming message in order for the condition or exception to apply.|header_contains|headerContains|
|**--importance**|choice||importance|importance|
|**--exceptions-is-approval-request**|boolean|Indicates whether an incoming message must be an approval request in order for the condition or exception to apply.|is_approval_request|isApprovalRequest|
|**--exceptions-is-automatic-forward**|boolean|Indicates whether an incoming message must be automatically forwarded in order for the condition or exception to apply.|is_automatic_forward|isAutomaticForward|
|**--exceptions-is-automatic-reply**|boolean|Indicates whether an incoming message must be an auto reply in order for the condition or exception to apply.|is_automatic_reply|isAutomaticReply|
|**--exceptions-is-encrypted**|boolean|Indicates whether an incoming message must be encrypted in order for the condition or exception to apply.|is_encrypted|isEncrypted|
|**--exceptions-is-meeting-request**|boolean|Indicates whether an incoming message must be a meeting request in order for the condition or exception to apply.|is_meeting_request|isMeetingRequest|
|**--exceptions-is-meeting-response**|boolean|Indicates whether an incoming message must be a meeting response in order for the condition or exception to apply.|is_meeting_response|isMeetingResponse|
|**--exceptions-is-non-delivery-report**|boolean|Indicates whether an incoming message must be a non-delivery report in order for the condition or exception to apply.|is_non_delivery_report|isNonDeliveryReport|
|**--exceptions-is-permission-controlled**|boolean|Indicates whether an incoming message must be permission controlled (RMS-protected) in order for the condition or exception to apply.|is_permission_controlled|isPermissionControlled|
|**--exceptions-is-read-receipt**|boolean|Indicates whether an incoming message must be a read receipt in order for the condition or exception to apply.|is_read_receipt|isReadReceipt|
|**--exceptions-is-signed**|boolean|Indicates whether an incoming message must be S/MIME-signed in order for the condition or exception to apply.|is_signed|isSigned|
|**--exceptions-is-voicemail**|boolean|Indicates whether an incoming message must be a voice mail in order for the condition or exception to apply.|is_voicemail|isVoicemail|
|**--message-action-flag**|choice||message_action_flag|messageActionFlag|
|**--not-sent-to-me**|boolean|Indicates whether the owner of the mailbox must not be a recipient of an incoming message in order for the condition or exception to apply.|not_sent_to_me|notSentToMe|
|**--recipient-contains**|array|Represents the strings that appear in either the toRecipients or ccRecipients properties of an incoming message in order for the condition or exception to apply.|recipient_contains|recipientContains|
|**--sender-contains**|array|Represents the strings that appear in the from property of an incoming message in order for the condition or exception to apply.|sender_contains|senderContains|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--sent-cc-me**|boolean|Indicates whether the owner of the mailbox must be in the ccRecipients property of an incoming message in order for the condition or exception to apply.|sent_cc_me|sentCcMe|
|**--sent-only-to-me**|boolean|Indicates whether the owner of the mailbox must be the only recipient in an incoming message in order for the condition or exception to apply.|sent_only_to_me|sentOnlyToMe|
|**--sent-to-addresses**|array|Represents the email addresses that an incoming message must have been sent to in order for the condition or exception to apply.|sent_to_addresses|sentToAddresses|
|**--sent-to-me**|boolean|Indicates whether the owner of the mailbox must be in the toRecipients property of an incoming message in order for the condition or exception to apply.|sent_to_me|sentToMe|
|**--sent-to-or-cc-me**|boolean|Indicates whether the owner of the mailbox must be in either a toRecipients or ccRecipients property of an incoming message in order for the condition or exception to apply.|sent_to_or_cc_me|sentToOrCcMe|
|**--subject-contains**|array|Represents the strings that appear in the subject of an incoming message in order for the condition or exception to apply.|subject_contains|subjectContains|
|**--within-size-range**|object|sizeRange|within_size_range|withinSizeRange|
|**--microsoft-graph-message-rule-predicates-body-contains**|array|Represents the strings that should appear in the body of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_body_contains|bodyContains|
|**--microsoft-graph-message-rule-predicates-body-or-subject-contains-body-or-subject-contains**|array|Represents the strings that should appear in the body or subject of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_body_or_subject_contains_body_or_subject_contains|bodyOrSubjectContains|
|**--microsoft-graph-message-rule-predicates-categories**|array|Represents the categories that an incoming message should be labeled with in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_categories|categories|
|**--microsoft-graph-message-rule-predicates-from-addresses**|array|Represents the specific sender email addresses of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_from_addresses|fromAddresses|
|**--boolean-has-attachments**|boolean|Indicates whether an incoming message must have attachments in order for the condition or exception to apply.|boolean_has_attachments|hasAttachments|
|**--microsoft-graph-message-rule-predicates-header-contains**|array|Represents the strings that appear in the headers of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_header_contains|headerContains|
|**--microsoft-graph-importance**|choice||microsoft_graph_importance|importance|
|**--is-approval-request**|boolean|Indicates whether an incoming message must be an approval request in order for the condition or exception to apply.|is_approval_request|isApprovalRequest|
|**--is-automatic-forward**|boolean|Indicates whether an incoming message must be automatically forwarded in order for the condition or exception to apply.|is_automatic_forward|isAutomaticForward|
|**--is-automatic-reply**|boolean|Indicates whether an incoming message must be an auto reply in order for the condition or exception to apply.|is_automatic_reply|isAutomaticReply|
|**--is-encrypted**|boolean|Indicates whether an incoming message must be encrypted in order for the condition or exception to apply.|is_encrypted|isEncrypted|
|**--is-meeting-request**|boolean|Indicates whether an incoming message must be a meeting request in order for the condition or exception to apply.|is_meeting_request|isMeetingRequest|
|**--is-meeting-response**|boolean|Indicates whether an incoming message must be a meeting response in order for the condition or exception to apply.|is_meeting_response|isMeetingResponse|
|**--is-non-delivery-report**|boolean|Indicates whether an incoming message must be a non-delivery report in order for the condition or exception to apply.|is_non_delivery_report|isNonDeliveryReport|
|**--is-permission-controlled**|boolean|Indicates whether an incoming message must be permission controlled (RMS-protected) in order for the condition or exception to apply.|is_permission_controlled|isPermissionControlled|
|**--is-read-receipt**|boolean|Indicates whether an incoming message must be a read receipt in order for the condition or exception to apply.|is_read_receipt|isReadReceipt|
|**--is-signed**|boolean|Indicates whether an incoming message must be S/MIME-signed in order for the condition or exception to apply.|is_signed|isSigned|
|**--is-voicemail**|boolean|Indicates whether an incoming message must be a voice mail in order for the condition or exception to apply.|is_voicemail|isVoicemail|
|**--microsoft-graph-message-action-flag-message-action-flag**|choice||microsoft_graph_message_action_flag_message_action_flag|messageActionFlag|
|**--boolean-not-sent-to-me**|boolean|Indicates whether the owner of the mailbox must not be a recipient of an incoming message in order for the condition or exception to apply.|boolean_not_sent_to_me|notSentToMe|
|**--microsoft-graph-message-rule-predicates-recipient-contains**|array|Represents the strings that appear in either the toRecipients or ccRecipients properties of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_recipient_contains|recipientContains|
|**--microsoft-graph-message-rule-predicates-sender-contains**|array|Represents the strings that appear in the from property of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_sender_contains|senderContains|
|**--microsoft-graph-sensitivity**|choice||microsoft_graph_sensitivity|sensitivity|
|**--boolean-sent-cc-me**|boolean|Indicates whether the owner of the mailbox must be in the ccRecipients property of an incoming message in order for the condition or exception to apply.|boolean_sent_cc_me|sentCcMe|
|**--boolean-sent-only-to-me**|boolean|Indicates whether the owner of the mailbox must be the only recipient in an incoming message in order for the condition or exception to apply.|boolean_sent_only_to_me|sentOnlyToMe|
|**--microsoft-graph-message-rule-predicates-sent-to-addresses-sent-to-addresses**|array|Represents the email addresses that an incoming message must have been sent to in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_sent_to_addresses_sent_to_addresses|sentToAddresses|
|**--boolean-sent-to-me**|boolean|Indicates whether the owner of the mailbox must be in the toRecipients property of an incoming message in order for the condition or exception to apply.|boolean_sent_to_me|sentToMe|
|**--boolean-sent-to-or-cc-me**|boolean|Indicates whether the owner of the mailbox must be in either a toRecipients or ccRecipients property of an incoming message in order for the condition or exception to apply.|boolean_sent_to_or_cc_me|sentToOrCcMe|
|**--microsoft-graph-message-rule-predicates-subject-contains**|array|Represents the strings that appear in the subject of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_subject_contains|subjectContains|
|**--microsoft-graph-size-range-within-size-range**|object|sizeRange|microsoft_graph_size_range_within_size_range|withinSizeRange|
|**--assign-categories**|array|A list of categories to be assigned to a message.|assign_categories|assignCategories|
|**--copy-to-folder**|string|The ID of a folder that a message is to be copied to.|copy_to_folder|copyToFolder|
|**--delete**|boolean|Indicates whether a message should be moved to the Deleted Items folder.|delete|delete|
|**--forward-as-attachment-to**|array|The email addresses of the recipients to which a message should be forwarded as an attachment.|forward_as_attachment_to|forwardAsAttachmentTo|
|**--forward-to**|array|The email addresses of the recipients to which a message should be forwarded.|forward_to|forwardTo|
|**--mark-as-read**|boolean|Indicates whether a message should be marked as read.|mark_as_read|markAsRead|
|**--mark-importance**|choice||mark_importance|markImportance|
|**--move-to-folder**|string|The ID of the folder that a message will be moved to.|move_to_folder|moveToFolder|
|**--permanent-delete**|boolean|Indicates whether a message should be permanently deleted and not saved to the Deleted Items folder.|permanent_delete|permanentDelete|
|**--redirect-to**|array|The email addresses to which a message should be redirected.|redirect_to|redirectTo|
|**--stop-processing-rules**|boolean|Indicates whether subsequent rules should be evaluated.|stop_processing_rules|stopProcessingRules|

#### <a name="users.mailFoldersCreateMultiValueExtendedProperties">Command `az mail user-mail-folder create-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.mailFoldersCreateSingleValueExtendedProperties">Command `az mail user-mail-folder create-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.mailFoldersDeleteChildFolders">Command `az mail user-mail-folder delete-child-folder`</a>

##### <a name="Parametersusers.mailFoldersDeleteChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFoldersDeleteMessages">Command `az mail user-mail-folder delete-message`</a>

##### <a name="Parametersusers.mailFoldersDeleteMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFoldersDeleteMessageRules">Command `az mail user-mail-folder delete-message-rule`</a>

##### <a name="Parametersusers.mailFoldersDeleteMessageRules">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-rule-id**|string|key: id of messageRule|message_rule_id|messageRule-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFoldersDeleteMultiValueExtendedProperties">Command `az mail user-mail-folder delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFoldersDeleteSingleValueExtendedProperties">Command `az mail user-mail-folder delete-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFoldersListChildFolders">Command `az mail user-mail-folder list-child-folder`</a>

##### <a name="Parametersusers.mailFoldersListChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersListMessages">Command `az mail user-mail-folder list-message`</a>

##### <a name="Parametersusers.mailFoldersListMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersListMessageRules">Command `az mail user-mail-folder list-message-rule`</a>

##### <a name="Parametersusers.mailFoldersListMessageRules">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersListMultiValueExtendedProperties">Command `az mail user-mail-folder list-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersListSingleValueExtendedProperties">Command `az mail user-mail-folder list-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersGetChildFolders">Command `az mail user-mail-folder show-child-folder`</a>

##### <a name="Parametersusers.mailFoldersGetChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersGetMessages">Command `az mail user-mail-folder show-message`</a>

##### <a name="Parametersusers.mailFoldersGetMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersGetMessageRules">Command `az mail user-mail-folder show-message-rule`</a>

##### <a name="Parametersusers.mailFoldersGetMessageRules">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-rule-id**|string|key: id of messageRule|message_rule_id|messageRule-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersGetMultiValueExtendedProperties">Command `az mail user-mail-folder show-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersGetSingleValueExtendedProperties">Command `az mail user-mail-folder show-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersUpdateChildFolders">Command `az mail user-mail-folder update-child-folder`</a>

##### <a name="Parametersusers.mailFoldersUpdateChildFolders">Parameters</a> 
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

#### <a name="users.mailFoldersUpdateMessages">Command `az mail user-mail-folder update-message`</a>

##### <a name="Parametersusers.mailFoldersUpdateMessages">Parameters</a> 
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
|**--web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--microsoft-graph-email-address**|object|emailAddress|microsoft_graph_email_address|emailAddress|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--flag-status**|choice||flag_status|flagStatus|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|

#### <a name="users.mailFoldersUpdateMessageRules">Command `az mail user-mail-folder update-message-rule`</a>

##### <a name="Parametersusers.mailFoldersUpdateMessageRules">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-rule-id**|string|key: id of messageRule|message_rule_id|messageRule-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the rule.|display_name|displayName|
|**--has-error**|boolean|Indicates whether the rule is in an error condition. Read-only.|has_error|hasError|
|**--is-enabled**|boolean|Indicates whether the rule is enabled to be applied to messages.|is_enabled|isEnabled|
|**--is-read-only**|boolean|Indicates if the rule is read-only and cannot be modified or deleted by the rules REST API.|is_read_only|isReadOnly|
|**--sequence**|integer|Indicates the order in which the rule is executed, among other rules.|sequence|sequence|
|**--body-contains**|array|Represents the strings that should appear in the body of an incoming message in order for the condition or exception to apply.|body_contains|bodyContains|
|**--body-or-subject-contains**|array|Represents the strings that should appear in the body or subject of an incoming message in order for the condition or exception to apply.|body_or_subject_contains|bodyOrSubjectContains|
|**--categories**|array|Represents the categories that an incoming message should be labeled with in order for the condition or exception to apply.|categories|categories|
|**--from-addresses**|array|Represents the specific sender email addresses of an incoming message in order for the condition or exception to apply.|from_addresses|fromAddresses|
|**--has-attachments**|boolean|Indicates whether an incoming message must have attachments in order for the condition or exception to apply.|has_attachments|hasAttachments|
|**--header-contains**|array|Represents the strings that appear in the headers of an incoming message in order for the condition or exception to apply.|header_contains|headerContains|
|**--importance**|choice||importance|importance|
|**--exceptions-is-approval-request**|boolean|Indicates whether an incoming message must be an approval request in order for the condition or exception to apply.|is_approval_request|isApprovalRequest|
|**--exceptions-is-automatic-forward**|boolean|Indicates whether an incoming message must be automatically forwarded in order for the condition or exception to apply.|is_automatic_forward|isAutomaticForward|
|**--exceptions-is-automatic-reply**|boolean|Indicates whether an incoming message must be an auto reply in order for the condition or exception to apply.|is_automatic_reply|isAutomaticReply|
|**--exceptions-is-encrypted**|boolean|Indicates whether an incoming message must be encrypted in order for the condition or exception to apply.|is_encrypted|isEncrypted|
|**--exceptions-is-meeting-request**|boolean|Indicates whether an incoming message must be a meeting request in order for the condition or exception to apply.|is_meeting_request|isMeetingRequest|
|**--exceptions-is-meeting-response**|boolean|Indicates whether an incoming message must be a meeting response in order for the condition or exception to apply.|is_meeting_response|isMeetingResponse|
|**--exceptions-is-non-delivery-report**|boolean|Indicates whether an incoming message must be a non-delivery report in order for the condition or exception to apply.|is_non_delivery_report|isNonDeliveryReport|
|**--exceptions-is-permission-controlled**|boolean|Indicates whether an incoming message must be permission controlled (RMS-protected) in order for the condition or exception to apply.|is_permission_controlled|isPermissionControlled|
|**--exceptions-is-read-receipt**|boolean|Indicates whether an incoming message must be a read receipt in order for the condition or exception to apply.|is_read_receipt|isReadReceipt|
|**--exceptions-is-signed**|boolean|Indicates whether an incoming message must be S/MIME-signed in order for the condition or exception to apply.|is_signed|isSigned|
|**--exceptions-is-voicemail**|boolean|Indicates whether an incoming message must be a voice mail in order for the condition or exception to apply.|is_voicemail|isVoicemail|
|**--message-action-flag**|choice||message_action_flag|messageActionFlag|
|**--not-sent-to-me**|boolean|Indicates whether the owner of the mailbox must not be a recipient of an incoming message in order for the condition or exception to apply.|not_sent_to_me|notSentToMe|
|**--recipient-contains**|array|Represents the strings that appear in either the toRecipients or ccRecipients properties of an incoming message in order for the condition or exception to apply.|recipient_contains|recipientContains|
|**--sender-contains**|array|Represents the strings that appear in the from property of an incoming message in order for the condition or exception to apply.|sender_contains|senderContains|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--sent-cc-me**|boolean|Indicates whether the owner of the mailbox must be in the ccRecipients property of an incoming message in order for the condition or exception to apply.|sent_cc_me|sentCcMe|
|**--sent-only-to-me**|boolean|Indicates whether the owner of the mailbox must be the only recipient in an incoming message in order for the condition or exception to apply.|sent_only_to_me|sentOnlyToMe|
|**--sent-to-addresses**|array|Represents the email addresses that an incoming message must have been sent to in order for the condition or exception to apply.|sent_to_addresses|sentToAddresses|
|**--sent-to-me**|boolean|Indicates whether the owner of the mailbox must be in the toRecipients property of an incoming message in order for the condition or exception to apply.|sent_to_me|sentToMe|
|**--sent-to-or-cc-me**|boolean|Indicates whether the owner of the mailbox must be in either a toRecipients or ccRecipients property of an incoming message in order for the condition or exception to apply.|sent_to_or_cc_me|sentToOrCcMe|
|**--subject-contains**|array|Represents the strings that appear in the subject of an incoming message in order for the condition or exception to apply.|subject_contains|subjectContains|
|**--within-size-range**|object|sizeRange|within_size_range|withinSizeRange|
|**--microsoft-graph-message-rule-predicates-body-contains**|array|Represents the strings that should appear in the body of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_body_contains|bodyContains|
|**--microsoft-graph-message-rule-predicates-body-or-subject-contains-body-or-subject-contains**|array|Represents the strings that should appear in the body or subject of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_body_or_subject_contains_body_or_subject_contains|bodyOrSubjectContains|
|**--microsoft-graph-message-rule-predicates-categories**|array|Represents the categories that an incoming message should be labeled with in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_categories|categories|
|**--microsoft-graph-message-rule-predicates-from-addresses**|array|Represents the specific sender email addresses of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_from_addresses|fromAddresses|
|**--boolean-has-attachments**|boolean|Indicates whether an incoming message must have attachments in order for the condition or exception to apply.|boolean_has_attachments|hasAttachments|
|**--microsoft-graph-message-rule-predicates-header-contains**|array|Represents the strings that appear in the headers of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_header_contains|headerContains|
|**--microsoft-graph-importance**|choice||microsoft_graph_importance|importance|
|**--is-approval-request**|boolean|Indicates whether an incoming message must be an approval request in order for the condition or exception to apply.|is_approval_request|isApprovalRequest|
|**--is-automatic-forward**|boolean|Indicates whether an incoming message must be automatically forwarded in order for the condition or exception to apply.|is_automatic_forward|isAutomaticForward|
|**--is-automatic-reply**|boolean|Indicates whether an incoming message must be an auto reply in order for the condition or exception to apply.|is_automatic_reply|isAutomaticReply|
|**--is-encrypted**|boolean|Indicates whether an incoming message must be encrypted in order for the condition or exception to apply.|is_encrypted|isEncrypted|
|**--is-meeting-request**|boolean|Indicates whether an incoming message must be a meeting request in order for the condition or exception to apply.|is_meeting_request|isMeetingRequest|
|**--is-meeting-response**|boolean|Indicates whether an incoming message must be a meeting response in order for the condition or exception to apply.|is_meeting_response|isMeetingResponse|
|**--is-non-delivery-report**|boolean|Indicates whether an incoming message must be a non-delivery report in order for the condition or exception to apply.|is_non_delivery_report|isNonDeliveryReport|
|**--is-permission-controlled**|boolean|Indicates whether an incoming message must be permission controlled (RMS-protected) in order for the condition or exception to apply.|is_permission_controlled|isPermissionControlled|
|**--is-read-receipt**|boolean|Indicates whether an incoming message must be a read receipt in order for the condition or exception to apply.|is_read_receipt|isReadReceipt|
|**--is-signed**|boolean|Indicates whether an incoming message must be S/MIME-signed in order for the condition or exception to apply.|is_signed|isSigned|
|**--is-voicemail**|boolean|Indicates whether an incoming message must be a voice mail in order for the condition or exception to apply.|is_voicemail|isVoicemail|
|**--microsoft-graph-message-action-flag-message-action-flag**|choice||microsoft_graph_message_action_flag_message_action_flag|messageActionFlag|
|**--boolean-not-sent-to-me**|boolean|Indicates whether the owner of the mailbox must not be a recipient of an incoming message in order for the condition or exception to apply.|boolean_not_sent_to_me|notSentToMe|
|**--microsoft-graph-message-rule-predicates-recipient-contains**|array|Represents the strings that appear in either the toRecipients or ccRecipients properties of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_recipient_contains|recipientContains|
|**--microsoft-graph-message-rule-predicates-sender-contains**|array|Represents the strings that appear in the from property of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_sender_contains|senderContains|
|**--microsoft-graph-sensitivity**|choice||microsoft_graph_sensitivity|sensitivity|
|**--boolean-sent-cc-me**|boolean|Indicates whether the owner of the mailbox must be in the ccRecipients property of an incoming message in order for the condition or exception to apply.|boolean_sent_cc_me|sentCcMe|
|**--boolean-sent-only-to-me**|boolean|Indicates whether the owner of the mailbox must be the only recipient in an incoming message in order for the condition or exception to apply.|boolean_sent_only_to_me|sentOnlyToMe|
|**--microsoft-graph-message-rule-predicates-sent-to-addresses-sent-to-addresses**|array|Represents the email addresses that an incoming message must have been sent to in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_sent_to_addresses_sent_to_addresses|sentToAddresses|
|**--boolean-sent-to-me**|boolean|Indicates whether the owner of the mailbox must be in the toRecipients property of an incoming message in order for the condition or exception to apply.|boolean_sent_to_me|sentToMe|
|**--boolean-sent-to-or-cc-me**|boolean|Indicates whether the owner of the mailbox must be in either a toRecipients or ccRecipients property of an incoming message in order for the condition or exception to apply.|boolean_sent_to_or_cc_me|sentToOrCcMe|
|**--microsoft-graph-message-rule-predicates-subject-contains**|array|Represents the strings that appear in the subject of an incoming message in order for the condition or exception to apply.|microsoft_graph_message_rule_predicates_subject_contains|subjectContains|
|**--microsoft-graph-size-range-within-size-range**|object|sizeRange|microsoft_graph_size_range_within_size_range|withinSizeRange|
|**--assign-categories**|array|A list of categories to be assigned to a message.|assign_categories|assignCategories|
|**--copy-to-folder**|string|The ID of a folder that a message is to be copied to.|copy_to_folder|copyToFolder|
|**--delete**|boolean|Indicates whether a message should be moved to the Deleted Items folder.|delete|delete|
|**--forward-as-attachment-to**|array|The email addresses of the recipients to which a message should be forwarded as an attachment.|forward_as_attachment_to|forwardAsAttachmentTo|
|**--forward-to**|array|The email addresses of the recipients to which a message should be forwarded.|forward_to|forwardTo|
|**--mark-as-read**|boolean|Indicates whether a message should be marked as read.|mark_as_read|markAsRead|
|**--mark-importance**|choice||mark_importance|markImportance|
|**--move-to-folder**|string|The ID of the folder that a message will be moved to.|move_to_folder|moveToFolder|
|**--permanent-delete**|boolean|Indicates whether a message should be permanently deleted and not saved to the Deleted Items folder.|permanent_delete|permanentDelete|
|**--redirect-to**|array|The email addresses to which a message should be redirected.|redirect_to|redirectTo|
|**--stop-processing-rules**|boolean|Indicates whether subsequent rules should be evaluated.|stop_processing_rules|stopProcessingRules|

#### <a name="users.mailFoldersUpdateMultiValueExtendedProperties">Command `az mail user-mail-folder update-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.mailFoldersUpdateSingleValueExtendedProperties">Command `az mail user-mail-folder update-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az mail user-mail-folder-message`
#### <a name="users.mailFolders.messagesCreateAttachments">Command `az mail user-mail-folder-message create-attachment`</a>

##### <a name="Parametersusers.mailFolders.messagesCreateAttachments">Parameters</a> 
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

#### <a name="users.mailFolders.messagesCreateExtensions">Command `az mail user-mail-folder-message create-extension`</a>

##### <a name="Parametersusers.mailFolders.messagesCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.mailFolders.messagesCreateMultiValueExtendedProperties">Command `az mail user-mail-folder-message create-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.mailFolders.messagesCreateSingleValueExtendedProperties">Command `az mail user-mail-folder-message create-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.mailFolders.messagesDeleteAttachments">Command `az mail user-mail-folder-message delete-attachment`</a>

##### <a name="Parametersusers.mailFolders.messagesDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFolders.messagesDeleteExtensions">Command `az mail user-mail-folder-message delete-extension`</a>

##### <a name="Parametersusers.mailFolders.messagesDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFolders.messagesDeleteMultiValueExtendedProperties">Command `az mail user-mail-folder-message delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFolders.messagesDeleteSingleValueExtendedProperties">Command `az mail user-mail-folder-message delete-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFolders.messagesListAttachments">Command `az mail user-mail-folder-message list-attachment`</a>

##### <a name="Parametersusers.mailFolders.messagesListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesListExtensions">Command `az mail user-mail-folder-message list-extension`</a>

##### <a name="Parametersusers.mailFolders.messagesListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesListMultiValueExtendedProperties">Command `az mail user-mail-folder-message list-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesListSingleValueExtendedProperties">Command `az mail user-mail-folder-message list-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesGetAttachments">Command `az mail user-mail-folder-message show-attachment`</a>

##### <a name="Parametersusers.mailFolders.messagesGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesGetExtensions">Command `az mail user-mail-folder-message show-extension`</a>

##### <a name="Parametersusers.mailFolders.messagesGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesGetMultiValueExtendedProperties">Command `az mail user-mail-folder-message show-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesGetSingleValueExtendedProperties">Command `az mail user-mail-folder-message show-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesUpdateAttachments">Command `az mail user-mail-folder-message update-attachment`</a>

##### <a name="Parametersusers.mailFolders.messagesUpdateAttachments">Parameters</a> 
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

#### <a name="users.mailFolders.messagesUpdateExtensions">Command `az mail user-mail-folder-message update-extension`</a>

##### <a name="Parametersusers.mailFolders.messagesUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.mailFolders.messagesUpdateMultiValueExtendedProperties">Command `az mail user-mail-folder-message update-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.mailFolders.messagesUpdateSingleValueExtendedProperties">Command `az mail user-mail-folder-message update-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az mail user-message`
#### <a name="users.messagesCreateAttachments">Command `az mail user-message create-attachment`</a>

##### <a name="Parametersusers.messagesCreateAttachments">Parameters</a> 
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

#### <a name="users.messagesCreateExtensions">Command `az mail user-message create-extension`</a>

##### <a name="Parametersusers.messagesCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.messagesCreateMultiValueExtendedProperties">Command `az mail user-message create-multi-value-extended-property`</a>

##### <a name="Parametersusers.messagesCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.messagesCreateSingleValueExtendedProperties">Command `az mail user-message create-single-value-extended-property`</a>

##### <a name="Parametersusers.messagesCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.messagesDeleteAttachments">Command `az mail user-message delete-attachment`</a>

##### <a name="Parametersusers.messagesDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.messagesDeleteExtensions">Command `az mail user-message delete-extension`</a>

##### <a name="Parametersusers.messagesDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.messagesDeleteMultiValueExtendedProperties">Command `az mail user-message delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.messagesDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.messagesDeleteSingleValueExtendedProperties">Command `az mail user-message delete-single-value-extended-property`</a>

##### <a name="Parametersusers.messagesDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.messagesListAttachments">Command `az mail user-message list-attachment`</a>

##### <a name="Parametersusers.messagesListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesListExtensions">Command `az mail user-message list-extension`</a>

##### <a name="Parametersusers.messagesListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesListMultiValueExtendedProperties">Command `az mail user-message list-multi-value-extended-property`</a>

##### <a name="Parametersusers.messagesListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesListSingleValueExtendedProperties">Command `az mail user-message list-single-value-extended-property`</a>

##### <a name="Parametersusers.messagesListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesGetAttachments">Command `az mail user-message show-attachment`</a>

##### <a name="Parametersusers.messagesGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesGetExtensions">Command `az mail user-message show-extension`</a>

##### <a name="Parametersusers.messagesGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesGetMultiValueExtendedProperties">Command `az mail user-message show-multi-value-extended-property`</a>

##### <a name="Parametersusers.messagesGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesGetSingleValueExtendedProperties">Command `az mail user-message show-single-value-extended-property`</a>

##### <a name="Parametersusers.messagesGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesUpdateAttachments">Command `az mail user-message update-attachment`</a>

##### <a name="Parametersusers.messagesUpdateAttachments">Parameters</a> 
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

#### <a name="users.messagesUpdateExtensions">Command `az mail user-message update-extension`</a>

##### <a name="Parametersusers.messagesUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.messagesUpdateMultiValueExtendedProperties">Command `az mail user-message update-multi-value-extended-property`</a>

##### <a name="Parametersusers.messagesUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.messagesUpdateSingleValueExtendedProperties">Command `az mail user-message update-single-value-extended-property`</a>

##### <a name="Parametersusers.messagesUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|
