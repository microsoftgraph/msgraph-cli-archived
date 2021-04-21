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
|az mail usersinferenceclassification|users.inferenceClassification|[commands](#CommandsInusers.inferenceClassification)|
|az mail usersmailfolder|users.mailFolders|[commands](#CommandsInusers.mailFolders)|
|az mail usersmailfoldersmessage|users.mailFolders.messages|[commands](#CommandsInusers.mailFolders.messages)|
|az mail usersmessage|users.messages|[commands](#CommandsInusers.messages)|

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

### <a name="CommandsInusers.inferenceClassification">Commands in `az mail usersinferenceclassification` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az mail usersinferenceclassification create-override](#users.inferenceClassificationCreateOverrides)|CreateOverrides|[Parameters](#Parametersusers.inferenceClassificationCreateOverrides)|Not Found|
|[az mail usersinferenceclassification delete-override](#users.inferenceClassificationDeleteOverrides)|DeleteOverrides|[Parameters](#Parametersusers.inferenceClassificationDeleteOverrides)|Not Found|
|[az mail usersinferenceclassification list-override](#users.inferenceClassificationListOverrides)|ListOverrides|[Parameters](#Parametersusers.inferenceClassificationListOverrides)|Not Found|
|[az mail usersinferenceclassification show-override](#users.inferenceClassificationGetOverrides)|GetOverrides|[Parameters](#Parametersusers.inferenceClassificationGetOverrides)|Not Found|
|[az mail usersinferenceclassification update-override](#users.inferenceClassificationUpdateOverrides)|UpdateOverrides|[Parameters](#Parametersusers.inferenceClassificationUpdateOverrides)|Not Found|

### <a name="CommandsInusers.mailFolders">Commands in `az mail usersmailfolder` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az mail usersmailfolder create-child-folder](#users.mailFoldersCreateChildFolders)|CreateChildFolders|[Parameters](#Parametersusers.mailFoldersCreateChildFolders)|Not Found|
|[az mail usersmailfolder create-message](#users.mailFoldersCreateMessages)|CreateMessages|[Parameters](#Parametersusers.mailFoldersCreateMessages)|Not Found|
|[az mail usersmailfolder create-message-rule](#users.mailFoldersCreateMessageRules)|CreateMessageRules|[Parameters](#Parametersusers.mailFoldersCreateMessageRules)|Not Found|
|[az mail usersmailfolder create-multi-value-extended-property](#users.mailFoldersCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersCreateMultiValueExtendedProperties)|Not Found|
|[az mail usersmailfolder create-single-value-extended-property](#users.mailFoldersCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersCreateSingleValueExtendedProperties)|Not Found|
|[az mail usersmailfolder delete-child-folder](#users.mailFoldersDeleteChildFolders)|DeleteChildFolders|[Parameters](#Parametersusers.mailFoldersDeleteChildFolders)|Not Found|
|[az mail usersmailfolder delete-message](#users.mailFoldersDeleteMessages)|DeleteMessages|[Parameters](#Parametersusers.mailFoldersDeleteMessages)|Not Found|
|[az mail usersmailfolder delete-message-rule](#users.mailFoldersDeleteMessageRules)|DeleteMessageRules|[Parameters](#Parametersusers.mailFoldersDeleteMessageRules)|Not Found|
|[az mail usersmailfolder delete-multi-value-extended-property](#users.mailFoldersDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersDeleteMultiValueExtendedProperties)|Not Found|
|[az mail usersmailfolder delete-single-value-extended-property](#users.mailFoldersDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersDeleteSingleValueExtendedProperties)|Not Found|
|[az mail usersmailfolder list-child-folder](#users.mailFoldersListChildFolders)|ListChildFolders|[Parameters](#Parametersusers.mailFoldersListChildFolders)|Not Found|
|[az mail usersmailfolder list-message](#users.mailFoldersListMessages)|ListMessages|[Parameters](#Parametersusers.mailFoldersListMessages)|Not Found|
|[az mail usersmailfolder list-message-rule](#users.mailFoldersListMessageRules)|ListMessageRules|[Parameters](#Parametersusers.mailFoldersListMessageRules)|Not Found|
|[az mail usersmailfolder list-multi-value-extended-property](#users.mailFoldersListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersListMultiValueExtendedProperties)|Not Found|
|[az mail usersmailfolder list-single-value-extended-property](#users.mailFoldersListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersListSingleValueExtendedProperties)|Not Found|
|[az mail usersmailfolder show-child-folder](#users.mailFoldersGetChildFolders)|GetChildFolders|[Parameters](#Parametersusers.mailFoldersGetChildFolders)|Not Found|
|[az mail usersmailfolder show-message](#users.mailFoldersGetMessages)|GetMessages|[Parameters](#Parametersusers.mailFoldersGetMessages)|Not Found|
|[az mail usersmailfolder show-message-rule](#users.mailFoldersGetMessageRules)|GetMessageRules|[Parameters](#Parametersusers.mailFoldersGetMessageRules)|Not Found|
|[az mail usersmailfolder show-multi-value-extended-property](#users.mailFoldersGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersGetMultiValueExtendedProperties)|Not Found|
|[az mail usersmailfolder show-single-value-extended-property](#users.mailFoldersGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersGetSingleValueExtendedProperties)|Not Found|
|[az mail usersmailfolder update-child-folder](#users.mailFoldersUpdateChildFolders)|UpdateChildFolders|[Parameters](#Parametersusers.mailFoldersUpdateChildFolders)|Not Found|
|[az mail usersmailfolder update-message](#users.mailFoldersUpdateMessages)|UpdateMessages|[Parameters](#Parametersusers.mailFoldersUpdateMessages)|Not Found|
|[az mail usersmailfolder update-message-rule](#users.mailFoldersUpdateMessageRules)|UpdateMessageRules|[Parameters](#Parametersusers.mailFoldersUpdateMessageRules)|Not Found|
|[az mail usersmailfolder update-multi-value-extended-property](#users.mailFoldersUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersUpdateMultiValueExtendedProperties)|Not Found|
|[az mail usersmailfolder update-single-value-extended-property](#users.mailFoldersUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFoldersUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.mailFolders.messages">Commands in `az mail usersmailfoldersmessage` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az mail usersmailfoldersmessage create-attachment](#users.mailFolders.messagesCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.mailFolders.messagesCreateAttachments)|Not Found|
|[az mail usersmailfoldersmessage create-extension](#users.mailFolders.messagesCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.mailFolders.messagesCreateExtensions)|Not Found|
|[az mail usersmailfoldersmessage create-multi-value-extended-property](#users.mailFolders.messagesCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesCreateMultiValueExtendedProperties)|Not Found|
|[az mail usersmailfoldersmessage create-single-value-extended-property](#users.mailFolders.messagesCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesCreateSingleValueExtendedProperties)|Not Found|
|[az mail usersmailfoldersmessage delete-attachment](#users.mailFolders.messagesDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.mailFolders.messagesDeleteAttachments)|Not Found|
|[az mail usersmailfoldersmessage delete-extension](#users.mailFolders.messagesDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.mailFolders.messagesDeleteExtensions)|Not Found|
|[az mail usersmailfoldersmessage delete-multi-value-extended-property](#users.mailFolders.messagesDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesDeleteMultiValueExtendedProperties)|Not Found|
|[az mail usersmailfoldersmessage delete-single-value-extended-property](#users.mailFolders.messagesDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesDeleteSingleValueExtendedProperties)|Not Found|
|[az mail usersmailfoldersmessage list-attachment](#users.mailFolders.messagesListAttachments)|ListAttachments|[Parameters](#Parametersusers.mailFolders.messagesListAttachments)|Not Found|
|[az mail usersmailfoldersmessage list-extension](#users.mailFolders.messagesListExtensions)|ListExtensions|[Parameters](#Parametersusers.mailFolders.messagesListExtensions)|Not Found|
|[az mail usersmailfoldersmessage list-multi-value-extended-property](#users.mailFolders.messagesListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesListMultiValueExtendedProperties)|Not Found|
|[az mail usersmailfoldersmessage list-single-value-extended-property](#users.mailFolders.messagesListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesListSingleValueExtendedProperties)|Not Found|
|[az mail usersmailfoldersmessage show-attachment](#users.mailFolders.messagesGetAttachments)|GetAttachments|[Parameters](#Parametersusers.mailFolders.messagesGetAttachments)|Not Found|
|[az mail usersmailfoldersmessage show-extension](#users.mailFolders.messagesGetExtensions)|GetExtensions|[Parameters](#Parametersusers.mailFolders.messagesGetExtensions)|Not Found|
|[az mail usersmailfoldersmessage show-multi-value-extended-property](#users.mailFolders.messagesGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesGetMultiValueExtendedProperties)|Not Found|
|[az mail usersmailfoldersmessage show-single-value-extended-property](#users.mailFolders.messagesGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesGetSingleValueExtendedProperties)|Not Found|
|[az mail usersmailfoldersmessage update-attachment](#users.mailFolders.messagesUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.mailFolders.messagesUpdateAttachments)|Not Found|
|[az mail usersmailfoldersmessage update-extension](#users.mailFolders.messagesUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.mailFolders.messagesUpdateExtensions)|Not Found|
|[az mail usersmailfoldersmessage update-multi-value-extended-property](#users.mailFolders.messagesUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesUpdateMultiValueExtendedProperties)|Not Found|
|[az mail usersmailfoldersmessage update-single-value-extended-property](#users.mailFolders.messagesUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.mailFolders.messagesUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.messages">Commands in `az mail usersmessage` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az mail usersmessage create-attachment](#users.messagesCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.messagesCreateAttachments)|Not Found|
|[az mail usersmessage create-extension](#users.messagesCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.messagesCreateExtensions)|Not Found|
|[az mail usersmessage create-multi-value-extended-property](#users.messagesCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.messagesCreateMultiValueExtendedProperties)|Not Found|
|[az mail usersmessage create-single-value-extended-property](#users.messagesCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.messagesCreateSingleValueExtendedProperties)|Not Found|
|[az mail usersmessage delete-attachment](#users.messagesDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.messagesDeleteAttachments)|Not Found|
|[az mail usersmessage delete-extension](#users.messagesDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.messagesDeleteExtensions)|Not Found|
|[az mail usersmessage delete-multi-value-extended-property](#users.messagesDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.messagesDeleteMultiValueExtendedProperties)|Not Found|
|[az mail usersmessage delete-single-value-extended-property](#users.messagesDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.messagesDeleteSingleValueExtendedProperties)|Not Found|
|[az mail usersmessage list-attachment](#users.messagesListAttachments)|ListAttachments|[Parameters](#Parametersusers.messagesListAttachments)|Not Found|
|[az mail usersmessage list-extension](#users.messagesListExtensions)|ListExtensions|[Parameters](#Parametersusers.messagesListExtensions)|Not Found|
|[az mail usersmessage list-multi-value-extended-property](#users.messagesListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.messagesListMultiValueExtendedProperties)|Not Found|
|[az mail usersmessage list-single-value-extended-property](#users.messagesListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.messagesListSingleValueExtendedProperties)|Not Found|
|[az mail usersmessage show-attachment](#users.messagesGetAttachments)|GetAttachments|[Parameters](#Parametersusers.messagesGetAttachments)|Not Found|
|[az mail usersmessage show-extension](#users.messagesGetExtensions)|GetExtensions|[Parameters](#Parametersusers.messagesGetExtensions)|Not Found|
|[az mail usersmessage show-multi-value-extended-property](#users.messagesGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.messagesGetMultiValueExtendedProperties)|Not Found|
|[az mail usersmessage show-single-value-extended-property](#users.messagesGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.messagesGetSingleValueExtendedProperties)|Not Found|
|[az mail usersmessage update-attachment](#users.messagesUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.messagesUpdateAttachments)|Not Found|
|[az mail usersmessage update-extension](#users.messagesUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.messagesUpdateExtensions)|Not Found|
|[az mail usersmessage update-multi-value-extended-property](#users.messagesUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.messagesUpdateMultiValueExtendedProperties)|Not Found|
|[az mail usersmessage update-single-value-extended-property](#users.messagesUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.messagesUpdateSingleValueExtendedProperties)|Not Found|


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
|**--body**|object|New navigation property|body|body|

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
|**--body**|object|New navigation property values|body|body|

### group `az mail usersinferenceclassification`
#### <a name="users.inferenceClassificationCreateOverrides">Command `az mail usersinferenceclassification create-override`</a>

##### <a name="Parametersusers.inferenceClassificationCreateOverrides">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--classify-as**|choice||classify_as|classifyAs|
|**--sender-email-address**|object|emailAddress|sender_email_address|senderEmailAddress|

#### <a name="users.inferenceClassificationDeleteOverrides">Command `az mail usersinferenceclassification delete-override`</a>

##### <a name="Parametersusers.inferenceClassificationDeleteOverrides">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.inferenceClassificationListOverrides">Command `az mail usersinferenceclassification list-override`</a>

##### <a name="Parametersusers.inferenceClassificationListOverrides">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.inferenceClassificationGetOverrides">Command `az mail usersinferenceclassification show-override`</a>

##### <a name="Parametersusers.inferenceClassificationGetOverrides">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.inferenceClassificationUpdateOverrides">Command `az mail usersinferenceclassification update-override`</a>

##### <a name="Parametersusers.inferenceClassificationUpdateOverrides">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--inference-classification-override-id**|string|key: id of inferenceClassificationOverride|inference_classification_override_id|inferenceClassificationOverride-id|
|**--id**|string|Read-only.|id|id|
|**--classify-as**|choice||classify_as|classifyAs|
|**--sender-email-address**|object|emailAddress|sender_email_address|senderEmailAddress|

### group `az mail usersmailfolder`
#### <a name="users.mailFoldersCreateChildFolders">Command `az mail usersmailfolder create-child-folder`</a>

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

#### <a name="users.mailFoldersCreateMessages">Command `az mail usersmailfolder create-message`</a>

##### <a name="Parametersusers.mailFoldersCreateMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.mailFoldersCreateMessageRules">Command `az mail usersmailfolder create-message-rule`</a>

##### <a name="Parametersusers.mailFoldersCreateMessageRules">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.mailFoldersCreateMultiValueExtendedProperties">Command `az mail usersmailfolder create-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.mailFoldersCreateSingleValueExtendedProperties">Command `az mail usersmailfolder create-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.mailFoldersDeleteChildFolders">Command `az mail usersmailfolder delete-child-folder`</a>

##### <a name="Parametersusers.mailFoldersDeleteChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFoldersDeleteMessages">Command `az mail usersmailfolder delete-message`</a>

##### <a name="Parametersusers.mailFoldersDeleteMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFoldersDeleteMessageRules">Command `az mail usersmailfolder delete-message-rule`</a>

##### <a name="Parametersusers.mailFoldersDeleteMessageRules">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-rule-id**|string|key: id of messageRule|message_rule_id|messageRule-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFoldersDeleteMultiValueExtendedProperties">Command `az mail usersmailfolder delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFoldersDeleteSingleValueExtendedProperties">Command `az mail usersmailfolder delete-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFoldersListChildFolders">Command `az mail usersmailfolder list-child-folder`</a>

##### <a name="Parametersusers.mailFoldersListChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersListMessages">Command `az mail usersmailfolder list-message`</a>

##### <a name="Parametersusers.mailFoldersListMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersListMessageRules">Command `az mail usersmailfolder list-message-rule`</a>

##### <a name="Parametersusers.mailFoldersListMessageRules">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersListMultiValueExtendedProperties">Command `az mail usersmailfolder list-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersListSingleValueExtendedProperties">Command `az mail usersmailfolder list-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersGetChildFolders">Command `az mail usersmailfolder show-child-folder`</a>

##### <a name="Parametersusers.mailFoldersGetChildFolders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersGetMessages">Command `az mail usersmailfolder show-message`</a>

##### <a name="Parametersusers.mailFoldersGetMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersGetMessageRules">Command `az mail usersmailfolder show-message-rule`</a>

##### <a name="Parametersusers.mailFoldersGetMessageRules">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-rule-id**|string|key: id of messageRule|message_rule_id|messageRule-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersGetMultiValueExtendedProperties">Command `az mail usersmailfolder show-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersGetSingleValueExtendedProperties">Command `az mail usersmailfolder show-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFoldersUpdateChildFolders">Command `az mail usersmailfolder update-child-folder`</a>

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

#### <a name="users.mailFoldersUpdateMessages">Command `az mail usersmailfolder update-message`</a>

##### <a name="Parametersusers.mailFoldersUpdateMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.mailFoldersUpdateMessageRules">Command `az mail usersmailfolder update-message-rule`</a>

##### <a name="Parametersusers.mailFoldersUpdateMessageRules">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-rule-id**|string|key: id of messageRule|message_rule_id|messageRule-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.mailFoldersUpdateMultiValueExtendedProperties">Command `az mail usersmailfolder update-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.mailFoldersUpdateSingleValueExtendedProperties">Command `az mail usersmailfolder update-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFoldersUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az mail usersmailfoldersmessage`
#### <a name="users.mailFolders.messagesCreateAttachments">Command `az mail usersmailfoldersmessage create-attachment`</a>

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

#### <a name="users.mailFolders.messagesCreateExtensions">Command `az mail usersmailfoldersmessage create-extension`</a>

##### <a name="Parametersusers.mailFolders.messagesCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.mailFolders.messagesCreateMultiValueExtendedProperties">Command `az mail usersmailfoldersmessage create-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.mailFolders.messagesCreateSingleValueExtendedProperties">Command `az mail usersmailfoldersmessage create-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.mailFolders.messagesDeleteAttachments">Command `az mail usersmailfoldersmessage delete-attachment`</a>

##### <a name="Parametersusers.mailFolders.messagesDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFolders.messagesDeleteExtensions">Command `az mail usersmailfoldersmessage delete-extension`</a>

##### <a name="Parametersusers.mailFolders.messagesDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFolders.messagesDeleteMultiValueExtendedProperties">Command `az mail usersmailfoldersmessage delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFolders.messagesDeleteSingleValueExtendedProperties">Command `az mail usersmailfoldersmessage delete-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.mailFolders.messagesListAttachments">Command `az mail usersmailfoldersmessage list-attachment`</a>

##### <a name="Parametersusers.mailFolders.messagesListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesListExtensions">Command `az mail usersmailfoldersmessage list-extension`</a>

##### <a name="Parametersusers.mailFolders.messagesListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesListMultiValueExtendedProperties">Command `az mail usersmailfoldersmessage list-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesListSingleValueExtendedProperties">Command `az mail usersmailfoldersmessage list-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesGetAttachments">Command `az mail usersmailfoldersmessage show-attachment`</a>

##### <a name="Parametersusers.mailFolders.messagesGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesGetExtensions">Command `az mail usersmailfoldersmessage show-extension`</a>

##### <a name="Parametersusers.mailFolders.messagesGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesGetMultiValueExtendedProperties">Command `az mail usersmailfoldersmessage show-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesGetSingleValueExtendedProperties">Command `az mail usersmailfoldersmessage show-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.mailFolders.messagesUpdateAttachments">Command `az mail usersmailfoldersmessage update-attachment`</a>

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

#### <a name="users.mailFolders.messagesUpdateExtensions">Command `az mail usersmailfoldersmessage update-extension`</a>

##### <a name="Parametersusers.mailFolders.messagesUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.mailFolders.messagesUpdateMultiValueExtendedProperties">Command `az mail usersmailfoldersmessage update-multi-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.mailFolders.messagesUpdateSingleValueExtendedProperties">Command `az mail usersmailfoldersmessage update-single-value-extended-property`</a>

##### <a name="Parametersusers.mailFolders.messagesUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az mail usersmessage`
#### <a name="users.messagesCreateAttachments">Command `az mail usersmessage create-attachment`</a>

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

#### <a name="users.messagesCreateExtensions">Command `az mail usersmessage create-extension`</a>

##### <a name="Parametersusers.messagesCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.messagesCreateMultiValueExtendedProperties">Command `az mail usersmessage create-multi-value-extended-property`</a>

##### <a name="Parametersusers.messagesCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.messagesCreateSingleValueExtendedProperties">Command `az mail usersmessage create-single-value-extended-property`</a>

##### <a name="Parametersusers.messagesCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.messagesDeleteAttachments">Command `az mail usersmessage delete-attachment`</a>

##### <a name="Parametersusers.messagesDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.messagesDeleteExtensions">Command `az mail usersmessage delete-extension`</a>

##### <a name="Parametersusers.messagesDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.messagesDeleteMultiValueExtendedProperties">Command `az mail usersmessage delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.messagesDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.messagesDeleteSingleValueExtendedProperties">Command `az mail usersmessage delete-single-value-extended-property`</a>

##### <a name="Parametersusers.messagesDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.messagesListAttachments">Command `az mail usersmessage list-attachment`</a>

##### <a name="Parametersusers.messagesListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesListExtensions">Command `az mail usersmessage list-extension`</a>

##### <a name="Parametersusers.messagesListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesListMultiValueExtendedProperties">Command `az mail usersmessage list-multi-value-extended-property`</a>

##### <a name="Parametersusers.messagesListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesListSingleValueExtendedProperties">Command `az mail usersmessage list-single-value-extended-property`</a>

##### <a name="Parametersusers.messagesListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesGetAttachments">Command `az mail usersmessage show-attachment`</a>

##### <a name="Parametersusers.messagesGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesGetExtensions">Command `az mail usersmessage show-extension`</a>

##### <a name="Parametersusers.messagesGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesGetMultiValueExtendedProperties">Command `az mail usersmessage show-multi-value-extended-property`</a>

##### <a name="Parametersusers.messagesGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesGetSingleValueExtendedProperties">Command `az mail usersmessage show-single-value-extended-property`</a>

##### <a name="Parametersusers.messagesGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.messagesUpdateAttachments">Command `az mail usersmessage update-attachment`</a>

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

#### <a name="users.messagesUpdateExtensions">Command `az mail usersmessage update-extension`</a>

##### <a name="Parametersusers.messagesUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.messagesUpdateMultiValueExtendedProperties">Command `az mail usersmessage update-multi-value-extended-property`</a>

##### <a name="Parametersusers.messagesUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.messagesUpdateSingleValueExtendedProperties">Command `az mail usersmessage update-single-value-extended-property`</a>

##### <a name="Parametersusers.messagesUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|
