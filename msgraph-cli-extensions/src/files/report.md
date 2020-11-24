# Azure CLI Module Creation Report

### files create-column

create-column a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-column|CreateColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--boolean**|dictionary|booleanColumn|boolean|boolean|
|**--calculated**|object|calculatedColumn|calculated|calculated|
|**--choice**|object|choiceColumn|choice|choice|
|**--column-group**|string|For site columns, the name of the group this column belongs to. Helps organize related columns.|column_group|columnGroup|
|**--date-time**|object|dateTimeColumn|date_time|dateTime|
|**--default-value**|object|defaultColumnValue|default_value|defaultValue|
|**--description**|string|The user-facing description of the column.|description|description|
|**--display-name**|string|The user-facing name of the column.|display_name|displayName|
|**--enforce-unique-values**|boolean|If true, no two list items may have the same value for this column.|enforce_unique_values|enforceUniqueValues|
|**--geolocation**|dictionary|geolocationColumn|geolocation|geolocation|
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

### files create-column-link

create-column-link a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-column-link|CreateColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

### files create-content-type

create-content-type a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-content-type|CreateContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
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

### files create-drive

create-drive a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-drive|CreateDrives|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
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
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--list-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--list-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--list-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--list-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--list-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--list-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--list-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--list-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--list-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--list-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--list-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--list-parent-reference-name**|string|The name of the item being referenced. Read-only.|name1|name|
|**--list-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--list-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--list-parent-reference-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--list-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-last-modified-by-application**|object|identity|application1|application|
|**--list-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-created-by-application**|object|identity|application2|application|
|**--list-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list-list**|object|listInfo|list|list|
|**--list-sharepoint-ids**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--list-system**|dictionary|systemFacet|microsoft_graph_system_facet_system|system|
|**--list-columns**|array|The collection of field definitions for this list.|columns|columns|
|**--list-content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--list-drive**|object|drive|drive|drive|
|**--list-items**|array|All items contained in the list.|microsoft_graph_list_items|items|
|**--list-subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--quota-deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--quota-remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--quota-state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--quota-storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--quota-total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--quota-used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--owner-application**|object|identity|application3|application|
|**--owner-device**|object|identity|device3|device|
|**--owner-user**|object|identity|user3|user|

### files create-following

create-following a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-following|CreateFollowing|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
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
|**--audio**|object|audio|audio|audio|
|**--content**|byte-array|The content stream, if the item represents a file.|content|content|
|**--c-tag**|string|An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.|c_tag|cTag|
|**--file-system-info**|object|fileSystemInfo|file_system_info|fileSystemInfo|
|**--image**|object|image|image|image|
|**--location**|object|geoCoordinates|location|location|
|**--photo**|object|photo|photo|photo|
|**--publication**|object|publicationFacet|publication|publication|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--size**|integer|Size of the item in bytes. Read-only.|size|size|
|**--video**|object|video|video|video|
|**--web-dav-url**|string|WebDAV compatible URL for the item.|web_dav_url|webDavUrl|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id1|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|name1|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application1|application|
|**--list-item-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-item-created-by-application**|object|identity|application2|application|
|**--list-item-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-analytics**|object|itemAnalytics|microsoft_graph_item_analytics|analytics|
|**--list-item-drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|microsoft_graph_list_item_versions|versions|
|**--list-item-fields-id**|string|Read-only.|id2|id|
|**--workbook-id**|string|Read-only.|id3|id|
|**--workbook-application**|object|workbookApplication|microsoft_graph_workbook_application|application|
|**--workbook-comments**|array||comments|comments|
|**--workbook-functions**|object|workbookFunctions|functions|functions|
|**--workbook-names**|array|Represents a collection of workbook scoped named items (named ranges and constants). Read-only.|names|names|
|**--workbook-operations**|array|The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.|operations|operations|
|**--workbook-tables**|array|Represents a collection of tables associated with the workbook. Read-only.|tables|tables|
|**--workbook-worksheets**|array|Represents a collection of worksheets associated with the workbook. Read-only.|worksheets|worksheets|
|**--special-folder-name**|string|The unique identifier for this item in the /drive/special collection|microsoft_graph_special_folder_name|name|
|**--shared-owner**|object|identitySet|owner|owner|
|**--shared-scope**|string|Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.|scope|scope|
|**--shared-shared-by**|object|identitySet|shared_by|sharedBy|
|**--shared-shared-date-time**|date-time|The UTC date and time when the item was shared. Read-only.|shared_date_time|sharedDateTime|
|**--search-result-on-click-telemetry-url**|string|A callback URL that can be used to record telemetry information. The application should issue a GET on this URL if the user interacts with this item to improve the quality of results.|on_click_telemetry_url|onClickTelemetryUrl|
|**--remote-item-created-by**|object|identitySet|created_by|createdBy|
|**--remote-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_remote_item_created_date_time_created_date_time|createdDateTime|
|**--remote-item-file**|object|file|file|file|
|**--remote-item-file-system-info**|object|fileSystemInfo|microsoft_graph_file_system_info_file_system_info|fileSystemInfo|
|**--remote-item-folder**|object|folder|folder|folder|
|**--remote-item-id**|string|Unique identifier for the remote item in its drive. Read-only.|microsoft_graph_remote_item_id|id|
|**--remote-item-image**|object|image|microsoft_graph_image|image|
|**--remote-item-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--remote-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_remote_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--remote-item-name**|string|Optional. Filename of the remote item. Read-only.|microsoft_graph_remote_item_name|name|
|**--remote-item-package**|object|package|package|package|
|**--remote-item-parent-reference**|object|itemReference|parent_reference|parentReference|
|**--remote-item-shared**|object|shared|shared|shared|
|**--remote-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids3|sharepointIds|
|**--remote-item-size**|integer|Size of the remote item. Read-only.|integer_size|size|
|**--remote-item-special-folder**|object|specialFolder|special_folder|specialFolder|
|**--remote-item-video**|object|video|microsoft_graph_video|video|
|**--remote-item-web-dav-url**|string|DAV compatible URL for the item.|microsoft_graph_remote_item_web_dav_url_web_dav_url|webDavUrl|
|**--remote-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_remote_item_web_url|webUrl|
|**--pending-operations-pending-content-update-queued-date-time**|date-time|Date and time the pending binary operation was queued in UTC time. Read-only.|queued_date_time|queuedDateTime|
|**--package-type**|string|A string indicating the type of package. While oneNote is the only currently defined value, you should expect other package types to be returned and handle them accordingly.|type|type|
|**--folder-child-count**|integer|Number of children contained immediately within this container.|child_count|childCount|
|**--folder-view**|object|folderView|view|view|
|**--file-hashes**|object|hashes|hashes|hashes|
|**--file-mime-type**|string|The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.|mime_type|mimeType|
|**--file-processing-metadata**|boolean||processing_metadata|processingMetadata|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### files create-item

create-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-item|CreateItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
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
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### files create-shared-drive-item

create-shared-drive-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.sharedDriveItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-shared-drive-item|CreateSharedDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### files create-special

create-special a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-special|CreateSpecial|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
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
|**--audio**|object|audio|audio|audio|
|**--content**|byte-array|The content stream, if the item represents a file.|content|content|
|**--c-tag**|string|An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.|c_tag|cTag|
|**--file-system-info**|object|fileSystemInfo|file_system_info|fileSystemInfo|
|**--image**|object|image|image|image|
|**--location**|object|geoCoordinates|location|location|
|**--photo**|object|photo|photo|photo|
|**--publication**|object|publicationFacet|publication|publication|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--size**|integer|Size of the item in bytes. Read-only.|size|size|
|**--video**|object|video|video|video|
|**--web-dav-url**|string|WebDAV compatible URL for the item.|web_dav_url|webDavUrl|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id1|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|name1|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application1|application|
|**--list-item-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-item-created-by-application**|object|identity|application2|application|
|**--list-item-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-analytics**|object|itemAnalytics|microsoft_graph_item_analytics|analytics|
|**--list-item-drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|microsoft_graph_list_item_versions|versions|
|**--list-item-fields-id**|string|Read-only.|id2|id|
|**--workbook-id**|string|Read-only.|id3|id|
|**--workbook-application**|object|workbookApplication|microsoft_graph_workbook_application|application|
|**--workbook-comments**|array||comments|comments|
|**--workbook-functions**|object|workbookFunctions|functions|functions|
|**--workbook-names**|array|Represents a collection of workbook scoped named items (named ranges and constants). Read-only.|names|names|
|**--workbook-operations**|array|The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.|operations|operations|
|**--workbook-tables**|array|Represents a collection of tables associated with the workbook. Read-only.|tables|tables|
|**--workbook-worksheets**|array|Represents a collection of worksheets associated with the workbook. Read-only.|worksheets|worksheets|
|**--special-folder-name**|string|The unique identifier for this item in the /drive/special collection|microsoft_graph_special_folder_name|name|
|**--shared-owner**|object|identitySet|owner|owner|
|**--shared-scope**|string|Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.|scope|scope|
|**--shared-shared-by**|object|identitySet|shared_by|sharedBy|
|**--shared-shared-date-time**|date-time|The UTC date and time when the item was shared. Read-only.|shared_date_time|sharedDateTime|
|**--search-result-on-click-telemetry-url**|string|A callback URL that can be used to record telemetry information. The application should issue a GET on this URL if the user interacts with this item to improve the quality of results.|on_click_telemetry_url|onClickTelemetryUrl|
|**--remote-item-created-by**|object|identitySet|created_by|createdBy|
|**--remote-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_remote_item_created_date_time_created_date_time|createdDateTime|
|**--remote-item-file**|object|file|file|file|
|**--remote-item-file-system-info**|object|fileSystemInfo|microsoft_graph_file_system_info_file_system_info|fileSystemInfo|
|**--remote-item-folder**|object|folder|folder|folder|
|**--remote-item-id**|string|Unique identifier for the remote item in its drive. Read-only.|microsoft_graph_remote_item_id|id|
|**--remote-item-image**|object|image|microsoft_graph_image|image|
|**--remote-item-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--remote-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_remote_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--remote-item-name**|string|Optional. Filename of the remote item. Read-only.|microsoft_graph_remote_item_name|name|
|**--remote-item-package**|object|package|package|package|
|**--remote-item-parent-reference**|object|itemReference|parent_reference|parentReference|
|**--remote-item-shared**|object|shared|shared|shared|
|**--remote-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids3|sharepointIds|
|**--remote-item-size**|integer|Size of the remote item. Read-only.|integer_size|size|
|**--remote-item-special-folder**|object|specialFolder|special_folder|specialFolder|
|**--remote-item-video**|object|video|microsoft_graph_video|video|
|**--remote-item-web-dav-url**|string|DAV compatible URL for the item.|microsoft_graph_remote_item_web_dav_url_web_dav_url|webDavUrl|
|**--remote-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_remote_item_web_url|webUrl|
|**--pending-operations-pending-content-update-queued-date-time**|date-time|Date and time the pending binary operation was queued in UTC time. Read-only.|queued_date_time|queuedDateTime|
|**--package-type**|string|A string indicating the type of package. While oneNote is the only currently defined value, you should expect other package types to be returned and handle them accordingly.|type|type|
|**--folder-child-count**|integer|Number of children contained immediately within this container.|child_count|childCount|
|**--folder-view**|object|folderView|view|view|
|**--file-hashes**|object|hashes|hashes|hashes|
|**--file-mime-type**|string|The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.|mime_type|mimeType|
|**--file-processing-metadata**|boolean||processing_metadata|processingMetadata|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### files create-subscription

create-subscription a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-subscription|CreateSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.|client_state|clientState|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--encryption-certificate**|string|A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional. Required when includeResourceData is true.|encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string|A custom app-provided identifier to help identify the certificate needed to decrypt resource data. Optional.|encryption_certificate_id|encryptionCertificateId|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string|Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.|latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string|The URL of the endpoint that receives lifecycle notifications, including subscriptionRemoved and missed notifications. This URL must make use of the HTTPS protocol. Optional. Read more about how Outlook resources use lifecycle notifications.|lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

### files create-version

create-version a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-version|CreateVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### files delete

delete a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDrives|
|delete|DeleteDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--if-match**|string|ETag|if_match|If-Match|

### files get-activity-by-interval53-ee

get-activity-by-interval53-ee a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval53-ee|getActivitiesByInterval-53ee|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

### files get-activity-by-interval96-b0

get-activity-by-interval96-b0 a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval96-b0|getActivitiesByInterval-96b0|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|

### files get-analytic

get-analytic a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-analytic|GetAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-column

get-column a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-column|GetColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-column-link

get-column-link a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-column-link|GetColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-content-type

get-content-type a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-content-type|GetContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-drive

get-drive a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive|GetDrives|
|get-drive|GetDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-drive-item

get-drive-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item|GetDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-drive-item-content

get-drive-item-content a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item-content|GetDriveItemContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|

### files get-field

get-field a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-field|GetFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-following

get-following a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-following|GetFollowing|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-following-content

get-following-content a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-following-content|GetFollowingContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|

### files get-item

get-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-item-content

get-item-content a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item-content|GetItemsContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|

### files get-list

get-list a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list|GetList|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-list-item

get-list-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list-item|GetListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-permission

get-permission a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-permission|GetPermission|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-ref-analytic

get-ref-analytic a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-analytic|GetRefAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|

### files get-root

get-root a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-root|GetRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-root-content

get-root-content a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-root-content|GetRootContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|

### files get-shared-drive-item

get-shared-drive-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.sharedDriveItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shared-drive-item|GetSharedDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-site

get-site a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-site|GetSite|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-special

get-special a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-special|GetSpecial|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-special-content

get-special-content a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-special-content|GetSpecialContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|

### files get-subscription

get-subscription a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-subscription|GetSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files get-version

get-version a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-version|GetVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files grant

grant a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.permission|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|grant|grant|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--roles**|array||roles|roles|
|**--recipients**|array||recipients|recipients|

### files list-column

list-column a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-column|ListColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files list-column-link

list-column-link a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-column-link|ListColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files list-content-type

list-content-type a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-content-type|ListContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files list-drive

list-drive a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-drive|ListDrives|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files list-following

list-following a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-following|ListFollowing|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files list-item

list-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-item|ListItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files list-shared-drive-item

list-shared-drive-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.sharedDriveItem|

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

### files list-special

list-special a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-special|ListSpecial|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files list-subscription

list-subscription a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-subscription|ListSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files list-version

list-version a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-version|ListVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### files recent

recent a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|recent|recent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|

### files restore-version

restore-version a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore-version|restoreVersion|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|

### files search

search a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|search|search|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--q**|string||q|q|

### files set-drive-item-content

set-drive-item-content a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-drive-item-content|SetDriveItemContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--data**|binary|New media content.|data|data|

### files set-following-content

set-following-content a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-following-content|SetFollowingContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--data**|binary|New media content.|data|data|

### files set-item-content

set-item-content a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-item-content|SetItemsContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--data**|binary|New media content.|data|data|

### files set-ref-analytic

set-ref-analytic a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-analytic|SetRefAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### files set-root-content

set-root-content a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-root-content|SetRootContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--data**|binary|New media content.|data|data|

### files set-special-content

set-special-content a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-special-content|SetSpecialContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--data**|binary|New media content.|data|data|

### files shared-with-me

shared-with-me a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|shared-with-me|sharedWithMe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|

### files update-column

update-column a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-column|UpdateColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--id**|string|Read-only.|id|id|
|**--boolean**|dictionary|booleanColumn|boolean|boolean|
|**--calculated**|object|calculatedColumn|calculated|calculated|
|**--choice**|object|choiceColumn|choice|choice|
|**--column-group**|string|For site columns, the name of the group this column belongs to. Helps organize related columns.|column_group|columnGroup|
|**--date-time**|object|dateTimeColumn|date_time|dateTime|
|**--default-value**|object|defaultColumnValue|default_value|defaultValue|
|**--description**|string|The user-facing description of the column.|description|description|
|**--display-name**|string|The user-facing name of the column.|display_name|displayName|
|**--enforce-unique-values**|boolean|If true, no two list items may have the same value for this column.|enforce_unique_values|enforceUniqueValues|
|**--geolocation**|dictionary|geolocationColumn|geolocation|geolocation|
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

### files update-column-link

update-column-link a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-column-link|UpdateColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

### files update-content-type

update-content-type a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-content-type|UpdateContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
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

### files update-drive

update-drive a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-drive|UpdateDrives|
|update-drive|UpdateDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
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
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--list-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--list-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--list-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--list-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--list-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--list-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--list-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--list-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--list-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id1|driveId|
|**--list-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--list-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--list-parent-reference-name**|string|The name of the item being referenced. Read-only.|name1|name|
|**--list-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--list-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--list-parent-reference-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--list-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-last-modified-by-application**|object|identity|application1|application|
|**--list-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-created-by-application**|object|identity|application2|application|
|**--list-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list-list**|object|listInfo|list|list|
|**--list-sharepoint-ids**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--list-system**|dictionary|systemFacet|microsoft_graph_system_facet_system|system|
|**--list-columns**|array|The collection of field definitions for this list.|columns|columns|
|**--list-content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--list-drive**|object|drive|drive|drive|
|**--list-items**|array|All items contained in the list.|microsoft_graph_list_items|items|
|**--list-subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--quota-deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--quota-remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--quota-state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--quota-storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--quota-total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--quota-used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--owner-application**|object|identity|application3|application|
|**--owner-device**|object|identity|device3|device|
|**--owner-user**|object|identity|user3|user|

### files update-drive-item

update-drive-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-drive-item|UpdateDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
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
|**--audio**|object|audio|audio|audio|
|**--content**|byte-array|The content stream, if the item represents a file.|content|content|
|**--c-tag**|string|An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.|c_tag|cTag|
|**--file-system-info**|object|fileSystemInfo|file_system_info|fileSystemInfo|
|**--image**|object|image|image|image|
|**--location**|object|geoCoordinates|location|location|
|**--photo**|object|photo|photo|photo|
|**--publication**|object|publicationFacet|publication|publication|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--size**|integer|Size of the item in bytes. Read-only.|size|size|
|**--video**|object|video|video|video|
|**--web-dav-url**|string|WebDAV compatible URL for the item.|web_dav_url|webDavUrl|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|name1|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application1|application|
|**--list-item-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-item-created-by-application**|object|identity|application2|application|
|**--list-item-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-analytics**|object|itemAnalytics|microsoft_graph_item_analytics|analytics|
|**--list-item-drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|microsoft_graph_list_item_versions|versions|
|**--list-item-fields-id**|string|Read-only.|id2|id|
|**--workbook-id**|string|Read-only.|id3|id|
|**--workbook-application**|object|workbookApplication|microsoft_graph_workbook_application|application|
|**--workbook-comments**|array||comments|comments|
|**--workbook-functions**|object|workbookFunctions|functions|functions|
|**--workbook-names**|array|Represents a collection of workbook scoped named items (named ranges and constants). Read-only.|names|names|
|**--workbook-operations**|array|The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.|operations|operations|
|**--workbook-tables**|array|Represents a collection of tables associated with the workbook. Read-only.|tables|tables|
|**--workbook-worksheets**|array|Represents a collection of worksheets associated with the workbook. Read-only.|worksheets|worksheets|
|**--special-folder-name**|string|The unique identifier for this item in the /drive/special collection|microsoft_graph_special_folder_name|name|
|**--shared-owner**|object|identitySet|owner|owner|
|**--shared-scope**|string|Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.|scope|scope|
|**--shared-shared-by**|object|identitySet|shared_by|sharedBy|
|**--shared-shared-date-time**|date-time|The UTC date and time when the item was shared. Read-only.|shared_date_time|sharedDateTime|
|**--search-result-on-click-telemetry-url**|string|A callback URL that can be used to record telemetry information. The application should issue a GET on this URL if the user interacts with this item to improve the quality of results.|on_click_telemetry_url|onClickTelemetryUrl|
|**--remote-item-created-by**|object|identitySet|created_by|createdBy|
|**--remote-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_remote_item_created_date_time_created_date_time|createdDateTime|
|**--remote-item-file**|object|file|file|file|
|**--remote-item-file-system-info**|object|fileSystemInfo|microsoft_graph_file_system_info_file_system_info|fileSystemInfo|
|**--remote-item-folder**|object|folder|folder|folder|
|**--remote-item-id**|string|Unique identifier for the remote item in its drive. Read-only.|microsoft_graph_remote_item_id|id|
|**--remote-item-image**|object|image|microsoft_graph_image|image|
|**--remote-item-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--remote-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_remote_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--remote-item-name**|string|Optional. Filename of the remote item. Read-only.|microsoft_graph_remote_item_name|name|
|**--remote-item-package**|object|package|package|package|
|**--remote-item-parent-reference**|object|itemReference|parent_reference|parentReference|
|**--remote-item-shared**|object|shared|shared|shared|
|**--remote-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids3|sharepointIds|
|**--remote-item-size**|integer|Size of the remote item. Read-only.|integer_size|size|
|**--remote-item-special-folder**|object|specialFolder|special_folder|specialFolder|
|**--remote-item-video**|object|video|microsoft_graph_video|video|
|**--remote-item-web-dav-url**|string|DAV compatible URL for the item.|microsoft_graph_remote_item_web_dav_url_web_dav_url|webDavUrl|
|**--remote-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_remote_item_web_url|webUrl|
|**--pending-operations-pending-content-update-queued-date-time**|date-time|Date and time the pending binary operation was queued in UTC time. Read-only.|queued_date_time|queuedDateTime|
|**--package-type**|string|A string indicating the type of package. While oneNote is the only currently defined value, you should expect other package types to be returned and handle them accordingly.|type|type|
|**--folder-child-count**|integer|Number of children contained immediately within this container.|child_count|childCount|
|**--folder-view**|object|folderView|view|view|
|**--file-hashes**|object|hashes|hashes|hashes|
|**--file-mime-type**|string|The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.|mime_type|mimeType|
|**--file-processing-metadata**|boolean||processing_metadata|processingMetadata|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### files update-field

update-field a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-field|UpdateFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|

### files update-following

update-following a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-following|UpdateFollowing|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
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
|**--audio**|object|audio|audio|audio|
|**--content**|byte-array|The content stream, if the item represents a file.|content|content|
|**--c-tag**|string|An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.|c_tag|cTag|
|**--file-system-info**|object|fileSystemInfo|file_system_info|fileSystemInfo|
|**--image**|object|image|image|image|
|**--location**|object|geoCoordinates|location|location|
|**--photo**|object|photo|photo|photo|
|**--publication**|object|publicationFacet|publication|publication|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--size**|integer|Size of the item in bytes. Read-only.|size|size|
|**--video**|object|video|video|video|
|**--web-dav-url**|string|WebDAV compatible URL for the item.|web_dav_url|webDavUrl|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id1|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|name1|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application1|application|
|**--list-item-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-item-created-by-application**|object|identity|application2|application|
|**--list-item-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-analytics**|object|itemAnalytics|microsoft_graph_item_analytics|analytics|
|**--list-item-drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|microsoft_graph_list_item_versions|versions|
|**--list-item-fields-id**|string|Read-only.|id2|id|
|**--workbook-id**|string|Read-only.|id3|id|
|**--workbook-application**|object|workbookApplication|microsoft_graph_workbook_application|application|
|**--workbook-comments**|array||comments|comments|
|**--workbook-functions**|object|workbookFunctions|functions|functions|
|**--workbook-names**|array|Represents a collection of workbook scoped named items (named ranges and constants). Read-only.|names|names|
|**--workbook-operations**|array|The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.|operations|operations|
|**--workbook-tables**|array|Represents a collection of tables associated with the workbook. Read-only.|tables|tables|
|**--workbook-worksheets**|array|Represents a collection of worksheets associated with the workbook. Read-only.|worksheets|worksheets|
|**--special-folder-name**|string|The unique identifier for this item in the /drive/special collection|microsoft_graph_special_folder_name|name|
|**--shared-owner**|object|identitySet|owner|owner|
|**--shared-scope**|string|Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.|scope|scope|
|**--shared-shared-by**|object|identitySet|shared_by|sharedBy|
|**--shared-shared-date-time**|date-time|The UTC date and time when the item was shared. Read-only.|shared_date_time|sharedDateTime|
|**--search-result-on-click-telemetry-url**|string|A callback URL that can be used to record telemetry information. The application should issue a GET on this URL if the user interacts with this item to improve the quality of results.|on_click_telemetry_url|onClickTelemetryUrl|
|**--remote-item-created-by**|object|identitySet|created_by|createdBy|
|**--remote-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_remote_item_created_date_time_created_date_time|createdDateTime|
|**--remote-item-file**|object|file|file|file|
|**--remote-item-file-system-info**|object|fileSystemInfo|microsoft_graph_file_system_info_file_system_info|fileSystemInfo|
|**--remote-item-folder**|object|folder|folder|folder|
|**--remote-item-id**|string|Unique identifier for the remote item in its drive. Read-only.|microsoft_graph_remote_item_id|id|
|**--remote-item-image**|object|image|microsoft_graph_image|image|
|**--remote-item-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--remote-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_remote_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--remote-item-name**|string|Optional. Filename of the remote item. Read-only.|microsoft_graph_remote_item_name|name|
|**--remote-item-package**|object|package|package|package|
|**--remote-item-parent-reference**|object|itemReference|parent_reference|parentReference|
|**--remote-item-shared**|object|shared|shared|shared|
|**--remote-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids3|sharepointIds|
|**--remote-item-size**|integer|Size of the remote item. Read-only.|integer_size|size|
|**--remote-item-special-folder**|object|specialFolder|special_folder|specialFolder|
|**--remote-item-video**|object|video|microsoft_graph_video|video|
|**--remote-item-web-dav-url**|string|DAV compatible URL for the item.|microsoft_graph_remote_item_web_dav_url_web_dav_url|webDavUrl|
|**--remote-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_remote_item_web_url|webUrl|
|**--pending-operations-pending-content-update-queued-date-time**|date-time|Date and time the pending binary operation was queued in UTC time. Read-only.|queued_date_time|queuedDateTime|
|**--package-type**|string|A string indicating the type of package. While oneNote is the only currently defined value, you should expect other package types to be returned and handle them accordingly.|type|type|
|**--folder-child-count**|integer|Number of children contained immediately within this container.|child_count|childCount|
|**--folder-view**|object|folderView|view|view|
|**--file-hashes**|object|hashes|hashes|hashes|
|**--file-mime-type**|string|The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.|mime_type|mimeType|
|**--file-processing-metadata**|boolean||processing_metadata|processingMetadata|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### files update-item

update-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
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
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### files update-list

update-list a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-list|UpdateList|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
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
|**--system**|dictionary|systemFacet|system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--items**|array|All items contained in the list.|items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|

### files update-list-item

update-list-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-list-item|UpdateListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
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
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### files update-permission

update-permission a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-permission|UpdatePermission|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New navigation property values|body|body|

### files update-root

update-root a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-root|UpdateRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
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
|**--audio**|object|audio|audio|audio|
|**--content**|byte-array|The content stream, if the item represents a file.|content|content|
|**--c-tag**|string|An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.|c_tag|cTag|
|**--file-system-info**|object|fileSystemInfo|file_system_info|fileSystemInfo|
|**--image**|object|image|image|image|
|**--location**|object|geoCoordinates|location|location|
|**--photo**|object|photo|photo|photo|
|**--publication**|object|publicationFacet|publication|publication|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--size**|integer|Size of the item in bytes. Read-only.|size|size|
|**--video**|object|video|video|video|
|**--web-dav-url**|string|WebDAV compatible URL for the item.|web_dav_url|webDavUrl|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|name1|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application1|application|
|**--list-item-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-item-created-by-application**|object|identity|application2|application|
|**--list-item-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-analytics**|object|itemAnalytics|microsoft_graph_item_analytics|analytics|
|**--list-item-drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|microsoft_graph_list_item_versions|versions|
|**--list-item-fields-id**|string|Read-only.|id2|id|
|**--workbook-id**|string|Read-only.|id3|id|
|**--workbook-application**|object|workbookApplication|microsoft_graph_workbook_application|application|
|**--workbook-comments**|array||comments|comments|
|**--workbook-functions**|object|workbookFunctions|functions|functions|
|**--workbook-names**|array|Represents a collection of workbook scoped named items (named ranges and constants). Read-only.|names|names|
|**--workbook-operations**|array|The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.|operations|operations|
|**--workbook-tables**|array|Represents a collection of tables associated with the workbook. Read-only.|tables|tables|
|**--workbook-worksheets**|array|Represents a collection of worksheets associated with the workbook. Read-only.|worksheets|worksheets|
|**--special-folder-name**|string|The unique identifier for this item in the /drive/special collection|microsoft_graph_special_folder_name|name|
|**--shared-owner**|object|identitySet|owner|owner|
|**--shared-scope**|string|Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.|scope|scope|
|**--shared-shared-by**|object|identitySet|shared_by|sharedBy|
|**--shared-shared-date-time**|date-time|The UTC date and time when the item was shared. Read-only.|shared_date_time|sharedDateTime|
|**--search-result-on-click-telemetry-url**|string|A callback URL that can be used to record telemetry information. The application should issue a GET on this URL if the user interacts with this item to improve the quality of results.|on_click_telemetry_url|onClickTelemetryUrl|
|**--remote-item-created-by**|object|identitySet|created_by|createdBy|
|**--remote-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_remote_item_created_date_time_created_date_time|createdDateTime|
|**--remote-item-file**|object|file|file|file|
|**--remote-item-file-system-info**|object|fileSystemInfo|microsoft_graph_file_system_info_file_system_info|fileSystemInfo|
|**--remote-item-folder**|object|folder|folder|folder|
|**--remote-item-id**|string|Unique identifier for the remote item in its drive. Read-only.|microsoft_graph_remote_item_id|id|
|**--remote-item-image**|object|image|microsoft_graph_image|image|
|**--remote-item-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--remote-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_remote_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--remote-item-name**|string|Optional. Filename of the remote item. Read-only.|microsoft_graph_remote_item_name|name|
|**--remote-item-package**|object|package|package|package|
|**--remote-item-parent-reference**|object|itemReference|parent_reference|parentReference|
|**--remote-item-shared**|object|shared|shared|shared|
|**--remote-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids3|sharepointIds|
|**--remote-item-size**|integer|Size of the remote item. Read-only.|integer_size|size|
|**--remote-item-special-folder**|object|specialFolder|special_folder|specialFolder|
|**--remote-item-video**|object|video|microsoft_graph_video|video|
|**--remote-item-web-dav-url**|string|DAV compatible URL for the item.|microsoft_graph_remote_item_web_dav_url_web_dav_url|webDavUrl|
|**--remote-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_remote_item_web_url|webUrl|
|**--pending-operations-pending-content-update-queued-date-time**|date-time|Date and time the pending binary operation was queued in UTC time. Read-only.|queued_date_time|queuedDateTime|
|**--package-type**|string|A string indicating the type of package. While oneNote is the only currently defined value, you should expect other package types to be returned and handle them accordingly.|type|type|
|**--folder-child-count**|integer|Number of children contained immediately within this container.|child_count|childCount|
|**--folder-view**|object|folderView|view|view|
|**--file-hashes**|object|hashes|hashes|hashes|
|**--file-mime-type**|string|The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.|mime_type|mimeType|
|**--file-processing-metadata**|boolean||processing_metadata|processingMetadata|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### files update-shared-drive-item

update-shared-drive-item a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.sharedDriveItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shared-drive-item|UpdateSharedDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New property values|body|body|

### files update-site

update-site a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-site|UpdateSite|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
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
|**--display-name**|string|The full title for the site. Read-only.|display_name|displayName|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--columns**|array|The collection of column definitions reusable across lists under this site.|columns|columns|
|**--content-types**|array|The collection of content types defined for this site.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|The collection of drives (document libraries) under this site.|drives|drives|
|**--items**|array|Used to address any item contained in this site. This collection cannot be enumerated.|items|items|
|**--lists**|array|The collection of lists under this site.|lists|lists|
|**--sites**|array|The collection of the sub-sites under this site.|sites|sites|
|**--onenote-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--onenote-notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--onenote-operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--onenote-pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|pages|pages|
|**--onenote-resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--onenote-section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--onenote-sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--site-collection-data-location-code**|string|The geographic region code for where this site collection resides. Read-only.|data_location_code|dataLocationCode|
|**--site-collection-hostname**|string|The hostname for the site collection. Read-only.|hostname|hostname|
|**--site-collection-root**|dictionary|root|microsoft_graph_root|root|
|**--error-code**|string||code|code|
|**--error-details**|array||details|details|
|**--error-inner-error**|object|publicInnerError|inner_error|innerError|
|**--error-message**|string||message|message|
|**--error-target**|string||target|target|

### files update-special

update-special a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|drives|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-special|UpdateSpecial|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
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
|**--audio**|object|audio|audio|audio|
|**--content**|byte-array|The content stream, if the item represents a file.|content|content|
|**--c-tag**|string|An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.|c_tag|cTag|
|**--file-system-info**|object|fileSystemInfo|file_system_info|fileSystemInfo|
|**--image**|object|image|image|image|
|**--location**|object|geoCoordinates|location|location|
|**--photo**|object|photo|photo|photo|
|**--publication**|object|publicationFacet|publication|publication|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--size**|integer|Size of the item in bytes. Read-only.|size|size|
|**--video**|object|video|video|video|
|**--web-dav-url**|string|WebDAV compatible URL for the item.|web_dav_url|webDavUrl|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id1|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|name1|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application1|application|
|**--list-item-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-item-created-by-application**|object|identity|application2|application|
|**--list-item-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-analytics**|object|itemAnalytics|microsoft_graph_item_analytics|analytics|
|**--list-item-drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|microsoft_graph_list_item_versions|versions|
|**--list-item-fields-id**|string|Read-only.|id2|id|
|**--workbook-id**|string|Read-only.|id3|id|
|**--workbook-application**|object|workbookApplication|microsoft_graph_workbook_application|application|
|**--workbook-comments**|array||comments|comments|
|**--workbook-functions**|object|workbookFunctions|functions|functions|
|**--workbook-names**|array|Represents a collection of workbook scoped named items (named ranges and constants). Read-only.|names|names|
|**--workbook-operations**|array|The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.|operations|operations|
|**--workbook-tables**|array|Represents a collection of tables associated with the workbook. Read-only.|tables|tables|
|**--workbook-worksheets**|array|Represents a collection of worksheets associated with the workbook. Read-only.|worksheets|worksheets|
|**--special-folder-name**|string|The unique identifier for this item in the /drive/special collection|microsoft_graph_special_folder_name|name|
|**--shared-owner**|object|identitySet|owner|owner|
|**--shared-scope**|string|Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.|scope|scope|
|**--shared-shared-by**|object|identitySet|shared_by|sharedBy|
|**--shared-shared-date-time**|date-time|The UTC date and time when the item was shared. Read-only.|shared_date_time|sharedDateTime|
|**--search-result-on-click-telemetry-url**|string|A callback URL that can be used to record telemetry information. The application should issue a GET on this URL if the user interacts with this item to improve the quality of results.|on_click_telemetry_url|onClickTelemetryUrl|
|**--remote-item-created-by**|object|identitySet|created_by|createdBy|
|**--remote-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_remote_item_created_date_time_created_date_time|createdDateTime|
|**--remote-item-file**|object|file|file|file|
|**--remote-item-file-system-info**|object|fileSystemInfo|microsoft_graph_file_system_info_file_system_info|fileSystemInfo|
|**--remote-item-folder**|object|folder|folder|folder|
|**--remote-item-id**|string|Unique identifier for the remote item in its drive. Read-only.|microsoft_graph_remote_item_id|id|
|**--remote-item-image**|object|image|microsoft_graph_image|image|
|**--remote-item-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--remote-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_remote_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--remote-item-name**|string|Optional. Filename of the remote item. Read-only.|microsoft_graph_remote_item_name|name|
|**--remote-item-package**|object|package|package|package|
|**--remote-item-parent-reference**|object|itemReference|parent_reference|parentReference|
|**--remote-item-shared**|object|shared|shared|shared|
|**--remote-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids3|sharepointIds|
|**--remote-item-size**|integer|Size of the remote item. Read-only.|integer_size|size|
|**--remote-item-special-folder**|object|specialFolder|special_folder|specialFolder|
|**--remote-item-video**|object|video|microsoft_graph_video|video|
|**--remote-item-web-dav-url**|string|DAV compatible URL for the item.|microsoft_graph_remote_item_web_dav_url_web_dav_url|webDavUrl|
|**--remote-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_remote_item_web_url|webUrl|
|**--pending-operations-pending-content-update-queued-date-time**|date-time|Date and time the pending binary operation was queued in UTC time. Read-only.|queued_date_time|queuedDateTime|
|**--package-type**|string|A string indicating the type of package. While oneNote is the only currently defined value, you should expect other package types to be returned and handle them accordingly.|type|type|
|**--folder-child-count**|integer|Number of children contained immediately within this container.|child_count|childCount|
|**--folder-view**|object|folderView|view|view|
|**--file-hashes**|object|hashes|hashes|hashes|
|**--file-mime-type**|string|The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.|mime_type|mimeType|
|**--file-processing-metadata**|boolean||processing_metadata|processingMetadata|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### files update-subscription

update-subscription a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.list|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-subscription|UpdateSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--id**|string|Read-only.|id|id|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.|client_state|clientState|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--encryption-certificate**|string|A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional. Required when includeResourceData is true.|encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string|A custom app-provided identifier to help identify the certificate needed to decrypt resource data. Optional.|encryption_certificate_id|encryptionCertificateId|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string|Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.|latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string|The URL of the endpoint that receives lifecycle notifications, including subscriptionRemoved and missed notifications. This URL must make use of the HTTPS protocol. Optional. Read more about how Outlook resources use lifecycle notifications.|lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

### files update-version

update-version a files.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|files|shares.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-version|UpdateVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|
