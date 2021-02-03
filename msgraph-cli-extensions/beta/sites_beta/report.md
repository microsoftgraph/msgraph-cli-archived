# Azure CLI Module Creation Report

### sites group create

create a sites group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--pages**|array||pages|pages|
|**--sites**|array|The collection of the sub-sites under this site.|sites|sites|
|**--onenote-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--onenote-notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--onenote-operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--onenote-pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|microsoft_graph_onenote_pages|pages|
|**--onenote-resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--onenote-section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--onenote-sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--site-collection-data-location-code**|string|The geographic region code for where this site collection resides. Read-only.|data_location_code|dataLocationCode|
|**--site-collection-hostname**|string|The hostname for the site collection. Read-only.|hostname|hostname|
|**--site-collection-root**|dictionary|root|microsoft_graph_root|root|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### sites group delete

delete a sites group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--if-match**|string|ETag|if_match|If-Match|

### sites group get

get a sites group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites group list

list a sites group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites group update

update a sites group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
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
|**--pages**|array||pages|pages|
|**--sites**|array|The collection of the sub-sites under this site.|sites|sites|
|**--onenote-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--onenote-notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--onenote-operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--onenote-pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|microsoft_graph_onenote_pages|pages|
|**--onenote-resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--onenote-section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--onenote-sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--site-collection-data-location-code**|string|The geographic region code for where this site collection resides. Read-only.|data_location_code|dataLocationCode|
|**--site-collection-hostname**|string|The hostname for the site collection. Read-only.|hostname|hostname|
|**--site-collection-root**|dictionary|root|microsoft_graph_root|root|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### sites site add

add a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|add|add|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

### sites site create

create a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateSites|

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
|**--pages**|array||pages|pages|
|**--sites**|array|The collection of the sub-sites under this site.|sites|sites|
|**--onenote-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--onenote-notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--onenote-operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--onenote-pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|microsoft_graph_onenote_pages|pages|
|**--onenote-resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--onenote-section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--onenote-sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--site-collection-data-location-code**|string|The geographic region code for where this site collection resides. Read-only.|data_location_code|dataLocationCode|
|**--site-collection-hostname**|string|The hostname for the site collection. Read-only.|hostname|hostname|
|**--site-collection-root**|dictionary|root|microsoft_graph_root|root|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### sites site create-column

create-column a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-column|CreateColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
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

### sites site create-content-type

create-content-type a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-content-type|CreateContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
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

### sites site create-drive

create-drive a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

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
|**--activities**|array||activities|activities|
|**--bundles**|array||bundles|bundles|
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

### sites site create-list

create-list a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

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
|**--activities**|array||activities|activities|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--items**|array|All items contained in the list.|items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|

### sites site create-page

create-page a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

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
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--page-layout-type**|string||page_layout_type|pageLayoutType|
|**--publishing-state**|object|publicationFacet|publishing_state|publishingState|
|**--title**|string||title|title|
|**--web-parts**|array||web_parts|webParts|

### sites site delete

delete a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteColumns|
|delete|DeleteContentTypes|
|delete|DeleteDrives|
|delete|DeleteLists|
|delete|DeletePages|
|delete|DeleteSites|
|delete|DeleteRefAnalytics|
|delete|DeleteDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--site-page-id**|string|key: id of sitePage|site_page_id|sitePage-id|
|**--site-id1**|string|key: id of site|site_id1|site-id1|
|**--if-match**|string|ETag|if_match|If-Match|

### sites site delta

delta a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### sites site get

get a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--site-id1**|string|key: id of site|site_id1|site-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site get-activity-by-interval

get-activity-by-interval a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval|getActivitiesByInterval|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

### sites site get-analytic

get-analytic a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-analytic|GetAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site get-by-path

get-by-path a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-path|getByPath|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--path**|string||path|path|

### sites site get-column

get-column a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-column|GetColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site get-content-type

get-content-type a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-content-type|GetContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site get-drive

get-drive a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive|GetDrives|
|get-drive|GetDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site get-list

get-list a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

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

### sites site get-page

get-page a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--site-page-id**|string|key: id of sitePage|site_page_id|sitePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site get-ref-analytic

get-ref-analytic a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-analytic|GetRefAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|

### sites site list

list a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site list-column

list-column a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-column|ListColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site list-content-type

list-content-type a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-content-type|ListContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site list-drive

list-drive a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

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

### sites site list-list

list-list a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

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

### sites site list-page

list-page a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site remove

remove a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remove|remove|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--value**|array||value|value|

### sites site set-ref-analytic

set-ref-analytic a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-analytic|SetRefAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### sites site update

update a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSites|

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
|**--pages**|array||pages|pages|
|**--sites**|array|The collection of the sub-sites under this site.|sites|sites|
|**--onenote-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--onenote-notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--onenote-operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--onenote-pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|microsoft_graph_onenote_pages|pages|
|**--onenote-resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--onenote-section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--onenote-sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--site-collection-data-location-code**|string|The geographic region code for where this site collection resides. Read-only.|data_location_code|dataLocationCode|
|**--site-collection-hostname**|string|The hostname for the site collection. Read-only.|hostname|hostname|
|**--site-collection-root**|dictionary|root|microsoft_graph_root|root|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### sites site update-column

update-column a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-column|UpdateColumns|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
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

### sites site update-content-type

update-content-type a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-content-type|UpdateContentTypes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
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

### sites site update-drive

update-drive a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-drive|UpdateDrives|
|update-drive|UpdateDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
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
|**--activities**|array||activities|activities|
|**--bundles**|array||bundles|bundles|
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

### sites site update-list

update-list a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

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
|**--activities**|array||activities|activities|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--items**|array|All items contained in the list.|items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|

### sites site update-page

update-page a sites site.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-page|UpdatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--site-page-id**|string|key: id of sitePage|site_page_id|sitePage-id|
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
|**--page-layout-type**|string||page_layout_type|pageLayoutType|
|**--publishing-state**|object|publicationFacet|publishing_state|publishingState|
|**--title**|string||title|title|
|**--web-parts**|array||web_parts|webParts|

### sites site-content-type create-column-link

create-column-link a sites site-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-content-type|sites.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-column-link|CreateColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

### sites site-content-type delete

delete a sites site-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-content-type|sites.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--if-match**|string|ETag|if_match|If-Match|

### sites site-content-type get-column-link

get-column-link a sites site-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-content-type|sites.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-column-link|GetColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-content-type list-column-link

list-column-link a sites site-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-content-type|sites.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-column-link|ListColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-content-type update-column-link

update-column-link a sites site-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-content-type|sites.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-column-link|UpdateColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

### sites site-list create-activity

create-activity a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity|CreateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--id**|string|Read-only.|id|id|
|**--times**|object|itemActivityTimeSet|times|times|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application|application|
|**--list-item-last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--list-item-created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--list-item-created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--list-item-activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--list-item-analytics**|object|itemAnalytics|analytics|analytics|
|**--list-item-drive-item**|object|driveItem|microsoft_graph_drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|versions|versions|
|**--list-item-fields-id**|string|Read-only.|id1|id|
|**--actor-application**|object|identity|application1|application|
|**--actor-device**|object|identity|device1|device|
|**--actor-user**|object|identity|user1|user|
|**--action-comment**|object|commentAction|comment|comment|
|**--action-create**|dictionary|createAction|create|create|
|**--action-delete**|object|deleteAction|delete|delete|
|**--action-edit**|dictionary|editAction|edit|edit|
|**--action-mention**|object|mentionAction|mention|mention|
|**--action-move**|object|moveAction|move|move|
|**--action-rename**|object|renameAction|rename|rename|
|**--action-restore**|dictionary|restoreAction|restore|restore|
|**--action-share**|object|shareAction|share|share|
|**--action-version**|object|versionAction|version|version|

### sites site-list create-column

create-column a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list create-content-type

create-content-type a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list create-item

create-item a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### sites site-list create-subscription

create-subscription a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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
|**--include-properties**|boolean||include_properties|includeProperties|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string|Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.|latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string|The URL of the endpoint that receives lifecycle notifications, including subscriptionRemoved and missed notifications. This URL must make use of the HTTPS protocol. Optional. Read more about how Outlook resources use lifecycle notifications.|lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

### sites site-list delete

delete a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteActivities|
|delete|DeleteColumns|
|delete|DeleteContentTypes|
|delete|DeleteItems|
|delete|DeleteSubscriptions|
|delete|DeleteDrive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--if-match**|string|ETag|if_match|If-Match|

### sites site-list get-activity

get-activity a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity|GetActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list get-column

get-column a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list get-content-type

get-content-type a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list get-drive

get-drive a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list get-item

get-item a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list get-subscription

get-subscription a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list list-activity

list-activity a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity|ListActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list list-column

list-column a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list list-content-type

list-content-type a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list list-item

list-item a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list list-subscription

list-subscription a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list update-activity

update-activity a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-activity|UpdateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--id**|string|Read-only.|id|id|
|**--times**|object|itemActivityTimeSet|times|times|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application|application|
|**--list-item-last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--list-item-created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--list-item-created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--list-item-activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--list-item-analytics**|object|itemAnalytics|analytics|analytics|
|**--list-item-drive-item**|object|driveItem|microsoft_graph_drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|versions|versions|
|**--list-item-fields-id**|string|Read-only.|id1|id|
|**--actor-application**|object|identity|application1|application|
|**--actor-device**|object|identity|device1|device|
|**--actor-user**|object|identity|user1|user|
|**--action-comment**|object|commentAction|comment|comment|
|**--action-create**|dictionary|createAction|create|create|
|**--action-delete**|object|deleteAction|delete|delete|
|**--action-edit**|dictionary|editAction|edit|edit|
|**--action-mention**|object|mentionAction|mention|mention|
|**--action-move**|object|moveAction|move|move|
|**--action-rename**|object|renameAction|rename|rename|
|**--action-restore**|dictionary|restoreAction|restore|restore|
|**--action-share**|object|shareAction|share|share|
|**--action-version**|object|versionAction|version|version|

### sites site-list update-column

update-column a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list update-content-type

update-content-type a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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

### sites site-list update-drive

update-drive a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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
|**--activities**|array||activities|activities|
|**--bundles**|array||bundles|bundles|
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

### sites site-list update-item

update-item a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### sites site-list update-subscription

update-subscription a sites site-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list|sites.lists|

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
|**--include-properties**|boolean||include_properties|includeProperties|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string|Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.|latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string|The URL of the endpoint that receives lifecycle notifications, including subscriptionRemoved and missed notifications. This URL must make use of the HTTPS protocol. Optional. Read more about how Outlook resources use lifecycle notifications.|lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

### sites site-list-activity delete

delete a sites site-list-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity|sites.lists.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDriveItem|
|delete|DeleteListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--if-match**|string|ETag|if_match|If-Match|

### sites site-list-activity get-drive-item

get-drive-item a sites site-list-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity|sites.lists.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item|GetDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-activity get-drive-item-content

get-drive-item-content a sites site-list-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity|sites.lists.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item-content|GetDriveItemContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|

### sites site-list-activity get-list-item

get-list-item a sites site-list-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity|sites.lists.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list-item|GetListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-activity set-drive-item-content

set-drive-item-content a sites site-list-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity|sites.lists.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-drive-item-content|SetDriveItemContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--data**|binary|New media content.|data|data|

### sites site-list-activity update-drive-item

update-drive-item a sites site-list-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity|sites.lists.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-drive-item|UpdateDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
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
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
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
|**--list-item-parent-reference-site-id**|string||site_id1|siteId|
|**--list-item-last-modified-by-application**|object|identity|application1|application|
|**--list-item-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-item-created-by-application**|object|identity|application2|application|
|**--list-item-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-activities**|array|The list of recent activities that took place on this item.|microsoft_graph_list_item_activities|activities|
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
|**--bundle-album**|object|album|album|album|
|**--bundle-child-count**|integer||integer_child_count|childCount|

### sites site-list-activity update-list-item

update-list-item a sites site-list-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity|sites.lists.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-list-item|UpdateListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
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
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### sites site-list-activity-list-item create-activity

create-activity a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity|CreateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--id**|string|Read-only.|id|id|
|**--times**|object|itemActivityTimeSet|times|times|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application|application|
|**--list-item-last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--list-item-created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--list-item-created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--list-item-activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--list-item-analytics**|object|itemAnalytics|analytics|analytics|
|**--list-item-drive-item**|object|driveItem|microsoft_graph_drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|versions|versions|
|**--list-item-fields-id**|string|Read-only.|id1|id|
|**--actor-application**|object|identity|application1|application|
|**--actor-device**|object|identity|device1|device|
|**--actor-user**|object|identity|user1|user|
|**--action-comment**|object|commentAction|comment|comment|
|**--action-create**|dictionary|createAction|create|create|
|**--action-delete**|object|deleteAction|delete|delete|
|**--action-edit**|dictionary|editAction|edit|edit|
|**--action-mention**|object|mentionAction|mention|mention|
|**--action-move**|object|moveAction|move|move|
|**--action-rename**|object|renameAction|rename|rename|
|**--action-restore**|dictionary|restoreAction|restore|restore|
|**--action-share**|object|shareAction|share|share|
|**--action-version**|object|versionAction|version|version|

### sites site-list-activity-list-item create-link

create-link a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-link|createLink|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--type**|string||type|type|
|**--scope**|string||scope|scope|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--password**|string||password|password|
|**--recipients**|array||recipients|recipients|

### sites site-list-activity-list-item create-version

create-version a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-version|CreateVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### sites site-list-activity-list-item delete

delete a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteActivities|
|delete|DeleteVersions|
|delete|DeleteRefAnalytics|
|delete|DeleteDriveItem|
|delete|DeleteFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--item-activity-old-id1**|string|key: id of itemActivityOLD|item_activity_old_id1|itemActivityOLD-id1|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--if-match**|string|ETag|if_match|If-Match|

### sites site-list-activity-list-item get-activity

get-activity a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity|GetActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--item-activity-old-id1**|string|key: id of itemActivityOLD|item_activity_old_id1|itemActivityOLD-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-activity-list-item get-activity-by-interval

get-activity-by-interval a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval|getActivitiesByInterval|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

### sites site-list-activity-list-item get-analytic

get-analytic a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-analytic|GetAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-activity-list-item get-drive-item

get-drive-item a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item|GetDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-activity-list-item get-drive-item-content

get-drive-item-content a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item-content|GetDriveItemContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|

### sites site-list-activity-list-item get-field

get-field a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-field|GetFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-activity-list-item get-ref-analytic

get-ref-analytic a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-analytic|GetRefAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|

### sites site-list-activity-list-item get-version

get-version a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-version|GetVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-activity-list-item list-activity

list-activity a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity|ListActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-activity-list-item list-version

list-version a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-version|ListVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-activity-list-item set-drive-item-content

set-drive-item-content a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-drive-item-content|SetDriveItemContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--data**|binary|New media content.|data|data|

### sites site-list-activity-list-item set-ref-analytic

set-ref-analytic a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-analytic|SetRefAnalytics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### sites site-list-activity-list-item update-activity

update-activity a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-activity|UpdateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--item-activity-old-id1**|string|key: id of itemActivityOLD|item_activity_old_id1|itemActivityOLD-id1|
|**--id**|string|Read-only.|id|id|
|**--times**|object|itemActivityTimeSet|times|times|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application|application|
|**--list-item-last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--list-item-created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--list-item-created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--list-item-activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--list-item-analytics**|object|itemAnalytics|analytics|analytics|
|**--list-item-drive-item**|object|driveItem|microsoft_graph_drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|versions|versions|
|**--list-item-fields-id**|string|Read-only.|id1|id|
|**--actor-application**|object|identity|application1|application|
|**--actor-device**|object|identity|device1|device|
|**--actor-user**|object|identity|user1|user|
|**--action-comment**|object|commentAction|comment|comment|
|**--action-create**|dictionary|createAction|create|create|
|**--action-delete**|object|deleteAction|delete|delete|
|**--action-edit**|dictionary|editAction|edit|edit|
|**--action-mention**|object|mentionAction|mention|mention|
|**--action-move**|object|moveAction|move|move|
|**--action-rename**|object|renameAction|rename|rename|
|**--action-restore**|dictionary|restoreAction|restore|restore|
|**--action-share**|object|shareAction|share|share|
|**--action-version**|object|versionAction|version|version|

### sites site-list-activity-list-item update-drive-item

update-drive-item a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-drive-item|UpdateDriveItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
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
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
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
|**--list-item-parent-reference-site-id**|string||site_id1|siteId|
|**--list-item-last-modified-by-application**|object|identity|application1|application|
|**--list-item-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-item-created-by-application**|object|identity|application2|application|
|**--list-item-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-activities**|array|The list of recent activities that took place on this item.|microsoft_graph_list_item_activities|activities|
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
|**--bundle-album**|object|album|album|album|
|**--bundle-child-count**|integer||integer_child_count|childCount|

### sites site-list-activity-list-item update-field

update-field a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-field|UpdateFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--id**|string|Read-only.|id|id|

### sites site-list-activity-list-item update-version

update-version a sites site-list-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item|sites.lists.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-version|UpdateVersions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### sites site-list-activity-list-item-version delete

delete a sites site-list-activity-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item-version|sites.lists.activities.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--if-match**|string|ETag|if_match|If-Match|

### sites site-list-activity-list-item-version get-field

get-field a sites site-list-activity-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item-version|sites.lists.activities.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-field|GetFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-activity-list-item-version restore-version

restore-version a sites site-list-activity-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item-version|sites.lists.activities.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore-version|restoreVersion|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|

### sites site-list-activity-list-item-version update-field

update-field a sites site-list-activity-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-activity-list-item-version|sites.lists.activities.listItem.versions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-field|UpdateFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|

### sites site-list-content-type create-column-link

create-column-link a sites site-list-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-content-type|sites.lists.contentTypes|

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

### sites site-list-content-type delete

delete a sites site-list-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-content-type|sites.lists.contentTypes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteColumnLinks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--if-match**|string|ETag|if_match|If-Match|

### sites site-list-content-type get-column-link

get-column-link a sites site-list-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-content-type|sites.lists.contentTypes|

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

### sites site-list-content-type list-column-link

list-column-link a sites site-list-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-content-type|sites.lists.contentTypes|

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

### sites site-list-content-type update-column-link

update-column-link a sites site-list-content-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-content-type|sites.lists.contentTypes|

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

### sites site-list-item create-activity

create-activity a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity|CreateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--id**|string|Read-only.|id|id|
|**--times**|object|itemActivityTimeSet|times|times|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application|application|
|**--list-item-last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--list-item-created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--list-item-created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--list-item-activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--list-item-analytics**|object|itemAnalytics|analytics|analytics|
|**--list-item-drive-item**|object|driveItem|microsoft_graph_drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|versions|versions|
|**--list-item-fields-id**|string|Read-only.|id1|id|
|**--actor-application**|object|identity|application1|application|
|**--actor-device**|object|identity|device1|device|
|**--actor-user**|object|identity|user1|user|
|**--action-comment**|object|commentAction|comment|comment|
|**--action-create**|dictionary|createAction|create|create|
|**--action-delete**|object|deleteAction|delete|delete|
|**--action-edit**|dictionary|editAction|edit|edit|
|**--action-mention**|object|mentionAction|mention|mention|
|**--action-move**|object|moveAction|move|move|
|**--action-rename**|object|renameAction|rename|rename|
|**--action-restore**|dictionary|restoreAction|restore|restore|
|**--action-share**|object|shareAction|share|share|
|**--action-version**|object|versionAction|version|version|

### sites site-list-item create-link

create-link a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-link|createLink|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--type**|string||type|type|
|**--scope**|string||scope|scope|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--password**|string||password|password|
|**--recipients**|array||recipients|recipients|

### sites site-list-item create-version

create-version a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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

### sites site-list-item delete

delete a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteActivities|
|delete|DeleteVersions|
|delete|DeleteRefAnalytics|
|delete|DeleteDriveItem|
|delete|DeleteFields|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--if-match**|string|ETag|if_match|If-Match|

### sites site-list-item get-activity

get-activity a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity|GetActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-item get-activity-by-interval

get-activity-by-interval a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval|getActivitiesByInterval|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

### sites site-list-item get-analytic

get-analytic a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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

### sites site-list-item get-drive-item

get-drive-item a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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

### sites site-list-item get-drive-item-content

get-drive-item-content a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item-content|GetDriveItemContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|

### sites site-list-item get-field

get-field a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-item get-ref-analytic

get-ref-analytic a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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

### sites site-list-item get-version

get-version a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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

### sites site-list-item list-activity

list-activity a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity|ListActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-item list-version

list-version a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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

### sites site-list-item set-drive-item-content

set-drive-item-content a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-drive-item-content|SetDriveItemContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--data**|binary|New media content.|data|data|

### sites site-list-item set-ref-analytic

set-ref-analytic a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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

### sites site-list-item update-activity

update-activity a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-activity|UpdateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--id**|string|Read-only.|id|id|
|**--times**|object|itemActivityTimeSet|times|times|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-application**|object|identity|application|application|
|**--list-item-last-modified-by-device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--list-item-created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--list-item-created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--list-item-activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--list-item-analytics**|object|itemAnalytics|analytics|analytics|
|**--list-item-drive-item**|object|driveItem|microsoft_graph_drive_item|driveItem|
|**--list-item-versions**|array|The list of previous versions of the list item.|versions|versions|
|**--list-item-fields-id**|string|Read-only.|id1|id|
|**--actor-application**|object|identity|application1|application|
|**--actor-device**|object|identity|device1|device|
|**--actor-user**|object|identity|user1|user|
|**--action-comment**|object|commentAction|comment|comment|
|**--action-create**|dictionary|createAction|create|create|
|**--action-delete**|object|deleteAction|delete|delete|
|**--action-edit**|dictionary|editAction|edit|edit|
|**--action-mention**|object|mentionAction|mention|mention|
|**--action-move**|object|moveAction|move|move|
|**--action-rename**|object|renameAction|rename|rename|
|**--action-restore**|dictionary|restoreAction|restore|restore|
|**--action-share**|object|shareAction|share|share|
|**--action-version**|object|versionAction|version|version|

### sites site-list-item update-drive-item

update-drive-item a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
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
|**--list-item-parent-reference-site-id**|string||site_id1|siteId|
|**--list-item-last-modified-by-application**|object|identity|application1|application|
|**--list-item-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-item-created-by-application**|object|identity|application2|application|
|**--list-item-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-activities**|array|The list of recent activities that took place on this item.|microsoft_graph_list_item_activities|activities|
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
|**--bundle-album**|object|album|album|album|
|**--bundle-child-count**|integer||integer_child_count|childCount|

### sites site-list-item update-field

update-field a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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
|**--id**|string|Read-only.|id|id|

### sites site-list-item update-version

update-version a sites site-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item|sites.lists.items|

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

### sites site-list-item-activity delete

delete a sites site-list-item-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-activity|sites.lists.items.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDriveItem|
|delete|DeleteListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--if-match**|string|ETag|if_match|If-Match|

### sites site-list-item-activity get-drive-item

get-drive-item a sites site-list-item-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-activity|sites.lists.items.activities|

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
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-item-activity get-drive-item-content

get-drive-item-content a sites site-list-item-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-activity|sites.lists.items.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-drive-item-content|GetDriveItemContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|

### sites site-list-item-activity get-list-item

get-list-item a sites site-list-item-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-activity|sites.lists.items.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list-item|GetListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sites site-list-item-activity set-drive-item-content

set-drive-item-content a sites site-list-item-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-activity|sites.lists.items.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-drive-item-content|SetDriveItemContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--data**|binary|New media content.|data|data|

### sites site-list-item-activity update-drive-item

update-drive-item a sites site-list-item-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-activity|sites.lists.items.activities|

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
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
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
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
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
|**--list-item-parent-reference-site-id**|string||site_id1|siteId|
|**--list-item-last-modified-by-application**|object|identity|application1|application|
|**--list-item-last-modified-by-device**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--list-item-created-by-application**|object|identity|application2|application|
|**--list-item-created-by-device**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-activities**|array|The list of recent activities that took place on this item.|microsoft_graph_list_item_activities|activities|
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
|**--bundle-album**|object|album|album|album|
|**--bundle-child-count**|integer||integer_child_count|childCount|

### sites site-list-item-activity update-list-item

update-list-item a sites site-list-item-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-activity|sites.lists.items.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-list-item|UpdateListItem|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
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
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--fields-id**|string|Read-only.|microsoft_graph_entity_id|id|

### sites site-list-item-activity-list-item create-link

create-link a sites site-list-item-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-activity-list-item|sites.lists.items.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-link|createLink|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--type**|string||type|type|
|**--scope**|string||scope|scope|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--password**|string||password|password|
|**--recipients**|array||recipients|recipients|

### sites site-list-item-activity-list-item get-activity-by-interval

get-activity-by-interval a sites site-list-item-activity-list-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-activity-list-item|sites.lists.items.activities.listItem|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity-by-interval|getActivitiesByInterval|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--list-id**|string|key: id of list|list_id|list-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--item-activity-old-id**|string|key: id of itemActivityOLD|item_activity_old_id|itemActivityOLD-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

### sites site-list-item-version delete

delete a sites site-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-version|sites.lists.items.versions|

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

### sites site-list-item-version get-field

get-field a sites site-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-version|sites.lists.items.versions|

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

### sites site-list-item-version restore-version

restore-version a sites site-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-version|sites.lists.items.versions|

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

### sites site-list-item-version update-field

update-field a sites site-list-item-version.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-list-item-version|sites.lists.items.versions|

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

### sites site-onenote-notebook copy-notebook

copy-notebook a sites site-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook|sites.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--post-content-schema-site-id**|string||post_content_schema_site_id|siteId|

### sites site-onenote-notebook get-notebook-from-web-url

get-notebook-from-web-url a sites site-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook|sites.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-notebook-from-web-url|getNotebookFromWebUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--web-url**|string||web_url|webUrl|

### sites site-onenote-notebook get-recent-notebook

get-recent-notebook a sites site-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook|sites.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-recent-notebook|getRecentNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--include-personal-notebooks**|boolean||include_personal_notebooks|includePersonalNotebooks|

### sites site-onenote-notebook-section copy-to-notebook

copy-to-notebook a sites site-onenote-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section|sites.onenote.notebooks.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section copy-to-section-group

copy-to-section-group a sites site-onenote-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section|sites.onenote.notebooks.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-group-parent-notebook copy-notebook

copy-notebook a sites site-onenote-notebook-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-group-parent-notebook|sites.onenote.notebooks.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-group-section copy-to-notebook

copy-to-notebook a sites site-onenote-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-group-section|sites.onenote.notebooks.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-group-section copy-to-section-group

copy-to-section-group a sites site-onenote-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-group-section|sites.onenote.notebooks.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-group-section-page copy-to-section

copy-to-section a sites site-onenote-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-group-section-page|sites.onenote.notebooks.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-group-section-page onenote-patch-content

onenote-patch-content a sites site-onenote-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-group-section-page|sites.onenote.notebooks.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### sites site-onenote-notebook-section-group-section-page preview

preview a sites site-onenote-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-group-section-page|sites.onenote.notebooks.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|preview|preview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### sites site-onenote-notebook-section-group-section-page-parent-notebook copy-notebook

copy-notebook a sites site-onenote-notebook-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-group-section-page-parent-notebook|sites.onenote.notebooks.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-group-section-page-parent-section copy-to-notebook

copy-to-notebook a sites site-onenote-notebook-section-group-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-group-section-page-parent-section|sites.onenote.notebooks.sectionGroups.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-group-section-page-parent-section copy-to-section-group

copy-to-section-group a sites site-onenote-notebook-section-group-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-group-section-page-parent-section|sites.onenote.notebooks.sectionGroups.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-group-section-parent-notebook copy-notebook

copy-notebook a sites site-onenote-notebook-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-group-section-parent-notebook|sites.onenote.notebooks.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-page copy-to-section

copy-to-section a sites site-onenote-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-page|sites.onenote.notebooks.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-page onenote-patch-content

onenote-patch-content a sites site-onenote-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-page|sites.onenote.notebooks.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### sites site-onenote-notebook-section-page preview

preview a sites site-onenote-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-page|sites.onenote.notebooks.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|preview|preview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### sites site-onenote-notebook-section-page-parent-notebook copy-notebook

copy-notebook a sites site-onenote-notebook-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-page-parent-notebook|sites.onenote.notebooks.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-page-parent-section copy-to-notebook

copy-to-notebook a sites site-onenote-notebook-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-page-parent-section|sites.onenote.notebooks.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-page-parent-section copy-to-section-group

copy-to-section-group a sites site-onenote-notebook-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-page-parent-section|sites.onenote.notebooks.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-parent-notebook copy-notebook

copy-notebook a sites site-onenote-notebook-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-parent-notebook|sites.onenote.notebooks.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-parent-section-group-parent-notebook copy-notebook

copy-notebook a sites site-onenote-notebook-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-parent-section-group-parent-notebook|sites.onenote.notebooks.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-parent-section-group-section copy-to-notebook

copy-to-notebook a sites site-onenote-notebook-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-parent-section-group-section|sites.onenote.notebooks.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-notebook-section-parent-section-group-section copy-to-section-group

copy-to-section-group a sites site-onenote-notebook-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-notebook-section-parent-section-group-section|sites.onenote.notebooks.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page copy-to-section

copy-to-section a sites site-onenote-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page|sites.onenote.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page onenote-patch-content

onenote-patch-content a sites site-onenote-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page|sites.onenote.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### sites site-onenote-page preview

preview a sites site-onenote-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page|sites.onenote.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|preview|preview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### sites site-onenote-page-parent-notebook copy-notebook

copy-notebook a sites site-onenote-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook|sites.onenote.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section copy-to-notebook

copy-to-notebook a sites site-onenote-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section|sites.onenote.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section copy-to-section-group

copy-to-section-group a sites site-onenote-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section|sites.onenote.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section-group-parent-notebook copy-notebook

copy-notebook a sites site-onenote-page-parent-notebook-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-group-parent-notebook|sites.onenote.pages.parentNotebook.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section-group-section copy-to-notebook

copy-to-notebook a sites site-onenote-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-group-section|sites.onenote.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section-group-section copy-to-section-group

copy-to-section-group a sites site-onenote-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-group-section|sites.onenote.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section-group-section-page copy-to-section

copy-to-section a sites site-onenote-page-parent-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-group-section-page|sites.onenote.pages.parentNotebook.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section-group-section-page onenote-patch-content

onenote-patch-content a sites site-onenote-page-parent-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-group-section-page|sites.onenote.pages.parentNotebook.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--commands**|array||commands|commands|

### sites site-onenote-page-parent-notebook-section-group-section-page preview

preview a sites site-onenote-page-parent-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-group-section-page|sites.onenote.pages.parentNotebook.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|preview|preview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|

### sites site-onenote-page-parent-notebook-section-group-section-parent-notebook copy-notebook

copy-notebook a sites site-onenote-page-parent-notebook-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-group-section-parent-notebook|sites.onenote.pages.parentNotebook.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section-page copy-to-section

copy-to-section a sites site-onenote-page-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-page|sites.onenote.pages.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section-page onenote-patch-content

onenote-patch-content a sites site-onenote-page-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-page|sites.onenote.pages.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--commands**|array||commands|commands|

### sites site-onenote-page-parent-notebook-section-page preview

preview a sites site-onenote-page-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-page|sites.onenote.pages.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|preview|preview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|

### sites site-onenote-page-parent-notebook-section-parent-notebook copy-notebook

copy-notebook a sites site-onenote-page-parent-notebook-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-parent-notebook|sites.onenote.pages.parentNotebook.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section-parent-section-group-parent-notebook copy-notebook

copy-notebook a sites site-onenote-page-parent-notebook-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-parent-section-group-parent-notebook|sites.onenote.pages.parentNotebook.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section-parent-section-group-section copy-to-notebook

copy-to-notebook a sites site-onenote-page-parent-notebook-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-parent-section-group-section|sites.onenote.pages.parentNotebook.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-notebook-section-parent-section-group-section copy-to-section-group

copy-to-section-group a sites site-onenote-page-parent-notebook-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-notebook-section-parent-section-group-section|sites.onenote.pages.parentNotebook.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section copy-to-notebook

copy-to-notebook a sites site-onenote-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section|sites.onenote.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section copy-to-section-group

copy-to-section-group a sites site-onenote-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section|sites.onenote.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-page copy-to-section

copy-to-section a sites site-onenote-page-parent-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-page|sites.onenote.pages.parentSection.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-page onenote-patch-content

onenote-patch-content a sites site-onenote-page-parent-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-page|sites.onenote.pages.parentSection.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--commands**|array||commands|commands|

### sites site-onenote-page-parent-section-page preview

preview a sites site-onenote-page-parent-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-page|sites.onenote.pages.parentSection.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|preview|preview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|

### sites site-onenote-page-parent-section-parent-notebook copy-notebook

copy-notebook a sites site-onenote-page-parent-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-notebook|sites.onenote.pages.parentSection.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-parent-notebook-section copy-to-notebook

copy-to-notebook a sites site-onenote-page-parent-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-notebook-section|sites.onenote.pages.parentSection.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-parent-notebook-section copy-to-section-group

copy-to-section-group a sites site-onenote-page-parent-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-notebook-section|sites.onenote.pages.parentSection.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-parent-notebook-section-group-parent-notebook copy-notebook

copy-notebook a sites site-onenote-page-parent-section-parent-notebook-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-notebook-section-group-parent-notebook|sites.onenote.pages.parentSection.parentNotebook.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-parent-notebook-section-group-section copy-to-notebook

copy-to-notebook a sites site-onenote-page-parent-section-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-notebook-section-group-section|sites.onenote.pages.parentSection.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-parent-notebook-section-group-section copy-to-section-group

copy-to-section-group a sites site-onenote-page-parent-section-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-notebook-section-group-section|sites.onenote.pages.parentSection.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-parent-section-group-parent-notebook copy-notebook

copy-notebook a sites site-onenote-page-parent-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-section-group-parent-notebook|sites.onenote.pages.parentSection.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-parent-section-group-parent-notebook-section copy-to-notebook

copy-to-notebook a sites site-onenote-page-parent-section-parent-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-section-group-parent-notebook-section|sites.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-parent-section-group-parent-notebook-section copy-to-section-group

copy-to-section-group a sites site-onenote-page-parent-section-parent-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-section-group-parent-notebook-section|sites.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-parent-section-group-section copy-to-notebook

copy-to-notebook a sites site-onenote-page-parent-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-section-group-section|sites.onenote.pages.parentSection.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-page-parent-section-parent-section-group-section copy-to-section-group

copy-to-section-group a sites site-onenote-page-parent-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-page-parent-section-parent-section-group-section|sites.onenote.pages.parentSection.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section copy-to-notebook

copy-to-notebook a sites site-onenote-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section|sites.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section copy-to-section-group

copy-to-section-group a sites site-onenote-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section|sites.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-parent-notebook copy-notebook

copy-notebook a sites site-onenote-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-parent-notebook|sites.onenote.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-parent-notebook-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-parent-notebook-section|sites.onenote.sectionGroups.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-parent-notebook-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-parent-notebook-section|sites.onenote.sectionGroups.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-parent-notebook-section-page copy-to-section

copy-to-section a sites site-onenote-section-group-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-parent-notebook-section-page|sites.onenote.sectionGroups.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-parent-notebook-section-page onenote-patch-content

onenote-patch-content a sites site-onenote-section-group-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-parent-notebook-section-page|sites.onenote.sectionGroups.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### sites site-onenote-section-group-parent-notebook-section-page preview

preview a sites site-onenote-section-group-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-parent-notebook-section-page|sites.onenote.sectionGroups.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|preview|preview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### sites site-onenote-section-group-parent-notebook-section-page-parent-notebook copy-notebook

copy-notebook a sites site-onenote-section-group-parent-notebook-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-parent-notebook-section-page-parent-notebook|sites.onenote.sectionGroups.parentNotebook.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-parent-notebook-section-page-parent-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-group-parent-notebook-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-parent-notebook-section-page-parent-section|sites.onenote.sectionGroups.parentNotebook.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-parent-notebook-section-page-parent-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-group-parent-notebook-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-parent-notebook-section-page-parent-section|sites.onenote.sectionGroups.parentNotebook.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-parent-notebook-section-parent-notebook copy-notebook

copy-notebook a sites site-onenote-section-group-parent-notebook-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-parent-notebook-section-parent-notebook|sites.onenote.sectionGroups.parentNotebook.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section|sites.onenote.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section|sites.onenote.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section-page copy-to-section

copy-to-section a sites site-onenote-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-page|sites.onenote.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section-page onenote-patch-content

onenote-patch-content a sites site-onenote-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-page|sites.onenote.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### sites site-onenote-section-group-section-page preview

preview a sites site-onenote-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-page|sites.onenote.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|preview|preview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### sites site-onenote-section-group-section-page-parent-notebook copy-notebook

copy-notebook a sites site-onenote-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-page-parent-notebook|sites.onenote.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section-page-parent-notebook-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-group-section-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-page-parent-notebook-section|sites.onenote.sectionGroups.sections.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section-page-parent-notebook-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-group-section-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-page-parent-notebook-section|sites.onenote.sectionGroups.sections.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section-page-parent-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-group-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-page-parent-section|sites.onenote.sectionGroups.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section-page-parent-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-group-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-page-parent-section|sites.onenote.sectionGroups.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section-parent-notebook copy-notebook

copy-notebook a sites site-onenote-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-parent-notebook|sites.onenote.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section-parent-notebook-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-group-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-parent-notebook-section|sites.onenote.sectionGroups.sections.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-group-section-parent-notebook-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-group-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-group-section-parent-notebook-section|sites.onenote.sectionGroups.sections.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-page copy-to-section

copy-to-section a sites site-onenote-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page|sites.onenote.sections.pages|

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

### sites site-onenote-section-page onenote-patch-content

onenote-patch-content a sites site-onenote-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page|sites.onenote.sections.pages|

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

### sites site-onenote-section-page preview

preview a sites site-onenote-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page|sites.onenote.sections.pages|

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

### sites site-onenote-section-page-parent-notebook copy-notebook

copy-notebook a sites site-onenote-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page-parent-notebook|sites.onenote.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-page-parent-notebook-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page-parent-notebook-section|sites.onenote.sections.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-page-parent-notebook-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page-parent-notebook-section|sites.onenote.sections.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-page-parent-notebook-section-group-parent-notebook copy-notebook

copy-notebook a sites site-onenote-section-page-parent-notebook-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page-parent-notebook-section-group-parent-notebook|sites.onenote.sections.pages.parentNotebook.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-page-parent-notebook-section-group-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page-parent-notebook-section-group-section|sites.onenote.sections.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-page-parent-notebook-section-group-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page-parent-notebook-section-group-section|sites.onenote.sections.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-page-parent-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page-parent-section|sites.onenote.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-page-parent-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-page-parent-section|sites.onenote.sections.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-parent-notebook copy-notebook

copy-notebook a sites site-onenote-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-notebook|sites.onenote.sections.parentNotebook|

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

### sites site-onenote-section-parent-notebook-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-notebook-section|sites.onenote.sections.parentNotebook.sections|

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

### sites site-onenote-section-parent-notebook-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-notebook-section|sites.onenote.sections.parentNotebook.sections|

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

### sites site-onenote-section-parent-notebook-section-group-parent-notebook copy-notebook

copy-notebook a sites site-onenote-section-parent-notebook-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-notebook-section-group-parent-notebook|sites.onenote.sections.parentNotebook.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-parent-notebook-section-group-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-notebook-section-group-section|sites.onenote.sections.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-parent-notebook-section-group-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-notebook-section-group-section|sites.onenote.sections.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--string-site-id**|string||string_site_id|siteId|

### sites site-onenote-section-parent-section-group-parent-notebook copy-notebook

copy-notebook a sites site-onenote-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-section-group-parent-notebook|sites.onenote.sections.parentSectionGroup.parentNotebook|

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

### sites site-onenote-section-parent-section-group-parent-notebook-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-parent-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-section-group-parent-notebook-section|sites.onenote.sections.parentSectionGroup.parentNotebook.sections|

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

### sites site-onenote-section-parent-section-group-parent-notebook-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-parent-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-section-group-parent-notebook-section|sites.onenote.sections.parentSectionGroup.parentNotebook.sections|

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

### sites site-onenote-section-parent-section-group-section copy-to-notebook

copy-to-notebook a sites site-onenote-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-section-group-section|sites.onenote.sections.parentSectionGroup.sections|

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

### sites site-onenote-section-parent-section-group-section copy-to-section-group

copy-to-section-group a sites site-onenote-section-parent-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-onenote-section-parent-section-group-section|sites.onenote.sections.parentSectionGroup.sections|

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

### sites site-page publish

publish a sites site-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites site-page|sites.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|publish|publish|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: id of site|site_id|site-id|
|**--site-page-id**|string|key: id of sitePage|site_page_id|sitePage-id|

### sites user create-ref-followed-site

create-ref-followed-site a sites user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-followed-site|CreateRefFollowedSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### sites user list-followed-site

list-followed-site a sites user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites user|users|

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

### sites user list-ref-followed-site

list-ref-followed-site a sites user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sites user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-followed-site|ListRefFollowedSites|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
