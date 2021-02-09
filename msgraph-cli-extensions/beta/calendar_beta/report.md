# Azure CLI Module Creation Report

### calendar group create-event

create-event a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-event|CreateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group create-view

create-view a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-view|CreateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group delete

delete a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCalendarView|
|delete|DeleteEvents|
|delete|DeleteCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar group get

get a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group get-event

get-event a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-event|GetEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group get-view

get-view a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group list-event

list-event a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-event|ListEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group list-view

list-view a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group update

update a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--calendar-group-id**|string||calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar group update-event

update-event a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-event|UpdateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group update-view

update-view a calendar group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-view|UpdateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar create-event

create-event a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-event|CreateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar create-multi-value-extended-property

create-multi-value-extended-property a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-calendar create-permission

create-permission a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-permission|CreateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar group-calendar create-single-value-extended-property

create-single-value-extended-property a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-calendar create-view

create-view a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-view|CreateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar delete

delete a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

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
|**--group-id**|string|key: id of group|group_id|group-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar group-calendar get-event

get-event a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-event|GetEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar get-multi-value-extended-property

get-multi-value-extended-property a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar get-permission

get-permission a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission|GetCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar get-single-value-extended-property

get-single-value-extended-property a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar get-view

get-view a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar list-event

list-event a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-event|ListEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar list-multi-value-extended-property

list-multi-value-extended-property a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar list-permission

list-permission a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-permission|ListCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar list-single-value-extended-property

list-single-value-extended-property a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar list-view

list-view a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar update-event

update-event a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-event|UpdateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar update-multi-value-extended-property

update-multi-value-extended-property a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-calendar update-permission

update-permission a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-permission|UpdateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar group-calendar update-single-value-extended-property

update-single-value-extended-property a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-calendar update-view

update-view a calendar group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar|groups.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-view|UpdateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-event create-attachment

create-attachment a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar group-calendar-event create-exception-occurrence

create-exception-occurrence a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-exception-occurrence|CreateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-event create-extension

create-extension a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

### calendar group-calendar-event create-instance

create-instance a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-instance|CreateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-event create-multi-value-extended-property

create-multi-value-extended-property a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-calendar-event create-single-value-extended-property

create-single-value-extended-property a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-calendar-event delete

delete a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExceptionOccurrences|
|delete|DeleteExtensions|
|delete|DeleteInstances|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar group-calendar-event get

get a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event get-attachment

get-attachment a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event get-exception-occurrence

get-exception-occurrence a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-exception-occurrence|GetExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event get-extension

get-extension a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event get-instance

get-instance a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-instance|GetInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event get-multi-value-extended-property

get-multi-value-extended-property a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event get-single-value-extended-property

get-single-value-extended-property a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event list-attachment

list-attachment a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event list-exception-occurrence

list-exception-occurrence a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-exception-occurrence|ListExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event list-extension

list-extension a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event list-instance

list-instance a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-instance|ListInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event list-multi-value-extended-property

list-multi-value-extended-property a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event list-single-value-extended-property

list-single-value-extended-property a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-event update

update a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--calendar-group-id**|string||calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar group-calendar-event update-attachment

update-attachment a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar group-calendar-event update-exception-occurrence

update-exception-occurrence a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-exception-occurrence|UpdateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-event update-extension

update-extension a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### calendar group-calendar-event update-instance

update-instance a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-instance|UpdateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-event update-multi-value-extended-property

update-multi-value-extended-property a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-calendar-event update-single-value-extended-property

update-single-value-extended-property a calendar group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-event|groups.calendar.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-calendar-view create-attachment

create-attachment a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar group-calendar-view create-exception-occurrence

create-exception-occurrence a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-exception-occurrence|CreateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-view create-extension

create-extension a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

### calendar group-calendar-view create-instance

create-instance a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-instance|CreateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-view create-multi-value-extended-property

create-multi-value-extended-property a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-calendar-view create-single-value-extended-property

create-single-value-extended-property a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-calendar-view delete

delete a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExceptionOccurrences|
|delete|DeleteExtensions|
|delete|DeleteInstances|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar group-calendar-view get

get a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view get-attachment

get-attachment a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view get-exception-occurrence

get-exception-occurrence a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-exception-occurrence|GetExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view get-extension

get-extension a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view get-instance

get-instance a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-instance|GetInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view get-multi-value-extended-property

get-multi-value-extended-property a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view get-single-value-extended-property

get-single-value-extended-property a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view list-attachment

list-attachment a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view list-exception-occurrence

list-exception-occurrence a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-exception-occurrence|ListExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view list-extension

list-extension a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view list-instance

list-instance a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-instance|ListInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view list-multi-value-extended-property

list-multi-value-extended-property a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view list-single-value-extended-property

list-single-value-extended-property a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view update

update a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--calendar-group-id**|string||calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar group-calendar-view update-attachment

update-attachment a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar group-calendar-view update-exception-occurrence

update-exception-occurrence a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-exception-occurrence|UpdateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-view update-extension

update-extension a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### calendar group-calendar-view update-instance

update-instance a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-instance|UpdateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-view update-multi-value-extended-property

update-multi-value-extended-property a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-calendar-view update-single-value-extended-property

update-single-value-extended-property a calendar group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view|groups.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-calendar-view-calendar create-event

create-event a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-event|CreateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-view-calendar create-multi-value-extended-property

create-multi-value-extended-property a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-calendar-view-calendar create-permission

create-permission a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-permission|CreateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar group-calendar-view-calendar create-single-value-extended-property

create-single-value-extended-property a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-calendar-view-calendar create-view

create-view a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-view|CreateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-view-calendar delete

delete a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

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
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar group-calendar-view-calendar get-event

get-event a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-event|GetEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view-calendar get-multi-value-extended-property

get-multi-value-extended-property a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view-calendar get-permission

get-permission a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission|GetCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view-calendar get-single-value-extended-property

get-single-value-extended-property a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view-calendar get-view

get-view a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view-calendar list-event

list-event a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-event|ListEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view-calendar list-multi-value-extended-property

list-multi-value-extended-property a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view-calendar list-permission

list-permission a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-permission|ListCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view-calendar list-single-value-extended-property

list-single-value-extended-property a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view-calendar list-view

list-view a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-calendar-view-calendar update-event

update-event a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-event|UpdateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-calendar-view-calendar update-multi-value-extended-property

update-multi-value-extended-property a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-calendar-view-calendar update-permission

update-permission a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-permission|UpdateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar group-calendar-view-calendar update-single-value-extended-property

update-single-value-extended-property a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-calendar-view-calendar update-view

update-view a calendar group-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-calendar-view-calendar|groups.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-view|UpdateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-event create-attachment

create-attachment a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar group-event create-exception-occurrence

create-exception-occurrence a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-exception-occurrence|CreateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-event create-extension

create-extension a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

### calendar group-event create-instance

create-instance a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-instance|CreateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-event create-multi-value-extended-property

create-multi-value-extended-property a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-event create-single-value-extended-property

create-single-value-extended-property a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-event delete

delete a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExceptionOccurrences|
|delete|DeleteExtensions|
|delete|DeleteInstances|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar group-event get

get a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event get-attachment

get-attachment a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event get-exception-occurrence

get-exception-occurrence a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-exception-occurrence|GetExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event get-extension

get-extension a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event get-instance

get-instance a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-instance|GetInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event get-multi-value-extended-property

get-multi-value-extended-property a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event get-single-value-extended-property

get-single-value-extended-property a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event list-attachment

list-attachment a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event list-exception-occurrence

list-exception-occurrence a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-exception-occurrence|ListExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event list-extension

list-extension a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event list-instance

list-instance a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-instance|ListInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event list-multi-value-extended-property

list-multi-value-extended-property a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event list-single-value-extended-property

list-single-value-extended-property a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event update

update a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--calendar-group-id**|string||calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar group-event update-attachment

update-attachment a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar group-event update-exception-occurrence

update-exception-occurrence a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-exception-occurrence|UpdateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-event update-extension

update-extension a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### calendar group-event update-instance

update-instance a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-instance|UpdateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-event update-multi-value-extended-property

update-multi-value-extended-property a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-event update-single-value-extended-property

update-single-value-extended-property a calendar group-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event|groups.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-event-calendar create-event

create-event a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-event|CreateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-event-calendar create-multi-value-extended-property

create-multi-value-extended-property a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-event-calendar create-permission

create-permission a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-permission|CreateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar group-event-calendar create-single-value-extended-property

create-single-value-extended-property a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-event-calendar create-view

create-view a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-view|CreateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-event-calendar delete

delete a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

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
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar group-event-calendar get-event

get-event a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-event|GetEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event-calendar get-multi-value-extended-property

get-multi-value-extended-property a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event-calendar get-permission

get-permission a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission|GetCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event-calendar get-single-value-extended-property

get-single-value-extended-property a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event-calendar get-view

get-view a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event-calendar list-event

list-event a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-event|ListEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event-calendar list-multi-value-extended-property

list-multi-value-extended-property a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event-calendar list-permission

list-permission a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-permission|ListCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event-calendar list-single-value-extended-property

list-single-value-extended-property a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event-calendar list-view

list-view a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar group-event-calendar update-event

update-event a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-event|UpdateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar group-event-calendar update-multi-value-extended-property

update-multi-value-extended-property a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar group-event-calendar update-permission

update-permission a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-permission|UpdateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar group-event-calendar update-single-value-extended-property

update-single-value-extended-property a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar group-event-calendar update-view

update-view a calendar group-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar group-event-calendar|groups.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-view|UpdateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar place-place create-place

create-place a calendar place-place.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar place-place|places.place|

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

### calendar place-place delete

delete a calendar place-place.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar place-place|places.place|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePlace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--place-id**|string|key: id of place|place_id|place-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar place-place get-place

get-place a calendar place-place.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar place-place|places.place|

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

### calendar place-place list-place

list-place a calendar place-place.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar place-place|places.place|

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

### calendar place-place update-place

update-place a calendar place-place.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar place-place|places.place|

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

### calendar user create

create a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateCalendars|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--calendar-group-id**|string||calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar user create-event

create-event a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-event|CreateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user create-group

create-group a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-group|CreateCalendarGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string|Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--class-id**|uuid|The class identifier. Read-only.|class_id|classId|
|**--name**|string|The group name.|name|name|
|**--calendars**|array|The calendars in the calendar group. Navigation property. Read-only. Nullable.|calendars|calendars|

### calendar user create-view

create-view a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-view|CreateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user delete

delete a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCalendarGroups|
|delete|DeleteCalendars|
|delete|DeleteCalendarView|
|delete|DeleteEvents|
|delete|DeleteCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar user get

get a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendars|
|get|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user get-event

get-event a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-event|GetEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user get-group

get-group a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-group|GetCalendarGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user get-view

get-view a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user list

list a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListCalendars|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user list-event

list-event a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-event|ListEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user list-group

list-group a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-group|ListCalendarGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user list-view

list-view a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user update

update a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendars|
|update|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--calendar-group-id**|string||calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar user update-event

update-event a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-event|UpdateEvents|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user update-group

update-group a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-group|UpdateCalendarGroups|

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

### calendar user update-view

update-view a calendar user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-view|UpdateCalendarView|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar create-event

create-event a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-event|CreateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar create-multi-value-extended-property

create-multi-value-extended-property a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar user-calendar create-permission

create-permission a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-permission|CreateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar user-calendar create-single-value-extended-property

create-single-value-extended-property a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar user-calendar create-view

create-view a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-view|CreateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar delete

delete a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

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
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar user-calendar get-event

get-event a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-event|GetEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar get-multi-value-extended-property

get-multi-value-extended-property a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar get-permission

get-permission a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission|GetCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar get-single-value-extended-property

get-single-value-extended-property a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar get-view

get-view a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar list-event

list-event a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-event|ListEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar list-multi-value-extended-property

list-multi-value-extended-property a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar list-permission

list-permission a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-permission|ListCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar list-single-value-extended-property

list-single-value-extended-property a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar list-view

list-view a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar update-event

update-event a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-event|UpdateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar update-multi-value-extended-property

update-multi-value-extended-property a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar user-calendar update-permission

update-permission a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-permission|UpdateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar user-calendar update-single-value-extended-property

update-single-value-extended-property a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar user-calendar update-view

update-view a calendar user-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar|users.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-view|UpdateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-event create-attachment

create-attachment a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar user-calendar-event create-exception-occurrence

create-exception-occurrence a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-exception-occurrence|CreateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-event create-extension

create-extension a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

### calendar user-calendar-event create-instance

create-instance a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-instance|CreateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-event create-multi-value-extended-property

create-multi-value-extended-property a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar user-calendar-event create-single-value-extended-property

create-single-value-extended-property a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar user-calendar-event delete

delete a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExceptionOccurrences|
|delete|DeleteExtensions|
|delete|DeleteInstances|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar user-calendar-event get

get a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event get-attachment

get-attachment a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event get-exception-occurrence

get-exception-occurrence a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-exception-occurrence|GetExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event get-extension

get-extension a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event get-instance

get-instance a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-instance|GetInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event get-multi-value-extended-property

get-multi-value-extended-property a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event get-single-value-extended-property

get-single-value-extended-property a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event list-attachment

list-attachment a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event list-exception-occurrence

list-exception-occurrence a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-exception-occurrence|ListExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event list-extension

list-extension a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event list-instance

list-instance a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-instance|ListInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event list-multi-value-extended-property

list-multi-value-extended-property a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event list-single-value-extended-property

list-single-value-extended-property a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-event update

update a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--calendar-group-id**|string||calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar user-calendar-event update-attachment

update-attachment a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar user-calendar-event update-exception-occurrence

update-exception-occurrence a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-exception-occurrence|UpdateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-event update-extension

update-extension a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### calendar user-calendar-event update-instance

update-instance a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-instance|UpdateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-event update-multi-value-extended-property

update-multi-value-extended-property a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar user-calendar-event update-single-value-extended-property

update-single-value-extended-property a calendar user-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-event|users.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar user-calendar-group create

create a calendar user-calendar-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group|users.calendarGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateCalendars|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--microsoft-graph-calendar-group-id-calendar-group-id**|string||microsoft_graph_calendar_group_id_calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar user-calendar-group delete

delete a calendar user-calendar-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group|users.calendarGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCalendars|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar user-calendar-group get

get a calendar user-calendar-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group|users.calendarGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendars|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group list

list a calendar user-calendar-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group|users.calendarGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListCalendars|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group update

update a calendar user-calendar-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group|users.calendarGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendars|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--microsoft-graph-calendar-group-id-calendar-group-id**|string||microsoft_graph_calendar_group_id_calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar user-calendar-group-calendar create-event

create-event a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-event|CreateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar create-multi-value-extended-property

create-multi-value-extended-property a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar user-calendar-group-calendar create-permission

create-permission a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-permission|CreateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar user-calendar-group-calendar create-single-value-extended-property

create-single-value-extended-property a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar user-calendar-group-calendar create-view

create-view a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-view|CreateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--allow-new-time-proposals**|boolean|True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.|allow_new_time_proposals|allowNewTimeProposals|
|**--attendees**|array|The collection of attendees for the event.|attendees|attendees|
|**--body**|object|itemBody|body|body|
|**--body-preview**|string|The preview of the message associated with the event. It is in text format.|body_preview|bodyPreview|
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar delete

delete a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

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
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar user-calendar-group-calendar get-event

get-event a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-event|GetEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar get-multi-value-extended-property

get-multi-value-extended-property a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar get-permission

get-permission a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission|GetCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar get-single-value-extended-property

get-single-value-extended-property a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar get-view

get-view a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar list-event

list-event a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-event|ListEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar list-multi-value-extended-property

list-multi-value-extended-property a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar list-permission

list-permission a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-permission|ListCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar list-single-value-extended-property

list-single-value-extended-property a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar list-view

list-view a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar update-event

update-event a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-event|UpdateEvents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar update-multi-value-extended-property

update-multi-value-extended-property a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar user-calendar-group-calendar update-permission

update-permission a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-permission|UpdateCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

### calendar user-calendar-group-calendar update-single-value-extended-property

update-single-value-extended-property a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar user-calendar-group-calendar update-view

update-view a calendar user-calendar-group-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar|users.calendarGroups.calendars|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-view|UpdateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar-event create-attachment

create-attachment a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar user-calendar-group-calendar-event create-exception-occurrence

create-exception-occurrence a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-exception-occurrence|CreateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar-event create-extension

create-extension a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

### calendar user-calendar-group-calendar-event create-instance

create-instance a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-instance|CreateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar-event create-multi-value-extended-property

create-multi-value-extended-property a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar user-calendar-group-calendar-event create-single-value-extended-property

create-single-value-extended-property a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar user-calendar-group-calendar-event delete

delete a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExceptionOccurrences|
|delete|DeleteExtensions|
|delete|DeleteInstances|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar user-calendar-group-calendar-event get

get a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event get-attachment

get-attachment a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event get-exception-occurrence

get-exception-occurrence a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-exception-occurrence|GetExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event get-extension

get-extension a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event get-instance

get-instance a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-instance|GetInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event get-multi-value-extended-property

get-multi-value-extended-property a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event get-single-value-extended-property

get-single-value-extended-property a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event list-attachment

list-attachment a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event list-exception-occurrence

list-exception-occurrence a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-exception-occurrence|ListExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event list-extension

list-extension a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event list-instance

list-instance a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-instance|ListInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event list-multi-value-extended-property

list-multi-value-extended-property a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event list-single-value-extended-property

list-single-value-extended-property a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-event update

update a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--microsoft-graph-calendar-group-id-calendar-group-id**|string||microsoft_graph_calendar_group_id_calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar user-calendar-group-calendar-event update-attachment

update-attachment a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar user-calendar-group-calendar-event update-exception-occurrence

update-exception-occurrence a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-exception-occurrence|UpdateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar-event update-extension

update-extension a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### calendar user-calendar-group-calendar-event update-instance

update-instance a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-instance|UpdateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar-event update-multi-value-extended-property

update-multi-value-extended-property a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar user-calendar-group-calendar-event update-single-value-extended-property

update-single-value-extended-property a calendar user-calendar-group-calendar-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-event|users.calendarGroups.calendars.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar user-calendar-group-calendar-view create-attachment

create-attachment a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar user-calendar-group-calendar-view create-exception-occurrence

create-exception-occurrence a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-exception-occurrence|CreateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar-view create-extension

create-extension a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

### calendar user-calendar-group-calendar-view create-instance

create-instance a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-instance|CreateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar-view create-multi-value-extended-property

create-multi-value-extended-property a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar user-calendar-group-calendar-view create-single-value-extended-property

create-single-value-extended-property a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar user-calendar-group-calendar-view delete

delete a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExceptionOccurrences|
|delete|DeleteExtensions|
|delete|DeleteInstances|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar user-calendar-group-calendar-view get

get a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view get-attachment

get-attachment a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view get-exception-occurrence

get-exception-occurrence a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-exception-occurrence|GetExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view get-extension

get-extension a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view get-instance

get-instance a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-instance|GetInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view get-multi-value-extended-property

get-multi-value-extended-property a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view get-single-value-extended-property

get-single-value-extended-property a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view list-attachment

list-attachment a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view list-exception-occurrence

list-exception-occurrence a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-exception-occurrence|ListExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view list-extension

list-extension a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view list-instance

list-instance a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-instance|ListInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view list-multi-value-extended-property

list-multi-value-extended-property a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view list-single-value-extended-property

list-single-value-extended-property a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-group-calendar-view update

update a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--microsoft-graph-calendar-group-id-calendar-group-id**|string||microsoft_graph_calendar_group_id_calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar user-calendar-group-calendar-view update-attachment

update-attachment a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### calendar user-calendar-group-calendar-view update-exception-occurrence

update-exception-occurrence a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-exception-occurrence|UpdateExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar-view update-extension

update-extension a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### calendar user-calendar-group-calendar-view update-instance

update-instance a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-instance|UpdateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-group-calendar-view update-multi-value-extended-property

update-multi-value-extended-property a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### calendar user-calendar-group-calendar-view update-single-value-extended-property

update-single-value-extended-property a calendar user-calendar-group-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-group-calendar-view|users.calendarGroups.calendars.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### calendar user-calendar-view create-attachment

create-attachment a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view create-exception-occurrence

create-exception-occurrence a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-exception-occurrence|CreateExceptionOccurrences|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-view create-extension

create-extension a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view create-instance

create-instance a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-view create-multi-value-extended-property

create-multi-value-extended-property a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view create-single-value-extended-property

create-single-value-extended-property a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view delete

delete a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExceptionOccurrences|
|delete|DeleteExtensions|
|delete|DeleteInstances|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar user-calendar-view get

get a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-view get-attachment

get-attachment a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view get-exception-occurrence

get-exception-occurrence a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-exception-occurrence|GetExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-view get-extension

get-extension a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view get-instance

get-instance a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view get-multi-value-extended-property

get-multi-value-extended-property a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view get-single-value-extended-property

get-single-value-extended-property a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view list-attachment

list-attachment a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view list-exception-occurrence

list-exception-occurrence a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-exception-occurrence|ListExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-view list-extension

list-extension a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view list-instance

list-instance a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view list-multi-value-extended-property

list-multi-value-extended-property a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view list-single-value-extended-property

list-single-value-extended-property a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view update

update a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--calendar-group-id**|string||calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar user-calendar-view update-attachment

update-attachment a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view update-exception-occurrence

update-exception-occurrence a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-exception-occurrence|UpdateExceptionOccurrences|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-view update-extension

update-extension a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view update-instance

update-instance a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-view update-multi-value-extended-property

update-multi-value-extended-property a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view update-single-value-extended-property

update-single-value-extended-property a calendar user-calendar-view.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view|users.calendarView|

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

### calendar user-calendar-view-calendar create-event

create-event a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-view-calendar create-multi-value-extended-property

create-multi-value-extended-property a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar create-permission

create-permission a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-permission|CreateCalendarPermissions|

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

### calendar user-calendar-view-calendar create-single-value-extended-property

create-single-value-extended-property a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar create-view

create-view a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-view|CreateCalendarView|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-view-calendar delete

delete a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar get-event

get-event a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar get-multi-value-extended-property

get-multi-value-extended-property a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar get-permission

get-permission a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission|GetCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-view-calendar get-single-value-extended-property

get-single-value-extended-property a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar get-view

get-view a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-view-calendar list-event

list-event a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar list-multi-value-extended-property

list-multi-value-extended-property a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar list-permission

list-permission a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-permission|ListCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-view-calendar list-single-value-extended-property

list-single-value-extended-property a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar list-view

list-view a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-calendar-view-calendar update-event

update-event a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-calendar-view-calendar update-multi-value-extended-property

update-multi-value-extended-property a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar update-permission

update-permission a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-permission|UpdateCalendarPermissions|

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

### calendar user-calendar-view-calendar update-single-value-extended-property

update-single-value-extended-property a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

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

### calendar user-calendar-view-calendar update-view

update-view a calendar user-calendar-view-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-calendar-view-calendar|users.calendarView.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-view|UpdateCalendarView|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-event create-attachment

create-attachment a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event create-exception-occurrence

create-exception-occurrence a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-exception-occurrence|CreateExceptionOccurrences|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-event create-extension

create-extension a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event create-instance

create-instance a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-event create-multi-value-extended-property

create-multi-value-extended-property a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event create-single-value-extended-property

create-single-value-extended-property a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event delete

delete a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteExceptionOccurrences|
|delete|DeleteExtensions|
|delete|DeleteInstances|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### calendar user-event get

get a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-event get-attachment

get-attachment a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event get-exception-occurrence

get-exception-occurrence a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-exception-occurrence|GetExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-event get-extension

get-extension a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event get-instance

get-instance a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event get-multi-value-extended-property

get-multi-value-extended-property a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event get-single-value-extended-property

get-single-value-extended-property a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event list-attachment

list-attachment a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event list-exception-occurrence

list-exception-occurrence a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-exception-occurrence|ListExceptionOccurrences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-event list-extension

list-extension a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event list-instance

list-instance a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event list-multi-value-extended-property

list-multi-value-extended-property a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event list-single-value-extended-property

list-single-value-extended-property a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event update

update a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCalendar|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--calendar-group-id**|string||calendar_group_id|calendarGroupId|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--hex-color**|string||hex_color|hexColor|
|**--is-default-calendar**|boolean||is_default_calendar|isDefaultCalendar|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-shared**|boolean||is_shared|isShared|
|**--is-shared-with-me**|boolean||is_shared_with_me|isSharedWithMe|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### calendar user-event update-attachment

update-attachment a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event update-exception-occurrence

update-exception-occurrence a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-exception-occurrence|UpdateExceptionOccurrences|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-event update-extension

update-extension a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event update-instance

update-instance a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-event update-multi-value-extended-property

update-multi-value-extended-property a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event update-single-value-extended-property

update-single-value-extended-property a calendar user-event.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event|users.events|

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

### calendar user-event-calendar create-event

create-event a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-event-calendar create-multi-value-extended-property

create-multi-value-extended-property a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar create-permission

create-permission a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-permission|CreateCalendarPermissions|

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

### calendar user-event-calendar create-single-value-extended-property

create-single-value-extended-property a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar create-view

create-view a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-view|CreateCalendarView|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-event-calendar delete

delete a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar get-event

get-event a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar get-multi-value-extended-property

get-multi-value-extended-property a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar get-permission

get-permission a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission|GetCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-event-calendar get-single-value-extended-property

get-single-value-extended-property a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar get-view

get-view a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-event-calendar list-event

list-event a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar list-multi-value-extended-property

list-multi-value-extended-property a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar list-permission

list-permission a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-permission|ListCalendarPermissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-event-calendar list-single-value-extended-property

list-single-value-extended-property a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar list-view

list-view a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### calendar user-event-calendar update-event

update-event a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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

### calendar user-event-calendar update-multi-value-extended-property

update-multi-value-extended-property a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar update-permission

update-permission a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-permission|UpdateCalendarPermissions|

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

### calendar user-event-calendar update-single-value-extended-property

update-single-value-extended-property a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

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

### calendar user-event-calendar update-view

update-view a calendar user-event-calendar.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|calendar user-event-calendar|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-view|UpdateCalendarView|

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
|**--cancelled-occurrences**|array||cancelled_occurrences|cancelledOccurrences|
|**--end**|object|dateTimeTimeZone|end|end|
|**--has-attachments**|boolean|Set to true if the event has attachments.|has_attachments|hasAttachments|
|**--hide-attendees**|boolean||hide_attendees|hideAttendees|
|**--importance**|choice||importance|importance|
|**--is-all-day**|boolean|Set to true if the event lasts all day.|is_all_day|isAllDay|
|**--is-cancelled**|boolean|Set to true if the event has been canceled.|is_cancelled|isCancelled|
|**--is-draft**|boolean||is_draft|isDraft|
|**--is-online-meeting**|boolean|True if this event has online meeting information, false otherwise. Default is false. Optional.|is_online_meeting|isOnlineMeeting|
|**--is-organizer**|boolean|Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). This also applies if a delegate organized the event on behalf of the owner.|is_organizer|isOrganizer|
|**--is-reminder-on**|boolean|Set to true if an alert is set to remind the user of the event.|is_reminder_on|isReminderOn|
|**--locations**|array|The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.|locations|locations|
|**--occurrence-id**|string||occurrence_id|occurrenceId|
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
|**--uid**|string||uid|uid|
|**--web-link**|string|The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--attachments**|array|The collection of fileAttachment and itemAttachment attachments for the event. Navigation property. Read-only. Nullable.|attachments|attachments|
|**--calendar**|object|calendar|calendar|calendar|
|**--exception-occurrences**|array||exception_occurrences|exceptionOccurrences|
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