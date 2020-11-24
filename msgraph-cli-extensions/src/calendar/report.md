# Azure CLI Module Creation Report

### calendar create-attachment

create-attachment a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar create-calendar

create-calendar a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.calendarGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-calendar|CreateCalendars|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar create-calendar-group

create-calendar-group a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-calendar-group|CreateCalendarGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string|Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--class-id**|uuid|The class identifier. Read-only.|class_id|classId|
|**--name**|string|The group name.|name|name|
|**--calendars**|array|The calendars in the calendar group. Navigation property. Read-only. Nullable.|calendars|calendars|

### calendar create-calendar-permission

create-calendar-permission a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-calendar-permission|CreateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar create-calendar-view

create-calendar-view a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-calendar-view|CreateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--i-cal-u-id**|string|A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.|i_cal_u_id|iCalUId|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--online-meeting-provider**|choice||online_meeting_provider|onlineMeetingProvider|
|**--online-meeting-url**|string|A URL for an online meeting. The property is set only when an organizer specifies an event as an online meeting such as a Skype meeting. Read-only.|online_meeting_url|onlineMeetingUrl|
|**--original-end-time-zone**|string|The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_end_time_zone|originalEndTimeZone|
|**--original-start**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|original_start|originalStart|
|**--original-start-time-zone**|string|The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_start_time_zone|originalStartTimeZone|
|**--reminder-minutes-before-start**|integer|The number of minutes before the event start time that the reminder alert occurs.|reminder_minutes_before_start|reminderMinutesBeforeStart|
|**--response-requested**|boolean|Default is true, which represents the organizer would like an invitee to send a response to the event.|response_requested|responseRequested|
|**--response-status**|object|responseStatus|response_status|responseStatus|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--series-master-id**|string|The ID for the recurring series master item, if this event is part of a recurring series.|series_master_id|seriesMasterId|
|**--show-as**|choice||show_as|showAs|
|**--start**|object|dateTimeTimeZone|start|start|
|**--subject**|string|The text of the event's subject line.|subject|subject|
|**--transaction-id**|string|A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. This is useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you cannot change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.|transaction_id|transactionId|
|**--type**|choice||type|type|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--extensions**|array|The collection of open extensions defined for the event. Read-only. Nullable.|extensions|extensions|
|**--instances**|array|The instances of the event. Navigation property. Read-only. Nullable.|instances|instances|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the event. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the event. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|
|**--organizer-email-address**|object|emailAddress|email_address|emailAddress|
|**--online-meeting-conference-id**|string|The ID of the conference.|conference_id|conferenceId|
|**--online-meeting-join-url**|string|The external link that launches the online meeting. This is a URL that clients will launch into a browser and will redirect the user to join the meeting.|join_url|joinUrl|
|**--online-meeting-phones**|array|All of the phone numbers associated with this conference.|phones|phones|
|**--online-meeting-quick-dial**|string|The pre-formatted quickdial for this call.|quick_dial|quickDial|
|**--online-meeting-toll-free-numbers**|array|The toll free numbers that can be used to join the conference.|toll_free_numbers|tollFreeNumbers|
|**--online-meeting-toll-number**|string|The toll number that can be used to join the conference.|toll_number|tollNumber|
|**--location-address**|object|physicalAddress|address|address|
|**--location-coordinates**|object|outlookGeoCoordinates|coordinates|coordinates|
|**--location-display-name**|string|The name associated with the location.|display_name|displayName|
|**--location-location-email-address**|string|Optional email address of the location.|location_email_address|locationEmailAddress|
|**--location-location-type**|choice||location_type|locationType|
|**--location-location-uri**|string|Optional URI representing the location.|location_uri|locationUri|
|**--location-unique-id**|string|For internal use only.|unique_id|uniqueId|
|**--location-unique-id-type**|choice||unique_id_type|uniqueIdType|

### calendar create-event

create-event a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-event|CreateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--i-cal-u-id**|string|A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.|i_cal_u_id|iCalUId|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--online-meeting-provider**|choice||online_meeting_provider|onlineMeetingProvider|
|**--online-meeting-url**|string|A URL for an online meeting. The property is set only when an organizer specifies an event as an online meeting such as a Skype meeting. Read-only.|online_meeting_url|onlineMeetingUrl|
|**--original-end-time-zone**|string|The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_end_time_zone|originalEndTimeZone|
|**--original-start**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|original_start|originalStart|
|**--original-start-time-zone**|string|The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_start_time_zone|originalStartTimeZone|
|**--reminder-minutes-before-start**|integer|The number of minutes before the event start time that the reminder alert occurs.|reminder_minutes_before_start|reminderMinutesBeforeStart|
|**--response-requested**|boolean|Default is true, which represents the organizer would like an invitee to send a response to the event.|response_requested|responseRequested|
|**--response-status**|object|responseStatus|response_status|responseStatus|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--series-master-id**|string|The ID for the recurring series master item, if this event is part of a recurring series.|series_master_id|seriesMasterId|
|**--show-as**|choice||show_as|showAs|
|**--start**|object|dateTimeTimeZone|start|start|
|**--subject**|string|The text of the event's subject line.|subject|subject|
|**--transaction-id**|string|A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. This is useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you cannot change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.|transaction_id|transactionId|
|**--type**|choice||type|type|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--extensions**|array|The collection of open extensions defined for the event. Read-only. Nullable.|extensions|extensions|
|**--instances**|array|The instances of the event. Navigation property. Read-only. Nullable.|instances|instances|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the event. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the event. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|
|**--organizer-email-address**|object|emailAddress|email_address|emailAddress|
|**--online-meeting-conference-id**|string|The ID of the conference.|conference_id|conferenceId|
|**--online-meeting-join-url**|string|The external link that launches the online meeting. This is a URL that clients will launch into a browser and will redirect the user to join the meeting.|join_url|joinUrl|
|**--online-meeting-phones**|array|All of the phone numbers associated with this conference.|phones|phones|
|**--online-meeting-quick-dial**|string|The pre-formatted quickdial for this call.|quick_dial|quickDial|
|**--online-meeting-toll-free-numbers**|array|The toll free numbers that can be used to join the conference.|toll_free_numbers|tollFreeNumbers|
|**--online-meeting-toll-number**|string|The toll number that can be used to join the conference.|toll_number|tollNumber|
|**--location-address**|object|physicalAddress|address|address|
|**--location-coordinates**|object|outlookGeoCoordinates|coordinates|coordinates|
|**--location-display-name**|string|The name associated with the location.|display_name|displayName|
|**--location-location-email-address**|string|Optional email address of the location.|location_email_address|locationEmailAddress|
|**--location-location-type**|choice||location_type|locationType|
|**--location-location-uri**|string|Optional URI representing the location.|location_uri|locationUri|
|**--location-unique-id**|string|For internal use only.|unique_id|uniqueId|
|**--location-unique-id-type**|choice||unique_id_type|uniqueIdType|

### calendar create-extension

create-extension a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

### calendar create-instance

create-instance a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-instance|CreateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--i-cal-u-id**|string|A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.|i_cal_u_id|iCalUId|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--online-meeting-provider**|choice||online_meeting_provider|onlineMeetingProvider|
|**--online-meeting-url**|string|A URL for an online meeting. The property is set only when an organizer specifies an event as an online meeting such as a Skype meeting. Read-only.|online_meeting_url|onlineMeetingUrl|
|**--original-end-time-zone**|string|The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_end_time_zone|originalEndTimeZone|
|**--original-start**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|original_start|originalStart|
|**--original-start-time-zone**|string|The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_start_time_zone|originalStartTimeZone|
|**--reminder-minutes-before-start**|integer|The number of minutes before the event start time that the reminder alert occurs.|reminder_minutes_before_start|reminderMinutesBeforeStart|
|**--response-requested**|boolean|Default is true, which represents the organizer would like an invitee to send a response to the event.|response_requested|responseRequested|
|**--response-status**|object|responseStatus|response_status|responseStatus|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--series-master-id**|string|The ID for the recurring series master item, if this event is part of a recurring series.|series_master_id|seriesMasterId|
|**--show-as**|choice||show_as|showAs|
|**--start**|object|dateTimeTimeZone|start|start|
|**--subject**|string|The text of the event's subject line.|subject|subject|
|**--transaction-id**|string|A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. This is useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you cannot change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.|transaction_id|transactionId|
|**--type**|choice||type|type|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--extensions**|array|The collection of open extensions defined for the event. Read-only. Nullable.|extensions|extensions|
|**--instances**|array|The instances of the event. Navigation property. Read-only. Nullable.|instances|instances|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the event. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the event. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|
|**--organizer-email-address**|object|emailAddress|email_address|emailAddress|
|**--online-meeting-conference-id**|string|The ID of the conference.|conference_id|conferenceId|
|**--online-meeting-join-url**|string|The external link that launches the online meeting. This is a URL that clients will launch into a browser and will redirect the user to join the meeting.|join_url|joinUrl|
|**--online-meeting-phones**|array|All of the phone numbers associated with this conference.|phones|phones|
|**--online-meeting-quick-dial**|string|The pre-formatted quickdial for this call.|quick_dial|quickDial|
|**--online-meeting-toll-free-numbers**|array|The toll free numbers that can be used to join the conference.|toll_free_numbers|tollFreeNumbers|
|**--online-meeting-toll-number**|string|The toll number that can be used to join the conference.|toll_number|tollNumber|
|**--location-address**|object|physicalAddress|address|address|
|**--location-coordinates**|object|outlookGeoCoordinates|coordinates|coordinates|
|**--location-display-name**|string|The name associated with the location.|display_name|displayName|
|**--location-location-email-address**|string|Optional email address of the location.|location_email_address|locationEmailAddress|
|**--location-location-type**|choice||location_type|locationType|
|**--location-location-uri**|string|Optional URI representing the location.|location_uri|locationUri|
|**--location-unique-id**|string|For internal use only.|unique_id|uniqueId|
|**--location-unique-id-type**|choice||unique_id_type|uniqueIdType|

### calendar create-multi-value-extended-property

create-multi-value-extended-property a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar create-place

create-place a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|places.place|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-place|CreatePlace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--address**|object|physicalAddress|address|address|
|**--display-name**|string|The name associated with the place.|display_name|displayName|
|**--geo-coordinates**|object|outlookGeoCoordinates|geo_coordinates|geoCoordinates|
|**--phone**|string|The phone number of the place.|phone|phone|

### calendar create-single-value-extended-property

create-single-value-extended-property a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar delete

delete a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCalendarPermissions|
|delete|DeleteCalendarView|
|delete|DeleteEvents|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar get-attachment

get-attachment a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar get-calendar

get-calendar a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-calendar|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar get-calendar-group

get-calendar-group a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-calendar-group|GetCalendarGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar get-calendar-permission

get-calendar-permission a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-calendar-permission|GetCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar get-calendar-view

get-calendar-view a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-calendar-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar get-event

get-event a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-event|GetEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar get-extension

get-extension a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar get-instance

get-instance a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-instance|GetInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar get-multi-value-extended-property

get-multi-value-extended-property a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar get-place

get-place a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|places.place|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-place|GetPlace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--place-id**|string|key: id of place|place_id|place-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar get-single-value-extended-property

get-single-value-extended-property a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-attachment

list-attachment a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-calendar

list-calendar a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.calendarGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-calendar|ListCalendars|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-calendar-group

list-calendar-group a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-calendar-group|ListCalendarGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-calendar-permission

list-calendar-permission a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-calendar-permission|ListCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-calendar-view

list-calendar-view a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-calendar-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-event

list-event a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-event|ListEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-extension

list-extension a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-instance

list-instance a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-instance|ListInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-multi-value-extended-property

list-multi-value-extended-property a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-place

list-place a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|places.place|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-place|ListPlace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar list-single-value-extended-property

list-single-value-extended-property a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar update-attachment

update-attachment a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar update-calendar

update-calendar a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-calendar|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar update-calendar-group

update-calendar-group a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-calendar-group|UpdateCalendarGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string|Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--class-id**|uuid|The class identifier. Read-only.|class_id|classId|
|**--name**|string|The group name.|name|name|
|**--calendars**|array|The calendars in the calendar group. Navigation property. Read-only. Nullable.|calendars|calendars|

### calendar update-calendar-permission

update-calendar-permission a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-calendar-permission|UpdateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar update-calendar-view

update-calendar-view a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-calendar-view|UpdateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--i-cal-u-id**|string|A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.|i_cal_u_id|iCalUId|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--online-meeting-provider**|choice||online_meeting_provider|onlineMeetingProvider|
|**--online-meeting-url**|string|A URL for an online meeting. The property is set only when an organizer specifies an event as an online meeting such as a Skype meeting. Read-only.|online_meeting_url|onlineMeetingUrl|
|**--original-end-time-zone**|string|The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_end_time_zone|originalEndTimeZone|
|**--original-start**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|original_start|originalStart|
|**--original-start-time-zone**|string|The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_start_time_zone|originalStartTimeZone|
|**--reminder-minutes-before-start**|integer|The number of minutes before the event start time that the reminder alert occurs.|reminder_minutes_before_start|reminderMinutesBeforeStart|
|**--response-requested**|boolean|Default is true, which represents the organizer would like an invitee to send a response to the event.|response_requested|responseRequested|
|**--response-status**|object|responseStatus|response_status|responseStatus|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--series-master-id**|string|The ID for the recurring series master item, if this event is part of a recurring series.|series_master_id|seriesMasterId|
|**--show-as**|choice||show_as|showAs|
|**--start**|object|dateTimeTimeZone|start|start|
|**--subject**|string|The text of the event's subject line.|subject|subject|
|**--transaction-id**|string|A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. This is useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you cannot change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.|transaction_id|transactionId|
|**--type**|choice||type|type|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--extensions**|array|The collection of open extensions defined for the event. Read-only. Nullable.|extensions|extensions|
|**--instances**|array|The instances of the event. Navigation property. Read-only. Nullable.|instances|instances|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the event. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the event. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|
|**--organizer-email-address**|object|emailAddress|email_address|emailAddress|
|**--online-meeting-conference-id**|string|The ID of the conference.|conference_id|conferenceId|
|**--online-meeting-join-url**|string|The external link that launches the online meeting. This is a URL that clients will launch into a browser and will redirect the user to join the meeting.|join_url|joinUrl|
|**--online-meeting-phones**|array|All of the phone numbers associated with this conference.|phones|phones|
|**--online-meeting-quick-dial**|string|The pre-formatted quickdial for this call.|quick_dial|quickDial|
|**--online-meeting-toll-free-numbers**|array|The toll free numbers that can be used to join the conference.|toll_free_numbers|tollFreeNumbers|
|**--online-meeting-toll-number**|string|The toll number that can be used to join the conference.|toll_number|tollNumber|
|**--location-address**|object|physicalAddress|address|address|
|**--location-coordinates**|object|outlookGeoCoordinates|coordinates|coordinates|
|**--location-display-name**|string|The name associated with the location.|display_name|displayName|
|**--location-location-email-address**|string|Optional email address of the location.|location_email_address|locationEmailAddress|
|**--location-location-type**|choice||location_type|locationType|
|**--location-location-uri**|string|Optional URI representing the location.|location_uri|locationUri|
|**--location-unique-id**|string|For internal use only.|unique_id|uniqueId|
|**--location-unique-id-type**|choice||unique_id_type|uniqueIdType|

### calendar update-event

update-event a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-event|UpdateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--i-cal-u-id**|string|A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.|i_cal_u_id|iCalUId|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--online-meeting-provider**|choice||online_meeting_provider|onlineMeetingProvider|
|**--online-meeting-url**|string|A URL for an online meeting. The property is set only when an organizer specifies an event as an online meeting such as a Skype meeting. Read-only.|online_meeting_url|onlineMeetingUrl|
|**--original-end-time-zone**|string|The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_end_time_zone|originalEndTimeZone|
|**--original-start**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|original_start|originalStart|
|**--original-start-time-zone**|string|The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_start_time_zone|originalStartTimeZone|
|**--reminder-minutes-before-start**|integer|The number of minutes before the event start time that the reminder alert occurs.|reminder_minutes_before_start|reminderMinutesBeforeStart|
|**--response-requested**|boolean|Default is true, which represents the organizer would like an invitee to send a response to the event.|response_requested|responseRequested|
|**--response-status**|object|responseStatus|response_status|responseStatus|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--series-master-id**|string|The ID for the recurring series master item, if this event is part of a recurring series.|series_master_id|seriesMasterId|
|**--show-as**|choice||show_as|showAs|
|**--start**|object|dateTimeTimeZone|start|start|
|**--subject**|string|The text of the event's subject line.|subject|subject|
|**--transaction-id**|string|A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. This is useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you cannot change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.|transaction_id|transactionId|
|**--type**|choice||type|type|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--extensions**|array|The collection of open extensions defined for the event. Read-only. Nullable.|extensions|extensions|
|**--instances**|array|The instances of the event. Navigation property. Read-only. Nullable.|instances|instances|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the event. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the event. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|
|**--organizer-email-address**|object|emailAddress|email_address|emailAddress|
|**--online-meeting-conference-id**|string|The ID of the conference.|conference_id|conferenceId|
|**--online-meeting-join-url**|string|The external link that launches the online meeting. This is a URL that clients will launch into a browser and will redirect the user to join the meeting.|join_url|joinUrl|
|**--online-meeting-phones**|array|All of the phone numbers associated with this conference.|phones|phones|
|**--online-meeting-quick-dial**|string|The pre-formatted quickdial for this call.|quick_dial|quickDial|
|**--online-meeting-toll-free-numbers**|array|The toll free numbers that can be used to join the conference.|toll_free_numbers|tollFreeNumbers|
|**--online-meeting-toll-number**|string|The toll number that can be used to join the conference.|toll_number|tollNumber|
|**--location-address**|object|physicalAddress|address|address|
|**--location-coordinates**|object|outlookGeoCoordinates|coordinates|coordinates|
|**--location-display-name**|string|The name associated with the location.|display_name|displayName|
|**--location-location-email-address**|string|Optional email address of the location.|location_email_address|locationEmailAddress|
|**--location-location-type**|choice||location_type|locationType|
|**--location-location-uri**|string|Optional URI representing the location.|location_uri|locationUri|
|**--location-unique-id**|string|For internal use only.|unique_id|uniqueId|
|**--location-unique-id-type**|choice||unique_id_type|uniqueIdType|

### calendar update-extension

update-extension a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### calendar update-instance

update-instance a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-instance|UpdateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--i-cal-u-id**|string|A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.|i_cal_u_id|iCalUId|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--online-meeting-provider**|choice||online_meeting_provider|onlineMeetingProvider|
|**--online-meeting-url**|string|A URL for an online meeting. The property is set only when an organizer specifies an event as an online meeting such as a Skype meeting. Read-only.|online_meeting_url|onlineMeetingUrl|
|**--original-end-time-zone**|string|The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_end_time_zone|originalEndTimeZone|
|**--original-start**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|original_start|originalStart|
|**--original-start-time-zone**|string|The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.|original_start_time_zone|originalStartTimeZone|
|**--reminder-minutes-before-start**|integer|The number of minutes before the event start time that the reminder alert occurs.|reminder_minutes_before_start|reminderMinutesBeforeStart|
|**--response-requested**|boolean|Default is true, which represents the organizer would like an invitee to send a response to the event.|response_requested|responseRequested|
|**--response-status**|object|responseStatus|response_status|responseStatus|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--series-master-id**|string|The ID for the recurring series master item, if this event is part of a recurring series.|series_master_id|seriesMasterId|
|**--show-as**|choice||show_as|showAs|
|**--start**|object|dateTimeTimeZone|start|start|
|**--subject**|string|The text of the event's subject line.|subject|subject|
|**--transaction-id**|string|A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. This is useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you cannot change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.|transaction_id|transactionId|
|**--type**|choice||type|type|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--extensions**|array|The collection of open extensions defined for the event. Read-only. Nullable.|extensions|extensions|
|**--instances**|array|The instances of the event. Navigation property. Read-only. Nullable.|instances|instances|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the event. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the event. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|
|**--organizer-email-address**|object|emailAddress|email_address|emailAddress|
|**--online-meeting-conference-id**|string|The ID of the conference.|conference_id|conferenceId|
|**--online-meeting-join-url**|string|The external link that launches the online meeting. This is a URL that clients will launch into a browser and will redirect the user to join the meeting.|join_url|joinUrl|
|**--online-meeting-phones**|array|All of the phone numbers associated with this conference.|phones|phones|
|**--online-meeting-quick-dial**|string|The pre-formatted quickdial for this call.|quick_dial|quickDial|
|**--online-meeting-toll-free-numbers**|array|The toll free numbers that can be used to join the conference.|toll_free_numbers|tollFreeNumbers|
|**--online-meeting-toll-number**|string|The toll number that can be used to join the conference.|toll_number|tollNumber|
|**--location-address**|object|physicalAddress|address|address|
|**--location-coordinates**|object|outlookGeoCoordinates|coordinates|coordinates|
|**--location-display-name**|string|The name associated with the location.|display_name|displayName|
|**--location-location-email-address**|string|Optional email address of the location.|location_email_address|locationEmailAddress|
|**--location-location-type**|choice||location_type|locationType|
|**--location-location-uri**|string|Optional URI representing the location.|location_uri|locationUri|
|**--location-unique-id**|string|For internal use only.|unique_id|uniqueId|
|**--location-unique-id-type**|choice||unique_id_type|uniqueIdType|

### calendar update-multi-value-extended-property

update-multi-value-extended-property a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar update-place

update-place a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|places.place|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-place|UpdatePlace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--place-id**|string|key: id of place|place_id|place-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|physicalAddress|address|address|
|**--display-name**|string|The name associated with the place.|display_name|displayName|
|**--geo-coordinates**|object|outlookGeoCoordinates|geo_coordinates|geoCoordinates|
|**--phone**|string|The phone number of the place.|phone|phone|

### calendar update-single-value-extended-property

update-single-value-extended-property a calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|
