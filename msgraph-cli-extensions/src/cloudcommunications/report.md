# Azure CLI Module Creation Report

### cloudcommunications create-online-meeting

create-online-meeting a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-online-meeting|CreateOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--audio-conferencing**|object|audioConferencing|audio_conferencing|audioConferencing|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--creation-date-time**|date-time|The meeting creation time in UTC. Read-only.|creation_date_time|creationDateTime|
|**--end-date-time**|date-time|The meeting end time in UTC.|end_date_time|endDateTime|
|**--external-id**|string||external_id|externalId|
|**--join-information**|object|itemBody|join_information|joinInformation|
|**--join-web-url**|string|The join URL of the online meeting. Read-only.|join_web_url|joinWebUrl|
|**--start-date-time**|date-time|The meeting start time in UTC.|start_date_time|startDateTime|
|**--subject**|string|The subject of the online meeting.|subject|subject|
|**--video-teleconference-id**|string|The video teleconferencing ID. Read-only.|video_teleconference_id|videoTeleconferenceId|
|**--participants-attendees**|array||attendees|attendees|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|

### cloudcommunications delete

delete a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--if-match**|string|ETag|if_match|If-Match|

### cloudcommunications get-online-meeting

get-online-meeting a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-online-meeting|GetOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications list-online-meeting

list-online-meeting a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-online-meeting|ListOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications update-online-meeting

update-online-meeting a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-online-meeting|UpdateOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--id**|string|Read-only.|id|id|
|**--audio-conferencing**|object|audioConferencing|audio_conferencing|audioConferencing|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--creation-date-time**|date-time|The meeting creation time in UTC. Read-only.|creation_date_time|creationDateTime|
|**--end-date-time**|date-time|The meeting end time in UTC.|end_date_time|endDateTime|
|**--external-id**|string||external_id|externalId|
|**--join-information**|object|itemBody|join_information|joinInformation|
|**--join-web-url**|string|The join URL of the online meeting. Read-only.|join_web_url|joinWebUrl|
|**--start-date-time**|date-time|The meeting start time in UTC.|start_date_time|startDateTime|
|**--subject**|string|The subject of the online meeting.|subject|subject|
|**--video-teleconference-id**|string|The video teleconferencing ID. Read-only.|video_teleconference_id|videoTeleconferenceId|
|**--participants-attendees**|array||attendees|attendees|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
