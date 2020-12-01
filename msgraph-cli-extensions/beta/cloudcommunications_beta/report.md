# Azure CLI Module Creation Report

### cloudcommunications answer

answer a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|answer|answer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--callback-uri**|string||callback_uri|callbackUri|
|**--accepted-modalities**|array||accepted_modalities|acceptedModalities|
|**--media-config-remove-from-default-audio-group**|boolean||remove_from_default_audio_group|removeFromDefaultAudioGroup|

### cloudcommunications cancel-media-processing

cancel-media-processing a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel-media-processing|cancelMediaProcessing|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications change-screen-sharing-role

change-screen-sharing-role a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|change-screen-sharing-role|changeScreenSharingRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--role**|choice||role|role|

### cloudcommunications create-audio-routing-group

create-audio-routing-group a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-audio-routing-group|CreateAudioRoutingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--routing-mode**|choice||routing_mode|routingMode|
|**--sources**|array||sources|sources|
|**--receivers**|array||receivers|receivers|

### cloudcommunications create-call

create-call a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-call|CreateCalls|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--state**|choice||state|state|
|**--result-info**|object|ResultInfo|result_info|resultInfo|
|**--termination-reason**|string||termination_reason|terminationReason|
|**--direction**|choice||direction|direction|
|**--ringing-timeout-in-seconds**|integer||ringing_timeout_in_seconds|ringingTimeoutInSeconds|
|**--subject**|string|The subject of the conversation.|subject|subject|
|**--callback-uri**|string|The callback URL on which callbacks will be delivered. Must be https.|callback_uri|callbackUri|
|**--call-routes**|array||call_routes|callRoutes|
|**--targets**|array|The targets of the call. Required information for creating peer to peer call.|targets|targets|
|**--requested-modalities**|array|The list of requested modalities.|requested_modalities|requestedModalities|
|**--active-modalities**|array||active_modalities|activeModalities|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--call-options**|any|Any object|call_options|callOptions|
|**--meeting-capability**|object|meetingCapability|meeting_capability|meetingCapability|
|**--routing-policies**|array||routing_policies|routingPolicies|
|**--tenant-id**|string||tenant_id|tenantId|
|**--my-participant-id**|string|Read-only.|my_participant_id|myParticipantId|
|**--tone-info**|object|toneInfo|tone_info|toneInfo|
|**--participants**|array|Read-only. Nullable.|participants|participants|
|**--audio-routing-groups**|array||audio_routing_groups|audioRoutingGroups|
|**--operations**|array|Read-only. Nullable.|operations|operations|
|**--incoming-context-source-participant-id**|string||source_participant_id|sourceParticipantId|
|**--incoming-context-observed-participant-id**|string||observed_participant_id|observedParticipantId|
|**--incoming-context-on-behalf-of**|object|identitySet|on_behalf_of|onBehalfOf|
|**--incoming-context-transferor**|object|identitySet|transferor|transferor|
|**--meeting-info-allow-conversation-without-host**|boolean||allow_conversation_without_host|allowConversationWithoutHost|
|**--media-config-remove-from-default-audio-group**|boolean||remove_from_default_audio_group|removeFromDefaultAudioGroup|
|**--answered-by-identity**|object|identitySet|identity|identity|
|**--answered-by-endpoint-type**|choice||endpoint_type|endpointType|
|**--answered-by-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|
|**--answered-by-language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--answered-by-country-code**|string||country_code|countryCode|
|**--source-identity**|object|identitySet|microsoft_graph_identity_set_identity|identity|
|**--source-endpoint-type**|choice||microsoft_graph_endpoint_type|endpointType|
|**--source-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|microsoft_graph_participant_info_region|region|
|**--source-language-id**|string|The language culture string. Read-only.|microsoft_graph_participant_info_language_id|languageId|
|**--source-country-code**|string||microsoft_graph_participant_info_country_code|countryCode|
|**--media-state-audio**|choice||audio|audio|

### cloudcommunications create-call-record

create-call-record a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-call-record|CreateCallRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--version**|integer||version|version|
|**--type**|choice||type|type|
|**--modalities**|array||modalities|modalities|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--participants**|array||participants|participants|
|**--join-web-url**|string||join_web_url|joinWebUrl|
|**--sessions**|array||sessions|sessions|
|**--organizer-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--organizer-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--organizer-device-id**|string|Unique identifier for the identity.|id1|id|
|**--organizer-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--organizer-application-id**|string|Unique identifier for the identity.|id2|id|
|**--organizer-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|

### cloudcommunications create-online-meeting

create-online-meeting a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-online-meeting|CreateOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
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
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--participants-attendees**|array||attendees|attendees|
|**--participants-producers**|array||producers|producers|
|**--participants-contributors**|array||contributors|contributors|

### cloudcommunications create-operation

create-operation a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-operation|CreateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--status**|choice||status|status|
|**--client-context**|string|Unique Client Context string. Max limit is 256 chars.|client_context|clientContext|
|**--result-info-code**|integer||code|code|
|**--result-info-subcode**|integer||subcode|subcode|
|**--result-info-message**|string||message|message|

### cloudcommunications create-participant

create-participant a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-participant|CreateParticipants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--media-streams**|array|The list of media streams.|media_streams|mediaStreams|
|**--metadata**|string||metadata|metadata|
|**--is-muted**|boolean|true if the participant is muted (client or server muted).|is_muted|isMuted|
|**--is-in-lobby**|boolean|true if the participant is in lobby.|is_in_lobby|isInLobby|
|**--recording-info-recording-status**|choice||recording_status|recordingStatus|
|**--recording-info-initiated-by**|object|participantInfo|initiated_by|initiatedBy|
|**--recording-info-initiator**|object|identitySet|initiator|initiator|
|**--info-identity**|object|identitySet|identity|identity|
|**--info-endpoint-type**|choice||endpoint_type|endpointType|
|**--info-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|
|**--info-language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--info-country-code**|string||country_code|countryCode|

### cloudcommunications create-segment

create-segment a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.callRecords.sessions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-segment|CreateSegments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: callRecord-id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: session-id of session|session_id|session-id|
|**--id**|string|Read-only.|id|id|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--failure-info**|object|failureInfo|failure_info|failureInfo|
|**--media**|array||media|media|
|**--callee-user-agent**|object|userAgent|user_agent|userAgent|
|**--caller-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

### cloudcommunications create-session

create-session a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.callRecords|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-session|CreateSessions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: callRecord-id of callRecord|call_record_id|callRecord-id|
|**--id**|string|Read-only.|id|id|
|**--modalities**|array||modalities|modalities|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--failure-info**|object|failureInfo|failure_info|failureInfo|
|**--segments**|array||segments|segments|
|**--callee-user-agent**|object|userAgent|user_agent|userAgent|
|**--caller-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

### cloudcommunications get-audio-routing-group

get-audio-routing-group a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-audio-routing-group|GetAudioRoutingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--audio-routing-group-id**|string|key: audioRoutingGroup-id of audioRoutingGroup|audio_routing_group_id|audioRoutingGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications get-call

get-call a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-call|GetCalls|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications get-call-record

get-call-record a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-call-record|GetCallRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: callRecord-id of callRecord|call_record_id|callRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications get-cloud-communication

get-cloud-communication a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.cloudCommunications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-cloud-communication|GetCloudCommunications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications get-online-meeting

get-online-meeting a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-online-meeting|GetOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--online-meeting-id**|string|key: onlineMeeting-id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications get-operation

get-operation a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-operation|GetOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--comms-operation-id**|string|key: commsOperation-id of commsOperation|comms_operation_id|commsOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications get-participant

get-participant a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-participant|GetParticipants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--participant-id**|string|key: participant-id of participant|participant_id|participant-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications get-presence-by-user-id

get-presence-by-user-id a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-presence-by-user-id|getPresencesByUserId|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|

### cloudcommunications get-segment

get-segment a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.callRecords.sessions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-segment|GetSegments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: callRecord-id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: session-id of session|session_id|session-id|
|**--segment-id**|string|key: segment-id of segment|segment_id|segment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications get-session

get-session a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.callRecords|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-session|GetSessions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: callRecord-id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: session-id of session|session_id|session-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications invite

invite a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls.participants|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|invite|invite|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--participants**|array||participants|participants|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications keep-alive

keep-alive a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|keep-alive|keepAlive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|

### cloudcommunications list-audio-routing-group

list-audio-routing-group a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-audio-routing-group|ListAudioRoutingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications list-call

list-call a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-call|ListCalls|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications list-call-record

list-call-record a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-call-record|ListCallRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications list-online-meeting

list-online-meeting a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-online-meeting|ListOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications list-operation

list-operation a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-operation|ListOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications list-participant

list-participant a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-participant|ListParticipants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications list-segment

list-segment a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.callRecords.sessions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-segment|ListSegments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: callRecord-id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: session-id of session|session_id|session-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications list-session

list-session a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.callRecords|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-session|ListSessions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: callRecord-id of callRecord|call_record_id|callRecord-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications mute

mute a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls.participants|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|mute|mute|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--participant-id**|string|key: participant-id of participant|participant_id|participant-id|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications mute-all

mute-all a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls.participants|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|mute-all|muteAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--participants**|array||participants|participants|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications play-prompt

play-prompt a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|play-prompt|playPrompt|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--prompts**|array||prompts|prompts|
|**--loop**|boolean||loop|loop|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications record

record a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|record|record|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--prompts**|array||prompts|prompts|
|**--barge-in-allowed**|boolean||barge_in_allowed|bargeInAllowed|
|**--initial-silence-timeout-in-seconds**|integer||initial_silence_timeout_in_seconds|initialSilenceTimeoutInSeconds|
|**--max-silence-timeout-in-seconds**|integer||max_silence_timeout_in_seconds|maxSilenceTimeoutInSeconds|
|**--max-record-duration-in-seconds**|integer||max_record_duration_in_seconds|maxRecordDurationInSeconds|
|**--play-beep**|boolean||play_beep|playBeep|
|**--stream-while-recording**|boolean||stream_while_recording|streamWhileRecording|
|**--stop-tones**|array||stop_tones|stopTones|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications record-response

record-response a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|record-response|recordResponse|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--prompts**|array||prompts|prompts|
|**--barge-in-allowed**|boolean||barge_in_allowed|bargeInAllowed|
|**--initial-silence-timeout-in-seconds**|integer||initial_silence_timeout_in_seconds|initialSilenceTimeoutInSeconds|
|**--max-silence-timeout-in-seconds**|integer||max_silence_timeout_in_seconds|maxSilenceTimeoutInSeconds|
|**--max-record-duration-in-seconds**|integer||max_record_duration_in_seconds|maxRecordDurationInSeconds|
|**--play-beep**|boolean||play_beep|playBeep|
|**--stream-while-recording**|boolean||stream_while_recording|streamWhileRecording|
|**--stop-tones**|array||stop_tones|stopTones|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications redirect

redirect a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|redirect|redirect|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--targets**|array||targets|targets|
|**--target-disposition**|choice||target_disposition|targetDisposition|
|**--timeout**|integer||timeout|timeout|
|**--mask-callee**|boolean||mask_callee|maskCallee|
|**--mask-caller**|boolean||mask_caller|maskCaller|
|**--callback-uri**|string||callback_uri|callbackUri|

### cloudcommunications reject

reject a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reject|reject|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--reason**|choice||reason|reason|
|**--callback-uri**|string||callback_uri|callbackUri|

### cloudcommunications subscribe-to-tone

subscribe-to-tone a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|subscribe-to-tone|subscribeToTone|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications transfer

transfer a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|transfer|transfer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--transfer-target-endpoint-type**|choice||endpoint_type|endpointType|
|**--transfer-target-replaces-call-id**|string|Optional. The call which the target identity is currently a part of. This call will be dropped once the participant is added.|replaces_call_id|replacesCallId|
|**--transfer-target-identity-user-id**|string|Unique identifier for the identity.|id|id|
|**--transfer-target-identity-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--transfer-target-identity-device-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--transfer-target-identity-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--transfer-target-identity-application-id**|string|Unique identifier for the identity.|id1|id|
|**--transfer-target-identity-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|

### cloudcommunications unmute

unmute a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unmute|unmute|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications update-audio-routing-group

update-audio-routing-group a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-audio-routing-group|UpdateAudioRoutingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--audio-routing-group-id**|string|key: audioRoutingGroup-id of audioRoutingGroup|audio_routing_group_id|audioRoutingGroup-id|
|**--id**|string|Read-only.|id|id|
|**--routing-mode**|choice||routing_mode|routingMode|
|**--sources**|array||sources|sources|
|**--receivers**|array||receivers|receivers|

### cloudcommunications update-call

update-call a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-call|UpdateCalls|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--state**|choice||state|state|
|**--result-info**|object|ResultInfo|result_info|resultInfo|
|**--termination-reason**|string||termination_reason|terminationReason|
|**--direction**|choice||direction|direction|
|**--ringing-timeout-in-seconds**|integer||ringing_timeout_in_seconds|ringingTimeoutInSeconds|
|**--subject**|string|The subject of the conversation.|subject|subject|
|**--callback-uri**|string|The callback URL on which callbacks will be delivered. Must be https.|callback_uri|callbackUri|
|**--call-routes**|array||call_routes|callRoutes|
|**--targets**|array|The targets of the call. Required information for creating peer to peer call.|targets|targets|
|**--requested-modalities**|array|The list of requested modalities.|requested_modalities|requestedModalities|
|**--active-modalities**|array||active_modalities|activeModalities|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--call-options**|any|Any object|call_options|callOptions|
|**--meeting-capability**|object|meetingCapability|meeting_capability|meetingCapability|
|**--routing-policies**|array||routing_policies|routingPolicies|
|**--tenant-id**|string||tenant_id|tenantId|
|**--my-participant-id**|string|Read-only.|my_participant_id|myParticipantId|
|**--tone-info**|object|toneInfo|tone_info|toneInfo|
|**--participants**|array|Read-only. Nullable.|participants|participants|
|**--audio-routing-groups**|array||audio_routing_groups|audioRoutingGroups|
|**--operations**|array|Read-only. Nullable.|operations|operations|
|**--incoming-context-source-participant-id**|string||source_participant_id|sourceParticipantId|
|**--incoming-context-observed-participant-id**|string||observed_participant_id|observedParticipantId|
|**--incoming-context-on-behalf-of**|object|identitySet|on_behalf_of|onBehalfOf|
|**--incoming-context-transferor**|object|identitySet|transferor|transferor|
|**--meeting-info-allow-conversation-without-host**|boolean||allow_conversation_without_host|allowConversationWithoutHost|
|**--media-config-remove-from-default-audio-group**|boolean||remove_from_default_audio_group|removeFromDefaultAudioGroup|
|**--answered-by-identity**|object|identitySet|identity|identity|
|**--answered-by-endpoint-type**|choice||endpoint_type|endpointType|
|**--answered-by-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|
|**--answered-by-language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--answered-by-country-code**|string||country_code|countryCode|
|**--source-identity**|object|identitySet|microsoft_graph_identity_set_identity|identity|
|**--source-endpoint-type**|choice||microsoft_graph_endpoint_type|endpointType|
|**--source-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|microsoft_graph_participant_info_region|region|
|**--source-language-id**|string|The language culture string. Read-only.|microsoft_graph_participant_info_language_id|languageId|
|**--source-country-code**|string||microsoft_graph_participant_info_country_code|countryCode|
|**--media-state-audio**|choice||audio|audio|

### cloudcommunications update-call-record

update-call-record a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-call-record|UpdateCallRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: callRecord-id of callRecord|call_record_id|callRecord-id|
|**--id**|string|Read-only.|id|id|
|**--version**|integer||version|version|
|**--type**|choice||type|type|
|**--modalities**|array||modalities|modalities|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--participants**|array||participants|participants|
|**--join-web-url**|string||join_web_url|joinWebUrl|
|**--sessions**|array||sessions|sessions|
|**--organizer-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--organizer-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--organizer-device-id**|string|Unique identifier for the identity.|id1|id|
|**--organizer-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--organizer-application-id**|string|Unique identifier for the identity.|id2|id|
|**--organizer-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|

### cloudcommunications update-cloud-communication

update-cloud-communication a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.cloudCommunications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-cloud-communication|UpdateCloudCommunications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--calls**|array||calls|calls|
|**--call-records**|array||call_records|callRecords|
|**--online-meetings**|array||online_meetings|onlineMeetings|

### cloudcommunications update-online-meeting

update-online-meeting a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-online-meeting|UpdateOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
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
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--participants-attendees**|array||attendees|attendees|
|**--participants-producers**|array||producers|producers|
|**--participants-contributors**|array||contributors|contributors|

### cloudcommunications update-operation

update-operation a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-operation|UpdateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--comms-operation-id**|string|key: commsOperation-id of commsOperation|comms_operation_id|commsOperation-id|
|**--id**|string|Read-only.|id|id|
|**--status**|choice||status|status|
|**--client-context**|string|Unique Client Context string. Max limit is 256 chars.|client_context|clientContext|
|**--result-info-code**|integer||code|code|
|**--result-info-subcode**|integer||subcode|subcode|
|**--result-info-message**|string||message|message|

### cloudcommunications update-participant

update-participant a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-participant|UpdateParticipants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--participant-id**|string|key: participant-id of participant|participant_id|participant-id|
|**--id**|string|Read-only.|id|id|
|**--media-streams**|array|The list of media streams.|media_streams|mediaStreams|
|**--metadata**|string||metadata|metadata|
|**--is-muted**|boolean|true if the participant is muted (client or server muted).|is_muted|isMuted|
|**--is-in-lobby**|boolean|true if the participant is in lobby.|is_in_lobby|isInLobby|
|**--recording-info-recording-status**|choice||recording_status|recordingStatus|
|**--recording-info-initiated-by**|object|participantInfo|initiated_by|initiatedBy|
|**--recording-info-initiator**|object|identitySet|initiator|initiator|
|**--info-identity**|object|identitySet|identity|identity|
|**--info-endpoint-type**|choice||endpoint_type|endpointType|
|**--info-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|
|**--info-language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--info-country-code**|string||country_code|countryCode|

### cloudcommunications update-recording-status

update-recording-status a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-recording-status|updateRecordingStatus|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: call-id of call|call_id|call-id|
|**--status**|choice||status|status|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications update-segment

update-segment a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.callRecords.sessions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-segment|UpdateSegments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: callRecord-id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: session-id of session|session_id|session-id|
|**--segment-id**|string|key: segment-id of segment|segment_id|segment-id|
|**--id**|string|Read-only.|id|id|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--failure-info**|object|failureInfo|failure_info|failureInfo|
|**--media**|array||media|media|
|**--callee-user-agent**|object|userAgent|user_agent|userAgent|
|**--caller-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

### cloudcommunications update-session

update-session a cloudcommunications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications|communications.callRecords|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-session|UpdateSessions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: callRecord-id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: session-id of session|session_id|session-id|
|**--id**|string|Read-only.|id|id|
|**--modalities**|array||modalities|modalities|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--failure-info**|object|failureInfo|failure_info|failureInfo|
|**--segments**|array||segments|segments|
|**--callee-user-agent**|object|userAgent|user_agent|userAgent|
|**--caller-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|
