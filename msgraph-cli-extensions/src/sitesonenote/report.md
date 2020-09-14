# Azure CLI Module Creation Report

### sitesonenote create-notebook

create-notebook a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-notebook|CreateNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
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
|**--user-role**|choice||user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### sitesonenote create-operation

create-operation a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-operation|CreateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--id**|string|Read-only.|id|id|
|**--status**|choice||status|status|
|**--created-date-time**|date-time|The start time of the operation.|created_date_time|createdDateTime|
|**--last-action-date-time**|date-time|The time of the last action of the operation.|last_action_date_time|lastActionDateTime|
|**--resource-location**|string|The resource URI for the object. For example, the resource URI for a copied page or section.|resource_location|resourceLocation|
|**--resource-id**|string|The resource id.|resource_id|resourceId|
|**--error**|object|onenoteOperationError|error|error|
|**--percent-complete**|string|The operation percent complete if the operation is still in running status|percent_complete|percentComplete|

### sitesonenote create-page

create-page a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--body**|object|New navigation property|body|body|

### sitesonenote create-resource

create-resource a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-resource|CreateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--content**|byte-array|The content stream|content|content|
|**--content-url**|string|The URL for downloading the content|content_url|contentUrl|

### sitesonenote create-section

create-section a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
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

### sitesonenote create-section-group

create-section-group a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
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

### sitesonenote get-notebook

get-notebook a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-notebook|GetNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--notebook-id**|string|key: notebook-id of notebook|notebook_id|notebook-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote get-onenote

get-onenote a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-onenote|GetOnenote|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote get-operation

get-operation a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-operation|GetOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-operation-id**|string|key: onenoteOperation-id of onenoteOperation|onenote_operation_id|onenoteOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote get-page

get-page a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote get-parent-notebook

get-parent-notebook a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote get-parent-section

get-parent-section a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section|GetParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote get-parent-section-group

get-parent-section-group a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote get-resource

get-resource a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-resource-id**|string|key: onenoteResource-id of onenoteResource|onenote_resource_id|onenoteResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote get-section

get-section a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: onenoteSection-id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote get-section-group

get-section-group a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: sectionGroup-id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote list-notebook

list-notebook a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-notebook|ListNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote list-operation

list-operation a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-operation|ListOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote list-page

list-page a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote list-resource

list-resource a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-resource|ListResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote list-section

list-section a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote list-section-group

list-section-group a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### sitesonenote update-notebook

update-notebook a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-notebook|UpdateNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
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
|**--is-default**|boolean|Indicates whether this is the user's default notebook. Read-only.|is_default|isDefault|
|**--user-role**|choice||user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### sitesonenote update-onenote

update-onenote a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-onenote|UpdateOnenote|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--id**|string|Read-only.|id|id|
|**--notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|pages|pages|
|**--resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|

### sitesonenote update-operation

update-operation a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-operation|UpdateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-operation-id**|string|key: onenoteOperation-id of onenoteOperation|onenote_operation_id|onenoteOperation-id|
|**--id**|string|Read-only.|id|id|
|**--status**|choice||status|status|
|**--created-date-time**|date-time|The start time of the operation.|created_date_time|createdDateTime|
|**--last-action-date-time**|date-time|The time of the last action of the operation.|last_action_date_time|lastActionDateTime|
|**--resource-location**|string|The resource URI for the object. For example, the resource URI for a copied page or section.|resource_location|resourceLocation|
|**--resource-id**|string|The resource id.|resource_id|resourceId|
|**--error**|object|onenoteOperationError|error|error|
|**--percent-complete**|string|The operation percent complete if the operation is still in running status|percent_complete|percentComplete|

### sitesonenote update-page

update-page a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-page|UpdatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: onenotePage-id of onenotePage|onenote_page_id|onenotePage-id|
|**--body**|object|New navigation property values|body|body|

### sitesonenote update-parent-notebook

update-parent-notebook a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-parent-notebook|UpdateParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
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
|**--user-role**|choice||user_role|userRole|
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### sitesonenote update-parent-section

update-parent-section a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-parent-section|UpdateParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
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

### sitesonenote update-parent-section-group

update-parent-section-group a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-parent-section-group|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
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

### sitesonenote update-resource

update-resource a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-resource|UpdateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-resource-id**|string|key: onenoteResource-id of onenoteResource|onenote_resource_id|onenoteResource-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--content**|byte-array|The content stream|content|content|
|**--content-url**|string|The URL for downloading the content|content_url|contentUrl|

### sitesonenote update-section

update-section a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-section|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
|**--onenote-section-id**|string|key: onenoteSection-id of onenoteSection|onenote_section_id|onenoteSection-id|
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
|**--is-default**|boolean|Indicates whether this is the user's default section. Read-only.|is_default|isDefault|
|**--pages-url**|string|The pages endpoint where you can get details for all the pages in the section. Read-only.|pages_url|pagesUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--pages**|array|The collection of pages in the section.  Read-only. Nullable.|pages|pages|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### sitesonenote update-section-group

update-section-group a sitesonenote.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|sitesonenote|sites.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-section-group|UpdateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--site-id**|string|key: site-id of site|site_id|site-id|
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
