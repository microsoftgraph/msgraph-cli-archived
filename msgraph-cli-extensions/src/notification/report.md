# Azure CLI Module Creation Report

### notification user create-notification

create-notification a notification user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notification user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-notification|CreateNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--target-host-name**|string||target_host_name|targetHostName|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--display-time-to-live**|integer||display_time_to_live|displayTimeToLive|
|**--priority**|choice|priority|priority|priority|
|**--group-name**|string||group_name|groupName|
|**--target-policy**|object|targetPolicyEndpoints|target_policy|targetPolicy|
|**--payload-raw-content**|string||raw_content|rawContent|
|**--payload-visual-content**|object|visualProperties|visual_content|visualContent|

### notification user get-notification

get-notification a notification user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notification user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-notification|GetNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notification-id**|string|key: notification-id of notification|notification_id|notification-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notification user list-notification

list-notification a notification user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notification user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-notification|ListNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notification user update

update a notification user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notification user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notification-id**|string|key: notification-id of notification|notification_id|notification-id|
|**--id**|string|Read-only.|id|id|
|**--target-host-name**|string||target_host_name|targetHostName|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--display-time-to-live**|integer||display_time_to_live|displayTimeToLive|
|**--priority**|choice|priority|priority|priority|
|**--group-name**|string||group_name|groupName|
|**--target-policy**|object|targetPolicyEndpoints|target_policy|targetPolicy|
|**--payload-raw-content**|string||raw_content|rawContent|
|**--payload-visual-content**|object|visualProperties|visual_content|visualContent|
