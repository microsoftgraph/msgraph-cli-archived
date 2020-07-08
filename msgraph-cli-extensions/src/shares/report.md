# Azure CLI Module Creation Report

### shares share create-item

create-item a shares share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-item|CreateItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New navigation property|body|body|

### shares share get-drive-item

get-drive-item a shares share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item|GetDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share get-item

get-item a shares share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--drive-item-id**|string|key: driveItem-id of driveItem|drive_item_id|driveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share get-list

get-list a shares share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list|GetList|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share get-list-item

get-list-item a shares share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list-item|GetListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share get-permission

get-permission a shares share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission|GetPermission|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share get-root

get-root a shares share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-root|GetRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share get-site

get-site a shares share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-site|GetSite|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share list-item

list-item a shares share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-item|ListItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share update

update a shares share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateItems|
|update|UpdateDriveItem|
|update|UpdateList|
|update|UpdateListItem|
|update|UpdatePermission|
|update|UpdateRoot|
|update|UpdateSite|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--drive-item-id**|string|key: driveItem-id of driveItem|drive_item_id|driveItem-id|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--parent-reference-site-id**|string||site_id|siteId|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--system**|any|Any object|system|system|
|**--activities**|array||activities|activities|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--items**|array|All items contained in the list.|items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--root**|any|Any object|root|root|
|**--drives**|array|The collection of drives (document libraries) under this site.|drives|drives|
|**--lists**|array|The collection of lists under this site.|lists|lists|
|**--pages**|array||pages|pages|
|**--sites**|array|The collection of the sub-sites under this site.|sites|sites|
|**--onenote-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--onenote-notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--onenote-sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--onenote-section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--onenote-pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|microsoft_graph_onenote_pages|pages|
|**--onenote-resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--onenote-operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--site-collection-data-location-code**|string|The geographic region code for where this site collection resides. Read-only.|data_location_code|dataLocationCode|
|**--site-collection-hostname**|string|The hostname for the site collection. Read-only.|hostname|hostname|
|**--site-collection-root**|any|Any object|any_root|root|

### shares share-list create-activity

create-activity a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity|CreateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New navigation property|body|body|

### shares share-list create-column

create-column a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-column|CreateColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--boolean**|any|Any object|boolean|boolean|
|**--calculated**|object|calculatedColumn|calculated|calculated|
|**--choice**|object|choiceColumn|choice|choice|
|**--column-group**|string|For site columns, the name of the group this column belongs to. Helps organize related columns.|column_group|columnGroup|
|**--date-time**|object|dateTimeColumn|date_time|dateTime|
|**--default-value**|object|defaultColumnValue|default_value|defaultValue|
|**--description**|string|The user-facing description of the column.|description|description|
|**--display-name**|string|The user-facing name of the column.|display_name|displayName|
|**--enforce-unique-values**|boolean|If true, no two list items may have the same value for this column.|enforce_unique_values|enforceUniqueValues|
|**--geolocation**|any|Any object|geolocation|geolocation|
|**--hidden**|boolean|Specifies whether the column is displayed in the user interface.|hidden|hidden|
|**--indexed**|boolean|Specifies whether the column values can used for sorting and searching.|indexed|indexed|
|**--lookup**|object|lookupColumn|lookup|lookup|
|**--name**|string|The API-facing name of the column as it appears in the [fields][] on a [listItem][]. For the user-facing name, see displayName.|name|name|
|**--number**|object|numberColumn|number|number|
|**--person-or-group**|object|personOrGroupColumn|person_or_group|personOrGroup|
|**--read-only**|boolean|Specifies whether the column values can be modified.|read_only|readOnly|
|**--required**|boolean|Specifies whether the column value is not optional.|required|required|
|**--text**|object|textColumn|text|text|
|**--currency-locale**|string|Specifies the locale from which to infer the currency symbol.|locale|locale|

### shares share-list create-content-type

create-content-type a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-content-type|CreateContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|The descriptive text for the item.|description|description|
|**--group**|string|The name of the group this content type belongs to. Helps organize related content types.|group|group|
|**--hidden**|boolean|Indicates whether the content type is hidden in the list's 'New' menu.|hidden|hidden|
|**--name**|string|The name of the content type.|name|name|
|**--order**|object|contentTypeOrder|order|order|
|**--parent-id**|string|The unique identifier of the content type.|parent_id|parentId|
|**--read-only**|boolean|If true, the content type cannot be modified unless this value is first set to false.|read_only|readOnly|
|**--sealed**|boolean|If true, the content type cannot be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.|sealed|sealed|
|**--column-links**|array|The collection of columns that are required by this content type|column_links|columnLinks|
|**--inherited-from-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--inherited-from-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--inherited-from-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--inherited-from-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--inherited-from-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--inherited-from-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--inherited-from-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--inherited-from-site-id**|string||site_id|siteId|

### shares share-list create-item

create-item a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-item|CreateItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--parent-reference-site-id**|string||site_id|siteId|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### shares share-list create-subscription

create-subscription a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-subscription|CreateSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
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

### shares share-list get-activity

get-activity a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity|GetActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list get-column

get-column a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-column|GetColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--column-definition-id**|string|key: columnDefinition-id of columnDefinition|column_definition_id|columnDefinition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list get-content-type

get-content-type a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-content-type|GetContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: contentType-id of contentType|content_type_id|contentType-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list get-drive

get-drive a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive|GetDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list get-item

get-item a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: listItem-id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list get-subscription

get-subscription a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-subscription|GetSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--subscription-id**|string|key: subscription-id of subscription|subscription_id|subscription-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list list-activity

list-activity a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity|ListActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list list-column

list-column a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-column|ListColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list list-content-type

list-content-type a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-content-type|ListContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list list-item

list-item a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-item|ListItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list list-subscription

list-subscription a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-subscription|ListSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list update

update a shares share-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateActivities|
|update|UpdateColumns|
|update|UpdateContentTypes|
|update|UpdateItems|
|update|UpdateSubscriptions|
|update|UpdateDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--body**|object|New navigation property values|body|body|
|**--column-definition-id**|string|key: columnDefinition-id of columnDefinition|column_definition_id|columnDefinition-id|
|**--content-type-id**|string|key: contentType-id of contentType|content_type_id|contentType-id|
|**--list-item-id**|string|key: listItem-id of listItem|list_item_id|listItem-id|
|**--subscription-id**|string|key: subscription-id of subscription|subscription_id|subscription-id|
|**--id**|string|Read-only.|id|id|
|**--boolean**|any|Any object|boolean|boolean|
|**--calculated**|object|calculatedColumn|calculated|calculated|
|**--choice**|object|choiceColumn|choice|choice|
|**--column-group**|string|For site columns, the name of the group this column belongs to. Helps organize related columns.|column_group|columnGroup|
|**--date-time**|object|dateTimeColumn|date_time|dateTime|
|**--default-value**|object|defaultColumnValue|default_value|defaultValue|
|**--description**|string|The user-facing description of the column.|description|description|
|**--display-name**|string|The user-facing name of the column.|display_name|displayName|
|**--enforce-unique-values**|boolean|If true, no two list items may have the same value for this column.|enforce_unique_values|enforceUniqueValues|
|**--geolocation**|any|Any object|geolocation|geolocation|
|**--hidden**|boolean|Specifies whether the column is displayed in the user interface.|hidden|hidden|
|**--indexed**|boolean|Specifies whether the column values can used for sorting and searching.|indexed|indexed|
|**--lookup**|object|lookupColumn|lookup|lookup|
|**--name**|string|The API-facing name of the column as it appears in the [fields][] on a [listItem][]. For the user-facing name, see displayName.|name|name|
|**--number**|object|numberColumn|number|number|
|**--person-or-group**|object|personOrGroupColumn|person_or_group|personOrGroup|
|**--read-only**|boolean|Specifies whether the column values can be modified.|read_only|readOnly|
|**--required**|boolean|Specifies whether the column value is not optional.|required|required|
|**--text**|object|textColumn|text|text|
|**--currency-locale**|string|Specifies the locale from which to infer the currency symbol.|locale|locale|
|**--group**|string|The name of the group this content type belongs to. Helps organize related content types.|group|group|
|**--order**|object|contentTypeOrder|order|order|
|**--parent-id**|string|The unique identifier of the content type.|parent_id|parentId|
|**--sealed**|boolean|If true, the content type cannot be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.|sealed|sealed|
|**--column-links**|array|The collection of columns that are required by this content type|column_links|columnLinks|
|**--inherited-from-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--inherited-from-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--inherited-from-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--inherited-from-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--inherited-from-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--inherited-from-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--inherited-from-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--inherited-from-site-id**|string||site_id|siteId|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--parent-reference-site-id**|string||site_id|siteId|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|
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
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|any|Any object|system|system|
|**--bundles**|array||bundles|bundles|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--list**|object|list|list|list|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--quota-deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--quota-remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--quota-state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--quota-total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--quota-used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--quota-storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--owner-application**|object|identity|application1|application|
|**--owner-device**|object|identity|device1|device|
|**--owner-user**|object|identity|user1|user|

### shares share-list-activity get-drive-item

get-drive-item a shares share-list-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity|shares.list.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item|GetDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-activity get-list-item

get-list-item a shares share-list-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity|shares.list.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list-item|GetListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-activity update

update a shares share-list-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity|shares.list.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateDriveItem|
|update|UpdateListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--parent-reference-site-id**|string||site_id|siteId|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### shares share-list-activity-list-item create-activity

create-activity a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity|CreateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--body**|object|New navigation property|body|body|

### shares share-list-activity-list-item create-version

create-version a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-version|CreateVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### shares share-list-activity-list-item get-activity

get-activity a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity|GetActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--item-activity-old-id1**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id1|itemActivityOLD-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-activity-list-item get-activity-by-interval

get-activity-by-interval a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval|getActivitiesByInterval|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

### shares share-list-activity-list-item get-analytic

get-analytic a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-analytic|GetAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-activity-list-item get-drive-item

get-drive-item a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item|GetDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-activity-list-item get-field

get-field a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-field|GetFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-activity-list-item get-version

get-version a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-version|GetVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: listItemVersion-id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-activity-list-item list-activity

list-activity a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity|ListActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-activity-list-item list-version

list-version a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-version|ListVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-activity-list-item update

update a shares share-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item|shares.list.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateActivities|
|update|UpdateVersions|
|update|UpdateDriveItem|
|update|UpdateFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--item-activity-old-id1**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id1|itemActivityOLD-id1|
|**--body**|object|New navigation property values|body|body|
|**--list-item-version-id**|string|key: listItemVersion-id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### shares share-list-activity-list-item-version get-field

get-field a shares share-list-activity-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item-version|shares.list.activities.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-field|GetFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: listItemVersion-id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-activity-list-item-version restore-version

restore-version a shares share-list-activity-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item-version|shares.list.activities.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore-version|restoreVersion|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: listItemVersion-id of listItemVersion|list_item_version_id|listItemVersion-id|

### shares share-list-activity-list-item-version update

update a shares share-list-activity-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-activity-list-item-version|shares.list.activities.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: listItemVersion-id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|

### shares share-list-content-type create-column-link

create-column-link a shares share-list-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-content-type|shares.list.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-column-link|CreateColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: contentType-id of contentType|content_type_id|contentType-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

### shares share-list-content-type get-column-link

get-column-link a shares share-list-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-content-type|shares.list.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-column-link|GetColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: contentType-id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: columnLink-id of columnLink|column_link_id|columnLink-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-content-type list-column-link

list-column-link a shares share-list-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-content-type|shares.list.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-column-link|ListColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: contentType-id of contentType|content_type_id|contentType-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-content-type update

update a shares share-list-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-content-type|shares.list.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: contentType-id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: columnLink-id of columnLink|column_link_id|columnLink-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

### shares share-list-item create-activity

create-activity a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity|CreateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New navigation property|body|body|

### shares share-list-item create-version

create-version a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-version|CreateVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### shares share-list-item get-activity

get-activity a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity|GetActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-item get-activity-by-interval

get-activity-by-interval a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval|getActivitiesByInterval|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

### shares share-list-item get-analytic

get-analytic a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-analytic|GetAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-item get-drive-item

get-drive-item a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item|GetDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-item get-field

get-field a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-field|GetFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-item get-version

get-version a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-version|GetVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: listItemVersion-id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-item list-activity

list-activity a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity|ListActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-item list-version

list-version a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-version|ListVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-item update

update a shares share-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateActivities|
|update|UpdateVersions|
|update|UpdateDriveItem|
|update|UpdateFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--body**|object|New navigation property values|body|body|
|**--list-item-version-id**|string|key: listItemVersion-id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### shares share-list-item-activity get-drive-item

get-drive-item a shares share-list-item-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item-activity|shares.listItem.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item|GetDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-item-activity get-list-item

get-list-item a shares share-list-item-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item-activity|shares.listItem.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list-item|GetListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-item-activity update

update a shares share-list-item-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item-activity|shares.listItem.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateDriveItem|
|update|UpdateListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--parent-reference-site-id**|string||site_id|siteId|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### shares share-list-item-activity-list-item get-activity-by-interval

get-activity-by-interval a shares share-list-item-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item-activity-list-item|shares.listItem.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval|getActivitiesByInterval|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--item-activity-old-id**|string|key: itemActivityOLD-id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

### shares share-list-item-version get-field

get-field a shares share-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item-version|shares.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-field|GetFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: listItemVersion-id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-list-item-version restore-version

restore-version a shares share-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item-version|shares.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore-version|restoreVersion|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: listItemVersion-id of listItemVersion|list_item_version_id|listItemVersion-id|

### shares share-list-item-version update

update a shares share-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-list-item-version|shares.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: listItemVersion-id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|

### shares share-permission grant

grant a shares share-permission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-permission|shares.permission|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|grant|grant|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--roles**|array||roles|roles|
|**--recipients**|array||recipients|recipients|

### shares share-shared-drive-item create-shared-drive-item

create-shared-drive-item a shares share-shared-drive-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-shared-drive-item|shares.sharedDriveItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-shared-drive-item|CreateSharedDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### shares share-shared-drive-item delete

delete a shares share-shared-drive-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-shared-drive-item|shares.sharedDriveItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSharedDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

### shares share-shared-drive-item get-shared-drive-item

get-shared-drive-item a shares share-shared-drive-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-shared-drive-item|shares.sharedDriveItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shared-drive-item|GetSharedDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-shared-drive-item list-shared-drive-item

list-shared-drive-item a shares share-shared-drive-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-shared-drive-item|shares.sharedDriveItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-shared-drive-item|ListSharedDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### shares share-shared-drive-item update

update a shares share-shared-drive-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|shares share-shared-drive-item|shares.sharedDriveItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSharedDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: sharedDriveItem-id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New property values|body|body|
