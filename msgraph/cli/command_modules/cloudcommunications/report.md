# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az cloudcommunications|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az cloudcommunications` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az cloudcommunications user|users|[commands](#CommandsInusers)|

## COMMANDS
### <a name="CommandsInusers">Commands in `az cloudcommunications user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cloudcommunications user create-online-meeting](#usersCreateOnlineMeetings)|CreateOnlineMeetings|[Parameters](#ParametersusersCreateOnlineMeetings)|Not Found|
|[az cloudcommunications user delete-online-meeting](#usersDeleteOnlineMeetings)|DeleteOnlineMeetings|[Parameters](#ParametersusersDeleteOnlineMeetings)|Not Found|
|[az cloudcommunications user list-online-meeting](#usersListOnlineMeetings)|ListOnlineMeetings|[Parameters](#ParametersusersListOnlineMeetings)|Not Found|
|[az cloudcommunications user show-online-meeting](#usersGetOnlineMeetings)|GetOnlineMeetings|[Parameters](#ParametersusersGetOnlineMeetings)|Not Found|
|[az cloudcommunications user update-online-meeting](#usersUpdateOnlineMeetings)|UpdateOnlineMeetings|[Parameters](#ParametersusersUpdateOnlineMeetings)|Not Found|


## COMMAND DETAILS
### group `az cloudcommunications user`
#### <a name="usersCreateOnlineMeetings">Command `az cloudcommunications user create-online-meeting`</a>


##### <a name="ParametersusersCreateOnlineMeetings">Parameters</a> 
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
|**--attendees**|array||attendees|attendees|
|**--organizer**|object|meetingParticipantInfo|organizer|organizer|

#### <a name="usersDeleteOnlineMeetings">Command `az cloudcommunications user delete-online-meeting`</a>


##### <a name="ParametersusersDeleteOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListOnlineMeetings">Command `az cloudcommunications user list-online-meeting`</a>


##### <a name="ParametersusersListOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetOnlineMeetings">Command `az cloudcommunications user show-online-meeting`</a>


##### <a name="ParametersusersGetOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateOnlineMeetings">Command `az cloudcommunications user update-online-meeting`</a>


##### <a name="ParametersusersUpdateOnlineMeetings">Parameters</a> 
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
|**--attendees**|array||attendees|attendees|
|**--organizer**|object|meetingParticipantInfo|organizer|organizer|
