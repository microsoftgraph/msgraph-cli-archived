# Azure CLI Module Creation Report

### notes create-notebook

create-notebook a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-notebook|CreateNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
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
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--user-role**|choice||user_role|userRole|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### notes create-operation

create-operation a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-operation|CreateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The start time of the operation.|created_date_time|createdDateTime|
|**--last-action-date-time**|date-time|The time of the last action of the operation.|last_action_date_time|lastActionDateTime|
|**--status**|choice||status|status|
|**--error**|object|onenoteOperationError|error|error|
|**--percent-complete**|string|The operation percent complete if the operation is still in running status|percent_complete|percentComplete|
|**--resource-id**|string|The resource id.|resource_id|resourceId|
|**--resource-location**|string|The resource URI for the object. For example, the resource URI for a copied page or section.|resource_location|resourceLocation|

### notes create-page

create-page a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-page|CreatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--body**|object|New navigation property|body|body|

### notes create-resource

create-resource a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-resource|CreateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--content**|byte-array|The content stream|content|content|
|**--content-url**|string|The URL for downloading the content|content_url|contentUrl|

### notes create-section

create-section a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section|CreateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--body**|object|New navigation property|body|body|

### notes create-section-group

create-section-group a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-section-group|CreateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
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
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|

### notes delete

delete a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSectionGroups|
|delete|DeleteSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--if-match**|string|ETag|if_match|If-Match|

### notes get-notebook

get-notebook a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-notebook|GetNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes get-onenote

get-onenote a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-onenote|GetOnenote|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes get-operation

get-operation a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-operation|GetOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-operation-id**|string|key: id of onenoteOperation|onenote_operation_id|onenoteOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes get-page

get-page a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page|GetPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes get-page-content

get-page-content a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-page-content|GetPagesContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### notes get-parent-notebook

get-parent-notebook a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-notebook|GetParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes get-parent-section

get-parent-section a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section|GetParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes get-parent-section-group

get-parent-section-group a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-parent-section-group|GetParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes get-resource

get-resource a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-resource-id**|string|key: id of onenoteResource|onenote_resource_id|onenoteResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes get-resource-content

get-resource-content a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource-content|GetResourcesContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-resource-id**|string|key: id of onenoteResource|onenote_resource_id|onenoteResource-id|

### notes get-section

get-section a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section|GetSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes get-section-group

get-section-group a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-section-group|GetSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes list-notebook

list-notebook a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-notebook|ListNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes list-operation

list-operation a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-operation|ListOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes list-page

list-page a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-page|ListPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes list-resource

list-resource a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-resource|ListResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes list-section

list-section a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section|ListSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes list-section-group

list-section-group a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-section-group|ListSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### notes set-page-content

set-page-content a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-page-content|SetPagesContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--data**|binary|New media content.|data|data|

### notes set-resource-content

set-resource-content a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-resource-content|SetResourcesContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-resource-id**|string|key: id of onenoteResource|onenote_resource_id|onenoteResource-id|
|**--data**|binary|New media content.|data|data|

### notes update-notebook

update-notebook a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-notebook|UpdateNotebooks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
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
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--user-role**|choice||user_role|userRole|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### notes update-onenote

update-onenote a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-onenote|UpdateOnenote|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|pages|pages|
|**--resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|

### notes update-operation

update-operation a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-operation|UpdateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-operation-id**|string|key: id of onenoteOperation|onenote_operation_id|onenoteOperation-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The start time of the operation.|created_date_time|createdDateTime|
|**--last-action-date-time**|date-time|The time of the last action of the operation.|last_action_date_time|lastActionDateTime|
|**--status**|choice||status|status|
|**--error**|object|onenoteOperationError|error|error|
|**--percent-complete**|string|The operation percent complete if the operation is still in running status|percent_complete|percentComplete|
|**--resource-id**|string|The resource id.|resource_id|resourceId|
|**--resource-location**|string|The resource URI for the object. For example, the resource URI for a copied page or section.|resource_location|resourceLocation|

### notes update-page

update-page a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-page|UpdatePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--body**|object|New navigation property values|body|body|

### notes update-parent-notebook

update-parent-notebook a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-parent-notebook|UpdateParentNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
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
|**--is-shared**|boolean|Indicates whether the notebook is shared. If true, the contents of the notebook can be seen by people other than the owner. Read-only.|is_shared|isShared|
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the notebook. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the notebook. Read-only.|sections_url|sectionsUrl|
|**--user-role**|choice||user_role|userRole|
|**--section-groups**|array|The section groups in the notebook. Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in the notebook. Read-only. Nullable.|sections|sections|
|**--links-one-note-client-url**|object|externalLink|one_note_client_url|oneNoteClientUrl|
|**--links-one-note-web-url**|object|externalLink|one_note_web_url|oneNoteWebUrl|

### notes update-parent-section

update-parent-section a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-parent-section|UpdateParentSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--body**|object|New navigation property values|body|body|

### notes update-parent-section-group

update-parent-section-group a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-parent-section-group|UpdateParentSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
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
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|

### notes update-resource

update-resource a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-resource|UpdateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-resource-id**|string|key: id of onenoteResource|onenote_resource_id|onenoteResource-id|
|**--id**|string|Read-only.|id|id|
|**--self**|string|The endpoint where you can get details about the page. Read-only.|self|self|
|**--content**|byte-array|The content stream|content|content|
|**--content-url**|string|The URL for downloading the content|content_url|contentUrl|

### notes update-section

update-section a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-section|UpdateSections|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--body**|object|New navigation property values|body|body|

### notes update-section-group

update-section-group a notes.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|notes|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-section-group|UpdateSectionGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
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
|**--section-groups-url**|string|The URL for the sectionGroups navigation property, which returns all the section groups in the section group. Read-only.|section_groups_url|sectionGroupsUrl|
|**--sections-url**|string|The URL for the sections navigation property, which returns all the sections in the section group. Read-only.|sections_url|sectionsUrl|
|**--parent-notebook**|object|notebook|parent_notebook|parentNotebook|
|**--parent-section-group**|object|sectionGroup|parent_section_group|parentSectionGroup|
|**--section-groups**|array|The section groups in the section. Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in the section group. Read-only. Nullable.|sections|sections|
