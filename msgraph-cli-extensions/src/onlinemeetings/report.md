# Azure CLI Module Creation Report

### onlinemeetings create-online-meeting

create-online-meeting a onlinemeetings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onlinemeetings|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-online-meeting|CreateOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--creation-date-time**|date-time|The meeting creation time in UTC. Read-only.|creation_date_time|creationDateTime|
|**--start-date-time**|date-time|The meeting start time in UTC.|start_date_time|startDateTime|
|**--end-date-time**|date-time|The meeting end time in UTC.|end_date_time|endDateTime|
|**--canceled-date-time**|date-time||canceled_date_time|canceledDateTime|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--entry-exit-announcement**|boolean||entry_exit_announcement|entryExitAnnouncement|
|**--join-url**|string||join_url|joinUrl|
|**--subject**|string|The subject of the online meeting.|subject|subject|
|**--is-cancelled**|boolean||is_cancelled|isCancelled|
|**--is-broadcast**|boolean||is_broadcast|isBroadcast|
|**--access-level**|choice||access_level|accessLevel|
|**--capabilities**|array||capabilities|capabilities|
|**--audio-conferencing**|object|audioConferencing|audio_conferencing|audioConferencing|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--video-teleconference-id**|string|The video teleconferencing ID. Read-only.|video_teleconference_id|videoTeleconferenceId|
|**--external-id**|string||external_id|externalId|
|**--join-information**|object|itemBody|join_information|joinInformation|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--participants-attendees**|array||attendees|attendees|
|**--participants-producers**|array||producers|producers|
|**--participants-contributors**|array||contributors|contributors|

### onlinemeetings get-online-meeting

get-online-meeting a onlinemeetings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onlinemeetings|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-online-meeting|GetOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--online-meeting-id**|string|key: onlineMeeting-id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onlinemeetings list-online-meeting

list-online-meeting a onlinemeetings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onlinemeetings|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-online-meeting|ListOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onlinemeetings update

update a onlinemeetings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onlinemeetings|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--online-meeting-id**|string|key: onlineMeeting-id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--id**|string|Read-only.|id|id|
|**--creation-date-time**|date-time|The meeting creation time in UTC. Read-only.|creation_date_time|creationDateTime|
|**--start-date-time**|date-time|The meeting start time in UTC.|start_date_time|startDateTime|
|**--end-date-time**|date-time|The meeting end time in UTC.|end_date_time|endDateTime|
|**--canceled-date-time**|date-time||canceled_date_time|canceledDateTime|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--entry-exit-announcement**|boolean||entry_exit_announcement|entryExitAnnouncement|
|**--join-url**|string||join_url|joinUrl|
|**--subject**|string|The subject of the online meeting.|subject|subject|
|**--is-cancelled**|boolean||is_cancelled|isCancelled|
|**--is-broadcast**|boolean||is_broadcast|isBroadcast|
|**--access-level**|choice||access_level|accessLevel|
|**--capabilities**|array||capabilities|capabilities|
|**--audio-conferencing**|object|audioConferencing|audio_conferencing|audioConferencing|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--video-teleconference-id**|string|The video teleconferencing ID. Read-only.|video_teleconference_id|videoTeleconferenceId|
|**--external-id**|string||external_id|externalId|
|**--join-information**|object|itemBody|join_information|joinInformation|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--participants-attendees**|array||attendees|attendees|
|**--participants-producers**|array||producers|producers|
|**--participants-contributors**|array||contributors|contributors|
