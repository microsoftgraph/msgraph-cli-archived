# Azure CLI Module Creation Report

### conversation group create-conversation

create-conversation a conversation group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-conversation|CreateConversations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--topic**|string|The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.|topic|topic|
|**--has-attachments**|boolean|Indicates whether any of the posts within this Conversation has at least one attachment.|has_attachments|hasAttachments|
|**--last-delivered-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_delivered_date_time|lastDeliveredDateTime|
|**--unique-senders**|array|All the users that sent a message to this Conversation.|unique_senders|uniqueSenders|
|**--preview**|string|A short summary from the body of the latest post in this converstaion.|preview|preview|
|**--threads**|array|A collection of all the conversation threads in the conversation. A navigation property. Read-only. Nullable.|threads|threads|

### conversation group get-conversation

get-conversation a conversation group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-conversation|GetConversations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group list-conversation

list-conversation a conversation group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-conversation|ListConversations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group update

update a conversation group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateConversations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--id**|string|Read-only.|id|id|
|**--topic**|string|The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.|topic|topic|
|**--has-attachments**|boolean|Indicates whether any of the posts within this Conversation has at least one attachment.|has_attachments|hasAttachments|
|**--last-delivered-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_delivered_date_time|lastDeliveredDateTime|
|**--unique-senders**|array|All the users that sent a message to this Conversation.|unique_senders|uniqueSenders|
|**--preview**|string|A short summary from the body of the latest post in this converstaion.|preview|preview|
|**--threads**|array|A collection of all the conversation threads in the conversation. A navigation property. Read-only. Nullable.|threads|threads|

### conversation group-conversation create-thread

create-thread a conversation group-conversation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation|groups.conversations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-thread|CreateThreads|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--id**|string|Read-only.|id|id|
|**--to-recipients**|array|The To: recipients for the thread.|to_recipients|toRecipients|
|**--topic**|string|The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.|topic|topic|
|**--has-attachments**|boolean|Indicates whether any of the posts within this thread has at least one attachment.|has_attachments|hasAttachments|
|**--last-delivered-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_delivered_date_time|lastDeliveredDateTime|
|**--unique-senders**|array|All the users that sent a message to this thread.|unique_senders|uniqueSenders|
|**--cc-recipients**|array|The Cc: recipients for the thread.|cc_recipients|ccRecipients|
|**--preview**|string|A short summary from the body of the latest post in this converstaion.|preview|preview|
|**--is-locked**|boolean|Indicates if the thread is locked.|is_locked|isLocked|
|**--posts**|array|Read-only. Nullable.|posts|posts|

### conversation group-conversation get-thread

get-thread a conversation group-conversation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation|groups.conversations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-thread|GetThreads|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation list-thread

list-thread a conversation group-conversation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation|groups.conversations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-thread|ListThreads|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation update

update a conversation group-conversation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation|groups.conversations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateThreads|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--id**|string|Read-only.|id|id|
|**--to-recipients**|array|The To: recipients for the thread.|to_recipients|toRecipients|
|**--topic**|string|The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.|topic|topic|
|**--has-attachments**|boolean|Indicates whether any of the posts within this thread has at least one attachment.|has_attachments|hasAttachments|
|**--last-delivered-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_delivered_date_time|lastDeliveredDateTime|
|**--unique-senders**|array|All the users that sent a message to this thread.|unique_senders|uniqueSenders|
|**--cc-recipients**|array|The Cc: recipients for the thread.|cc_recipients|ccRecipients|
|**--preview**|string|A short summary from the body of the latest post in this converstaion.|preview|preview|
|**--is-locked**|boolean|Indicates if the thread is locked.|is_locked|isLocked|
|**--posts**|array|Read-only. Nullable.|posts|posts|

### conversation group-conversation-thread create-post

create-post a conversation group-conversation-thread.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread|groups.conversations.threads|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-post|CreatePosts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--body**|object|itemBody|body|body|
|**--received-date-time**|date-time|Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|received_date_time|receivedDateTime|
|**--has-attachments**|boolean|Indicates whether the post has at least one attachment. This is a default property.|has_attachments|hasAttachments|
|**--microsoft-graph-post-conversation-thread-id-conversation-thread-id**|string|Unique ID of the conversation thread. Read-only.|microsoft_graph_post_conversation_thread_id_conversation_thread_id|conversationThreadId|
|**--new-participants**|array|Conversation participants that were added to the thread as part of this post.|new_participants|newParticipants|
|**--microsoft-graph-post-conversation-id**|string|Unique ID of the conversation. Read-only.|microsoft_graph_post_conversation_id|conversationId|
|**--importance**|choice|importance|importance|importance|
|**--in-reply-to**|object|post|in_reply_to|inReplyTo|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the post. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the post. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--extensions**|array|The collection of open extensions defined for the post. Read-only. Nullable.|extensions|extensions|
|**--attachments**|array|Read-only. Nullable.|attachments|attachments|
|**--mentions**|array||mentions|mentions|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|
|**--from-email-address-name**|string|The display name of the person or entity.|microsoft_graph_email_address_name|name|
|**--from-email-address-address**|string|The email address of the person or entity.|microsoft_graph_email_address|address|

### conversation group-conversation-thread get-post

get-post a conversation group-conversation-thread.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread|groups.conversations.threads|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-post|GetPosts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread list-post

list-post a conversation group-conversation-thread.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread|groups.conversations.threads|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-post|ListPosts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread update

update a conversation group-conversation-thread.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread|groups.conversations.threads|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePosts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--body**|object|itemBody|body|body|
|**--received-date-time**|date-time|Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|received_date_time|receivedDateTime|
|**--has-attachments**|boolean|Indicates whether the post has at least one attachment. This is a default property.|has_attachments|hasAttachments|
|**--microsoft-graph-post-conversation-thread-id-conversation-thread-id**|string|Unique ID of the conversation thread. Read-only.|microsoft_graph_post_conversation_thread_id_conversation_thread_id|conversationThreadId|
|**--new-participants**|array|Conversation participants that were added to the thread as part of this post.|new_participants|newParticipants|
|**--microsoft-graph-post-conversation-id**|string|Unique ID of the conversation. Read-only.|microsoft_graph_post_conversation_id|conversationId|
|**--importance**|choice|importance|importance|importance|
|**--in-reply-to**|object|post|in_reply_to|inReplyTo|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the post. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the post. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--extensions**|array|The collection of open extensions defined for the post. Read-only. Nullable.|extensions|extensions|
|**--attachments**|array|Read-only. Nullable.|attachments|attachments|
|**--mentions**|array||mentions|mentions|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|
|**--from-email-address-name**|string|The display name of the person or entity.|microsoft_graph_email_address_name|name|
|**--from-email-address-address**|string|The email address of the person or entity.|microsoft_graph_email_address|address|

### conversation group-conversation-thread-post create-attachment

create-attachment a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--size**|integer|The length of the attachment in bytes.|size|size|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|

### conversation group-conversation-thread-post create-extension

create-extension a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|

### conversation group-conversation-thread-post create-mention

create-mention a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-mention|CreateMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--mentioned**|object|emailAddress|mentioned|mentioned|
|**--mention-text**|string||mention_text|mentionText|
|**--client-reference**|string||client_reference|clientReference|
|**--created-by**|object|emailAddress|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--server-created-date-time**|date-time||server_created_date_time|serverCreatedDateTime|
|**--deep-link**|string||deep_link|deepLink|
|**--application**|string||application|application|

### conversation group-conversation-thread-post create-multi-value-extended-property

create-multi-value-extended-property a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### conversation group-conversation-thread-post create-single-value-extended-property

create-single-value-extended-property a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### conversation group-conversation-thread-post get-attachment

get-attachment a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--attachment-id**|string|key: attachment-id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post get-extension

get-extension a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--extension-id**|string|key: extension-id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post get-in-reply-to

get-in-reply-to a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-in-reply-to|GetInReplyTo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post get-mention

get-mention a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mention|GetMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--mention-id**|string|key: mention-id of mention|mention_id|mention-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post get-multi-value-extended-property

get-multi-value-extended-property a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post get-single-value-extended-property

get-single-value-extended-property a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post list-attachment

list-attachment a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post list-extension

list-extension a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post list-mention

list-mention a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-mention|ListMentions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post list-multi-value-extended-property

list-multi-value-extended-property a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post list-single-value-extended-property

list-single-value-extended-property a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### conversation group-conversation-thread-post update

update a conversation group-conversation-thread-post.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|conversation group-conversation-thread-post|groups.conversations.threads.posts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAttachments|
|update|UpdateExtensions|
|update|UpdateMentions|
|update|UpdateMultiValueExtendedProperties|
|update|UpdateSingleValueExtendedProperties|
|update|UpdateInReplyTo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--conversation-id**|string|key: conversation-id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: conversationThread-id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: post-id of post|post_id|post-id|
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
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--body**|object|itemBody|body|body|
|**--received-date-time**|date-time|Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|received_date_time|receivedDateTime|
|**--has-attachments**|boolean|Indicates whether the post has at least one attachment. This is a default property.|has_attachments|hasAttachments|
|**--microsoft-graph-post-conversation-thread-id-conversation-thread-id**|string|Unique ID of the conversation thread. Read-only.|microsoft_graph_post_conversation_thread_id_conversation_thread_id|conversationThreadId|
|**--new-participants**|array|Conversation participants that were added to the thread as part of this post.|new_participants|newParticipants|
|**--microsoft-graph-post-conversation-id**|string|Unique ID of the conversation. Read-only.|microsoft_graph_post_conversation_id|conversationId|
|**--importance**|choice|importance|importance|importance|
|**--in-reply-to**|object|post|in_reply_to|inReplyTo|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the post. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the post. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--extensions**|array|The collection of open extensions defined for the post. Read-only. Nullable.|extensions|extensions|
|**--attachments**|array|Read-only. Nullable.|attachments|attachments|
|**--mentions**|array||mentions|mentions|
|**--sender-email-address-name**|string|The display name of the person or entity.|name|name|
|**--sender-email-address-address**|string|The email address of the person or entity.|address|address|
|**--from-email-address-name**|string|The display name of the person or entity.|microsoft_graph_email_address_name|name|
|**--from-email-address-address**|string|The email address of the person or entity.|microsoft_graph_email_address|address|
