# Azure CLI Module Creation Report

### sites add

add a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|add|add|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

### sites copy-notebook

copy-notebook a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites copy-to-notebook

copy-to-notebook a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.onenote.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites copy-to-section

copy-to-section a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites copy-to-section-group

copy-to-section-group a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.onenote.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites create-column

create-column a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-column|CreateColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
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

### sites create-column-link

create-column-link a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-column-link|CreateColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

### sites create-content-type

create-content-type a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-content-type|CreateContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
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
|**--inherited-from-site-id**|string||microsoft_graph_item_reference_site_id|siteId|

### sites create-drive

create-drive a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-drive|CreateDrives|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
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
|**--parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
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
|**--list**|object|list|list|list|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--quota-deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--quota-remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--quota-state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--quota-storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--quota-total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--quota-used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--owner-application**|object|identity|application1|application|
|**--owner-device**|object|identity|device1|device|
|**--owner-user**|object|identity|user1|user|

### sites create-item

create-item a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-item|CreateItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
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
|**--parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
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

### sites create-list

create-list a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-list|CreateLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
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
|**--parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
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

### sites create-ref-followed-site

create-ref-followed-site a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-followed-site|CreateRefFollowedSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### sites create-site

create-site a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-site|CreateSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
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
|**--parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
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

### sites create-subscription

create-subscription a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-subscription|CreateSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--id**|string|Read-only.|id|id|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.|client_state|clientState|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--encryption-certificate**|string|A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional. Required when includeResourceData is true.|encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string|A custom app-provided identifier to help identify the certificate needed to decrypt resource data. Optional.|encryption_certificate_id|encryptionCertificateId|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string||latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string||lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

### sites create-version

create-version a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-version|CreateVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### sites delete

delete a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--if-match**|string|ETag|if_match|If-Match|

### sites get-activity-by-interval53-ee

get-activity-by-interval53-ee a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval53-ee|getActivitiesByInterval-53ee|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

### sites get-activity-by-interval96-b0

get-activity-by-interval96-b0 a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval96-b0|getActivitiesByInterval-96b0|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|

### sites get-analytic

get-analytic a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-analytic|GetAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-by-path

get-by-path a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-path|getByPath|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--path**|string||path|path|

### sites get-column

get-column a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-column|GetColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-column-link

get-column-link a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-column-link|GetColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-content-type

get-content-type a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-content-type|GetContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-drive

get-drive a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive|GetDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-drive-item

get-drive-item a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item|GetDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-field

get-field a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-field|GetFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-item

get-item a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-item|GetItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-list

get-list a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list|GetLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-notebook-from-web-url

get-notebook-from-web-url a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-notebook-from-web-url|getNotebookFromWebUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--web-url**|string||web_url|webUrl|

### sites get-recent-notebook

get-recent-notebook a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-recent-notebook|getRecentNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--include-personal-notebooks**|boolean||include_personal_notebooks|includePersonalNotebooks|

### sites get-ref-analytic

get-ref-analytic a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-analytic|GetRefAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|

### sites get-site

get-site a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-site|GetSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--site-id1**|string|key: id of site|site_id1|site-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-subscription

get-subscription a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-subscription|GetSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites get-version

get-version a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-version|GetVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites list-column

list-column a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-column|ListColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites list-column-link

list-column-link a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-column-link|ListColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites list-content-type

list-content-type a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-content-type|ListContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites list-drive

list-drive a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-drive|ListDrives|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites list-followed-site

list-followed-site a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-followed-site|ListFollowedSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites list-item

list-item a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-item|ListItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites list-list

list-list a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-list|ListLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites list-ref-followed-site

list-ref-followed-site a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-followed-site|ListRefFollowedSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### sites list-site

list-site a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-site|ListSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites list-subscription

list-subscription a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-subscription|ListSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites list-version

list-version a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-version|ListVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites onenote-patch-content

onenote-patch-content a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### sites preview

preview a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|preview|preview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### sites remove

remove a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remove|remove|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

### sites restore-version

restore-version a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore-version|restoreVersion|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|

### sites set-ref-analytic

set-ref-analytic a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-analytic|SetRefAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### sites update-column

update-column a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-column|UpdateColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
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

### sites update-column-link

update-column-link a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-column-link|UpdateColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

### sites update-content-type

update-content-type a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-content-type|UpdateContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
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
|**--inherited-from-site-id**|string||microsoft_graph_item_reference_site_id|siteId|

### sites update-drive

update-drive a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-drive|UpdateDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
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
|**--parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
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
|**--list**|object|list|list|list|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--quota-deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--quota-remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--quota-state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--quota-storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--quota-total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--quota-used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--owner-application**|object|identity|application1|application|
|**--owner-device**|object|identity|device1|device|
|**--owner-user**|object|identity|user1|user|

### sites update-drive-item

update-drive-item a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-drive-item|UpdateDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--body**|object|New navigation property values|body|body|

### sites update-field

update-field a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-field|UpdateFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|

### sites update-item

update-item a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-item|UpdateItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
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
|**--parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
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

### sites update-list

update-list a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-list|UpdateLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
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
|**--parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
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

### sites update-site

update-site a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-site|UpdateSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--site-id1**|string|key: id of site|site_id1|site-id1|
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
|**--parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
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

### sites update-subscription

update-subscription a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-subscription|UpdateSubscriptions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
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
|**--latest-supported-tls-version**|string||latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string||lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

### sites update-version

update-version a sites.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-version|UpdateVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|
