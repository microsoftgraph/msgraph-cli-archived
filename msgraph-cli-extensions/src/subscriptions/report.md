# Azure CLI Module Creation Report

### subscriptions create-subscription

create-subscription a subscriptions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|subscriptions|subscriptions.subscription|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-subscription|CreateSubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list notifications support only the updated changeType. User and group notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each notification. The maximum length is 128 characters. The client can check that the notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each notification.|client_state|clientState|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--include-properties**|boolean||include_properties|includeProperties|
|**--include-resource-data**|boolean||include_resource_data|includeResourceData|
|**--lifecycle-notification-url**|string||lifecycle_notification_url|lifecycleNotificationUrl|
|**--encryption-certificate**|string||encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string||encryption_certificate_id|encryptionCertificateId|
|**--latest-supported-tls-version**|string|Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.|latest_supported_tls_version|latestSupportedTlsVersion|

### subscriptions delete

delete a subscriptions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|subscriptions|subscriptions.subscription|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|key: subscription-id of subscription|subscription_id|subscription-id|
|**--if-match**|string|ETag|if_match|If-Match|

### subscriptions get-subscription

get-subscription a subscriptions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|subscriptions|subscriptions.subscription|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-subscription|GetSubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|key: subscription-id of subscription|subscription_id|subscription-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### subscriptions list-subscription

list-subscription a subscriptions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|subscriptions|subscriptions.subscription|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-subscription|ListSubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### subscriptions update-subscription

update-subscription a subscriptions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|subscriptions|subscriptions.subscription|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-subscription|UpdateSubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|key: subscription-id of subscription|subscription_id|subscription-id|
|**--id**|string|Read-only.|id|id|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list notifications support only the updated changeType. User and group notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each notification. The maximum length is 128 characters. The client can check that the notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each notification.|client_state|clientState|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--include-properties**|boolean||include_properties|includeProperties|
|**--include-resource-data**|boolean||include_resource_data|includeResourceData|
|**--lifecycle-notification-url**|string||lifecycle_notification_url|lifecycleNotificationUrl|
|**--encryption-certificate**|string||encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string||encryption_certificate_id|encryptionCertificateId|
|**--latest-supported-tls-version**|string|Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.|latest_supported_tls_version|latestSupportedTlsVersion|
