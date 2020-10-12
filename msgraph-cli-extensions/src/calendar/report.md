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
|**--body**|object|New navigation property|body|body|

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
|**--body**|object|New navigation property|body|body|

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
|**--body**|object|New navigation property|body|body|

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
|**--body**|object|New navigation property values|body|body|

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
|**--body**|object|New navigation property values|body|body|

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
|**--body**|object|New navigation property values|body|body|

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
