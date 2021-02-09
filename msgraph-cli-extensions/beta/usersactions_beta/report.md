# Azure CLI Module Creation Report

### usersactions user assign-license

assign-license a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|assign-license|assignLicense|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--add-licenses**|array||add_licenses|addLicenses|
|**--remove-licenses**|array||remove_licenses|removeLicenses|

### usersactions user change-password

change-password a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|change-password|changePassword|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--current-password**|string||current_password|currentPassword|
|**--new-password**|string||new_password|newPassword|

### usersactions user check-member-group

check-member-group a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--group-ids**|array||group_ids|groupIds|

### usersactions user check-member-object

check-member-object a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--ids**|array||ids|ids|

### usersactions user export-personal-data

export-personal-data a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|export-personal-data|exportPersonalData|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--storage-location**|string||storage_location|storageLocation|

### usersactions user find-meeting-time

find-meeting-time a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|find-meeting-time|findMeetingTimes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--attendees**|array||attendees|attendees|
|**--meeting-duration**|duration||meeting_duration|meetingDuration|
|**--max-candidates**|integer||max_candidates|maxCandidates|
|**--is-organizer-optional**|boolean||is_organizer_optional|isOrganizerOptional|
|**--return-suggestion-reasons**|boolean||return_suggestion_reasons|returnSuggestionReasons|
|**--minimum-attendee-percentage**|number||minimum_attendee_percentage|minimumAttendeePercentage|
|**--time-constraint-activity-domain**|choice||activity_domain|activityDomain|
|**--time-constraint-time-slots**|array||time_slots|timeSlots|
|**--location-constraint-is-required**|boolean|The client requests the service to include in the response a meeting location for the meeting. If this is true and all the resources are busy, findMeetingTimes will not return any meeting time suggestions. If this is false and all the resources are busy, findMeetingTimes would still look for meeting times without locations.|is_required|isRequired|
|**--location-constraint-locations**|array|Constraint information for one or more locations that the client requests for the meeting.|locations|locations|
|**--location-constraint-suggest-location**|boolean|The client requests the service to suggest one or more meeting locations.|suggest_location|suggestLocation|

### usersactions user get-by-id

get-by-id a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### usersactions user get-mail-tip

get-mail-tip a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mail-tip|getMailTips|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--email-addresses**|array||email_addresses|EmailAddresses|
|**--mail-tips-options**|choice||mail_tips_options|MailTipsOptions|

### usersactions user get-member-group

get-member-group a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### usersactions user get-member-object

get-member-object a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### usersactions user get-user-owned-object

get-user-owned-object a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-owned-object|getUserOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string||user_id|userId|
|**--type**|string||type|type|

### usersactions user invalidate-all-refresh-token

invalidate-all-refresh-token a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|invalidate-all-refresh-token|invalidateAllRefreshTokens|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions user remove-all-device-from-management

remove-all-device-from-management a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remove-all-device-from-management|removeAllDevicesFromManagement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions user reprocess-license-assignment

reprocess-license-assignment a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reprocess-license-assignment|reprocessLicenseAssignment|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions user restore

restore a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions user revoke-sign-in-session

revoke-sign-in-session a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|revoke-sign-in-session|revokeSignInSessions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions user send-mail

send-mail a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send-mail|sendMail|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--save-to-sent-items**|boolean||save_to_sent_items|SaveToSentItems|
|**--message-id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user translate-exchange-id

translate-exchange-id a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|translate-exchange-id|translateExchangeIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--input-ids**|array||input_ids|InputIds|
|**--target-id-type**|choice||target_id_type|TargetIdType|
|**--source-id-type**|choice||source_id_type|SourceIdType|

### usersactions user unblock-managed-app

unblock-managed-app a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unblock-managed-app|unblockManagedApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions user validate-property

validate-property a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|validate-property|validateProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### usersactions user wipe-and-block-managed-app

wipe-and-block-managed-app a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|wipe-and-block-managed-app|wipeAndBlockManagedApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions user wipe-managed-app-registration-by-device-tag

wipe-managed-app-registration-by-device-tag a usersactions user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|wipe-managed-app-registration-by-device-tag|wipeManagedAppRegistrationByDeviceTag|
|wipe-managed-app-registration-by-device-tag|wipeManagedAppRegistrationsByDeviceTag|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-tag**|string||device_tag|deviceTag|

### usersactions user-authentication-method disable-sm-sign-in

disable-sm-sign-in a usersactions user-authentication-method.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-authentication-method|users.authentication.methods|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|disable-sm-sign-in|disableSmsSignIn|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--authentication-method-id**|string|key: id of authenticationMethod|authentication_method_id|authenticationMethod-id|

### usersactions user-authentication-method enable-sm-sign-in

enable-sm-sign-in a usersactions user-authentication-method.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-authentication-method|users.authentication.methods|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|enable-sm-sign-in|enableSmsSignIn|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--authentication-method-id**|string|key: id of authenticationMethod|authentication_method_id|authenticationMethod-id|

### usersactions user-authentication-method reset-password

reset-password a usersactions user-authentication-method.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-authentication-method|users.authentication.methods|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reset-password|resetPassword|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--authentication-method-id**|string|key: id of authenticationMethod|authentication_method_id|authenticationMethod-id|
|**--new-password**|string||new_password|newPassword|
|**--require-change-on-next-sign-in**|boolean||require_change_on_next_sign_in|requireChangeOnNextSignIn|

### usersactions user-calendar get-schedule

get-schedule a usersactions user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schedule|getSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### usersactions user-calendar-calendar-view accept

accept a usersactions user-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view|users.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-calendar-view cancel

cancel a usersactions user-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view|users.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-calendar-view decline

decline a usersactions user-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view|users.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-calendar-view dismiss-reminder

dismiss-reminder a usersactions user-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view|users.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|

### usersactions user-calendar-calendar-view forward

forward a usersactions user-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view|users.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-calendar-view snooze-reminder

snooze-reminder a usersactions user-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view|users.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-calendar-view tentatively-accept

tentatively-accept a usersactions user-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view|users.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-calendar-view-attachment create-upload-session

create-upload-session a usersactions user-calendar-calendar-view-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-attachment|users.calendars.calendarView.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-calendar-calendar-view-calendar get-schedule

get-schedule a usersactions user-calendar-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-calendar|users.calendars.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schedule|getSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### usersactions user-calendar-calendar-view-exception-occurrence accept

accept a usersactions user-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-exception-occurrence|users.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-calendar-view-exception-occurrence cancel

cancel a usersactions user-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-exception-occurrence|users.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-calendar-view-exception-occurrence decline

decline a usersactions user-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-exception-occurrence|users.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-calendar-view-exception-occurrence dismiss-reminder

dismiss-reminder a usersactions user-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-exception-occurrence|users.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-calendar-view-exception-occurrence forward

forward a usersactions user-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-exception-occurrence|users.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-calendar-view-exception-occurrence snooze-reminder

snooze-reminder a usersactions user-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-exception-occurrence|users.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-calendar-view-exception-occurrence tentatively-accept

tentatively-accept a usersactions user-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-exception-occurrence|users.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-calendar-view-instance accept

accept a usersactions user-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-instance|users.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-calendar-view-instance cancel

cancel a usersactions user-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-instance|users.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-calendar-view-instance decline

decline a usersactions user-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-instance|users.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-calendar-view-instance dismiss-reminder

dismiss-reminder a usersactions user-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-instance|users.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-calendar-view-instance forward

forward a usersactions user-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-instance|users.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-calendar-view-instance snooze-reminder

snooze-reminder a usersactions user-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-instance|users.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-calendar-view-instance tentatively-accept

tentatively-accept a usersactions user-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-calendar-view-instance|users.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-event accept

accept a usersactions user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-event cancel

cancel a usersactions user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-event decline

decline a usersactions user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-event dismiss-reminder

dismiss-reminder a usersactions user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|

### usersactions user-calendar-event forward

forward a usersactions user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-event snooze-reminder

snooze-reminder a usersactions user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-event tentatively-accept

tentatively-accept a usersactions user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-event-attachment create-upload-session

create-upload-session a usersactions user-calendar-event-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-attachment|users.calendars.events.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-calendar-event-calendar get-schedule

get-schedule a usersactions user-calendar-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-calendar|users.calendars.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schedule|getSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### usersactions user-calendar-event-exception-occurrence accept

accept a usersactions user-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-exception-occurrence|users.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-event-exception-occurrence cancel

cancel a usersactions user-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-exception-occurrence|users.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-event-exception-occurrence decline

decline a usersactions user-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-exception-occurrence|users.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-event-exception-occurrence dismiss-reminder

dismiss-reminder a usersactions user-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-exception-occurrence|users.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-event-exception-occurrence forward

forward a usersactions user-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-exception-occurrence|users.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-event-exception-occurrence snooze-reminder

snooze-reminder a usersactions user-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-exception-occurrence|users.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-event-exception-occurrence tentatively-accept

tentatively-accept a usersactions user-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-exception-occurrence|users.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-event-instance accept

accept a usersactions user-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-instance|users.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-event-instance cancel

cancel a usersactions user-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-instance|users.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-event-instance decline

decline a usersactions user-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-instance|users.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-event-instance dismiss-reminder

dismiss-reminder a usersactions user-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-instance|users.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-event-instance forward

forward a usersactions user-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-instance|users.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-event-instance snooze-reminder

snooze-reminder a usersactions user-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-instance|users.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-event-instance tentatively-accept

tentatively-accept a usersactions user-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-event-instance|users.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar get-schedule

get-schedule a usersactions user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schedule|getSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### usersactions user-calendar-group-calendar-calendar-view accept

accept a usersactions user-calendar-group-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-calendar-view cancel

cancel a usersactions user-calendar-group-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-calendar-view decline

decline a usersactions user-calendar-group-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-calendar-view dismiss-reminder

dismiss-reminder a usersactions user-calendar-group-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|

### usersactions user-calendar-group-calendar-calendar-view forward

forward a usersactions user-calendar-group-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-calendar-view snooze-reminder

snooze-reminder a usersactions user-calendar-group-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-group-calendar-calendar-view tentatively-accept

tentatively-accept a usersactions user-calendar-group-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-calendar-view-attachment create-upload-session

create-upload-session a usersactions user-calendar-group-calendar-calendar-view-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-attachment|users.calendarGroups.calendars.calendarView.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-calendar-group-calendar-calendar-view-calendar get-schedule

get-schedule a usersactions user-calendar-group-calendar-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-calendar|users.calendarGroups.calendars.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schedule|getSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### usersactions user-calendar-group-calendar-calendar-view-exception-occurrence accept

accept a usersactions user-calendar-group-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-exception-occurrence|users.calendarGroups.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-calendar-view-exception-occurrence cancel

cancel a usersactions user-calendar-group-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-exception-occurrence|users.calendarGroups.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-calendar-view-exception-occurrence decline

decline a usersactions user-calendar-group-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-exception-occurrence|users.calendarGroups.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-calendar-view-exception-occurrence dismiss-reminder

dismiss-reminder a usersactions user-calendar-group-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-exception-occurrence|users.calendarGroups.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-group-calendar-calendar-view-exception-occurrence forward

forward a usersactions user-calendar-group-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-exception-occurrence|users.calendarGroups.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-calendar-view-exception-occurrence snooze-reminder

snooze-reminder a usersactions user-calendar-group-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-exception-occurrence|users.calendarGroups.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-group-calendar-calendar-view-exception-occurrence tentatively-accept

tentatively-accept a usersactions user-calendar-group-calendar-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-exception-occurrence|users.calendarGroups.calendars.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-calendar-view-instance accept

accept a usersactions user-calendar-group-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-instance|users.calendarGroups.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-calendar-view-instance cancel

cancel a usersactions user-calendar-group-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-instance|users.calendarGroups.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-calendar-view-instance decline

decline a usersactions user-calendar-group-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-instance|users.calendarGroups.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-calendar-view-instance dismiss-reminder

dismiss-reminder a usersactions user-calendar-group-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-instance|users.calendarGroups.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-group-calendar-calendar-view-instance forward

forward a usersactions user-calendar-group-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-instance|users.calendarGroups.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-calendar-view-instance snooze-reminder

snooze-reminder a usersactions user-calendar-group-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-instance|users.calendarGroups.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-group-calendar-calendar-view-instance tentatively-accept

tentatively-accept a usersactions user-calendar-group-calendar-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-calendar-view-instance|users.calendarGroups.calendars.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-event accept

accept a usersactions user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-event cancel

cancel a usersactions user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-event decline

decline a usersactions user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-event dismiss-reminder

dismiss-reminder a usersactions user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|

### usersactions user-calendar-group-calendar-event forward

forward a usersactions user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-event snooze-reminder

snooze-reminder a usersactions user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-group-calendar-event tentatively-accept

tentatively-accept a usersactions user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-event-attachment create-upload-session

create-upload-session a usersactions user-calendar-group-calendar-event-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-attachment|users.calendarGroups.calendars.events.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-calendar-group-calendar-event-calendar get-schedule

get-schedule a usersactions user-calendar-group-calendar-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-calendar|users.calendarGroups.calendars.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schedule|getSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### usersactions user-calendar-group-calendar-event-exception-occurrence accept

accept a usersactions user-calendar-group-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-exception-occurrence|users.calendarGroups.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-event-exception-occurrence cancel

cancel a usersactions user-calendar-group-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-exception-occurrence|users.calendarGroups.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-event-exception-occurrence decline

decline a usersactions user-calendar-group-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-exception-occurrence|users.calendarGroups.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-event-exception-occurrence dismiss-reminder

dismiss-reminder a usersactions user-calendar-group-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-exception-occurrence|users.calendarGroups.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-group-calendar-event-exception-occurrence forward

forward a usersactions user-calendar-group-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-exception-occurrence|users.calendarGroups.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-event-exception-occurrence snooze-reminder

snooze-reminder a usersactions user-calendar-group-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-exception-occurrence|users.calendarGroups.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-group-calendar-event-exception-occurrence tentatively-accept

tentatively-accept a usersactions user-calendar-group-calendar-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-exception-occurrence|users.calendarGroups.calendars.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-event-instance accept

accept a usersactions user-calendar-group-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-instance|users.calendarGroups.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-event-instance cancel

cancel a usersactions user-calendar-group-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-instance|users.calendarGroups.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-event-instance decline

decline a usersactions user-calendar-group-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-instance|users.calendarGroups.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-group-calendar-event-instance dismiss-reminder

dismiss-reminder a usersactions user-calendar-group-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-instance|users.calendarGroups.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-group-calendar-event-instance forward

forward a usersactions user-calendar-group-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-instance|users.calendarGroups.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-group-calendar-event-instance snooze-reminder

snooze-reminder a usersactions user-calendar-group-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-instance|users.calendarGroups.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-group-calendar-event-instance tentatively-accept

tentatively-accept a usersactions user-calendar-group-calendar-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-group-calendar-event-instance|users.calendarGroups.calendars.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view accept

accept a usersactions user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view cancel

cancel a usersactions user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-view decline

decline a usersactions user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view dismiss-reminder

dismiss-reminder a usersactions user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|

### usersactions user-calendar-view forward

forward a usersactions user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-view snooze-reminder

snooze-reminder a usersactions user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-view tentatively-accept

tentatively-accept a usersactions user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-attachment create-upload-session

create-upload-session a usersactions user-calendar-view-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-attachment|users.calendarView.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-calendar-view-calendar get-schedule

get-schedule a usersactions user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar|users.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schedule|getSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### usersactions user-calendar-view-calendar-calendar-view accept

accept a usersactions user-calendar-view-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-calendar-view|users.calendarView.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-calendar-calendar-view cancel

cancel a usersactions user-calendar-view-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-calendar-view|users.calendarView.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-view-calendar-calendar-view decline

decline a usersactions user-calendar-view-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-calendar-view|users.calendarView.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-calendar-calendar-view dismiss-reminder

dismiss-reminder a usersactions user-calendar-view-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-calendar-view|users.calendarView.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-view-calendar-calendar-view forward

forward a usersactions user-calendar-view-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-calendar-view|users.calendarView.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-view-calendar-calendar-view snooze-reminder

snooze-reminder a usersactions user-calendar-view-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-calendar-view|users.calendarView.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-view-calendar-calendar-view tentatively-accept

tentatively-accept a usersactions user-calendar-view-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-calendar-view|users.calendarView.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-calendar-event accept

accept a usersactions user-calendar-view-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-event|users.calendarView.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-calendar-event cancel

cancel a usersactions user-calendar-view-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-event|users.calendarView.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-view-calendar-event decline

decline a usersactions user-calendar-view-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-event|users.calendarView.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-calendar-event dismiss-reminder

dismiss-reminder a usersactions user-calendar-view-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-event|users.calendarView.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-view-calendar-event forward

forward a usersactions user-calendar-view-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-event|users.calendarView.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-view-calendar-event snooze-reminder

snooze-reminder a usersactions user-calendar-view-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-event|users.calendarView.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-view-calendar-event tentatively-accept

tentatively-accept a usersactions user-calendar-view-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-calendar-event|users.calendarView.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-exception-occurrence accept

accept a usersactions user-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-exception-occurrence|users.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-exception-occurrence cancel

cancel a usersactions user-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-exception-occurrence|users.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-view-exception-occurrence decline

decline a usersactions user-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-exception-occurrence|users.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-exception-occurrence dismiss-reminder

dismiss-reminder a usersactions user-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-exception-occurrence|users.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-view-exception-occurrence forward

forward a usersactions user-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-exception-occurrence|users.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-view-exception-occurrence snooze-reminder

snooze-reminder a usersactions user-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-exception-occurrence|users.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-view-exception-occurrence tentatively-accept

tentatively-accept a usersactions user-calendar-view-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-exception-occurrence|users.calendarView.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-instance accept

accept a usersactions user-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-instance|users.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-instance cancel

cancel a usersactions user-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-instance|users.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-view-instance decline

decline a usersactions user-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-instance|users.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-calendar-view-instance dismiss-reminder

dismiss-reminder a usersactions user-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-instance|users.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-calendar-view-instance forward

forward a usersactions user-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-instance|users.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-calendar-view-instance snooze-reminder

snooze-reminder a usersactions user-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-instance|users.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-calendar-view-instance tentatively-accept

tentatively-accept a usersactions user-calendar-view-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-calendar-view-instance|users.calendarView.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-device-enrollment-configuration assign

assign a usersactions user-device-enrollment-configuration.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-device-enrollment-configuration|users.deviceEnrollmentConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|assign|assign|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-enrollment-configuration-id**|string|key: id of deviceEnrollmentConfiguration|device_enrollment_configuration_id|deviceEnrollmentConfiguration-id|
|**--enrollment-configuration-assignments**|array||enrollment_configuration_assignments|enrollmentConfigurationAssignments|

### usersactions user-device-enrollment-configuration has-payload-link

has-payload-link a usersactions user-device-enrollment-configuration.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-device-enrollment-configuration|users.deviceEnrollmentConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|has-payload-link|hasPayloadLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--payload-ids**|array||payload_ids|payloadIds|

### usersactions user-device-enrollment-configuration set-priority

set-priority a usersactions user-device-enrollment-configuration.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-device-enrollment-configuration|users.deviceEnrollmentConfigurations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-priority|setPriority|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-enrollment-configuration-id**|string|key: id of deviceEnrollmentConfiguration|device_enrollment_configuration_id|deviceEnrollmentConfiguration-id|
|**--priority**|integer||priority|priority|

### usersactions user-event accept

accept a usersactions user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event cancel

cancel a usersactions user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|

### usersactions user-event decline

decline a usersactions user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event dismiss-reminder

dismiss-reminder a usersactions user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|

### usersactions user-event forward

forward a usersactions user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-event snooze-reminder

snooze-reminder a usersactions user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-event tentatively-accept

tentatively-accept a usersactions user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-attachment create-upload-session

create-upload-session a usersactions user-event-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-attachment|users.events.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-event-calendar get-schedule

get-schedule a usersactions user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schedule|getSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### usersactions user-event-calendar-calendar-view accept

accept a usersactions user-event-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-calendar-view|users.events.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-calendar-calendar-view cancel

cancel a usersactions user-event-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-calendar-view|users.events.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-event-calendar-calendar-view decline

decline a usersactions user-event-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-calendar-view|users.events.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-calendar-calendar-view dismiss-reminder

dismiss-reminder a usersactions user-event-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-calendar-view|users.events.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-event-calendar-calendar-view forward

forward a usersactions user-event-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-calendar-view|users.events.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-event-calendar-calendar-view snooze-reminder

snooze-reminder a usersactions user-event-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-calendar-view|users.events.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-event-calendar-calendar-view tentatively-accept

tentatively-accept a usersactions user-event-calendar-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-calendar-view|users.events.calendar.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-calendar-event accept

accept a usersactions user-event-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-event|users.events.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-calendar-event cancel

cancel a usersactions user-event-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-event|users.events.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-event-calendar-event decline

decline a usersactions user-event-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-event|users.events.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-calendar-event dismiss-reminder

dismiss-reminder a usersactions user-event-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-event|users.events.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-event-calendar-event forward

forward a usersactions user-event-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-event|users.events.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-event-calendar-event snooze-reminder

snooze-reminder a usersactions user-event-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-event|users.events.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-event-calendar-event tentatively-accept

tentatively-accept a usersactions user-event-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-calendar-event|users.events.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-exception-occurrence accept

accept a usersactions user-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-exception-occurrence|users.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-exception-occurrence cancel

cancel a usersactions user-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-exception-occurrence|users.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-event-exception-occurrence decline

decline a usersactions user-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-exception-occurrence|users.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-exception-occurrence dismiss-reminder

dismiss-reminder a usersactions user-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-exception-occurrence|users.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-event-exception-occurrence forward

forward a usersactions user-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-exception-occurrence|users.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-event-exception-occurrence snooze-reminder

snooze-reminder a usersactions user-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-exception-occurrence|users.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-event-exception-occurrence tentatively-accept

tentatively-accept a usersactions user-event-exception-occurrence.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-exception-occurrence|users.events.exceptionOccurrences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-instance accept

accept a usersactions user-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-instance|users.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-instance cancel

cancel a usersactions user-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-instance|users.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

### usersactions user-event-instance decline

decline a usersactions user-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-instance|users.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-event-instance dismiss-reminder

dismiss-reminder a usersactions user-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-instance|users.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

### usersactions user-event-instance forward

forward a usersactions user-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-instance|users.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

### usersactions user-event-instance snooze-reminder

snooze-reminder a usersactions user-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-instance|users.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions user-event-instance tentatively-accept

tentatively-accept a usersactions user-event-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-event-instance|users.events.instances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions user-mail-folder copy

copy a usersactions user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy|copy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--destination-id**|string||destination_id|DestinationId|

### usersactions user-mail-folder move

move a usersactions user-mail-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder|users.mailFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|move|move|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--destination-id**|string||destination_id|DestinationId|

### usersactions user-mail-folder-child-folder copy

copy a usersactions user-mail-folder-child-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-child-folder|users.mailFolders.childFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy|copy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--destination-id**|string||destination_id|DestinationId|

### usersactions user-mail-folder-child-folder move

move a usersactions user-mail-folder-child-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-child-folder|users.mailFolders.childFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|move|move|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--mail-folder-id1**|string|key: id of mailFolder|mail_folder_id1|mailFolder-id1|
|**--destination-id**|string||destination_id|DestinationId|

### usersactions user-mail-folder-message copy

copy a usersactions user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy|copy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--destination-id**|string||destination_id|DestinationId|

### usersactions user-mail-folder-message create-forward

create-forward a usersactions user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-forward|createForward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|microsoft_graph_message_to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-mail-folder-message create-reply

create-reply a usersactions user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-reply|createReply|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-mail-folder-message create-reply-all

create-reply-all a usersactions user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-reply-all|createReplyAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-mail-folder-message forward

forward a usersactions user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|microsoft_graph_message_to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-mail-folder-message move

move a usersactions user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|move|move|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--destination-id**|string||destination_id|DestinationId|

### usersactions user-mail-folder-message reply

reply a usersactions user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reply|reply|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-mail-folder-message reply-all

reply-all a usersactions user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reply-all|replyAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-mail-folder-message send

send a usersactions user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send|send|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|

### usersactions user-mail-folder-message unsubscribe

unsubscribe a usersactions user-mail-folder-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message|users.mailFolders.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unsubscribe|unsubscribe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|

### usersactions user-mail-folder-message-attachment create-upload-session

create-upload-session a usersactions user-mail-folder-message-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mail-folder-message-attachment|users.mailFolders.messages.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mail-folder-id**|string|key: id of mailFolder|mail_folder_id|mailFolder-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-managed-device bypass-activation-lock

bypass-activation-lock a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|bypass-activation-lock|bypassActivationLock|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device clean-window-device

clean-window-device a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|clean-window-device|cleanWindowsDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--keep-user-data**|boolean||keep_user_data|keepUserData|

### usersactions user-managed-device create-device-log-collection-request

create-device-log-collection-request a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-device-log-collection-request|createDeviceLogCollectionRequest|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--template-type-id**|string|The unique identifier|id|id|

### usersactions user-managed-device delete-user-from-shared-apple-device

delete-user-from-shared-apple-device a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete-user-from-shared-apple-device|deleteUserFromSharedAppleDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### usersactions user-managed-device disable-lost-mode

disable-lost-mode a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|disable-lost-mode|disableLostMode|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device enable-lost-mode

enable-lost-mode a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|enable-lost-mode|enableLostMode|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--message**|string||message|message|
|**--phone-number**|string||phone_number|phoneNumber|
|**--footer**|string||footer|footer|

### usersactions user-managed-device execute-action

execute-action a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|execute-action|executeAction|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--action-name**|choice||action_name|actionName|
|**--keep-enrollment-data**|boolean||keep_enrollment_data|keepEnrollmentData|
|**--keep-user-data**|boolean||keep_user_data|keepUserData|
|**--device-ids**|array||device_ids|deviceIds|
|**--notification-title**|string||notification_title|notificationTitle|
|**--notification-body**|string||notification_body|notificationBody|
|**--device-name**|string||device_name|deviceName|

### usersactions user-managed-device locate-device

locate-device a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|locate-device|locateDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device logout-shared-apple-device-active-user

logout-shared-apple-device-active-user a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|logout-shared-apple-device-active-user|logoutSharedAppleDeviceActiveUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device override-compliance-state

override-compliance-state a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|override-compliance-state|overrideComplianceState|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--compliance-state**|choice||compliance_state|complianceState|
|**--remediation-url**|string||remediation_url|remediationUrl|

### usersactions user-managed-device play-lost-mode-sound

play-lost-mode-sound a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|play-lost-mode-sound|playLostModeSound|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device reboot-now

reboot-now a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reboot-now|rebootNow|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device recover-passcode

recover-passcode a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|recover-passcode|recoverPasscode|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device remote-lock

remote-lock a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remote-lock|remoteLock|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device request-remote-assistance

request-remote-assistance a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|request-remote-assistance|requestRemoteAssistance|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device reset-passcode

reset-passcode a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reset-passcode|resetPasscode|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device retire

retire a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|retire|retire|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device revoke-apple-vpp-license

revoke-apple-vpp-license a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|revoke-apple-vpp-license|revokeAppleVppLicenses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device rotate-bit-locker-key

rotate-bit-locker-key a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|rotate-bit-locker-key|rotateBitLockerKeys|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device rotate-file-vault-key

rotate-file-vault-key a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|rotate-file-vault-key|rotateFileVaultKey|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device send-custom-notification-to-company-portal

send-custom-notification-to-company-portal a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send-custom-notification-to-company-portal|sendCustomNotificationToCompanyPortal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--notification-title**|string||notification_title|notificationTitle|
|**--notification-body**|string||notification_body|notificationBody|

### usersactions user-managed-device set-device-name

set-device-name a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-device-name|setDeviceName|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-name**|string||device_name|deviceName|

### usersactions user-managed-device shut-down

shut-down a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|shut-down|shutDown|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device sync-device

sync-device a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|sync-device|syncDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device trigger-configuration-manager-action

trigger-configuration-manager-action a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|trigger-configuration-manager-action|triggerConfigurationManagerAction|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--configuration-manager-action-action**|choice||action|action|

### usersactions user-managed-device update-window-device-account

update-window-device-account a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-window-device-account|updateWindowsDeviceAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--update-windows-device-account-action-parameter-calendar-sync-enabled**|boolean|Not yet documented|calendar_sync_enabled|calendarSyncEnabled|
|**--update-windows-device-account-action-parameter-device-account**|object|windowsDeviceAccount|device_account|deviceAccount|
|**--update-windows-device-account-action-parameter-device-account-email**|string|Not yet documented|device_account_email|deviceAccountEmail|
|**--update-windows-device-account-action-parameter-exchange-server**|string|Not yet documented|exchange_server|exchangeServer|
|**--update-windows-device-account-action-parameter-password-rotation-enabled**|boolean|Not yet documented|password_rotation_enabled|passwordRotationEnabled|
|**--update-windows-device-account-action-parameter-session-initiation-protocal-address**|string|Not yet documented|session_initiation_protocal_address|sessionInitiationProtocalAddress|

### usersactions user-managed-device window-defender-scan

window-defender-scan a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|window-defender-scan|windowsDefenderScan|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--quick-scan**|boolean||quick_scan|quickScan|

### usersactions user-managed-device window-defender-update-signature

window-defender-update-signature a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|window-defender-update-signature|windowsDefenderUpdateSignatures|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions user-managed-device wipe

wipe a usersactions user-managed-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|wipe|wipe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--keep-enrollment-data**|boolean||keep_enrollment_data|keepEnrollmentData|
|**--keep-user-data**|boolean||keep_user_data|keepUserData|
|**--mac-os-unlock-code**|string||mac_os_unlock_code|macOsUnlockCode|
|**--use-protected-wipe**|boolean||use_protected_wipe|useProtectedWipe|

### usersactions user-managed-device-log-collection-request create-download-url

create-download-url a usersactions user-managed-device-log-collection-request.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-managed-device-log-collection-request|users.managedDevices.logCollectionRequests|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-download-url|createDownloadUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-log-collection-response-id**|string|key: id of deviceLogCollectionResponse|device_log_collection_response_id|deviceLogCollectionResponse-id|

### usersactions user-message copy

copy a usersactions user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy|copy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--destination-id**|string||destination_id|DestinationId|

### usersactions user-message create-forward

create-forward a usersactions user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-forward|createForward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|microsoft_graph_message_to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-message create-reply

create-reply a usersactions user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-reply|createReply|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-message create-reply-all

create-reply-all a usersactions user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-reply-all|createReplyAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-message forward

forward a usersactions user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|microsoft_graph_message_to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-message move

move a usersactions user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|move|move|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--destination-id**|string||destination_id|DestinationId|

### usersactions user-message reply

reply a usersactions user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reply|reply|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-message reply-all

reply-all a usersactions user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reply-all|replyAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-mentions-preview**|object|mentionsPreview|mentions_preview|mentionsPreview|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-unsubscribe-data**|array||unsubscribe_data|unsubscribeData|
|**--message-unsubscribe-enabled**|boolean||unsubscribe_enabled|unsubscribeEnabled|
|**--message-web-link**|string|The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook on the web review pane.The message will open in the browser if you are logged in to your mailbox via Outlook on the web. You will be prompted to login if you are not already logged in with the browser.This URL cannot be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-mentions**|array||mentions|mentions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions user-message send

send a usersactions user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send|send|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|

### usersactions user-message unsubscribe

unsubscribe a usersactions user-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unsubscribe|unsubscribe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|

### usersactions user-message-attachment create-upload-session

create-upload-session a usersactions user-message-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-message-attachment|users.messages.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-mobile-app-troubleshooting-event-app-log-collection-request create-download-url

create-download-url a usersactions user-mobile-app-troubleshooting-event-app-log-collection-request.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-mobile-app-troubleshooting-event-app-log-collection-request|users.mobileAppTroubleshootingEvents.appLogCollectionRequests|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-download-url|createDownloadUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--mobile-app-troubleshooting-event-id**|string|key: id of mobileAppTroubleshootingEvent|mobile_app_troubleshooting_event_id|mobileAppTroubleshootingEvent-id|
|**--app-log-collection-request-id**|string|key: id of appLogCollectionRequest|app_log_collection_request_id|appLogCollectionRequest-id|

### usersactions user-onenote-notebook copy-notebook

copy-notebook a usersactions user-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook|users.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook get-notebook-from-web-url

get-notebook-from-web-url a usersactions user-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook|users.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-notebook-from-web-url|getNotebookFromWebUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--web-url**|string||web_url|webUrl|

### usersactions user-onenote-notebook-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section|users.onenote.notebooks.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section|users.onenote.notebooks.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-group-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-notebook-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-group-parent-notebook|users.onenote.notebooks.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-group-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-group-section|users.onenote.notebooks.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-group-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-group-section|users.onenote.notebooks.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-group-section-page copy-to-section

copy-to-section a usersactions user-onenote-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-group-section-page|users.onenote.notebooks.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-group-section-page onenote-patch-content

onenote-patch-content a usersactions user-onenote-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-group-section-page|users.onenote.notebooks.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### usersactions user-onenote-notebook-section-group-section-page-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-notebook-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-group-section-page-parent-notebook|users.onenote.notebooks.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-group-section-page-parent-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-notebook-section-group-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-group-section-page-parent-section|users.onenote.notebooks.sectionGroups.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-group-section-page-parent-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-notebook-section-group-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-group-section-page-parent-section|users.onenote.notebooks.sectionGroups.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-group-section-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-notebook-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-group-section-parent-notebook|users.onenote.notebooks.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-page copy-to-section

copy-to-section a usersactions user-onenote-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-page|users.onenote.notebooks.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-page onenote-patch-content

onenote-patch-content a usersactions user-onenote-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-page|users.onenote.notebooks.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### usersactions user-onenote-notebook-section-page-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-notebook-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-page-parent-notebook|users.onenote.notebooks.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-page-parent-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-notebook-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-page-parent-section|users.onenote.notebooks.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-page-parent-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-notebook-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-page-parent-section|users.onenote.notebooks.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-notebook-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-parent-notebook|users.onenote.notebooks.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-parent-section-group-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-notebook-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-parent-section-group-parent-notebook|users.onenote.notebooks.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-parent-section-group-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-notebook-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-parent-section-group-section|users.onenote.notebooks.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-notebook-section-parent-section-group-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-notebook-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-notebook-section-parent-section-group-section|users.onenote.notebooks.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page copy-to-section

copy-to-section a usersactions user-onenote-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page|users.onenote.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page onenote-patch-content

onenote-patch-content a usersactions user-onenote-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page|users.onenote.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### usersactions user-onenote-page-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook|users.onenote.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section|users.onenote.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section|users.onenote.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section-group-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-page-parent-notebook-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-group-parent-notebook|users.onenote.pages.parentNotebook.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section-group-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-group-section|users.onenote.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section-group-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-group-section|users.onenote.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section-group-section-page copy-to-section

copy-to-section a usersactions user-onenote-page-parent-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-group-section-page|users.onenote.pages.parentNotebook.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section-group-section-page onenote-patch-content

onenote-patch-content a usersactions user-onenote-page-parent-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-group-section-page|users.onenote.pages.parentNotebook.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--commands**|array||commands|commands|

### usersactions user-onenote-page-parent-notebook-section-group-section-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-page-parent-notebook-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-group-section-parent-notebook|users.onenote.pages.parentNotebook.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section-page copy-to-section

copy-to-section a usersactions user-onenote-page-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-page|users.onenote.pages.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section-page onenote-patch-content

onenote-patch-content a usersactions user-onenote-page-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-page|users.onenote.pages.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--commands**|array||commands|commands|

### usersactions user-onenote-page-parent-notebook-section-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-page-parent-notebook-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-parent-notebook|users.onenote.pages.parentNotebook.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section-parent-section-group-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-page-parent-notebook-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-parent-section-group-parent-notebook|users.onenote.pages.parentNotebook.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section-parent-section-group-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-page-parent-notebook-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-parent-section-group-section|users.onenote.pages.parentNotebook.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-notebook-section-parent-section-group-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-page-parent-notebook-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-notebook-section-parent-section-group-section|users.onenote.pages.parentNotebook.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section|users.onenote.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section|users.onenote.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-page copy-to-section

copy-to-section a usersactions user-onenote-page-parent-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-page|users.onenote.pages.parentSection.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-page onenote-patch-content

onenote-patch-content a usersactions user-onenote-page-parent-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-page|users.onenote.pages.parentSection.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--commands**|array||commands|commands|

### usersactions user-onenote-page-parent-section-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-page-parent-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-notebook|users.onenote.pages.parentSection.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-parent-notebook-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-page-parent-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-notebook-section|users.onenote.pages.parentSection.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-parent-notebook-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-page-parent-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-notebook-section|users.onenote.pages.parentSection.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-parent-notebook-section-group-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-page-parent-section-parent-notebook-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-notebook-section-group-parent-notebook|users.onenote.pages.parentSection.parentNotebook.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-parent-notebook-section-group-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-page-parent-section-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-notebook-section-group-section|users.onenote.pages.parentSection.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-parent-notebook-section-group-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-page-parent-section-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-notebook-section-group-section|users.onenote.pages.parentSection.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-parent-section-group-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-page-parent-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-section-group-parent-notebook|users.onenote.pages.parentSection.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-parent-section-group-parent-notebook-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-page-parent-section-parent-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-section-group-parent-notebook-section|users.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-parent-section-group-parent-notebook-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-page-parent-section-parent-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-section-group-parent-notebook-section|users.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-parent-section-group-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-page-parent-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-section-group-section|users.onenote.pages.parentSection.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-page-parent-section-parent-section-group-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-page-parent-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-page-parent-section-parent-section-group-section|users.onenote.pages.parentSection.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-parent-notebook|users.onenote.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-parent-notebook-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-parent-notebook-section|users.onenote.sectionGroups.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-parent-notebook-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-parent-notebook-section|users.onenote.sectionGroups.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-parent-notebook-section-page copy-to-section

copy-to-section a usersactions user-onenote-section-group-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-parent-notebook-section-page|users.onenote.sectionGroups.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-parent-notebook-section-page onenote-patch-content

onenote-patch-content a usersactions user-onenote-section-group-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-parent-notebook-section-page|users.onenote.sectionGroups.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### usersactions user-onenote-section-group-parent-notebook-section-page-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-section-group-parent-notebook-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-parent-notebook-section-page-parent-notebook|users.onenote.sectionGroups.parentNotebook.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-parent-notebook-section-page-parent-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-group-parent-notebook-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-parent-notebook-section-page-parent-section|users.onenote.sectionGroups.parentNotebook.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-parent-notebook-section-page-parent-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-group-parent-notebook-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-parent-notebook-section-page-parent-section|users.onenote.sectionGroups.parentNotebook.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-parent-notebook-section-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-section-group-parent-notebook-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-parent-notebook-section-parent-notebook|users.onenote.sectionGroups.parentNotebook.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section|users.onenote.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section|users.onenote.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section-page copy-to-section

copy-to-section a usersactions user-onenote-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section-page|users.onenote.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section-page onenote-patch-content

onenote-patch-content a usersactions user-onenote-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section-page|users.onenote.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### usersactions user-onenote-section-group-section-page-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section-page-parent-notebook|users.onenote.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section-page-parent-notebook-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-group-section-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section-page-parent-notebook-section|users.onenote.sectionGroups.sections.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section-page-parent-notebook-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-group-section-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section-page-parent-notebook-section|users.onenote.sectionGroups.sections.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section-page-parent-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-group-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section-page-parent-section|users.onenote.sectionGroups.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section-page-parent-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-group-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section-page-parent-section|users.onenote.sectionGroups.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section-parent-notebook|users.onenote.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section-parent-notebook-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-group-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section-parent-notebook-section|users.onenote.sectionGroups.sections.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-group-section-parent-notebook-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-group-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-group-section-parent-notebook-section|users.onenote.sectionGroups.sections.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-page copy-to-section

copy-to-section a usersactions user-onenote-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-page|users.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-page onenote-patch-content

onenote-patch-content a usersactions user-onenote-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-page|users.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### usersactions user-onenote-section-page-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-page-parent-notebook|users.onenote.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-page-parent-notebook-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-page-parent-notebook-section|users.onenote.sections.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-page-parent-notebook-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-page-parent-notebook-section|users.onenote.sections.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-page-parent-notebook-section-group-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-section-page-parent-notebook-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-page-parent-notebook-section-group-parent-notebook|users.onenote.sections.pages.parentNotebook.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-page-parent-notebook-section-group-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-page-parent-notebook-section-group-section|users.onenote.sections.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-page-parent-notebook-section-group-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-page-parent-notebook-section-group-section|users.onenote.sections.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-page-parent-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-page-parent-section|users.onenote.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-page-parent-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-page-parent-section|users.onenote.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-notebook|users.onenote.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-notebook-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-notebook-section|users.onenote.sections.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-notebook-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-notebook-section|users.onenote.sections.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-notebook-section-group-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-section-parent-notebook-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-notebook-section-group-parent-notebook|users.onenote.sections.parentNotebook.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-notebook-section-group-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-notebook-section-group-section|users.onenote.sections.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-notebook-section-group-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-notebook-section-group-section|users.onenote.sections.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-section-group-parent-notebook copy-notebook

copy-notebook a usersactions user-onenote-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-section-group-parent-notebook|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-section-group-parent-notebook-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-parent-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-section-group-parent-notebook-section|users.onenote.sections.parentSectionGroup.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-section-group-parent-notebook-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-parent-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-section-group-parent-notebook-section|users.onenote.sections.parentSectionGroup.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-section-group-section copy-to-notebook

copy-to-notebook a usersactions user-onenote-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-section-group-section|users.onenote.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-onenote-section-parent-section-group-section copy-to-section-group

copy-to-section-group a usersactions user-onenote-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-onenote-section-parent-section-group-section|users.onenote.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions user-online-meeting create-or-get

create-or-get a usersactions user-online-meeting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-online-meeting|users.onlineMeetings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-or-get|createOrGet|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--external-id**|string||external_id|externalId|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--subject**|string||subject|subject|
|**--participants-attendees**|array||attendees|attendees|
|**--participants-contributors**|array||contributors|contributors|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--participants-producers**|array||producers|producers|

### usersactions user-outlook-task complete

complete a usersactions user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|complete|complete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|

### usersactions user-outlook-task-attachment create-upload-session

create-upload-session a usersactions user-outlook-task-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-outlook-task-attachment|users.outlook.tasks.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-outlook-task-folder-task complete

complete a usersactions user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|complete|complete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|

### usersactions user-outlook-task-folder-task-attachment create-upload-session

create-upload-session a usersactions user-outlook-task-folder-task-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-outlook-task-folder-task-attachment|users.outlook.taskFolders.tasks.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-outlook-task-group-task-folder-task complete

complete a usersactions user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|complete|complete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|

### usersactions user-outlook-task-group-task-folder-task-attachment create-upload-session

create-upload-session a usersactions user-outlook-task-group-task-folder-task-attachment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-outlook-task-group-task-folder-task-attachment|users.outlook.taskGroups.taskFolders.tasks.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions user-pending-access-review-instance accept-recommendation

accept-recommendation a usersactions user-pending-access-review-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-pending-access-review-instance|users.pendingAccessReviewInstances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept-recommendation|acceptRecommendations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--access-review-instance-id**|string|key: id of accessReviewInstance|access_review_instance_id|accessReviewInstance-id|

### usersactions user-pending-access-review-instance apply-decision

apply-decision a usersactions user-pending-access-review-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-pending-access-review-instance|users.pendingAccessReviewInstances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|apply-decision|applyDecisions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--access-review-instance-id**|string|key: id of accessReviewInstance|access_review_instance_id|accessReviewInstance-id|

### usersactions user-pending-access-review-instance reset-decision

reset-decision a usersactions user-pending-access-review-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-pending-access-review-instance|users.pendingAccessReviewInstances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reset-decision|resetDecisions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--access-review-instance-id**|string|key: id of accessReviewInstance|access_review_instance_id|accessReviewInstance-id|

### usersactions user-pending-access-review-instance send-reminder

send-reminder a usersactions user-pending-access-review-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-pending-access-review-instance|users.pendingAccessReviewInstances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send-reminder|sendReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--access-review-instance-id**|string|key: id of accessReviewInstance|access_review_instance_id|accessReviewInstance-id|

### usersactions user-pending-access-review-instance stop

stop a usersactions user-pending-access-review-instance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-pending-access-review-instance|users.pendingAccessReviewInstances|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|stop|stop|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--access-review-instance-id**|string|key: id of accessReviewInstance|access_review_instance_id|accessReviewInstance-id|

### usersactions user-pending-access-review-instance-definition stop

stop a usersactions user-pending-access-review-instance-definition.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-pending-access-review-instance-definition|users.pendingAccessReviewInstances.definition|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|stop|stop|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--access-review-instance-id**|string|key: id of accessReviewInstance|access_review_instance_id|accessReviewInstance-id|

### usersactions user-teamwork send-activity-notification

send-activity-notification a usersactions user-teamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions user-teamwork|users.teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send-activity-notification|sendActivityNotification|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--topic**|object|teamworkActivityTopic|topic|topic|
|**--activity-type**|string||activity_type|activityType|
|**--chain-id**|integer||chain_id|chainId|
|**--preview-text**|object|itemBody|preview_text|previewText|
|**--template-parameters**|array||template_parameters|templateParameters|
