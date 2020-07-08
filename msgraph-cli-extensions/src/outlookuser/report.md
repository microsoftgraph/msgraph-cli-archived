# Azure CLI Module Creation Report

### outlookuser user get-outlook

get-outlook a outlookuser user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-outlook|GetOutlook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user update

update a outlookuser user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateOutlook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--master-categories**|array|A list of categories defined for the user.|master_categories|masterCategories|
|**--task-groups**|array||task_groups|taskGroups|
|**--task-folders**|array||task_folders|taskFolders|
|**--tasks**|array||tasks|tasks|

### outlookuser user-outlook create-master-category

create-master-category a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-master-category|CreateMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.|display_name|displayName|
|**--color**|choice|categoryColor|color|color|

### outlookuser user-outlook create-task

create-task a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice|importance|importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice|sensitivity|sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice|taskStatus|status|status|
|**--subject**|string||subject|subject|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--attachments**|array||attachments|attachments|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### outlookuser user-outlook create-task-folder

create-task-folder a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-folder|CreateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--name**|string||name|name|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--tasks**|array||tasks|tasks|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|

### outlookuser user-outlook create-task-group

create-task-group a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-group|CreateTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--is-default-group**|boolean||is_default_group|isDefaultGroup|
|**--name**|string||name|name|
|**--group-key**|uuid||group_key|groupKey|
|**--task-folders**|array||task_folders|taskFolders|

### outlookuser user-outlook get-master-category

get-master-category a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-master-category|GetMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-category-id**|string|key: outlookCategory-id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook get-task

get-task a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook get-task-folder

get-task-folder a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-folder|GetTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook get-task-group

get-task-group a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-group|GetTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook list-master-category

list-master-category a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-master-category|ListMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook list-task

list-task a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook list-task-folder

list-task-folder a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-folder|ListTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook list-task-group

list-task-group a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-group|ListTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook update

update a outlookuser user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateMasterCategories|
|update|UpdateTaskFolders|
|update|UpdateTaskGroups|
|update|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-category-id**|string|key: outlookCategory-id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.|display_name|displayName|
|**--color**|choice|categoryColor|color|color|
|**--change-key**|string||change_key|changeKey|
|**--name**|string||name|name|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--tasks**|array||tasks|tasks|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--is-default-group**|boolean||is_default_group|isDefaultGroup|
|**--group-key**|uuid||group_key|groupKey|
|**--task-folders**|array||task_folders|taskFolders|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice|importance|importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice|sensitivity|sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice|taskStatus|status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### outlookuser user-outlook-task create-attachment

create-attachment a outlookuser user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--size**|integer|The length of the attachment in bytes.|size|size|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|

### outlookuser user-outlook-task create-multi-value-extended-property

create-multi-value-extended-property a outlookuser user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### outlookuser user-outlook-task create-single-value-extended-property

create-single-value-extended-property a outlookuser user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### outlookuser user-outlook-task get-attachment

get-attachment a outlookuser user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: attachment-id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task get-multi-value-extended-property

get-multi-value-extended-property a outlookuser user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task get-single-value-extended-property

get-single-value-extended-property a outlookuser user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task list-attachment

list-attachment a outlookuser user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task list-multi-value-extended-property

list-multi-value-extended-property a outlookuser user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task list-single-value-extended-property

list-single-value-extended-property a outlookuser user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task update

update a outlookuser user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAttachments|
|update|UpdateMultiValueExtendedProperties|
|update|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: attachment-id of attachment|attachment_id|attachment-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--size**|integer|The length of the attachment in bytes.|size|size|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--value**|array|A collection of property values.|value|value|

### outlookuser user-outlook-task-folder create-multi-value-extended-property

create-multi-value-extended-property a outlookuser user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### outlookuser user-outlook-task-folder create-single-value-extended-property

create-single-value-extended-property a outlookuser user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### outlookuser user-outlook-task-folder create-task

create-task a outlookuser user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice|importance|importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice|sensitivity|sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice|taskStatus|status|status|
|**--subject**|string||subject|subject|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--attachments**|array||attachments|attachments|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### outlookuser user-outlook-task-folder get-multi-value-extended-property

get-multi-value-extended-property a outlookuser user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder get-single-value-extended-property

get-single-value-extended-property a outlookuser user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder get-task

get-task a outlookuser user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder list-multi-value-extended-property

list-multi-value-extended-property a outlookuser user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder list-single-value-extended-property

list-single-value-extended-property a outlookuser user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder list-task

list-task a outlookuser user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder update

update a outlookuser user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateMultiValueExtendedProperties|
|update|UpdateSingleValueExtendedProperties|
|update|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice|importance|importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice|sensitivity|sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice|taskStatus|status|status|
|**--subject**|string||subject|subject|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--attachments**|array||attachments|attachments|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### outlookuser user-outlook-task-folder-task create-attachment

create-attachment a outlookuser user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--size**|integer|The length of the attachment in bytes.|size|size|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|

### outlookuser user-outlook-task-folder-task create-multi-value-extended-property

create-multi-value-extended-property a outlookuser user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### outlookuser user-outlook-task-folder-task create-single-value-extended-property

create-single-value-extended-property a outlookuser user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### outlookuser user-outlook-task-folder-task get-attachment

get-attachment a outlookuser user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: attachment-id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder-task get-multi-value-extended-property

get-multi-value-extended-property a outlookuser user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder-task get-single-value-extended-property

get-single-value-extended-property a outlookuser user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder-task list-attachment

list-attachment a outlookuser user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder-task list-multi-value-extended-property

list-multi-value-extended-property a outlookuser user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder-task list-single-value-extended-property

list-single-value-extended-property a outlookuser user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-folder-task update

update a outlookuser user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAttachments|
|update|UpdateMultiValueExtendedProperties|
|update|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: attachment-id of attachment|attachment_id|attachment-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--size**|integer|The length of the attachment in bytes.|size|size|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--value**|array|A collection of property values.|value|value|

### outlookuser user-outlook-task-group create-task-folder

create-task-folder a outlookuser user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-folder|CreateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--name**|string||name|name|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--tasks**|array||tasks|tasks|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|

### outlookuser user-outlook-task-group get-task-folder

get-task-folder a outlookuser user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-folder|GetTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group list-task-folder

list-task-folder a outlookuser user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-folder|ListTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group update

update a outlookuser user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--name**|string||name|name|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--tasks**|array||tasks|tasks|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|

### outlookuser user-outlook-task-group-task-folder create-multi-value-extended-property

create-multi-value-extended-property a outlookuser user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### outlookuser user-outlook-task-group-task-folder create-single-value-extended-property

create-single-value-extended-property a outlookuser user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### outlookuser user-outlook-task-group-task-folder create-task

create-task a outlookuser user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice|importance|importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice|sensitivity|sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice|taskStatus|status|status|
|**--subject**|string||subject|subject|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--attachments**|array||attachments|attachments|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### outlookuser user-outlook-task-group-task-folder get-multi-value-extended-property

get-multi-value-extended-property a outlookuser user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder get-single-value-extended-property

get-single-value-extended-property a outlookuser user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder get-task

get-task a outlookuser user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder list-multi-value-extended-property

list-multi-value-extended-property a outlookuser user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder list-single-value-extended-property

list-single-value-extended-property a outlookuser user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder list-task

list-task a outlookuser user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder update

update a outlookuser user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateMultiValueExtendedProperties|
|update|UpdateSingleValueExtendedProperties|
|update|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice|importance|importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice|sensitivity|sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice|taskStatus|status|status|
|**--subject**|string||subject|subject|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--attachments**|array||attachments|attachments|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### outlookuser user-outlook-task-group-task-folder-task create-attachment

create-attachment a outlookuser user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--size**|integer|The length of the attachment in bytes.|size|size|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|

### outlookuser user-outlook-task-group-task-folder-task create-multi-value-extended-property

create-multi-value-extended-property a outlookuser user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### outlookuser user-outlook-task-group-task-folder-task create-single-value-extended-property

create-single-value-extended-property a outlookuser user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### outlookuser user-outlook-task-group-task-folder-task get-attachment

get-attachment a outlookuser user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: attachment-id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder-task get-multi-value-extended-property

get-multi-value-extended-property a outlookuser user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder-task get-single-value-extended-property

get-single-value-extended-property a outlookuser user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder-task list-attachment

list-attachment a outlookuser user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder-task list-multi-value-extended-property

list-multi-value-extended-property a outlookuser user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder-task list-single-value-extended-property

list-single-value-extended-property a outlookuser user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### outlookuser user-outlook-task-group-task-folder-task update

update a outlookuser user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|outlookuser user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAttachments|
|update|UpdateMultiValueExtendedProperties|
|update|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: outlookTaskGroup-id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: outlookTaskFolder-id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: outlookTask-id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: attachment-id of attachment|attachment_id|attachment-id|
|**--multi-value-legacy-extended-property-id**|string|key: multiValueLegacyExtendedProperty-id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: singleValueLegacyExtendedProperty-id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--size**|integer|The length of the attachment in bytes.|size|size|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--value**|array|A collection of property values.|value|value|
