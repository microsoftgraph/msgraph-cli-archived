# Azure CLI Module Creation Report

### cloudcommunications communication create-call

create-call a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-call|CreateCalls|

#### Parameters
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
|**--source-country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|country_code|countryCode|
|**--source-endpoint-type**|choice||endpoint_type|endpointType|
|**--source-identity**|object|identitySet|identity|identity|
|**--source-language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--source-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|
|**--meeting-info-allow-conversation-without-host**|boolean||allow_conversation_without_host|allowConversationWithoutHost|
|**--media-state-audio**|choice||audio|audio|
|**--media-config-remove-from-default-audio-group**|boolean||remove_from_default_audio_group|removeFromDefaultAudioGroup|
|**--incoming-context-observed-participant-id**|string|The ID of the participant that is under observation. Read-only.|observed_participant_id|observedParticipantId|
|**--incoming-context-on-behalf-of**|object|identitySet|on_behalf_of|onBehalfOf|
|**--incoming-context-source-participant-id**|string|The ID of the participant that triggered the incoming call. Read-only.|source_participant_id|sourceParticipantId|
|**--incoming-context-transferor**|object|identitySet|transferor|transferor|
|**--answered-by-country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|microsoft_graph_participant_info_country_code|countryCode|
|**--answered-by-endpoint-type**|choice||microsoft_graph_endpoint_type|endpointType|
|**--answered-by-identity**|object|identitySet|microsoft_graph_identity_set_identity|identity|
|**--answered-by-language-id**|string|The language culture string. Read-only.|microsoft_graph_participant_info_language_id|languageId|
|**--answered-by-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|microsoft_graph_participant_info_region|region|

### cloudcommunications communication create-call-record

create-call-record a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-call-record|CreateCallRecords|

#### Parameters
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
|**--organizer-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--organizer-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--organizer-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--organizer-device-id**|string|Unique identifier for the identity.|id1|id|
|**--organizer-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--organizer-application-id**|string|Unique identifier for the identity.|id2|id|

### cloudcommunications communication create-online-meeting

create-online-meeting a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-online-meeting|CreateOnlineMeetings|

#### Parameters
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
|**--participants-attendees**|array||attendees|attendees|
|**--participants-contributors**|array||contributors|contributors|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--participants-producers**|array||producers|producers|

### cloudcommunications communication create-presence

create-presence a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-presence|CreatePresences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity**|string||activity|activity|
|**--availability**|string||availability|availability|

### cloudcommunications communication delete

delete a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCallRecords|
|delete|DeleteCalls|
|delete|DeleteOnlineMeetings|
|delete|DeletePresences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--presence-id**|string|key: id of presence|presence_id|presence-id|
|**--if-match**|string|ETag|if_match|If-Match|

### cloudcommunications communication get-call

get-call a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-call|GetCalls|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication get-call-record

get-call-record a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-call-record|GetCallRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication get-online-meeting

get-online-meeting a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-online-meeting|GetOnlineMeetings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication get-presence

get-presence a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-presence|GetPresences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--presence-id**|string|key: id of presence|presence_id|presence-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication get-presence-by-user-id

get-presence-by-user-id a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-presence-by-user-id|getPresencesByUserId|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|

### cloudcommunications communication list-call

list-call a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

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

### cloudcommunications communication list-call-record

list-call-record a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

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

### cloudcommunications communication list-online-meeting

list-online-meeting a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

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

### cloudcommunications communication list-presence

list-presence a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-presence|ListPresences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication update-call

update-call a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-call|UpdateCalls|

#### Parameters
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
|**--source-country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|country_code|countryCode|
|**--source-endpoint-type**|choice||endpoint_type|endpointType|
|**--source-identity**|object|identitySet|identity|identity|
|**--source-language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--source-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|
|**--meeting-info-allow-conversation-without-host**|boolean||allow_conversation_without_host|allowConversationWithoutHost|
|**--media-state-audio**|choice||audio|audio|
|**--media-config-remove-from-default-audio-group**|boolean||remove_from_default_audio_group|removeFromDefaultAudioGroup|
|**--incoming-context-observed-participant-id**|string|The ID of the participant that is under observation. Read-only.|observed_participant_id|observedParticipantId|
|**--incoming-context-on-behalf-of**|object|identitySet|on_behalf_of|onBehalfOf|
|**--incoming-context-source-participant-id**|string|The ID of the participant that triggered the incoming call. Read-only.|source_participant_id|sourceParticipantId|
|**--incoming-context-transferor**|object|identitySet|transferor|transferor|
|**--answered-by-country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|microsoft_graph_participant_info_country_code|countryCode|
|**--answered-by-endpoint-type**|choice||microsoft_graph_endpoint_type|endpointType|
|**--answered-by-identity**|object|identitySet|microsoft_graph_identity_set_identity|identity|
|**--answered-by-language-id**|string|The language culture string. Read-only.|microsoft_graph_participant_info_language_id|languageId|
|**--answered-by-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|microsoft_graph_participant_info_region|region|

### cloudcommunications communication update-call-record

update-call-record a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-call-record|UpdateCallRecords|

#### Parameters
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
|**--organizer-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--organizer-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--organizer-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--organizer-device-id**|string|Unique identifier for the identity.|id1|id|
|**--organizer-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--organizer-application-id**|string|Unique identifier for the identity.|id2|id|

### cloudcommunications communication update-online-meeting

update-online-meeting a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-online-meeting|UpdateOnlineMeetings|

#### Parameters
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
|**--participants-attendees**|array||attendees|attendees|
|**--participants-contributors**|array||contributors|contributors|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--participants-producers**|array||producers|producers|

### cloudcommunications communication update-presence

update-presence a cloudcommunications communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication|communications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-presence|UpdatePresences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--presence-id**|string|key: id of presence|presence_id|presence-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|string||activity|activity|
|**--availability**|string||availability|availability|

### cloudcommunications communication-call answer

answer a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|answer|answer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--callback-uri**|string||callback_uri|callbackUri|
|**--accepted-modalities**|array||accepted_modalities|acceptedModalities|
|**--media-config-remove-from-default-audio-group**|boolean||remove_from_default_audio_group|removeFromDefaultAudioGroup|

### cloudcommunications communication-call cancel-media-processing

cancel-media-processing a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel-media-processing|cancelMediaProcessing|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications communication-call change-screen-sharing-role

change-screen-sharing-role a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|change-screen-sharing-role|changeScreenSharingRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--role**|choice||role|role|

### cloudcommunications communication-call create-audio-routing-group

create-audio-routing-group a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-audio-routing-group|CreateAudioRoutingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--receivers**|array||receivers|receivers|
|**--routing-mode**|choice||routing_mode|routingMode|
|**--sources**|array||sources|sources|

### cloudcommunications communication-call create-operation

create-operation a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-operation|CreateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--client-context**|string|Unique Client Context string. Max limit is 256 chars.|client_context|clientContext|
|**--status**|choice||status|status|
|**--result-info-code**|integer||code|code|
|**--result-info-message**|string||message|message|
|**--result-info-subcode**|integer||subcode|subcode|

### cloudcommunications communication-call create-participant

create-participant a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-participant|CreateParticipants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--id**|string|Read-only.|id|id|
|**--is-in-lobby**|boolean|true if the participant is in lobby.|is_in_lobby|isInLobby|
|**--is-muted**|boolean|true if the participant is muted (client or server muted).|is_muted|isMuted|
|**--media-streams**|array|The list of media streams.|media_streams|mediaStreams|
|**--metadata**|string||metadata|metadata|
|**--recording-info-initiated-by**|object|participantInfo|initiated_by|initiatedBy|
|**--recording-info-initiator**|object|identitySet|initiator|initiator|
|**--recording-info-recording-status**|choice||recording_status|recordingStatus|
|**--info-country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|country_code|countryCode|
|**--info-endpoint-type**|choice||endpoint_type|endpointType|
|**--info-identity**|object|identitySet|identity|identity|
|**--info-language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--info-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|

### cloudcommunications communication-call delete

delete a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAudioRoutingGroups|
|delete|DeleteOperations|
|delete|DeleteParticipants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--audio-routing-group-id**|string|key: id of audioRoutingGroup|audio_routing_group_id|audioRoutingGroup-id|
|**--comms-operation-id**|string|key: id of commsOperation|comms_operation_id|commsOperation-id|
|**--participant-id**|string|key: id of participant|participant_id|participant-id|
|**--if-match**|string|ETag|if_match|If-Match|

### cloudcommunications communication-call get-audio-routing-group

get-audio-routing-group a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-audio-routing-group|GetAudioRoutingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--audio-routing-group-id**|string|key: id of audioRoutingGroup|audio_routing_group_id|audioRoutingGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-call get-operation

get-operation a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-operation|GetOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--comms-operation-id**|string|key: id of commsOperation|comms_operation_id|commsOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-call get-participant

get-participant a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-participant|GetParticipants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--participant-id**|string|key: id of participant|participant_id|participant-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-call keep-alive

keep-alive a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|keep-alive|keepAlive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|

### cloudcommunications communication-call list-audio-routing-group

list-audio-routing-group a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-audio-routing-group|ListAudioRoutingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-call list-operation

list-operation a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-operation|ListOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-call list-participant

list-participant a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-participant|ListParticipants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-call log-teleconference-device-quality

log-teleconference-device-quality a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|log-teleconference-device-quality|logTeleconferenceDeviceQuality|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--quality-call-chain-id**|uuid|A unique identifier for all  the participant calls in a conference or a unique identifier for two participant calls in P2P call. This needs to be copied over from Microsoft.Graph.Call.CallChainId.|call_chain_id|callChainId|
|**--quality-cloud-service-deployment-environment**|string|A geo-region where the service is deployed, such as ProdNoam.|cloud_service_deployment_environment|cloudServiceDeploymentEnvironment|
|**--quality-cloud-service-deployment-id**|string|A unique deployment identifier assigned by Azure.|cloud_service_deployment_id|cloudServiceDeploymentId|
|**--quality-cloud-service-instance-name**|string|The Azure deployed cloud service instance name, such as FrontEnd_IN_3.|cloud_service_instance_name|cloudServiceInstanceName|
|**--quality-cloud-service-name**|string|The Azure deployed cloud service name, such as contoso.cloudapp.net.|cloud_service_name|cloudServiceName|
|**--quality-device-description**|string|Any additional description, such as VTC Bldg 30/21.|device_description|deviceDescription|
|**--quality-device-name**|string|The user media agent name, such as Cisco SX80.|device_name|deviceName|
|**--quality-media-leg-id**|uuid|A unique identifier for a specific media leg of a participant in a conference.  One participant can have multiple media leg identifiers if retargeting happens. CVI partner assigns this value.|media_leg_id|mediaLegId|
|**--quality-media-quality-list**|array|The list of media qualities in a media session (call), such as audio quality, video quality, and/or screen sharing quality.|media_quality_list|mediaQualityList|
|**--quality-participant-id**|uuid|A unique identifier for a specific participant in a conference. The CVI partner needs to copy over Call.MyParticipantId to this property.|participant_id|participantId|

### cloudcommunications communication-call mute

mute a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|mute|mute|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications communication-call play-prompt

play-prompt a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|play-prompt|playPrompt|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--prompts**|array||prompts|prompts|
|**--loop**|boolean||loop|loop|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications communication-call record

record a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|record|record|

#### Parameters
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

### cloudcommunications communication-call record-response

record-response a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|record-response|recordResponse|

#### Parameters
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

### cloudcommunications communication-call redirect

redirect a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|redirect|redirect|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--targets**|array||targets|targets|
|**--target-disposition**|choice||target_disposition|targetDisposition|
|**--timeout**|integer||timeout|timeout|
|**--mask-callee**|boolean||mask_callee|maskCallee|
|**--mask-caller**|boolean||mask_caller|maskCaller|
|**--callback-uri**|string||callback_uri|callbackUri|

### cloudcommunications communication-call reject

reject a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reject|reject|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--reason**|choice||reason|reason|
|**--callback-uri**|string||callback_uri|callbackUri|

### cloudcommunications communication-call subscribe-to-tone

subscribe-to-tone a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|subscribe-to-tone|subscribeToTone|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications communication-call transfer

transfer a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|transfer|transfer|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--transfer-target-endpoint-type**|choice||endpoint_type|endpointType|
|**--transfer-target-replaces-call-id**|string|Optional. The call which the target identity is currently a part of. This call will be dropped once the participant is added.|replaces_call_id|replacesCallId|
|**--transfer-target-identity-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--transfer-target-identity-user-id**|string|Unique identifier for the identity.|id|id|
|**--transfer-target-identity-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--transfer-target-identity-device-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--transfer-target-identity-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--transfer-target-identity-application-id**|string|Unique identifier for the identity.|id1|id|

### cloudcommunications communication-call unmute

unmute a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unmute|unmute|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications communication-call update-audio-routing-group

update-audio-routing-group a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-audio-routing-group|UpdateAudioRoutingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--audio-routing-group-id**|string|key: id of audioRoutingGroup|audio_routing_group_id|audioRoutingGroup-id|
|**--id**|string|Read-only.|id|id|
|**--receivers**|array||receivers|receivers|
|**--routing-mode**|choice||routing_mode|routingMode|
|**--sources**|array||sources|sources|

### cloudcommunications communication-call update-operation

update-operation a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-operation|UpdateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--comms-operation-id**|string|key: id of commsOperation|comms_operation_id|commsOperation-id|
|**--id**|string|Read-only.|id|id|
|**--client-context**|string|Unique Client Context string. Max limit is 256 chars.|client_context|clientContext|
|**--status**|choice||status|status|
|**--result-info-code**|integer||code|code|
|**--result-info-message**|string||message|message|
|**--result-info-subcode**|integer||subcode|subcode|

### cloudcommunications communication-call update-participant

update-participant a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-participant|UpdateParticipants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--participant-id**|string|key: id of participant|participant_id|participant-id|
|**--id**|string|Read-only.|id|id|
|**--is-in-lobby**|boolean|true if the participant is in lobby.|is_in_lobby|isInLobby|
|**--is-muted**|boolean|true if the participant is muted (client or server muted).|is_muted|isMuted|
|**--media-streams**|array|The list of media streams.|media_streams|mediaStreams|
|**--metadata**|string||metadata|metadata|
|**--recording-info-initiated-by**|object|participantInfo|initiated_by|initiatedBy|
|**--recording-info-initiator**|object|identitySet|initiator|initiator|
|**--recording-info-recording-status**|choice||recording_status|recordingStatus|
|**--info-country-code**|string|The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.|country_code|countryCode|
|**--info-endpoint-type**|choice||endpoint_type|endpointType|
|**--info-identity**|object|identitySet|identity|identity|
|**--info-language-id**|string|The language culture string. Read-only.|language_id|languageId|
|**--info-region**|string|The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location. Read-only.|region|region|

### cloudcommunications communication-call update-recording-status

update-recording-status a cloudcommunications communication-call.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call|communications.calls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-recording-status|updateRecordingStatus|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--status**|choice||status|status|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications communication-call-participant invite

invite a cloudcommunications communication-call-participant.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-participant|communications.calls.participants|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|invite|invite|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--participants**|array||participants|participants|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications communication-call-participant mute

mute a cloudcommunications communication-call-participant.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-participant|communications.calls.participants|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|mute|mute|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--participant-id**|string|key: id of participant|participant_id|participant-id|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications communication-call-participant mute-all

mute-all a cloudcommunications communication-call-participant.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-participant|communications.calls.participants|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|mute-all|muteAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-id**|string|key: id of call|call_id|call-id|
|**--participants**|array||participants|participants|
|**--client-context**|string||client_context|clientContext|

### cloudcommunications communication-call-record create-session

create-session a cloudcommunications communication-call-record.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-record|communications.callRecords|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-session|CreateSessions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--id**|string|Read-only.|id|id|
|**--end-date-time**|date-time|UTC time when the last user left the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--failure-info**|object|failureInfo|failure_info|failureInfo|
|**--modalities**|array|List of modalities present in the session. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.|modalities|modalities|
|**--start-date-time**|date-time|UTC fime when the first user joined the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--segments**|array|The list of segments involved in the session. Read-only. Nullable.|segments|segments|
|**--caller-user-agent**|object|userAgent|user_agent|userAgent|
|**--callee-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

### cloudcommunications communication-call-record delete

delete a cloudcommunications communication-call-record.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-record|communications.callRecords|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSessions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--if-match**|string|ETag|if_match|If-Match|

### cloudcommunications communication-call-record get-session

get-session a cloudcommunications communication-call-record.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-record|communications.callRecords|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-session|GetSessions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-call-record list-session

list-session a cloudcommunications communication-call-record.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-record|communications.callRecords|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-session|ListSessions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-call-record update-session

update-session a cloudcommunications communication-call-record.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-record|communications.callRecords|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-session|UpdateSessions|

#### Parameters
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
|**--caller-user-agent**|object|userAgent|user_agent|userAgent|
|**--callee-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

### cloudcommunications communication-call-record-session create-segment

create-segment a cloudcommunications communication-call-record-session.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-record-session|communications.callRecords.sessions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-segment|CreateSegments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--id**|string|Read-only.|id|id|
|**--end-date-time**|date-time|UTC time when the segment ended. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--failure-info**|object|failureInfo|failure_info|failureInfo|
|**--media**|array|Media associated with this segment.|media|media|
|**--start-date-time**|date-time|UTC time when the segment started. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--caller-user-agent**|object|userAgent|user_agent|userAgent|
|**--callee-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

### cloudcommunications communication-call-record-session delete

delete a cloudcommunications communication-call-record-session.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-record-session|communications.callRecords.sessions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSegments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--segment-id**|string|key: id of segment|segment_id|segment-id|
|**--if-match**|string|ETag|if_match|If-Match|

### cloudcommunications communication-call-record-session get-segment

get-segment a cloudcommunications communication-call-record-session.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-record-session|communications.callRecords.sessions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-segment|GetSegments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--segment-id**|string|key: id of segment|segment_id|segment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-call-record-session list-segment

list-segment a cloudcommunications communication-call-record-session.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-record-session|communications.callRecords.sessions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-segment|ListSegments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--call-record-id**|string|key: id of callRecord|call_record_id|callRecord-id|
|**--session-id**|string|key: id of session|session_id|session-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-call-record-session update-segment

update-segment a cloudcommunications communication-call-record-session.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-call-record-session|communications.callRecords.sessions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-segment|UpdateSegments|

#### Parameters
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
|**--caller-user-agent**|object|userAgent|user_agent|userAgent|
|**--callee-user-agent**|object|userAgent|microsoft_graph_call_records_user_agent|userAgent|

### cloudcommunications communication-cloud-communication get-cloud-communication

get-cloud-communication a cloudcommunications communication-cloud-communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-cloud-communication|communications.cloudCommunications|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-cloud-communication|GetCloudCommunications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications communication-cloud-communication update-cloud-communication

update-cloud-communication a cloudcommunications communication-cloud-communication.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-cloud-communication|communications.cloudCommunications|

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
|**--presences**|array||presences|presences|

### cloudcommunications communication-online-meeting create-or-get

create-or-get a cloudcommunications communication-online-meeting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications communication-online-meeting|communications.onlineMeetings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-or-get|createOrGet|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--external-id**|string||external_id|externalId|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--subject**|string||subject|subject|
|**--participants-attendees**|array||attendees|attendees|
|**--participants-contributors**|array||contributors|contributors|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--participants-producers**|array||producers|producers|

### cloudcommunications user create-online-meeting

create-online-meeting a cloudcommunications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-online-meeting|CreateOnlineMeetings|

#### Parameters
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
|**--participants-attendees**|array||attendees|attendees|
|**--participants-contributors**|array||contributors|contributors|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--participants-producers**|array||producers|producers|

### cloudcommunications user delete

delete a cloudcommunications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteOnlineMeetings|
|delete|DeletePresence|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--online-meeting-id**|string|key: id of onlineMeeting|online_meeting_id|onlineMeeting-id|
|**--if-match**|string|ETag|if_match|If-Match|

### cloudcommunications user get-online-meeting

get-online-meeting a cloudcommunications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications user|users|

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

### cloudcommunications user get-presence

get-presence a cloudcommunications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-presence|GetPresence|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### cloudcommunications user list-online-meeting

list-online-meeting a cloudcommunications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications user|users|

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

### cloudcommunications user update-online-meeting

update-online-meeting a cloudcommunications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications user|users|

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
|**--participants-attendees**|array||attendees|attendees|
|**--participants-contributors**|array||contributors|contributors|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|
|**--participants-producers**|array||producers|producers|

### cloudcommunications user update-presence

update-presence a cloudcommunications user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|cloudcommunications user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-presence|UpdatePresence|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|string||activity|activity|
|**--availability**|string||availability|availability|
