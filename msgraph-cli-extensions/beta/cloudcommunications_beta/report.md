# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az cloudcommunications_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az cloudcommunications_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az cloudcommunications communication-cloud-communication|communications.cloudCommunications|[commands](#CommandsIncommunications.cloudCommunications)|
|az cloudcommunications communication|communications|[commands](#CommandsIncommunications)|
|az cloudcommunications communication-call-record|communications.callRecords|[commands](#CommandsIncommunications.callRecords)|
|az cloudcommunications communication-call-record-session|communications.callRecords.sessions|[commands](#CommandsIncommunications.callRecords.sessions)|
|az cloudcommunications communication-call|communications.calls|[commands](#CommandsIncommunications.calls)|
|az cloudcommunications communication-call-participant|communications.calls.participants|[commands](#CommandsIncommunications.calls.participants)|
|az cloudcommunications communication-online-meeting|communications.onlineMeetings|[commands](#CommandsIncommunications.onlineMeetings)|
|az cloudcommunications user|users|[commands](#CommandsInusers)|

## COMMANDS
### <a name="CommandsIncommunications">Commands in `az cloudcommunications communication` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cloudcommunications communication delete](#communicationsDeleteCallRecords)|DeleteCallRecords|[Parameters](#ParameterscommunicationsDeleteCallRecords)|Not Found|
|[az cloudcommunications communication delete](#communicationsDeleteCalls)|DeleteCalls|[Parameters](#ParameterscommunicationsDeleteCalls)|Not Found|
|[az cloudcommunications communication delete](#communicationsDeleteOnlineMeetings)|DeleteOnlineMeetings|[Parameters](#ParameterscommunicationsDeleteOnlineMeetings)|Not Found|
|[az cloudcommunications communication delete](#communicationsDeletePresences)|DeletePresences|[Parameters](#ParameterscommunicationsDeletePresences)|Not Found|
|[az cloudcommunications communication create-call](#communicationsCreateCalls)|CreateCalls|[Parameters](#ParameterscommunicationsCreateCalls)|Not Found|
|[az cloudcommunications communication create-call-record](#communicationsCreateCallRecords)|CreateCallRecords|[Parameters](#ParameterscommunicationsCreateCallRecords)|Not Found|
|[az cloudcommunications communication create-online-meeting](#communicationsCreateOnlineMeetings)|CreateOnlineMeetings|[Parameters](#ParameterscommunicationsCreateOnlineMeetings)|Not Found|
|[az cloudcommunications communication create-presence](#communicationsCreatePresences)|CreatePresences|[Parameters](#ParameterscommunicationsCreatePresences)|Not Found|
|[az cloudcommunications communication get-presence-by-user-id](#communicationsgetPresencesByUserId)|getPresencesByUserId|[Parameters](#ParameterscommunicationsgetPresencesByUserId)|Not Found|
|[az cloudcommunications communication list-call](#communicationsListCalls)|ListCalls|[Parameters](#ParameterscommunicationsListCalls)|Not Found|
|[az cloudcommunications communication list-call-record](#communicationsListCallRecords)|ListCallRecords|[Parameters](#ParameterscommunicationsListCallRecords)|Not Found|
|[az cloudcommunications communication list-online-meeting](#communicationsListOnlineMeetings)|ListOnlineMeetings|[Parameters](#ParameterscommunicationsListOnlineMeetings)|Not Found|
|[az cloudcommunications communication list-presence](#communicationsListPresences)|ListPresences|[Parameters](#ParameterscommunicationsListPresences)|Not Found|
|[az cloudcommunications communication show-call](#communicationsGetCalls)|GetCalls|[Parameters](#ParameterscommunicationsGetCalls)|Not Found|
|[az cloudcommunications communication show-call-record](#communicationsGetCallRecords)|GetCallRecords|[Parameters](#ParameterscommunicationsGetCallRecords)|Not Found|
|[az cloudcommunications communication show-online-meeting](#communicationsGetOnlineMeetings)|GetOnlineMeetings|[Parameters](#ParameterscommunicationsGetOnlineMeetings)|Not Found|
|[az cloudcommunications communication show-presence](#communicationsGetPresences)|GetPresences|[Parameters](#ParameterscommunicationsGetPresences)|Not Found|
|[az cloudcommunications communication update-call](#communicationsUpdateCalls)|UpdateCalls|[Parameters](#ParameterscommunicationsUpdateCalls)|Not Found|
|[az cloudcommunications communication update-call-record](#communicationsUpdateCallRecords)|UpdateCallRecords|[Parameters](#ParameterscommunicationsUpdateCallRecords)|Not Found|
|[az cloudcommunications communication update-online-meeting](#communicationsUpdateOnlineMeetings)|UpdateOnlineMeetings|[Parameters](#ParameterscommunicationsUpdateOnlineMeetings)|Not Found|
|[az cloudcommunications communication update-presence](#communicationsUpdatePresences)|UpdatePresences|[Parameters](#ParameterscommunicationsUpdatePresences)|Not Found|

### <a name="CommandsIncommunications.calls">Commands in `az cloudcommunications communication-call` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cloudcommunications communication-call delete](#communications.callsDeleteAudioRoutingGroups)|DeleteAudioRoutingGroups|[Parameters](#Parameterscommunications.callsDeleteAudioRoutingGroups)|Not Found|
|[az cloudcommunications communication-call delete](#communications.callsDeleteOperations)|DeleteOperations|[Parameters](#Parameterscommunications.callsDeleteOperations)|Not Found|
|[az cloudcommunications communication-call delete](#communications.callsDeleteParticipants)|DeleteParticipants|[Parameters](#Parameterscommunications.callsDeleteParticipants)|Not Found|
|[az cloudcommunications communication-call answer](#communications.callsanswer)|answer|[Parameters](#Parameterscommunications.callsanswer)|Not Found|
|[az cloudcommunications communication-call cancel-media-processing](#communications.callscancelMediaProcessing)|cancelMediaProcessing|[Parameters](#Parameterscommunications.callscancelMediaProcessing)|Not Found|
|[az cloudcommunications communication-call change-screen-sharing-role](#communications.callschangeScreenSharingRole)|changeScreenSharingRole|[Parameters](#Parameterscommunications.callschangeScreenSharingRole)|Not Found|
|[az cloudcommunications communication-call create-audio-routing-group](#communications.callsCreateAudioRoutingGroups)|CreateAudioRoutingGroups|[Parameters](#Parameterscommunications.callsCreateAudioRoutingGroups)|Not Found|
|[az cloudcommunications communication-call create-operation](#communications.callsCreateOperations)|CreateOperations|[Parameters](#Parameterscommunications.callsCreateOperations)|Not Found|
|[az cloudcommunications communication-call create-participant](#communications.callsCreateParticipants)|CreateParticipants|[Parameters](#Parameterscommunications.callsCreateParticipants)|Not Found|
|[az cloudcommunications communication-call keep-alive](#communications.callskeepAlive)|keepAlive|[Parameters](#Parameterscommunications.callskeepAlive)|Not Found|
|[az cloudcommunications communication-call list-audio-routing-group](#communications.callsListAudioRoutingGroups)|ListAudioRoutingGroups|[Parameters](#Parameterscommunications.callsListAudioRoutingGroups)|Not Found|
|[az cloudcommunications communication-call list-operation](#communications.callsListOperations)|ListOperations|[Parameters](#Parameterscommunications.callsListOperations)|Not Found|
|[az cloudcommunications communication-call list-participant](#communications.callsListParticipants)|ListParticipants|[Parameters](#Parameterscommunications.callsListParticipants)|Not Found|
|[az cloudcommunications communication-call log-teleconference-device-quality](#communications.callslogTeleconferenceDeviceQuality)|logTeleconferenceDeviceQuality|[Parameters](#Parameterscommunications.callslogTeleconferenceDeviceQuality)|Not Found|
|[az cloudcommunications communication-call mute](#communications.callsmute)|mute|[Parameters](#Parameterscommunications.callsmute)|Not Found|
|[az cloudcommunications communication-call play-prompt](#communications.callsplayPrompt)|playPrompt|[Parameters](#Parameterscommunications.callsplayPrompt)|Not Found|
|[az cloudcommunications communication-call record](#communications.callsrecord)|record|[Parameters](#Parameterscommunications.callsrecord)|Not Found|
|[az cloudcommunications communication-call record-response](#communications.callsrecordResponse)|recordResponse|[Parameters](#Parameterscommunications.callsrecordResponse)|Not Found|
|[az cloudcommunications communication-call redirect](#communications.callsredirect)|redirect|[Parameters](#Parameterscommunications.callsredirect)|Not Found|
|[az cloudcommunications communication-call reject](#communications.callsreject)|reject|[Parameters](#Parameterscommunications.callsreject)|Not Found|
|[az cloudcommunications communication-call show-audio-routing-group](#communications.callsGetAudioRoutingGroups)|GetAudioRoutingGroups|[Parameters](#Parameterscommunications.callsGetAudioRoutingGroups)|Not Found|
|[az cloudcommunications communication-call show-operation](#communications.callsGetOperations)|GetOperations|[Parameters](#Parameterscommunications.callsGetOperations)|Not Found|
|[az cloudcommunications communication-call show-participant](#communications.callsGetParticipants)|GetParticipants|[Parameters](#Parameterscommunications.callsGetParticipants)|Not Found|
|[az cloudcommunications communication-call subscribe-to-tone](#communications.callssubscribeToTone)|subscribeToTone|[Parameters](#Parameterscommunications.callssubscribeToTone)|Not Found|
|[az cloudcommunications communication-call transfer](#communications.callstransfer)|transfer|[Parameters](#Parameterscommunications.callstransfer)|Not Found|
|[az cloudcommunications communication-call unmute](#communications.callsunmute)|unmute|[Parameters](#Parameterscommunications.callsunmute)|Not Found|
|[az cloudcommunications communication-call update-audio-routing-group](#communications.callsUpdateAudioRoutingGroups)|UpdateAudioRoutingGroups|[Parameters](#Parameterscommunications.callsUpdateAudioRoutingGroups)|Not Found|
|[az cloudcommunications communication-call update-operation](#communications.callsUpdateOperations)|UpdateOperations|[Parameters](#Parameterscommunications.callsUpdateOperations)|Not Found|
|[az cloudcommunications communication-call update-participant](#communications.callsUpdateParticipants)|UpdateParticipants|[Parameters](#Parameterscommunications.callsUpdateParticipants)|Not Found|
|[az cloudcommunications communication-call update-recording-status](#communications.callsupdateRecordingStatus)|updateRecordingStatus|[Parameters](#Parameterscommunications.callsupdateRecordingStatus)|Not Found|

### <a name="CommandsIncommunications.calls.participants">Commands in `az cloudcommunications communication-call-participant` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cloudcommunications communication-call-participant invite](#communications.calls.participantsinvite)|invite|[Parameters](#Parameterscommunications.calls.participantsinvite)|Not Found|
|[az cloudcommunications communication-call-participant mute](#communications.calls.participantsmute)|mute|[Parameters](#Parameterscommunications.calls.participantsmute)|Not Found|
|[az cloudcommunications communication-call-participant mute-all](#communications.calls.participantsmuteAll)|muteAll|[Parameters](#Parameterscommunications.calls.participantsmuteAll)|Not Found|

### <a name="CommandsIncommunications.callRecords">Commands in `az cloudcommunications communication-call-record` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cloudcommunications communication-call-record delete](#communications.callRecordsDeleteSessions)|DeleteSessions|[Parameters](#Parameterscommunications.callRecordsDeleteSessions)|Not Found|
|[az cloudcommunications communication-call-record create-session](#communications.callRecordsCreateSessions)|CreateSessions|[Parameters](#Parameterscommunications.callRecordsCreateSessions)|Not Found|
|[az cloudcommunications communication-call-record list-session](#communications.callRecordsListSessions)|ListSessions|[Parameters](#Parameterscommunications.callRecordsListSessions)|Not Found|
|[az cloudcommunications communication-call-record show-session](#communications.callRecordsGetSessions)|GetSessions|[Parameters](#Parameterscommunications.callRecordsGetSessions)|Not Found|
|[az cloudcommunications communication-call-record update-session](#communications.callRecordsUpdateSessions)|UpdateSessions|[Parameters](#Parameterscommunications.callRecordsUpdateSessions)|Not Found|

### <a name="CommandsIncommunications.callRecords.sessions">Commands in `az cloudcommunications communication-call-record-session` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cloudcommunications communication-call-record-session delete](#communications.callRecords.sessionsDeleteSegments)|DeleteSegments|[Parameters](#Parameterscommunications.callRecords.sessionsDeleteSegments)|Not Found|
|[az cloudcommunications communication-call-record-session create-segment](#communications.callRecords.sessionsCreateSegments)|CreateSegments|[Parameters](#Parameterscommunications.callRecords.sessionsCreateSegments)|Not Found|
|[az cloudcommunications communication-call-record-session list-segment](#communications.callRecords.sessionsListSegments)|ListSegments|[Parameters](#Parameterscommunications.callRecords.sessionsListSegments)|Not Found|
|[az cloudcommunications communication-call-record-session show-segment](#communications.callRecords.sessionsGetSegments)|GetSegments|[Parameters](#Parameterscommunications.callRecords.sessionsGetSegments)|Not Found|
|[az cloudcommunications communication-call-record-session update-segment](#communications.callRecords.sessionsUpdateSegments)|UpdateSegments|[Parameters](#Parameterscommunications.callRecords.sessionsUpdateSegments)|Not Found|

### <a name="CommandsIncommunications.cloudCommunications">Commands in `az cloudcommunications communication-cloud-communication` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cloudcommunications communication-cloud-communication show-cloud-communication](#communications.cloudCommunicationsGetCloudCommunications)|GetCloudCommunications|[Parameters](#Parameterscommunications.cloudCommunicationsGetCloudCommunications)|Not Found|
|[az cloudcommunications communication-cloud-communication update-cloud-communication](#communications.cloudCommunicationsUpdateCloudCommunications)|UpdateCloudCommunications|[Parameters](#Parameterscommunications.cloudCommunicationsUpdateCloudCommunications)|Not Found|

### <a name="CommandsIncommunications.onlineMeetings">Commands in `az cloudcommunications communication-online-meeting` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cloudcommunications communication-online-meeting create-or-get](#communications.onlineMeetingscreateOrGet)|createOrGet|[Parameters](#Parameterscommunications.onlineMeetingscreateOrGet)|Not Found|

### <a name="CommandsInusers">Commands in `az cloudcommunications user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cloudcommunications user delete](#usersDeleteOnlineMeetings)|DeleteOnlineMeetings|[Parameters](#ParametersusersDeleteOnlineMeetings)|Not Found|
|[az cloudcommunications user delete](#usersDeletePresence)|DeletePresence|[Parameters](#ParametersusersDeletePresence)|Not Found|
|[az cloudcommunications user create-online-meeting](#usersCreateOnlineMeetings)|CreateOnlineMeetings|[Parameters](#ParametersusersCreateOnlineMeetings)|Not Found|
|[az cloudcommunications user list-online-meeting](#usersListOnlineMeetings)|ListOnlineMeetings|[Parameters](#ParametersusersListOnlineMeetings)|Not Found|
|[az cloudcommunications user show-online-meeting](#usersGetOnlineMeetings)|GetOnlineMeetings|[Parameters](#ParametersusersGetOnlineMeetings)|Not Found|
|[az cloudcommunications user show-presence](#usersGetPresence)|GetPresence|[Parameters](#ParametersusersGetPresence)|Not Found|
|[az cloudcommunications user update-online-meeting](#usersUpdateOnlineMeetings)|UpdateOnlineMeetings|[Parameters](#ParametersusersUpdateOnlineMeetings)|Not Found|
|[az cloudcommunications user update-presence](#usersUpdatePresence)|UpdatePresence|[Parameters](#ParametersusersUpdatePresence)|Not Found|


## COMMAND DETAILS

### group `az cloudcommunications communication`
#### <a name="communicationsDeleteCallRecords">Command `az cloudcommunications communication delete`</a>

##### <a name="ParameterscommunicationsDeleteCallRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="communicationsDeleteCalls">Command `az cloudcommunications communication delete`</a>

##### <a name="ParameterscommunicationsDeleteCalls">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|

#### <a name="communicationsDeleteOnlineMeetings">Command `az cloudcommunications communication delete`</a>

##### <a name="ParameterscommunicationsDeleteOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|

#### <a name="communicationsDeletePresences">Command `az cloudcommunications communication delete`</a>

##### <a name="ParameterscommunicationsDeletePresences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--presence-id**|string|key: id of presence|presence_id|presence-id|

#### <a name="communicationsCreateCalls">Command `az cloudcommunications communication create-call`</a>

##### <a name="ParameterscommunicationsCreateCalls">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--active-modalities**|array||active_modalities|activeModalities|
|**--callback-uri**|string|The callback URL on which callbacks will be delivered. Must be https.|callback_uri|callbackUri|
|**--call-chain-id**|string|A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This needs to be copied over from Microsoft.Graph.Call.CallChainId.|call_chain_id|callChainId|
|**--call-options**|dictionary|callOptions|call_options|callOptions|
|**--call-routes**|array|The routing information on how the call was retargeted. Read-only.|call_routes|callRoutes|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--direction**|choice||direction|direction|
|**--meeting-capability**|object|meetingCapability|meeting_capability|meetingCapability|
|**--my-participant-id**|string||my_participant_id|myParticipantId|
|**--requested-modalities**|array||requested_modalities|requestedModalities|
|**--result-info**|object|ResultInfo|result_info|resultInfo|
|**--ringing-timeout-in-seconds**|integer||ringing_timeout_in_seconds|ringingTimeoutInSeconds|
|**--routing-policies**|array||routing_policies|routingPolicies|
|**--state**|choice||state|state|
|**--subject**|string||subject|subject|
|**--targets**|array||targets|targets|
|**--tenant-id**|string||tenant_id|tenantId|
|**--termination-reason**|string||termination_reason|terminationReason|
|**--tone-info**|object|toneInfo|tone_info|toneInfo|
|**--transcription**|object|callTranscriptionInfo|transcription|transcription|
|**--audio-routing-groups**|array||audio_routing_groups|audioRoutingGroups|
|**--operations**|array|Read-only. Nullable.|operations|operations|
|**--participants**|array|Read-only. Nullable.|participants|participants|
|**--country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|country_code|countryCode|
|**--endpoint-type**|choice||endpoint_type|endpointType|
|**--identity**|object|identitySet|identity|identity|
|**--language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|
|**--allow-conversation-without-host**|boolean||allow_conversation_without_host|allowConversationWithoutHost|
|**--audio**|choice||audio|audio|
|**--remove-from-default-audio-group**|boolean||remove_from_default_audio_group|removeFromDefaultAudioGroup|
|**--observed-participant-id**|string|The ID of the participant that is under observation. Read-only.|observed_participant_id|observedParticipantId|
|**--on-behalf-of**|object|identitySet|on_behalf_of|onBehalfOf|
|**--source-participant-id**|string|The ID of the participant that triggered the incoming call. Read-only.|source_participant_id|sourceParticipantId|
|**--transferor**|object|identitySet|transferor|transferor|
|**--microsoft-graph-participant-info-country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|microsoft_graph_participant_info_country_code|countryCode|
|**--microsoft-graph-endpoint-type**|choice||microsoft_graph_endpoint_type|endpointType|
|**--microsoft-graph-identity-set-identity**|object|identitySet|microsoft_graph_identity_set_identity|identity|
|**--microsoft-graph-participant-info-language-id**|string|The language culture string. Read-only.|microsoft_graph_participant_info_language_id|languageId|
|**--microsoft-graph-participant-info-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|microsoft_graph_participant_info_region|region|

#### <a name="communicationsCreateCallRecords">Command `az cloudcommunications communication create-call-record`</a>

##### <a name="ParameterscommunicationsCreateCallRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--end-date-time**|date-time|UTC time when the last user left the call. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--join-web-url**|string|Meeting URL associated to the call. May not be available for a peerToPeer call record type.|join_web_url|joinWebUrl|
|**--last-modified-date-time**|date-time|UTC time when the call record was created. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--modalities**|array|List of all the modalities used in the call. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.|modalities|modalities|
|**--participants**|array|List of distinct identities involved in the call.|participants|participants|
|**--start-date-time**|date-time|UTC time when the first user joined the call. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--type**|choice||type|type|
|**--version**|integer|Monotonically increasing version of the call record. Higher version call records with the same id includes additional data compared to the lower version.|version|version|
|**--sessions**|array|List of sessions involved in the call. Peer-to-peer calls typically only have one session, whereas group calls typically have at least one session per participant. Read-only. Nullable.|sessions|sessions|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="communicationsCreateOnlineMeetings">Command `az cloudcommunications communication create-online-meeting`</a>

##### <a name="ParameterscommunicationsCreateOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--access-level**|choice||access_level|accessLevel|
|**--allowed-presenters**|choice||allowed_presenters|allowedPresenters|
|**--audio-conferencing**|object|audioConferencing|audio_conferencing|audioConferencing|
|**--canceled-date-time**|date-time||canceled_date_time|canceledDateTime|
|**--capabilities**|array||capabilities|capabilities|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--creation-date-time**|date-time|The meeting creation time in UTC. Read-only.|creation_date_time|creationDateTime|
|**--end-date-time**|date-time|The meeting end time in UTC.|end_date_time|endDateTime|
|**--entry-exit-announcement**|boolean||entry_exit_announcement|entryExitAnnouncement|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--external-id**|string||external_id|externalId|
|**--is-broadcast**|boolean||is_broadcast|isBroadcast|
|**--is-cancelled**|boolean||is_cancelled|isCancelled|
|**--is-entry-exit-announced**|boolean||is_entry_exit_announced|isEntryExitAnnounced|
|**--join-information**|object|itemBody|join_information|joinInformation|
|**--join-url**|string||join_url|joinUrl|
|**--lobby-bypass-settings**|object|lobbyBypassSettings|lobby_bypass_settings|lobbyBypassSettings|
|**--start-date-time**|date-time|The meeting start time in UTC.|start_date_time|startDateTime|
|**--subject**|string|The subject of the online meeting.|subject|subject|
|**--video-teleconference-id**|string|The video teleconferencing ID. Read-only.|video_teleconference_id|videoTeleconferenceId|
|**--attendees**|array||attendees|attendees|
|**--contributors**|array||contributors|contributors|
|**--organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--producers**|array||producers|producers|

#### <a name="communicationsCreatePresences">Command `az cloudcommunications communication create-presence`</a>

##### <a name="ParameterscommunicationsCreatePresences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity**|string||activity|activity|
|**--availability**|string||availability|availability|

#### <a name="communicationsgetPresencesByUserId">Command `az cloudcommunications communication get-presence-by-user-id`</a>

##### <a name="ParameterscommunicationsgetPresencesByUserId">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|

#### <a name="communicationsListCalls">Command `az cloudcommunications communication list-call`</a>

##### <a name="ParameterscommunicationsListCalls">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communicationsListCallRecords">Command `az cloudcommunications communication list-call-record`</a>

##### <a name="ParameterscommunicationsListCallRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communicationsListOnlineMeetings">Command `az cloudcommunications communication list-online-meeting`</a>

##### <a name="ParameterscommunicationsListOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communicationsListPresences">Command `az cloudcommunications communication list-presence`</a>

##### <a name="ParameterscommunicationsListPresences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communicationsGetCalls">Command `az cloudcommunications communication show-call`</a>

##### <a name="ParameterscommunicationsGetCalls">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communicationsGetCallRecords">Command `az cloudcommunications communication show-call-record`</a>

##### <a name="ParameterscommunicationsGetCallRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communicationsGetOnlineMeetings">Command `az cloudcommunications communication show-online-meeting`</a>

##### <a name="ParameterscommunicationsGetOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communicationsGetPresences">Command `az cloudcommunications communication show-presence`</a>

##### <a name="ParameterscommunicationsGetPresences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--presence-id**|string|key: id of presence|presence_id|presence-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communicationsUpdateCalls">Command `az cloudcommunications communication update-call`</a>

##### <a name="ParameterscommunicationsUpdateCalls">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--active-modalities**|array||active_modalities|activeModalities|
|**--callback-uri**|string|The callback URL on which callbacks will be delivered. Must be https.|callback_uri|callbackUri|
|**--call-chain-id**|string|A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This needs to be copied over from Microsoft.Graph.Call.CallChainId.|call_chain_id|callChainId|
|**--call-options**|dictionary|callOptions|call_options|callOptions|
|**--call-routes**|array|The routing information on how the call was retargeted. Read-only.|call_routes|callRoutes|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--direction**|choice||direction|direction|
|**--meeting-capability**|object|meetingCapability|meeting_capability|meetingCapability|
|**--my-participant-id**|string||my_participant_id|myParticipantId|
|**--requested-modalities**|array||requested_modalities|requestedModalities|
|**--result-info**|object|ResultInfo|result_info|resultInfo|
|**--ringing-timeout-in-seconds**|integer||ringing_timeout_in_seconds|ringingTimeoutInSeconds|
|**--routing-policies**|array||routing_policies|routingPolicies|
|**--state**|choice||state|state|
|**--subject**|string||subject|subject|
|**--targets**|array||targets|targets|
|**--tenant-id**|string||tenant_id|tenantId|
|**--termination-reason**|string||termination_reason|terminationReason|
|**--tone-info**|object|toneInfo|tone_info|toneInfo|
|**--transcription**|object|callTranscriptionInfo|transcription|transcription|
|**--audio-routing-groups**|array||audio_routing_groups|audioRoutingGroups|
|**--operations**|array|Read-only. Nullable.|operations|operations|
|**--participants**|array|Read-only. Nullable.|participants|participants|
|**--country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|country_code|countryCode|
|**--endpoint-type**|choice||endpoint_type|endpointType|
|**--identity**|object|identitySet|identity|identity|
|**--language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|
|**--allow-conversation-without-host**|boolean||allow_conversation_without_host|allowConversationWithoutHost|
|**--audio**|choice||audio|audio|
|**--remove-from-default-audio-group**|boolean||remove_from_default_audio_group|removeFromDefaultAudioGroup|
|**--observed-participant-id**|string|The ID of the participant that is under observation. Read-only.|observed_participant_id|observedParticipantId|
|**--on-behalf-of**|object|identitySet|on_behalf_of|onBehalfOf|
|**--source-participant-id**|string|The ID of the participant that triggered the incoming call. Read-only.|source_participant_id|sourceParticipantId|
|**--transferor**|object|identitySet|transferor|transferor|
|**--microsoft-graph-participant-info-country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|microsoft_graph_participant_info_country_code|countryCode|
|**--microsoft-graph-endpoint-type**|choice||microsoft_graph_endpoint_type|endpointType|
|**--microsoft-graph-identity-set-identity**|object|identitySet|microsoft_graph_identity_set_identity|identity|
|**--microsoft-graph-participant-info-language-id**|string|The language culture string. Read-only.|microsoft_graph_participant_info_language_id|languageId|
|**--microsoft-graph-participant-info-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|microsoft_graph_participant_info_region|region|

#### <a name="communicationsUpdateCallRecords">Command `az cloudcommunications communication update-call-record`</a>

##### <a name="ParameterscommunicationsUpdateCallRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--id**|string|Read-only.|id|id|
|**--end-date-time**|date-time|UTC time when the last user left the call. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--join-web-url**|string|Meeting URL associated to the call. May not be available for a peerToPeer call record type.|join_web_url|joinWebUrl|
|**--last-modified-date-time**|date-time|UTC time when the call record was created. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--modalities**|array|List of all the modalities used in the call. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.|modalities|modalities|
|**--participants**|array|List of distinct identities involved in the call.|participants|participants|
|**--start-date-time**|date-time|UTC time when the first user joined the call. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--type**|choice||type|type|
|**--version**|integer|Monotonically increasing version of the call record. Higher version call records with the same id includes additional data compared to the lower version.|version|version|
|**--sessions**|array|List of sessions involved in the call. Peer-to-peer calls typically only have one session, whereas group calls typically have at least one session per participant. Read-only. Nullable.|sessions|sessions|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="communicationsUpdateOnlineMeetings">Command `az cloudcommunications communication update-online-meeting`</a>

##### <a name="ParameterscommunicationsUpdateOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--id**|string|Read-only.|id|id|
|**--access-level**|choice||access_level|accessLevel|
|**--allowed-presenters**|choice||allowed_presenters|allowedPresenters|
|**--audio-conferencing**|object|audioConferencing|audio_conferencing|audioConferencing|
|**--canceled-date-time**|date-time||canceled_date_time|canceledDateTime|
|**--capabilities**|array||capabilities|capabilities|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--creation-date-time**|date-time|The meeting creation time in UTC. Read-only.|creation_date_time|creationDateTime|
|**--end-date-time**|date-time|The meeting end time in UTC.|end_date_time|endDateTime|
|**--entry-exit-announcement**|boolean||entry_exit_announcement|entryExitAnnouncement|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--external-id**|string||external_id|externalId|
|**--is-broadcast**|boolean||is_broadcast|isBroadcast|
|**--is-cancelled**|boolean||is_cancelled|isCancelled|
|**--is-entry-exit-announced**|boolean||is_entry_exit_announced|isEntryExitAnnounced|
|**--join-information**|object|itemBody|join_information|joinInformation|
|**--join-url**|string||join_url|joinUrl|
|**--lobby-bypass-settings**|object|lobbyBypassSettings|lobby_bypass_settings|lobbyBypassSettings|
|**--start-date-time**|date-time|The meeting start time in UTC.|start_date_time|startDateTime|
|**--subject**|string|The subject of the online meeting.|subject|subject|
|**--video-teleconference-id**|string|The video teleconferencing ID. Read-only.|video_teleconference_id|videoTeleconferenceId|
|**--attendees**|array||attendees|attendees|
|**--contributors**|array||contributors|contributors|
|**--organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--producers**|array||producers|producers|

#### <a name="communicationsUpdatePresences">Command `az cloudcommunications communication update-presence`</a>

##### <a name="ParameterscommunicationsUpdatePresences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--presence-id**|string|key: id of presence|presence_id|presence-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|string||activity|activity|
|**--availability**|string||availability|availability|

### group `az cloudcommunications communication-call`
#### <a name="communications.callsDeleteAudioRoutingGroups">Command `az cloudcommunications communication-call delete`</a>

##### <a name="Parameterscommunications.callsDeleteAudioRoutingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--audio-routing-group-id**|string|key: id of audioRoutingGroup|audio_routing_group_id|audioRoutingGroup-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="communications.callsDeleteOperations">Command `az cloudcommunications communication-call delete`</a>

##### <a name="Parameterscommunications.callsDeleteOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--comms-operation-id**|string|key: id of commsOperation|comms_operation_id|commsOperation-id|

#### <a name="communications.callsDeleteParticipants">Command `az cloudcommunications communication-call delete`</a>

##### <a name="Parameterscommunications.callsDeleteParticipants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--participant-id**|string|key: id of participant|participant_id|participant-id|

#### <a name="communications.callsanswer">Command `az cloudcommunications communication-call answer`</a>

##### <a name="Parameterscommunications.callsanswer">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--callback-uri**|string||callback_uri|callbackUri|
|**--accepted-modalities**|array||accepted_modalities|acceptedModalities|
|**--remove-from-default-audio-group**|boolean||remove_from_default_audio_group|removeFromDefaultAudioGroup|

#### <a name="communications.callscancelMediaProcessing">Command `az cloudcommunications communication-call cancel-media-processing`</a>

##### <a name="Parameterscommunications.callscancelMediaProcessing">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

#### <a name="communications.callschangeScreenSharingRole">Command `az cloudcommunications communication-call change-screen-sharing-role`</a>

##### <a name="Parameterscommunications.callschangeScreenSharingRole">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--role**|choice||role|role|

#### <a name="communications.callsCreateAudioRoutingGroups">Command `az cloudcommunications communication-call create-audio-routing-group`</a>

##### <a name="Parameterscommunications.callsCreateAudioRoutingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--receivers**|array||receivers|receivers|
|**--routing-mode**|choice||routing_mode|routingMode|
|**--sources**|array||sources|sources|

#### <a name="communications.callsCreateOperations">Command `az cloudcommunications communication-call create-operation`</a>

##### <a name="Parameterscommunications.callsCreateOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--client-context**|string|Unique Client Context string. Max limit is 256 chars.|client_context|clientContext|
|**--result-info**|object|ResultInfo|result_info|resultInfo|
|**--status**|choice||status|status|

#### <a name="communications.callsCreateParticipants">Command `az cloudcommunications communication-call create-participant`</a>

##### <a name="Parameterscommunications.callsCreateParticipants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--is-in-lobby**|boolean|true if the participant is in lobby.|is_in_lobby|isInLobby|
|**--is-muted**|boolean|true if the participant is muted (client or server muted).|is_muted|isMuted|
|**--media-streams**|array|The list of media streams.|media_streams|mediaStreams|
|**--metadata**|string||metadata|metadata|
|**--initiated-by**|object|participantInfo|initiated_by|initiatedBy|
|**--initiator**|object|identitySet|initiator|initiator|
|**--recording-status**|choice||recording_status|recordingStatus|
|**--country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|country_code|countryCode|
|**--endpoint-type**|choice||endpoint_type|endpointType|
|**--identity**|object|identitySet|identity|identity|
|**--language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|

#### <a name="communications.callskeepAlive">Command `az cloudcommunications communication-call keep-alive`</a>

##### <a name="Parameterscommunications.callskeepAlive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|

#### <a name="communications.callsListAudioRoutingGroups">Command `az cloudcommunications communication-call list-audio-routing-group`</a>

##### <a name="Parameterscommunications.callsListAudioRoutingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.callsListOperations">Command `az cloudcommunications communication-call list-operation`</a>

##### <a name="Parameterscommunications.callsListOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.callsListParticipants">Command `az cloudcommunications communication-call list-participant`</a>

##### <a name="Parameterscommunications.callsListParticipants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.callslogTeleconferenceDeviceQuality">Command `az cloudcommunications communication-call log-teleconference-device-quality`</a>

##### <a name="Parameterscommunications.callslogTeleconferenceDeviceQuality">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-chain-id**|uuid|A unique identifier for all  the participant calls in a conference or a unique identifier for two participant calls in P2P call. This needs to be copied over from Microsoft.Graph.Call.CallChainId.|call_chain_id|callChainId|
|**--cloud-service-deployment-environment**|string|A geo-region where the service is deployed, such as ProdNoam.|cloud_service_deployment_environment|cloudServiceDeploymentEnvironment|
|**--cloud-service-deployment-id**|string|A unique deployment identifier assigned by Azure.|cloud_service_deployment_id|cloudServiceDeploymentId|
|**--cloud-service-instance-name**|string|The Azure deployed cloud service instance name, such as FrontEnd_IN_3.|cloud_service_instance_name|cloudServiceInstanceName|
|**--cloud-service-name**|string|The Azure deployed cloud service name, such as contoso.cloudapp.net.|cloud_service_name|cloudServiceName|
|**--device-description**|string|Any additional description, such as VTC Bldg 30/21.|device_description|deviceDescription|
|**--device-name**|string|The user media agent name, such as Cisco SX80.|device_name|deviceName|
|**--media-leg-id**|uuid|A unique identifier for a specific media leg of a participant in a conference.  One participant can have multiple media leg identifiers if retargeting happens. CVI partner assigns this value.|media_leg_id|mediaLegId|
|**--media-quality-list**|array|The list of media qualities in a media session (call), such as audio quality, video quality, and/or screen sharing quality.|media_quality_list|mediaQualityList|
|**--participant-id**|uuid|A unique identifier for a specific participant in a conference. The CVI partner needs to copy over Call.MyParticipantId to this property.|participant_id|participantId|

#### <a name="communications.callsmute">Command `az cloudcommunications communication-call mute`</a>

##### <a name="Parameterscommunications.callsmute">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

#### <a name="communications.callsplayPrompt">Command `az cloudcommunications communication-call play-prompt`</a>

##### <a name="Parameterscommunications.callsplayPrompt">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--prompts**|array||prompts|prompts|
|**--loop**|boolean||loop|loop|
|**--client-context**|string||client_context|clientContext|

#### <a name="communications.callsrecord">Command `az cloudcommunications communication-call record`</a>

##### <a name="Parameterscommunications.callsrecord">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--prompts**|array||prompts|prompts|
|**--barge-in-allowed**|boolean||barge_in_allowed|bargeInAllowed|
|**--initial-silence-timeout-in-seconds**|integer||initial_silence_timeout_in_seconds|initialSilenceTimeoutInSeconds|
|**--max-silence-timeout-in-seconds**|integer||max_silence_timeout_in_seconds|maxSilenceTimeoutInSeconds|
|**--max-record-duration-in-seconds**|integer||max_record_duration_in_seconds|maxRecordDurationInSeconds|
|**--play-beep**|boolean||play_beep|playBeep|
|**--stream-while-recording**|boolean||stream_while_recording|streamWhileRecording|
|**--stop-tones**|array||stop_tones|stopTones|
|**--client-context**|string||client_context|clientContext|

#### <a name="communications.callsrecordResponse">Command `az cloudcommunications communication-call record-response`</a>

##### <a name="Parameterscommunications.callsrecordResponse">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--prompts**|array||prompts|prompts|
|**--barge-in-allowed**|boolean||barge_in_allowed|bargeInAllowed|
|**--initial-silence-timeout-in-seconds**|integer||initial_silence_timeout_in_seconds|initialSilenceTimeoutInSeconds|
|**--max-silence-timeout-in-seconds**|integer||max_silence_timeout_in_seconds|maxSilenceTimeoutInSeconds|
|**--max-record-duration-in-seconds**|integer||max_record_duration_in_seconds|maxRecordDurationInSeconds|
|**--play-beep**|boolean||play_beep|playBeep|
|**--stream-while-recording**|boolean||stream_while_recording|streamWhileRecording|
|**--stop-tones**|array||stop_tones|stopTones|
|**--client-context**|string||client_context|clientContext|

#### <a name="communications.callsredirect">Command `az cloudcommunications communication-call redirect`</a>

##### <a name="Parameterscommunications.callsredirect">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--targets**|array||targets|targets|
|**--target-disposition**|choice||target_disposition|targetDisposition|
|**--timeout**|integer||timeout|timeout|
|**--mask-callee**|boolean||mask_callee|maskCallee|
|**--mask-caller**|boolean||mask_caller|maskCaller|
|**--callback-uri**|string||callback_uri|callbackUri|

#### <a name="communications.callsreject">Command `az cloudcommunications communication-call reject`</a>

##### <a name="Parameterscommunications.callsreject">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--reason**|choice||reason|reason|
|**--callback-uri**|string||callback_uri|callbackUri|

#### <a name="communications.callsGetAudioRoutingGroups">Command `az cloudcommunications communication-call show-audio-routing-group`</a>

##### <a name="Parameterscommunications.callsGetAudioRoutingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--audio-routing-group-id**|string|key: id of audioRoutingGroup|audio_routing_group_id|audioRoutingGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.callsGetOperations">Command `az cloudcommunications communication-call show-operation`</a>

##### <a name="Parameterscommunications.callsGetOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--comms-operation-id**|string|key: id of commsOperation|comms_operation_id|commsOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.callsGetParticipants">Command `az cloudcommunications communication-call show-participant`</a>

##### <a name="Parameterscommunications.callsGetParticipants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--participant-id**|string|key: id of participant|participant_id|participant-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.callssubscribeToTone">Command `az cloudcommunications communication-call subscribe-to-tone`</a>

##### <a name="Parameterscommunications.callssubscribeToTone">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

#### <a name="communications.callstransfer">Command `az cloudcommunications communication-call transfer`</a>

##### <a name="Parameterscommunications.callstransfer">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--endpoint-type**|choice||endpoint_type|endpointType|
|**--replaces-call-id**|string|Optional. The call which the target identity is currently a part of. This call will be dropped once the participant is added.|replaces_call_id|replacesCallId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="communications.callsunmute">Command `az cloudcommunications communication-call unmute`</a>

##### <a name="Parameterscommunications.callsunmute">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

#### <a name="communications.callsUpdateAudioRoutingGroups">Command `az cloudcommunications communication-call update-audio-routing-group`</a>

##### <a name="Parameterscommunications.callsUpdateAudioRoutingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--audio-routing-group-id**|string|key: id of audioRoutingGroup|audio_routing_group_id|audioRoutingGroup-id|
|**--id**|string|Read-only.|id|id|
|**--receivers**|array||receivers|receivers|
|**--routing-mode**|choice||routing_mode|routingMode|
|**--sources**|array||sources|sources|

#### <a name="communications.callsUpdateOperations">Command `az cloudcommunications communication-call update-operation`</a>

##### <a name="Parameterscommunications.callsUpdateOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--comms-operation-id**|string|key: id of commsOperation|comms_operation_id|commsOperation-id|
|**--id**|string|Read-only.|id|id|
|**--client-context**|string|Unique Client Context string. Max limit is 256 chars.|client_context|clientContext|
|**--result-info**|object|ResultInfo|result_info|resultInfo|
|**--status**|choice||status|status|

#### <a name="communications.callsUpdateParticipants">Command `az cloudcommunications communication-call update-participant`</a>

##### <a name="Parameterscommunications.callsUpdateParticipants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--participant-id**|string|key: id of participant|participant_id|participant-id|
|**--id**|string|Read-only.|id|id|
|**--is-in-lobby**|boolean|true if the participant is in lobby.|is_in_lobby|isInLobby|
|**--is-muted**|boolean|true if the participant is muted (client or server muted).|is_muted|isMuted|
|**--media-streams**|array|The list of media streams.|media_streams|mediaStreams|
|**--metadata**|string||metadata|metadata|
|**--initiated-by**|object|participantInfo|initiated_by|initiatedBy|
|**--initiator**|object|identitySet|initiator|initiator|
|**--recording-status**|choice||recording_status|recordingStatus|
|**--country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|country_code|countryCode|
|**--endpoint-type**|choice||endpoint_type|endpointType|
|**--identity**|object|identitySet|identity|identity|
|**--language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|

#### <a name="communications.callsupdateRecordingStatus">Command `az cloudcommunications communication-call update-recording-status`</a>

##### <a name="Parameterscommunications.callsupdateRecordingStatus">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--status**|choice||status|status|
|**--client-context**|string||client_context|clientContext|

### group `az cloudcommunications communication-call-participant`
#### <a name="communications.calls.participantsinvite">Command `az cloudcommunications communication-call-participant invite`</a>

##### <a name="Parameterscommunications.calls.participantsinvite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--participants**|array||participants|participants|
|**--client-context**|string||client_context|clientContext|

#### <a name="communications.calls.participantsmute">Command `az cloudcommunications communication-call-participant mute`</a>

##### <a name="Parameterscommunications.calls.participantsmute">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--participant-id**|string|key: id of participant|participant_id|participant-id|
|**--client-context**|string||client_context|clientContext|

#### <a name="communications.calls.participantsmuteAll">Command `az cloudcommunications communication-call-participant mute-all`</a>

##### <a name="Parameterscommunications.calls.participantsmuteAll">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--participants**|array||participants|participants|
|**--client-context**|string||client_context|clientContext|

### group `az cloudcommunications communication-call-record`
#### <a name="communications.callRecordsDeleteSessions">Command `az cloudcommunications communication-call-record delete`</a>

##### <a name="Parameterscommunications.callRecordsDeleteSessions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="communications.callRecordsCreateSessions">Command `az cloudcommunications communication-call-record create-session`</a>

##### <a name="Parameterscommunications.callRecordsCreateSessions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--id**|string|Read-only.|id|id|
|**--end-date-time**|date-time|UTC time when the last user left the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--failure-info**|object|failureInfo|failure_info|failureInfo|
|**--modalities**|array|List of modalities present in the session. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.|modalities|modalities|
|**--start-date-time**|date-time|UTC fime when the first user joined the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--segments**|array|The list of segments involved in the session. Read-only. Nullable.|segments|segments|
|**--user-agent**|object|userAgent|user_agent|userAgent|
|**--microsoft-graph-call-records-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

#### <a name="communications.callRecordsListSessions">Command `az cloudcommunications communication-call-record list-session`</a>

##### <a name="Parameterscommunications.callRecordsListSessions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.callRecordsGetSessions">Command `az cloudcommunications communication-call-record show-session`</a>

##### <a name="Parameterscommunications.callRecordsGetSessions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.callRecordsUpdateSessions">Command `az cloudcommunications communication-call-record update-session`</a>

##### <a name="Parameterscommunications.callRecordsUpdateSessions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--id**|string|Read-only.|id|id|
|**--end-date-time**|date-time|UTC time when the last user left the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--failure-info**|object|failureInfo|failure_info|failureInfo|
|**--modalities**|array|List of modalities present in the session. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.|modalities|modalities|
|**--start-date-time**|date-time|UTC fime when the first user joined the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--segments**|array|The list of segments involved in the session. Read-only. Nullable.|segments|segments|
|**--user-agent**|object|userAgent|user_agent|userAgent|
|**--microsoft-graph-call-records-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

### group `az cloudcommunications communication-call-record-session`
#### <a name="communications.callRecords.sessionsDeleteSegments">Command `az cloudcommunications communication-call-record-session delete`</a>

##### <a name="Parameterscommunications.callRecords.sessionsDeleteSegments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--segment-id**|string|key: id of segment|segment_id|segment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="communications.callRecords.sessionsCreateSegments">Command `az cloudcommunications communication-call-record-session create-segment`</a>

##### <a name="Parameterscommunications.callRecords.sessionsCreateSegments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--id**|string|Read-only.|id|id|
|**--end-date-time**|date-time|UTC time when the segment ended. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--failure-info**|object|failureInfo|failure_info|failureInfo|
|**--media**|array|Media associated with this segment.|media|media|
|**--start-date-time**|date-time|UTC time when the segment started. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--user-agent**|object|userAgent|user_agent|userAgent|
|**--microsoft-graph-call-records-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

#### <a name="communications.callRecords.sessionsListSegments">Command `az cloudcommunications communication-call-record-session list-segment`</a>

##### <a name="Parameterscommunications.callRecords.sessionsListSegments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.callRecords.sessionsGetSegments">Command `az cloudcommunications communication-call-record-session show-segment`</a>

##### <a name="Parameterscommunications.callRecords.sessionsGetSegments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--segment-id**|string|key: id of segment|segment_id|segment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.callRecords.sessionsUpdateSegments">Command `az cloudcommunications communication-call-record-session update-segment`</a>

##### <a name="Parameterscommunications.callRecords.sessionsUpdateSegments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--segment-id**|string|key: id of segment|segment_id|segment-id|
|**--id**|string|Read-only.|id|id|
|**--end-date-time**|date-time|UTC time when the segment ended. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--failure-info**|object|failureInfo|failure_info|failureInfo|
|**--media**|array|Media associated with this segment.|media|media|
|**--start-date-time**|date-time|UTC time when the segment started. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--user-agent**|object|userAgent|user_agent|userAgent|
|**--microsoft-graph-call-records-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

### group `az cloudcommunications communication-cloud-communication`
#### <a name="communications.cloudCommunicationsGetCloudCommunications">Command `az cloudcommunications communication-cloud-communication show-cloud-communication`</a>

##### <a name="Parameterscommunications.cloudCommunicationsGetCloudCommunications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="communications.cloudCommunicationsUpdateCloudCommunications">Command `az cloudcommunications communication-cloud-communication update-cloud-communication`</a>

##### <a name="Parameterscommunications.cloudCommunicationsUpdateCloudCommunications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--calls**|array||calls|calls|
|**--call-records**|array||call_records|callRecords|
|**--online-meetings**|array||online_meetings|onlineMeetings|
|**--presences**|array||presences|presences|

### group `az cloudcommunications communication-online-meeting`
#### <a name="communications.onlineMeetingscreateOrGet">Command `az cloudcommunications communication-online-meeting create-or-get`</a>

##### <a name="Parameterscommunications.onlineMeetingscreateOrGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--external-id**|string||external_id|externalId|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--subject**|string||subject|subject|
|**--attendees**|array||attendees|attendees|
|**--contributors**|array||contributors|contributors|
|**--organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--producers**|array||producers|producers|

### group `az cloudcommunications user`
#### <a name="usersDeleteOnlineMeetings">Command `az cloudcommunications user delete`</a>

##### <a name="ParametersusersDeleteOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeletePresence">Command `az cloudcommunications user delete`</a>

##### <a name="ParametersusersDeletePresence">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersCreateOnlineMeetings">Command `az cloudcommunications user create-online-meeting`</a>

##### <a name="ParametersusersCreateOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--access-level**|choice||access_level|accessLevel|
|**--allowed-presenters**|choice||allowed_presenters|allowedPresenters|
|**--audio-conferencing**|object|audioConferencing|audio_conferencing|audioConferencing|
|**--canceled-date-time**|date-time||canceled_date_time|canceledDateTime|
|**--capabilities**|array||capabilities|capabilities|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--creation-date-time**|date-time|The meeting creation time in UTC. Read-only.|creation_date_time|creationDateTime|
|**--end-date-time**|date-time|The meeting end time in UTC.|end_date_time|endDateTime|
|**--entry-exit-announcement**|boolean||entry_exit_announcement|entryExitAnnouncement|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--external-id**|string||external_id|externalId|
|**--is-broadcast**|boolean||is_broadcast|isBroadcast|
|**--is-cancelled**|boolean||is_cancelled|isCancelled|
|**--is-entry-exit-announced**|boolean||is_entry_exit_announced|isEntryExitAnnounced|
|**--join-information**|object|itemBody|join_information|joinInformation|
|**--join-url**|string||join_url|joinUrl|
|**--lobby-bypass-settings**|object|lobbyBypassSettings|lobby_bypass_settings|lobbyBypassSettings|
|**--start-date-time**|date-time|The meeting start time in UTC.|start_date_time|startDateTime|
|**--subject**|string|The subject of the online meeting.|subject|subject|
|**--video-teleconference-id**|string|The video teleconferencing ID. Read-only.|video_teleconference_id|videoTeleconferenceId|
|**--attendees**|array||attendees|attendees|
|**--contributors**|array||contributors|contributors|
|**--organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--producers**|array||producers|producers|

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

#### <a name="usersGetPresence">Command `az cloudcommunications user show-presence`</a>

##### <a name="ParametersusersGetPresence">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateOnlineMeetings">Command `az cloudcommunications user update-online-meeting`</a>

##### <a name="ParametersusersUpdateOnlineMeetings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--id**|string|Read-only.|id|id|
|**--access-level**|choice||access_level|accessLevel|
|**--allowed-presenters**|choice||allowed_presenters|allowedPresenters|
|**--audio-conferencing**|object|audioConferencing|audio_conferencing|audioConferencing|
|**--canceled-date-time**|date-time||canceled_date_time|canceledDateTime|
|**--capabilities**|array||capabilities|capabilities|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--creation-date-time**|date-time|The meeting creation time in UTC. Read-only.|creation_date_time|creationDateTime|
|**--end-date-time**|date-time|The meeting end time in UTC.|end_date_time|endDateTime|
|**--entry-exit-announcement**|boolean||entry_exit_announcement|entryExitAnnouncement|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--external-id**|string||external_id|externalId|
|**--is-broadcast**|boolean||is_broadcast|isBroadcast|
|**--is-cancelled**|boolean||is_cancelled|isCancelled|
|**--is-entry-exit-announced**|boolean||is_entry_exit_announced|isEntryExitAnnounced|
|**--join-information**|object|itemBody|join_information|joinInformation|
|**--join-url**|string||join_url|joinUrl|
|**--lobby-bypass-settings**|object|lobbyBypassSettings|lobby_bypass_settings|lobbyBypassSettings|
|**--start-date-time**|date-time|The meeting start time in UTC.|start_date_time|startDateTime|
|**--subject**|string|The subject of the online meeting.|subject|subject|
|**--video-teleconference-id**|string|The video teleconferencing ID. Read-only.|video_teleconference_id|videoTeleconferenceId|
|**--attendees**|array||attendees|attendees|
|**--contributors**|array||contributors|contributors|
|**--organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--producers**|array||producers|producers|

#### <a name="usersUpdatePresence">Command `az cloudcommunications user update-presence`</a>

##### <a name="ParametersusersUpdatePresence">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|string||activity|activity|
|**--availability**|string||availability|availability|
