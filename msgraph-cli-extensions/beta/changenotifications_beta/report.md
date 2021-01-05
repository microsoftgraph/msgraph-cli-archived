# Azure CLI Module Creation Report

### changenotifications create-subscription

create-subscription a changenotifications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|changenotifications|subscriptions.subscription|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-subscription|CreateSubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.|client_state|clientState|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--encryption-certificate**|string|A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional. Required when includeResourceData is true.|encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string|A custom app-provided identifier to help identify the certificate needed to decrypt resource data. Optional.|encryption_certificate_id|encryptionCertificateId|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--include-properties**|boolean||include_properties|includeProperties|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string|Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.|latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string|The URL of the endpoint that receives lifecycle notifications, including subscriptionRemoved and missed notifications. This URL must make use of the HTTPS protocol. Optional. Read more about how Outlook resources use lifecycle notifications.|lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

### changenotifications delete

delete a changenotifications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|changenotifications|subscriptions.subscription|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--if-match**|string|ETag|if_match|If-Match|

### changenotifications get-subscription

get-subscription a changenotifications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|changenotifications|subscriptions.subscription|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-subscription|GetSubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### changenotifications list-subscription

list-subscription a changenotifications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|changenotifications|subscriptions.subscription|

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

### changenotifications update-subscription

update-subscription a changenotifications.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|changenotifications|subscriptions.subscription|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-subscription|UpdateSubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--id**|string|Read-only.|id|id|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.|client_state|clientState|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--encryption-certificate**|string|A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional. Required when includeResourceData is true.|encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string|A custom app-provided identifier to help identify the certificate needed to decrypt resource data. Optional.|encryption_certificate_id|encryptionCertificateId|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--include-properties**|boolean||include_properties|includeProperties|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string|Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.|latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string|The URL of the endpoint that receives lifecycle notifications, including subscriptionRemoved and missed notifications. This URL must make use of the HTTPS protocol. Optional. Read more about how Outlook resources use lifecycle notifications.|lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|
