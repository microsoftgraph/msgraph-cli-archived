# Azure CLI Module Creation Report

### onenote user get-onenote

get-onenote a onenote user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-onenote|GetOnenote|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user update

update a onenote user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateOnenote|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|pages|pages|
|**--resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|

### onenote user-onenote create-notebook

create-notebook a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-notebook|CreateNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote create-operation

create-operation a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-operation|CreateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--status**|choice|operationStatus|status|status|
|**--created-date-time**|date-time|The start time of the operation.|created_date_time|createdDateTime|
|**--last-action-date-time**|date-time|The time of the last action of the operation.|last_action_date_time|lastActionDateTime|
|**--resource-location**|string|The resource URI for the object. For example, the resource URI for a copied page or section.|resource_location|resourceLocation|
|**--resource-id**|string|The resource id.|resource_id|resourceId|
|**--error**|object|onenoteOperationError|error|error|
|**--percent-complete**|string|The operation percent complete if the operation is still in running status|percent_complete|percentComplete|

### onenote user-onenote create-page

create-page a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--body**|object|New navigation property|body|body|

### onenote user-onenote create-resource

create-resource a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-resource|CreateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--content**|byte-array|The content stream|content|content|
|**--content-url**|string|The URL for downloading the content|content_url|contentUrl|

### onenote user-onenote create-section

create-section a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote create-section-group

create-section-group a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote get-notebook

get-notebook a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-notebook|GetNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote get-operation

get-operation a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-operation|GetOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-operation-id**|string|key: onenoteOperation-id of onenoteOperation|onenote_operation_id|onenoteOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote get-page

get-page a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote get-resource

get-resource a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-resource-id**|string|key: onenoteResource-id of onenoteResource|onenote_resource_id|onenoteResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote get-section

get-section a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote get-section-group

get-section-group a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote list-notebook

list-notebook a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-notebook|ListNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote list-operation

list-operation a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-operation|ListOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote list-page

list-page a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote list-resource

list-resource a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-resource|ListResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote list-section

list-section a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote list-section-group

list-section-group a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote update

update a onenote user-onenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateNotebooks|
|update|UpdateOperations|
|update|UpdatePages|
|update|UpdateResources|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-operation-id**|string|key: onenoteOperation-id of onenoteOperation|onenote_operation_id|onenoteOperation-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--body**|object|New navigation property values|body|body|
|**--onenote-resource-id**|string|key: onenoteResource-id of onenoteResource|onenote_resource_id|onenoteResource-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--status**|choice|operationStatus|status|status|
|**--last-action-date-time**|date-time|The time of the last action of the operation.|last_action_date_time|lastActionDateTime|
|**--resource-location**|string|The resource URI for the object. For example, the resource URI for a copied page or section.|resource_location|resourceLocation|
|**--resource-id**|string|The resource id.|resource_id|resourceId|
|**--error**|object|onenoteOperationError|error|error|
|**--percent-complete**|string|The operation percent complete if the operation is still in running status|percent_complete|percentComplete|
|**--content**|byte-array|The content stream|content|content|
|**--content-url**|string|The URL for downloading the content|content_url|contentUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|

### onenote user-onenote-notebook create-section

create-section a onenote user-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook|users.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-notebook create-section-group

create-section-group a onenote user-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook|users.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-notebook get-section

get-section a onenote user-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook|users.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook get-section-group

get-section-group a onenote user-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook|users.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook list-section

list-section a onenote user-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook|users.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook list-section-group

list-section-group a onenote user-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook|users.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook update

update a onenote user-onenote-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook|users.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-notebook-section create-page

create-page a onenote user-onenote-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section|users.onenote.notebooks.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--body**|object|New navigation property|body|body|

### onenote user-onenote-notebook-section get-page

get-page a onenote user-onenote-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section|users.onenote.notebooks.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section get-parent-notebook

get-parent-notebook a onenote user-onenote-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section|users.onenote.notebooks.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section get-parent-section-group

get-parent-section-group a onenote user-onenote-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section|users.onenote.notebooks.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section list-page

list-page a onenote user-onenote-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section|users.onenote.notebooks.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section update

update a onenote user-onenote-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section|users.onenote.notebooks.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePages|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|

### onenote user-onenote-notebook-section-group create-section

create-section a onenote user-onenote-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group|users.onenote.notebooks.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-notebook-section-group create-section-group

create-section-group a onenote user-onenote-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group|users.onenote.notebooks.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-notebook-section-group get-parent-notebook

get-parent-notebook a onenote user-onenote-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group|users.onenote.notebooks.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group get-parent-section-group

get-parent-section-group a onenote user-onenote-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group|users.onenote.notebooks.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group get-section

get-section a onenote user-onenote-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group|users.onenote.notebooks.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group get-section-group

get-section-group a onenote user-onenote-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group|users.onenote.notebooks.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group list-section

list-section a onenote user-onenote-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group|users.onenote.notebooks.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group list-section-group

list-section-group a onenote user-onenote-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group|users.onenote.notebooks.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group update

update a onenote user-onenote-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group|users.onenote.notebooks.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|

### onenote user-onenote-notebook-section-group-section create-page

create-page a onenote user-onenote-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group-section|users.onenote.notebooks.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--body**|object|New navigation property|body|body|

### onenote user-onenote-notebook-section-group-section get-page

get-page a onenote user-onenote-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group-section|users.onenote.notebooks.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group-section get-parent-notebook

get-parent-notebook a onenote user-onenote-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group-section|users.onenote.notebooks.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group-section get-parent-section-group

get-parent-section-group a onenote user-onenote-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group-section|users.onenote.notebooks.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group-section list-page

list-page a onenote user-onenote-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group-section|users.onenote.notebooks.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group-section update

update a onenote user-onenote-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group-section|users.onenote.notebooks.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePages|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|

### onenote user-onenote-notebook-section-group-section-page get-parent-notebook

get-parent-notebook a onenote user-onenote-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group-section-page|users.onenote.notebooks.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group-section-page get-parent-section

get-parent-section a onenote user-onenote-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group-section-page|users.onenote.notebooks.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section|GetParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-group-section-page update

update a onenote user-onenote-notebook-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-group-section-page|users.onenote.notebooks.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateParentNotebook|
|update|UpdateParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|

### onenote user-onenote-notebook-section-page get-parent-notebook

get-parent-notebook a onenote user-onenote-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-page|users.onenote.notebooks.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-page get-parent-section

get-parent-section a onenote user-onenote-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-page|users.onenote.notebooks.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section|GetParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-page update

update a onenote user-onenote-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-page|users.onenote.notebooks.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateParentNotebook|
|update|UpdateParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|

### onenote user-onenote-notebook-section-parent-section-group create-section

create-section a onenote user-onenote-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-parent-section-group|users.onenote.notebooks.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-notebook-section-parent-section-group create-section-group

create-section-group a onenote user-onenote-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-parent-section-group|users.onenote.notebooks.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-notebook-section-parent-section-group get-parent-notebook

get-parent-notebook a onenote user-onenote-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-parent-section-group|users.onenote.notebooks.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-parent-section-group get-parent-section-group

get-parent-section-group a onenote user-onenote-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-parent-section-group|users.onenote.notebooks.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-parent-section-group get-section

get-section a onenote user-onenote-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-parent-section-group|users.onenote.notebooks.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-parent-section-group get-section-group

get-section-group a onenote user-onenote-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-parent-section-group|users.onenote.notebooks.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-parent-section-group list-section

list-section a onenote user-onenote-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-parent-section-group|users.onenote.notebooks.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-parent-section-group list-section-group

list-section-group a onenote user-onenote-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-parent-section-group|users.onenote.notebooks.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-notebook-section-parent-section-group update

update a onenote user-onenote-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-notebook-section-parent-section-group|users.onenote.notebooks.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|

### onenote user-onenote-page get-parent-notebook

get-parent-notebook a onenote user-onenote-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page|users.onenote.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page get-parent-section

get-parent-section a onenote user-onenote-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page|users.onenote.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section|GetParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page update

update a onenote user-onenote-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page|users.onenote.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateParentNotebook|
|update|UpdateParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|

### onenote user-onenote-page-parent-notebook create-section

create-section a onenote user-onenote-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook|users.onenote.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-page-parent-notebook create-section-group

create-section-group a onenote user-onenote-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook|users.onenote.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-page-parent-notebook get-section

get-section a onenote user-onenote-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook|users.onenote.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook get-section-group

get-section-group a onenote user-onenote-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook|users.onenote.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook list-section

list-section a onenote user-onenote-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook|users.onenote.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook list-section-group

list-section-group a onenote user-onenote-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook|users.onenote.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook update

update a onenote user-onenote-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook|users.onenote.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-page-parent-notebook-section create-page

create-page a onenote user-onenote-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section|users.onenote.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--body**|object|New navigation property|body|body|

### onenote user-onenote-page-parent-notebook-section get-page

get-page a onenote user-onenote-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section|users.onenote.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: onenotePage-id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section get-parent-notebook

get-parent-notebook a onenote user-onenote-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section|users.onenote.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section get-parent-section-group

get-parent-section-group a onenote user-onenote-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section|users.onenote.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section list-page

list-page a onenote user-onenote-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section|users.onenote.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section update

update a onenote user-onenote-page-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section|users.onenote.pages.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePages|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: onenotePage-id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|

### onenote user-onenote-page-parent-notebook-section-group create-section

create-section a onenote user-onenote-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group|users.onenote.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-page-parent-notebook-section-group create-section-group

create-section-group a onenote user-onenote-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group|users.onenote.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-page-parent-notebook-section-group get-parent-notebook

get-parent-notebook a onenote user-onenote-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group|users.onenote.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-group get-parent-section-group

get-parent-section-group a onenote user-onenote-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group|users.onenote.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-group get-section

get-section a onenote user-onenote-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group|users.onenote.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-group get-section-group

get-section-group a onenote user-onenote-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group|users.onenote.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-group list-section

list-section a onenote user-onenote-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group|users.onenote.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-group list-section-group

list-section-group a onenote user-onenote-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group|users.onenote.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-group update

update a onenote user-onenote-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group|users.onenote.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|

### onenote user-onenote-page-parent-notebook-section-group-section create-page

create-page a onenote user-onenote-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group-section|users.onenote.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--body**|object|New navigation property|body|body|

### onenote user-onenote-page-parent-notebook-section-group-section get-page

get-page a onenote user-onenote-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group-section|users.onenote.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: onenotePage-id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-group-section get-parent-notebook

get-parent-notebook a onenote user-onenote-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group-section|users.onenote.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-group-section get-parent-section-group

get-parent-section-group a onenote user-onenote-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group-section|users.onenote.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-group-section list-page

list-page a onenote user-onenote-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group-section|users.onenote.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-group-section update

update a onenote user-onenote-page-parent-notebook-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-group-section|users.onenote.pages.parentNotebook.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePages|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: onenotePage-id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|

### onenote user-onenote-page-parent-notebook-section-parent-section-group create-section

create-section a onenote user-onenote-page-parent-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-parent-section-group|users.onenote.pages.parentNotebook.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-page-parent-notebook-section-parent-section-group create-section-group

create-section-group a onenote user-onenote-page-parent-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-parent-section-group|users.onenote.pages.parentNotebook.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-page-parent-notebook-section-parent-section-group get-parent-notebook

get-parent-notebook a onenote user-onenote-page-parent-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-parent-section-group|users.onenote.pages.parentNotebook.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-parent-section-group get-parent-section-group

get-parent-section-group a onenote user-onenote-page-parent-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-parent-section-group|users.onenote.pages.parentNotebook.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-parent-section-group get-section

get-section a onenote user-onenote-page-parent-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-parent-section-group|users.onenote.pages.parentNotebook.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-parent-section-group get-section-group

get-section-group a onenote user-onenote-page-parent-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-parent-section-group|users.onenote.pages.parentNotebook.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-parent-section-group list-section

list-section a onenote user-onenote-page-parent-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-parent-section-group|users.onenote.pages.parentNotebook.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-parent-section-group list-section-group

list-section-group a onenote user-onenote-page-parent-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-parent-section-group|users.onenote.pages.parentNotebook.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-notebook-section-parent-section-group update

update a onenote user-onenote-page-parent-notebook-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-notebook-section-parent-section-group|users.onenote.pages.parentNotebook.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|

### onenote user-onenote-page-parent-section create-page

create-page a onenote user-onenote-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section|users.onenote.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--body**|object|New navigation property|body|body|

### onenote user-onenote-page-parent-section get-page

get-page a onenote user-onenote-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section|users.onenote.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-page-id1**|string|key: onenotePage-id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section get-parent-notebook

get-parent-notebook a onenote user-onenote-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section|users.onenote.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section get-parent-section-group

get-parent-section-group a onenote user-onenote-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section|users.onenote.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section list-page

list-page a onenote user-onenote-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section|users.onenote.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section update

update a onenote user-onenote-page-parent-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section|users.onenote.pages.parentSection|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePages|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-page-id1**|string|key: onenotePage-id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|

### onenote user-onenote-page-parent-section-group create-section

create-section a onenote user-onenote-page-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group|users.onenote.pages.parentSection.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-page-parent-section-group create-section-group

create-section-group a onenote user-onenote-page-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group|users.onenote.pages.parentSection.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-page-parent-section-group get-parent-notebook

get-parent-notebook a onenote user-onenote-page-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group|users.onenote.pages.parentSection.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-group get-parent-section-group

get-parent-section-group a onenote user-onenote-page-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group|users.onenote.pages.parentSection.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-group get-section

get-section a onenote user-onenote-page-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group|users.onenote.pages.parentSection.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-group get-section-group

get-section-group a onenote user-onenote-page-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group|users.onenote.pages.parentSection.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-group list-section

list-section a onenote user-onenote-page-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group|users.onenote.pages.parentSection.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-group list-section-group

list-section-group a onenote user-onenote-page-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group|users.onenote.pages.parentSection.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-group update

update a onenote user-onenote-page-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group|users.onenote.pages.parentSection.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|

### onenote user-onenote-page-parent-section-group-parent-notebook create-section

create-section a onenote user-onenote-page-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group-parent-notebook|users.onenote.pages.parentSection.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-page-parent-section-group-parent-notebook create-section-group

create-section-group a onenote user-onenote-page-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group-parent-notebook|users.onenote.pages.parentSection.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-page-parent-section-group-parent-notebook get-section

get-section a onenote user-onenote-page-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group-parent-notebook|users.onenote.pages.parentSection.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-group-parent-notebook get-section-group

get-section-group a onenote user-onenote-page-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group-parent-notebook|users.onenote.pages.parentSection.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-group-parent-notebook list-section

list-section a onenote user-onenote-page-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group-parent-notebook|users.onenote.pages.parentSection.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-group-parent-notebook list-section-group

list-section-group a onenote user-onenote-page-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group-parent-notebook|users.onenote.pages.parentSection.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-group-parent-notebook update

update a onenote user-onenote-page-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-group-parent-notebook|users.onenote.pages.parentSection.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-page-parent-section-parent-notebook create-section

create-section a onenote user-onenote-page-parent-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook|users.onenote.pages.parentSection.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-page-parent-section-parent-notebook create-section-group

create-section-group a onenote user-onenote-page-parent-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook|users.onenote.pages.parentSection.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-page-parent-section-parent-notebook get-section

get-section a onenote user-onenote-page-parent-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook|users.onenote.pages.parentSection.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-parent-notebook get-section-group

get-section-group a onenote user-onenote-page-parent-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook|users.onenote.pages.parentSection.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-parent-notebook list-section

list-section a onenote user-onenote-page-parent-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook|users.onenote.pages.parentSection.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-parent-notebook list-section-group

list-section-group a onenote user-onenote-page-parent-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook|users.onenote.pages.parentSection.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-parent-notebook update

update a onenote user-onenote-page-parent-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook|users.onenote.pages.parentSection.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-page-parent-section-parent-notebook-section-group create-section

create-section a onenote user-onenote-page-parent-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook-section-group|users.onenote.pages.parentSection.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-page-parent-section-parent-notebook-section-group create-section-group

create-section-group a onenote user-onenote-page-parent-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook-section-group|users.onenote.pages.parentSection.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-page-parent-section-parent-notebook-section-group get-parent-notebook

get-parent-notebook a onenote user-onenote-page-parent-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook-section-group|users.onenote.pages.parentSection.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-parent-notebook-section-group get-parent-section-group

get-parent-section-group a onenote user-onenote-page-parent-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook-section-group|users.onenote.pages.parentSection.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-parent-notebook-section-group get-section

get-section a onenote user-onenote-page-parent-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook-section-group|users.onenote.pages.parentSection.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-parent-notebook-section-group get-section-group

get-section-group a onenote user-onenote-page-parent-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook-section-group|users.onenote.pages.parentSection.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-parent-notebook-section-group list-section

list-section a onenote user-onenote-page-parent-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook-section-group|users.onenote.pages.parentSection.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-parent-notebook-section-group list-section-group

list-section-group a onenote user-onenote-page-parent-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook-section-group|users.onenote.pages.parentSection.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-page-parent-section-parent-notebook-section-group update

update a onenote user-onenote-page-parent-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-page-parent-section-parent-notebook-section-group|users.onenote.pages.parentSection.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|

### onenote user-onenote-section create-page

create-page a onenote user-onenote-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--body**|object|New navigation property|body|body|

### onenote user-onenote-section get-page

get-page a onenote user-onenote-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section get-parent-notebook

get-parent-notebook a onenote user-onenote-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section get-parent-section-group

get-parent-section-group a onenote user-onenote-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section list-page

list-page a onenote user-onenote-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section update

update a onenote user-onenote-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePages|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|

### onenote user-onenote-section-group create-section

create-section a onenote user-onenote-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group|users.onenote.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-group create-section-group

create-section-group a onenote user-onenote-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group|users.onenote.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-section-group get-parent-notebook

get-parent-notebook a onenote user-onenote-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group|users.onenote.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group get-parent-section-group

get-parent-section-group a onenote user-onenote-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group|users.onenote.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group get-section

get-section a onenote user-onenote-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group|users.onenote.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group get-section-group

get-section-group a onenote user-onenote-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group|users.onenote.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group list-section

list-section a onenote user-onenote-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group|users.onenote.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group list-section-group

list-section-group a onenote user-onenote-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group|users.onenote.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group update

update a onenote user-onenote-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group|users.onenote.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|

### onenote user-onenote-section-group-parent-notebook create-section

create-section a onenote user-onenote-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook|users.onenote.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-group-parent-notebook create-section-group

create-section-group a onenote user-onenote-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook|users.onenote.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-section-group-parent-notebook get-section

get-section a onenote user-onenote-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook|users.onenote.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-parent-notebook get-section-group

get-section-group a onenote user-onenote-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook|users.onenote.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-parent-notebook list-section

list-section a onenote user-onenote-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook|users.onenote.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-parent-notebook list-section-group

list-section-group a onenote user-onenote-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook|users.onenote.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-parent-notebook update

update a onenote user-onenote-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook|users.onenote.sectionGroups.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-group-parent-notebook-section create-page

create-page a onenote user-onenote-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook-section|users.onenote.sectionGroups.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--body**|object|New navigation property|body|body|

### onenote user-onenote-section-group-parent-notebook-section get-page

get-page a onenote user-onenote-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook-section|users.onenote.sectionGroups.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-parent-notebook-section get-parent-notebook

get-parent-notebook a onenote user-onenote-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook-section|users.onenote.sectionGroups.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-parent-notebook-section get-parent-section-group

get-parent-section-group a onenote user-onenote-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook-section|users.onenote.sectionGroups.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-parent-notebook-section list-page

list-page a onenote user-onenote-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook-section|users.onenote.sectionGroups.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-parent-notebook-section update

update a onenote user-onenote-section-group-parent-notebook-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook-section|users.onenote.sectionGroups.parentNotebook.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePages|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|

### onenote user-onenote-section-group-parent-notebook-section-page get-parent-notebook

get-parent-notebook a onenote user-onenote-section-group-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook-section-page|users.onenote.sectionGroups.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-parent-notebook-section-page get-parent-section

get-parent-section a onenote user-onenote-section-group-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook-section-page|users.onenote.sectionGroups.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section|GetParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-parent-notebook-section-page update

update a onenote user-onenote-section-group-parent-notebook-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-parent-notebook-section-page|users.onenote.sectionGroups.parentNotebook.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateParentNotebook|
|update|UpdateParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|

### onenote user-onenote-section-group-section create-page

create-page a onenote user-onenote-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section|users.onenote.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--body**|object|New navigation property|body|body|

### onenote user-onenote-section-group-section get-page

get-page a onenote user-onenote-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section|users.onenote.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section get-parent-notebook

get-parent-notebook a onenote user-onenote-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section|users.onenote.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section get-parent-section-group

get-parent-section-group a onenote user-onenote-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section|users.onenote.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section list-page

list-page a onenote user-onenote-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section|users.onenote.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section update

update a onenote user-onenote-section-group-section.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section|users.onenote.sectionGroups.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePages|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|

### onenote user-onenote-section-group-section-page get-parent-notebook

get-parent-notebook a onenote user-onenote-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-page|users.onenote.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section-page get-parent-section

get-parent-section a onenote user-onenote-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-page|users.onenote.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section|GetParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section-page update

update a onenote user-onenote-section-group-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-page|users.onenote.sectionGroups.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateParentNotebook|
|update|UpdateParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|

### onenote user-onenote-section-group-section-page-parent-notebook create-section

create-section a onenote user-onenote-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-page-parent-notebook|users.onenote.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-group-section-page-parent-notebook create-section-group

create-section-group a onenote user-onenote-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-page-parent-notebook|users.onenote.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-section-group-section-page-parent-notebook get-section

get-section a onenote user-onenote-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-page-parent-notebook|users.onenote.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section-page-parent-notebook get-section-group

get-section-group a onenote user-onenote-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-page-parent-notebook|users.onenote.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section-page-parent-notebook list-section

list-section a onenote user-onenote-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-page-parent-notebook|users.onenote.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section-page-parent-notebook list-section-group

list-section-group a onenote user-onenote-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-page-parent-notebook|users.onenote.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section-page-parent-notebook update

update a onenote user-onenote-section-group-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-page-parent-notebook|users.onenote.sectionGroups.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-group-section-parent-notebook create-section

create-section a onenote user-onenote-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-parent-notebook|users.onenote.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-group-section-parent-notebook create-section-group

create-section-group a onenote user-onenote-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-parent-notebook|users.onenote.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-section-group-section-parent-notebook get-section

get-section a onenote user-onenote-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-parent-notebook|users.onenote.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section-parent-notebook get-section-group

get-section-group a onenote user-onenote-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-parent-notebook|users.onenote.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section-parent-notebook list-section

list-section a onenote user-onenote-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-parent-notebook|users.onenote.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section-parent-notebook list-section-group

list-section-group a onenote user-onenote-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-parent-notebook|users.onenote.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-group-section-parent-notebook update

update a onenote user-onenote-section-group-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-group-section-parent-notebook|users.onenote.sectionGroups.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-page get-parent-notebook

get-parent-notebook a onenote user-onenote-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page|users.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page get-parent-section

get-parent-section a onenote user-onenote-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page|users.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section|GetParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page update

update a onenote user-onenote-section-page.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page|users.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateParentNotebook|
|update|UpdateParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|

### onenote user-onenote-section-page-parent-notebook create-section

create-section a onenote user-onenote-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook|users.onenote.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-page-parent-notebook create-section-group

create-section-group a onenote user-onenote-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook|users.onenote.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-section-page-parent-notebook get-section

get-section a onenote user-onenote-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook|users.onenote.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page-parent-notebook get-section-group

get-section-group a onenote user-onenote-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook|users.onenote.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page-parent-notebook list-section

list-section a onenote user-onenote-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook|users.onenote.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page-parent-notebook list-section-group

list-section-group a onenote user-onenote-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook|users.onenote.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page-parent-notebook update

update a onenote user-onenote-section-page-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook|users.onenote.sections.pages.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-page-parent-notebook-section-group create-section

create-section a onenote user-onenote-section-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook-section-group|users.onenote.sections.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-page-parent-notebook-section-group create-section-group

create-section-group a onenote user-onenote-section-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook-section-group|users.onenote.sections.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-section-page-parent-notebook-section-group get-parent-notebook

get-parent-notebook a onenote user-onenote-section-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook-section-group|users.onenote.sections.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page-parent-notebook-section-group get-parent-section-group

get-parent-section-group a onenote user-onenote-section-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook-section-group|users.onenote.sections.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page-parent-notebook-section-group get-section

get-section a onenote user-onenote-section-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook-section-group|users.onenote.sections.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page-parent-notebook-section-group get-section-group

get-section-group a onenote user-onenote-section-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook-section-group|users.onenote.sections.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page-parent-notebook-section-group list-section

list-section a onenote user-onenote-section-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook-section-group|users.onenote.sections.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page-parent-notebook-section-group list-section-group

list-section-group a onenote user-onenote-section-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook-section-group|users.onenote.sections.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-page-parent-notebook-section-group update

update a onenote user-onenote-section-page-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-page-parent-notebook-section-group|users.onenote.sections.pages.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|

### onenote user-onenote-section-parent-notebook create-section

create-section a onenote user-onenote-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook|users.onenote.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-parent-notebook create-section-group

create-section-group a onenote user-onenote-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook|users.onenote.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-section-parent-notebook get-section

get-section a onenote user-onenote-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook|users.onenote.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-notebook get-section-group

get-section-group a onenote user-onenote-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook|users.onenote.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-notebook list-section

list-section a onenote user-onenote-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook|users.onenote.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-notebook list-section-group

list-section-group a onenote user-onenote-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook|users.onenote.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-notebook update

update a onenote user-onenote-section-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook|users.onenote.sections.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-parent-notebook-section-group create-section

create-section a onenote user-onenote-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook-section-group|users.onenote.sections.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-parent-notebook-section-group create-section-group

create-section-group a onenote user-onenote-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook-section-group|users.onenote.sections.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-section-parent-notebook-section-group get-parent-notebook

get-parent-notebook a onenote user-onenote-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook-section-group|users.onenote.sections.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-notebook-section-group get-parent-section-group

get-parent-section-group a onenote user-onenote-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook-section-group|users.onenote.sections.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-notebook-section-group get-section

get-section a onenote user-onenote-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook-section-group|users.onenote.sections.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-notebook-section-group get-section-group

get-section-group a onenote user-onenote-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook-section-group|users.onenote.sections.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-notebook-section-group list-section

list-section a onenote user-onenote-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook-section-group|users.onenote.sections.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-notebook-section-group list-section-group

list-section-group a onenote user-onenote-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook-section-group|users.onenote.sections.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-notebook-section-group update

update a onenote user-onenote-section-parent-notebook-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-notebook-section-group|users.onenote.sections.parentNotebook.sectionGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--section-group-id1**|string|key: sectionGroup-id of sectionGroup|section_group_id1|sectionGroup-id1|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|

### onenote user-onenote-section-parent-section-group create-section

create-section a onenote user-onenote-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-parent-section-group create-section-group

create-section-group a onenote user-onenote-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-section-parent-section-group get-parent-notebook

get-parent-notebook a onenote user-onenote-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-section-group get-parent-section-group

get-parent-section-group a onenote user-onenote-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-section-group get-section

get-section a onenote user-onenote-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-section-group get-section-group

get-section-group a onenote user-onenote-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-section-group list-section

list-section a onenote user-onenote-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-section-group list-section-group

list-section-group a onenote user-onenote-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-section-group update

update a onenote user-onenote-section-parent-section-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|
|update|UpdateParentNotebook|
|update|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
|**--user-role**|choice|onenoteUserRole|user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|

### onenote user-onenote-section-parent-section-group-parent-notebook create-section

create-section a onenote user-onenote-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group-parent-notebook|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### onenote user-onenote-section-parent-section-group-parent-notebook create-section-group

create-section-group a onenote user-onenote-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group-parent-notebook|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|

### onenote user-onenote-section-parent-section-group-parent-notebook get-section

get-section a onenote user-onenote-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group-parent-notebook|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-section-group-parent-notebook get-section-group

get-section-group a onenote user-onenote-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group-parent-notebook|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-section-group-parent-notebook list-section

list-section a onenote user-onenote-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group-parent-notebook|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-section-group-parent-notebook list-section-group

list-section-group a onenote user-onenote-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group-parent-notebook|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### onenote user-onenote-section-parent-section-group-parent-notebook update

update a onenote user-onenote-section-parent-section-group-parent-notebook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|onenote user-onenote-section-parent-section-group-parent-notebook|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateSectionGroups|
|update|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--created-date-time**|date-time|The date and time when the page was created. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The name of the notebook.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|
