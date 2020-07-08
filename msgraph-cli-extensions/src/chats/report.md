# Azure CLI Module Creation Report

### chats chat all-message

all-message a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|all-message|allMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### chats chat create-installed-app

create-installed-app a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-installed-app|CreateInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--teams-app-definition**|object|teamsAppDefinition|teams_app_definition|teamsAppDefinition|
|**--teams-app-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--teams-app-external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--teams-app-name**|string||name|name|
|**--teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|display_name|displayName|
|**--teams-app-distribution-method**|choice|teamsAppDistributionMethod|distribution_method|distributionMethod|
|**--teams-app-app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### chats chat create-member

create-member a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-member|CreateMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--roles**|array||roles|roles|
|**--display-name**|string||display_name|displayName|

### chats chat create-message

create-message a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-message|CreateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--reply-to-id**|string||reply_to_id|replyToId|
|**--etag**|string||etag|etag|
|**--message-type**|choice|chatMessageType|message_type|messageType|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--subject**|string||subject|subject|
|**--body**|object|itemBody|body|body|
|**--summary**|string||summary|summary|
|**--attachments**|array||attachments|attachments|
|**--mentions**|array||mentions|mentions|
|**--importance**|choice|chatMessageImportance|importance|importance|
|**--reactions**|array||reactions|reactions|
|**--locale**|string||locale|locale|
|**--web-url**|string||web_url|webUrl|
|**--replies**|array||replies|replies|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--policy-violation-dlp-action**|choice|chatMessagePolicyViolationDlpActionTypes|dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice|chatMessagePolicyViolationUserActionTypes|user_action|userAction|
|**--policy-violation-verdict-details**|choice|chatMessagePolicyViolationVerdictDetailsTypes|verdict_details|verdictDetails|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|

### chats chat get-installed-app

get-installed-app a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-installed-app|GetInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: teamsAppInstallation-id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat get-member

get-member a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member|GetMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--conversation-member-id**|string|key: conversationMember-id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat get-message

get-message a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-message|GetMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: chatMessage-id of chatMessage|chat_message_id|chatMessage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat list-installed-app

list-installed-app a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-installed-app|ListInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat list-member

list-member a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member|ListMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat list-message

list-message a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-message|ListMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat update

update a chats chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateInstalledApps|
|update|UpdateMembers|
|update|UpdateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: teamsAppInstallation-id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--conversation-member-id**|string|key: conversationMember-id of conversationMember|conversation_member_id|conversationMember-id|
|**--chat-message-id**|string|key: chatMessage-id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--teams-app-definition**|object|teamsAppDefinition|teams_app_definition|teamsAppDefinition|
|**--teams-app-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--teams-app-external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--teams-app-name**|string||name|name|
|**--teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|display_name|displayName|
|**--teams-app-distribution-method**|choice|teamsAppDistributionMethod|distribution_method|distributionMethod|
|**--teams-app-app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|
|**--roles**|array||roles|roles|
|**--display-name**|string||display_name|displayName|
|**--reply-to-id**|string||reply_to_id|replyToId|
|**--etag**|string||etag|etag|
|**--message-type**|choice|chatMessageType|message_type|messageType|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--subject**|string||subject|subject|
|**--body**|object|itemBody|body|body|
|**--summary**|string||summary|summary|
|**--attachments**|array||attachments|attachments|
|**--mentions**|array||mentions|mentions|
|**--importance**|choice|chatMessageImportance|importance|importance|
|**--reactions**|array||reactions|reactions|
|**--locale**|string||locale|locale|
|**--web-url**|string||web_url|webUrl|
|**--replies**|array||replies|replies|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--policy-violation-dlp-action**|choice|chatMessagePolicyViolationDlpActionTypes|dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice|chatMessagePolicyViolationUserActionTypes|user_action|userAction|
|**--policy-violation-verdict-details**|choice|chatMessagePolicyViolationVerdictDetailsTypes|verdict_details|verdictDetails|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|

### chats chat-chat create-chat

create-chat a chats chat-chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-chat|chats.chat|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-chat|CreateChat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--topic**|string||topic|topic|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--members**|array||members|members|
|**--messages**|array||messages|messages|
|**--installed-apps**|array||installed_apps|installedApps|

### chats chat-chat delete

delete a chats chat-chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-chat|chats.chat|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteChat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--if-match**|string|ETag|if_match|If-Match|

### chats chat-chat get-chat

get-chat a chats chat-chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-chat|chats.chat|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-chat|GetChat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat-chat list-chat

list-chat a chats chat-chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-chat|chats.chat|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-chat|ListChat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat-chat update

update a chats chat-chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-chat|chats.chat|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateChat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--topic**|string||topic|topic|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--members**|array||members|members|
|**--messages**|array||messages|messages|
|**--installed-apps**|array||installed_apps|installedApps|

### chats chat-installed-app get-team-app

get-team-app a chats chat-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-installed-app|chats.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-app|GetTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: teamsAppInstallation-id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat-installed-app get-team-app-definition

get-team-app-definition a chats chat-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-installed-app|chats.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-app-definition|GetTeamsAppDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: teamsAppInstallation-id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat-installed-app upgrade

upgrade a chats chat-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-installed-app|chats.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|upgrade|upgrade|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: teamsAppInstallation-id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

### chats chat-message create-hosted-content

create-hosted-content a chats chat-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-message|chats.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-hosted-content|CreateHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: chatMessage-id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|

### chats chat-message create-reply

create-reply a chats chat-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-message|chats.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-reply|CreateReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: chatMessage-id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--reply-to-id**|string||reply_to_id|replyToId|
|**--etag**|string||etag|etag|
|**--message-type**|choice|chatMessageType|message_type|messageType|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--subject**|string||subject|subject|
|**--body**|object|itemBody|body|body|
|**--summary**|string||summary|summary|
|**--attachments**|array||attachments|attachments|
|**--mentions**|array||mentions|mentions|
|**--importance**|choice|chatMessageImportance|importance|importance|
|**--reactions**|array||reactions|reactions|
|**--locale**|string||locale|locale|
|**--web-url**|string||web_url|webUrl|
|**--replies**|array||replies|replies|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--policy-violation-dlp-action**|choice|chatMessagePolicyViolationDlpActionTypes|dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice|chatMessagePolicyViolationUserActionTypes|user_action|userAction|
|**--policy-violation-verdict-details**|choice|chatMessagePolicyViolationVerdictDetailsTypes|verdict_details|verdictDetails|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|

### chats chat-message delta

delta a chats chat-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-message|chats.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|

### chats chat-message get-hosted-content

get-hosted-content a chats chat-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-message|chats.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-hosted-content|GetHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: chatMessage-id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: chatMessageHostedContent-id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat-message get-reply

get-reply a chats chat-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-message|chats.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-reply|GetReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: chatMessage-id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: chatMessage-id of chatMessage|chat_message_id1|chatMessage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat-message list-hosted-content

list-hosted-content a chats chat-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-message|chats.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-hosted-content|ListHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: chatMessage-id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat-message list-reply

list-reply a chats chat-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-message|chats.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-reply|ListReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: chatMessage-id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats chat-message update

update a chats chat-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-message|chats.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateHostedContents|
|update|UpdateReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: chatMessage-id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: chatMessageHostedContent-id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--chat-message-id1**|string|key: chatMessage-id of chatMessage|chat_message_id1|chatMessage-id1|
|**--id**|string|Read-only.|id|id|
|**--reply-to-id**|string||reply_to_id|replyToId|
|**--etag**|string||etag|etag|
|**--message-type**|choice|chatMessageType|message_type|messageType|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--subject**|string||subject|subject|
|**--body**|object|itemBody|body|body|
|**--summary**|string||summary|summary|
|**--attachments**|array||attachments|attachments|
|**--mentions**|array||mentions|mentions|
|**--importance**|choice|chatMessageImportance|importance|importance|
|**--reactions**|array||reactions|reactions|
|**--locale**|string||locale|locale|
|**--web-url**|string||web_url|webUrl|
|**--replies**|array||replies|replies|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--policy-violation-dlp-action**|choice|chatMessagePolicyViolationDlpActionTypes|dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice|chatMessagePolicyViolationUserActionTypes|user_action|userAction|
|**--policy-violation-verdict-details**|choice|chatMessagePolicyViolationVerdictDetailsTypes|verdict_details|verdictDetails|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|

### chats chat-message-reply delta

delta a chats chat-message-reply.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats chat-message-reply|chats.messages.replies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: chatMessage-id of chatMessage|chat_message_id|chatMessage-id|

### chats user create-chat

create-chat a chats user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-chat|CreateChats|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--topic**|string||topic|topic|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--members**|array||members|members|
|**--messages**|array||messages|messages|
|**--installed-apps**|array||installed_apps|installedApps|

### chats user get-chat

get-chat a chats user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-chat|GetChats|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats user list-chat

list-chat a chats user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-chat|ListChats|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### chats user update

update a chats user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|chats user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateChats|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--chat-id**|string|key: chat-id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--topic**|string||topic|topic|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--members**|array||members|members|
|**--messages**|array||messages|messages|
|**--installed-apps**|array||installed_apps|installedApps|
