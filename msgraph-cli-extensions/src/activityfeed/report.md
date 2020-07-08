# Azure CLI Module Creation Report

### activityfeed user create-activity

create-activity a activityfeed user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|activityfeed user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity|CreateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--activity-source-host**|string|Required. URL for the domain representing the cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per cross-platform app identity. For example, a separate file and domain is needed for Word vs. PowerPoint.|activity_source_host|activitySourceHost|
|**--activation-url**|string|Required. URL used to launch the activity in the best native experience represented by the appId. Might launch a web-based app if no native app exists.|activation_url|activationUrl|
|**--app-activity-id**|string|Required. The unique activity ID in the context of the app - supplied by caller and immutable thereafter.|app_activity_id|appActivityId|
|**--app-display-name**|string|Optional. Short text description of the app used to generate the activity for use in cases when the app is not installed on the user’s local device.|app_display_name|appDisplayName|
|**--content-url**|string|Optional. Used in the event the content can be rendered outside of a native or web-based app experience (for example, a pointer to an item in an RSS feed).|content_url|contentUrl|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--expiration-date-time**|date-time|Set by the server. DateTime in UTC when the object expired on the server.|expiration_date_time|expirationDateTime|
|**--fallback-url**|string|Optional. URL used to launch the activity in a web-based app, if available.|fallback_url|fallbackUrl|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time; values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--content-info**|any|Any object|content_info|contentInfo|
|**--status**|choice|status|status|status|
|**--history-items**|array|Optional. NavigationProperty/Containment; navigation property to the activity's historyItems.|history_items|historyItems|
|**--visual-elements-attribution**|object|imageInfo|attribution|attribution|
|**--visual-elements-background-color**|string|Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color|background_color|backgroundColor|
|**--visual-elements-description**|string|Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)|description|description|
|**--visual-elements-display-text**|string|Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)|display_text|displayText|
|**--visual-elements-content**|any|Any object|content|content|

### activityfeed user get-activity

get-activity a activityfeed user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|activityfeed user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity|GetActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--user-activity-id**|string|key: userActivity-id of userActivity|user_activity_id|userActivity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### activityfeed user list-activity

list-activity a activityfeed user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|activityfeed user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity|ListActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### activityfeed user update

update a activityfeed user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|activityfeed user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--user-activity-id**|string|key: userActivity-id of userActivity|user_activity_id|userActivity-id|
|**--id**|string|Read-only.|id|id|
|**--activity-source-host**|string|Required. URL for the domain representing the cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per cross-platform app identity. For example, a separate file and domain is needed for Word vs. PowerPoint.|activity_source_host|activitySourceHost|
|**--activation-url**|string|Required. URL used to launch the activity in the best native experience represented by the appId. Might launch a web-based app if no native app exists.|activation_url|activationUrl|
|**--app-activity-id**|string|Required. The unique activity ID in the context of the app - supplied by caller and immutable thereafter.|app_activity_id|appActivityId|
|**--app-display-name**|string|Optional. Short text description of the app used to generate the activity for use in cases when the app is not installed on the user’s local device.|app_display_name|appDisplayName|
|**--content-url**|string|Optional. Used in the event the content can be rendered outside of a native or web-based app experience (for example, a pointer to an item in an RSS feed).|content_url|contentUrl|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--expiration-date-time**|date-time|Set by the server. DateTime in UTC when the object expired on the server.|expiration_date_time|expirationDateTime|
|**--fallback-url**|string|Optional. URL used to launch the activity in a web-based app, if available.|fallback_url|fallbackUrl|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time; values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--content-info**|any|Any object|content_info|contentInfo|
|**--status**|choice|status|status|status|
|**--history-items**|array|Optional. NavigationProperty/Containment; navigation property to the activity's historyItems.|history_items|historyItems|
|**--visual-elements-attribution**|object|imageInfo|attribution|attribution|
|**--visual-elements-background-color**|string|Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color|background_color|backgroundColor|
|**--visual-elements-description**|string|Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)|description|description|
|**--visual-elements-display-text**|string|Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)|display_text|displayText|
|**--visual-elements-content**|any|Any object|content|content|

### activityfeed user-activity create-history-item

create-history-item a activityfeed user-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|activityfeed user-activity|users.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-history-item|CreateHistoryItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--user-activity-id**|string|key: userActivity-id of userActivity|user_activity_id|userActivity-id|
|**--id**|string|Read-only.|id|id|
|**--status**|choice|status|status|status|
|**--active-duration-seconds**|integer|Optional. The duration of active user engagement. if not supplied, this is calculated from the startedDateTime and lastActiveDateTime.|active_duration_seconds|activeDurationSeconds|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--last-active-date-time**|date-time|Optional. UTC DateTime when the historyItem (activity session) was last understood as active or finished - if null, historyItem status should be Ongoing.|last_active_date_time|lastActiveDateTime|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--expiration-date-time**|date-time|Optional. UTC DateTime when the historyItem will undergo hard-delete. Can be set by the client.|expiration_date_time|expirationDateTime|
|**--started-date-time**|date-time|Required. UTC DateTime when the historyItem (activity session) was started. Required for timeline history.|started_date_time|startedDateTime|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time. Values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--activity**|object|userActivity|activity|activity|

### activityfeed user-activity get-history-item

get-history-item a activityfeed user-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|activityfeed user-activity|users.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-history-item|GetHistoryItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--user-activity-id**|string|key: userActivity-id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: activityHistoryItem-id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### activityfeed user-activity list-history-item

list-history-item a activityfeed user-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|activityfeed user-activity|users.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-history-item|ListHistoryItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--user-activity-id**|string|key: userActivity-id of userActivity|user_activity_id|userActivity-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### activityfeed user-activity update

update a activityfeed user-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|activityfeed user-activity|users.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateHistoryItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--user-activity-id**|string|key: userActivity-id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: activityHistoryItem-id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--id**|string|Read-only.|id|id|
|**--status**|choice|status|status|status|
|**--active-duration-seconds**|integer|Optional. The duration of active user engagement. if not supplied, this is calculated from the startedDateTime and lastActiveDateTime.|active_duration_seconds|activeDurationSeconds|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--last-active-date-time**|date-time|Optional. UTC DateTime when the historyItem (activity session) was last understood as active or finished - if null, historyItem status should be Ongoing.|last_active_date_time|lastActiveDateTime|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--expiration-date-time**|date-time|Optional. UTC DateTime when the historyItem will undergo hard-delete. Can be set by the client.|expiration_date_time|expirationDateTime|
|**--started-date-time**|date-time|Required. UTC DateTime when the historyItem (activity session) was started. Required for timeline history.|started_date_time|startedDateTime|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time. Values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--activity**|object|userActivity|activity|activity|

### activityfeed user-activity-history-item get-activity

get-activity a activityfeed user-activity-history-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|activityfeed user-activity-history-item|users.activities.historyItems|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity|GetActivity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--user-activity-id**|string|key: userActivity-id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: activityHistoryItem-id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|
