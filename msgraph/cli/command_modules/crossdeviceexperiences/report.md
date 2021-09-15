# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az crossdeviceexperiences|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az crossdeviceexperiences` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az crossdeviceexperiences user|users|[commands](#CommandsInusers)|
|az crossdeviceexperiences usersactivitieshistoryitem|users.activities.historyItems|[commands](#CommandsInusers.activities.historyItems)|
|az crossdeviceexperiences usersactivity|users.activities|[commands](#CommandsInusers.activities)|

## COMMANDS
### <a name="CommandsInusers">Commands in `az crossdeviceexperiences user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az crossdeviceexperiences user create-activity](#usersCreateActivities)|CreateActivities|[Parameters](#ParametersusersCreateActivities)|Not Found|
|[az crossdeviceexperiences user delete-activity](#usersDeleteActivities)|DeleteActivities|[Parameters](#ParametersusersDeleteActivities)|Not Found|
|[az crossdeviceexperiences user list-activity](#usersListActivities)|ListActivities|[Parameters](#ParametersusersListActivities)|Not Found|
|[az crossdeviceexperiences user show-activity](#usersGetActivities)|GetActivities|[Parameters](#ParametersusersGetActivities)|Not Found|
|[az crossdeviceexperiences user update-activity](#usersUpdateActivities)|UpdateActivities|[Parameters](#ParametersusersUpdateActivities)|Not Found|

### <a name="CommandsInusers.activities.historyItems">Commands in `az crossdeviceexperiences usersactivitieshistoryitem` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az crossdeviceexperiences usersactivitieshistoryitem delete-ref-activity](#users.activities.historyItemsDeleteRefActivity)|DeleteRefActivity|[Parameters](#Parametersusers.activities.historyItemsDeleteRefActivity)|Not Found|
|[az crossdeviceexperiences usersactivitieshistoryitem set-ref-activity](#users.activities.historyItemsSetRefActivity)|SetRefActivity|[Parameters](#Parametersusers.activities.historyItemsSetRefActivity)|Not Found|
|[az crossdeviceexperiences usersactivitieshistoryitem show-activity](#users.activities.historyItemsGetActivity)|GetActivity|[Parameters](#Parametersusers.activities.historyItemsGetActivity)|Not Found|
|[az crossdeviceexperiences usersactivitieshistoryitem show-ref-activity](#users.activities.historyItemsGetRefActivity)|GetRefActivity|[Parameters](#Parametersusers.activities.historyItemsGetRefActivity)|Not Found|

### <a name="CommandsInusers.activities">Commands in `az crossdeviceexperiences usersactivity` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az crossdeviceexperiences usersactivity create-history-item](#users.activitiesCreateHistoryItems)|CreateHistoryItems|[Parameters](#Parametersusers.activitiesCreateHistoryItems)|Not Found|
|[az crossdeviceexperiences usersactivity delete-history-item](#users.activitiesDeleteHistoryItems)|DeleteHistoryItems|[Parameters](#Parametersusers.activitiesDeleteHistoryItems)|Not Found|
|[az crossdeviceexperiences usersactivity list-history-item](#users.activitiesListHistoryItems)|ListHistoryItems|[Parameters](#Parametersusers.activitiesListHistoryItems)|Not Found|
|[az crossdeviceexperiences usersactivity show-history-item](#users.activitiesGetHistoryItems)|GetHistoryItems|[Parameters](#Parametersusers.activitiesGetHistoryItems)|Not Found|
|[az crossdeviceexperiences usersactivity update-history-item](#users.activitiesUpdateHistoryItems)|UpdateHistoryItems|[Parameters](#Parametersusers.activitiesUpdateHistoryItems)|Not Found|


## COMMAND DETAILS
### group `az crossdeviceexperiences user`
#### <a name="usersCreateActivities">Command `az crossdeviceexperiences user create-activity`</a>


##### <a name="ParametersusersCreateActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--activation-url**|string|Required. URL used to launch the activity in the best native experience represented by the appId. Might launch a web-based app if no native app exists.|activation_url|activationUrl|
|**--activity-source-host**|string|Required. URL for the domain representing the cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per cross-platform app identity. For example, a separate file and domain is needed for Word vs. PowerPoint.|activity_source_host|activitySourceHost|
|**--app-activity-id**|string|Required. The unique activity ID in the context of the app - supplied by caller and immutable thereafter.|app_activity_id|appActivityId|
|**--app-display-name**|string|Optional. Short text description of the app used to generate the activity for use in cases when the app is not installed on the user’s local device.|app_display_name|appDisplayName|
|**--content-info**|dictionary|Json|content_info|contentInfo|
|**--content-url**|string|Optional. Used in the event the content can be rendered outside of a native or web-based app experience (for example, a pointer to an item in an RSS feed).|content_url|contentUrl|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--expiration-date-time**|date-time|Set by the server. DateTime in UTC when the object expired on the server.|expiration_date_time|expirationDateTime|
|**--fallback-url**|string|Optional. URL used to launch the activity in a web-based app, if available.|fallback_url|fallbackUrl|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--status**|choice||status|status|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time; values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--history-items**|array|Optional. NavigationProperty/Containment; navigation property to the activity's historyItems.|history_items|historyItems|
|**--attribution**|object|imageInfo|attribution|attribution|
|**--background-color**|string|Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color|background_color|backgroundColor|
|**--content**|dictionary|Json|content|content|
|**--description**|string|Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)|description|description|
|**--display-text**|string|Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)|display_text|displayText|

#### <a name="usersDeleteActivities">Command `az crossdeviceexperiences user delete-activity`</a>


##### <a name="ParametersusersDeleteActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListActivities">Command `az crossdeviceexperiences user list-activity`</a>


##### <a name="ParametersusersListActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetActivities">Command `az crossdeviceexperiences user show-activity`</a>


##### <a name="ParametersusersGetActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateActivities">Command `az crossdeviceexperiences user update-activity`</a>


##### <a name="ParametersusersUpdateActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--id**|string|Read-only.|id|id|
|**--activation-url**|string|Required. URL used to launch the activity in the best native experience represented by the appId. Might launch a web-based app if no native app exists.|activation_url|activationUrl|
|**--activity-source-host**|string|Required. URL for the domain representing the cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per cross-platform app identity. For example, a separate file and domain is needed for Word vs. PowerPoint.|activity_source_host|activitySourceHost|
|**--app-activity-id**|string|Required. The unique activity ID in the context of the app - supplied by caller and immutable thereafter.|app_activity_id|appActivityId|
|**--app-display-name**|string|Optional. Short text description of the app used to generate the activity for use in cases when the app is not installed on the user’s local device.|app_display_name|appDisplayName|
|**--content-info**|dictionary|Json|content_info|contentInfo|
|**--content-url**|string|Optional. Used in the event the content can be rendered outside of a native or web-based app experience (for example, a pointer to an item in an RSS feed).|content_url|contentUrl|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--expiration-date-time**|date-time|Set by the server. DateTime in UTC when the object expired on the server.|expiration_date_time|expirationDateTime|
|**--fallback-url**|string|Optional. URL used to launch the activity in a web-based app, if available.|fallback_url|fallbackUrl|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--status**|choice||status|status|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time; values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--history-items**|array|Optional. NavigationProperty/Containment; navigation property to the activity's historyItems.|history_items|historyItems|
|**--attribution**|object|imageInfo|attribution|attribution|
|**--background-color**|string|Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color|background_color|backgroundColor|
|**--content**|dictionary|Json|content|content|
|**--description**|string|Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)|description|description|
|**--display-text**|string|Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)|display_text|displayText|

### group `az crossdeviceexperiences usersactivitieshistoryitem`
#### <a name="users.activities.historyItemsDeleteRefActivity">Command `az crossdeviceexperiences usersactivitieshistoryitem delete-ref-activity`</a>


##### <a name="Parametersusers.activities.historyItemsDeleteRefActivity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.activities.historyItemsSetRefActivity">Command `az crossdeviceexperiences usersactivitieshistoryitem set-ref-activity`</a>


##### <a name="Parametersusers.activities.historyItemsSetRefActivity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="users.activities.historyItemsGetActivity">Command `az crossdeviceexperiences usersactivitieshistoryitem show-activity`</a>


##### <a name="Parametersusers.activities.historyItemsGetActivity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.activities.historyItemsGetRefActivity">Command `az crossdeviceexperiences usersactivitieshistoryitem show-ref-activity`</a>


##### <a name="Parametersusers.activities.historyItemsGetRefActivity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|

### group `az crossdeviceexperiences usersactivity`
#### <a name="users.activitiesCreateHistoryItems">Command `az crossdeviceexperiences usersactivity create-history-item`</a>


##### <a name="Parametersusers.activitiesCreateHistoryItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--id**|string|Read-only.|id|id|
|**--active-duration-seconds**|integer|Optional. The duration of active user engagement. if not supplied, this is calculated from the startedDateTime and lastActiveDateTime.|active_duration_seconds|activeDurationSeconds|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--expiration-date-time**|date-time|Optional. UTC DateTime when the historyItem will undergo hard-delete. Can be set by the client.|expiration_date_time|expirationDateTime|
|**--last-active-date-time**|date-time|Optional. UTC DateTime when the historyItem (activity session) was last understood as active or finished - if null, historyItem status should be Ongoing.|last_active_date_time|lastActiveDateTime|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--started-date-time**|date-time|Required. UTC DateTime when the historyItem (activity session) was started. Required for timeline history.|started_date_time|startedDateTime|
|**--status**|choice||status|status|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time. Values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--activity**|object|userActivity|activity|activity|

#### <a name="users.activitiesDeleteHistoryItems">Command `az crossdeviceexperiences usersactivity delete-history-item`</a>


##### <a name="Parametersusers.activitiesDeleteHistoryItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.activitiesListHistoryItems">Command `az crossdeviceexperiences usersactivity list-history-item`</a>


##### <a name="Parametersusers.activitiesListHistoryItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.activitiesGetHistoryItems">Command `az crossdeviceexperiences usersactivity show-history-item`</a>


##### <a name="Parametersusers.activitiesGetHistoryItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.activitiesUpdateHistoryItems">Command `az crossdeviceexperiences usersactivity update-history-item`</a>


##### <a name="Parametersusers.activitiesUpdateHistoryItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--id**|string|Read-only.|id|id|
|**--active-duration-seconds**|integer|Optional. The duration of active user engagement. if not supplied, this is calculated from the startedDateTime and lastActiveDateTime.|active_duration_seconds|activeDurationSeconds|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--expiration-date-time**|date-time|Optional. UTC DateTime when the historyItem will undergo hard-delete. Can be set by the client.|expiration_date_time|expirationDateTime|
|**--last-active-date-time**|date-time|Optional. UTC DateTime when the historyItem (activity session) was last understood as active or finished - if null, historyItem status should be Ongoing.|last_active_date_time|lastActiveDateTime|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--started-date-time**|date-time|Required. UTC DateTime when the historyItem (activity session) was started. Required for timeline history.|started_date_time|startedDateTime|
|**--status**|choice||status|status|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time. Values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--activity**|object|userActivity|activity|activity|
