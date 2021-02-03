# Azure CLI Module Creation Report

### planner group delete

delete a planner group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner group get

get a planner group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetPlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group update

update a planner group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--plans**|array|Read-only. Nullable. Returns the plannerPlans owned by the group.|plans|plans|

### planner group-planner create-plan

create-plan a planner group-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner|groups.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-plan|CreatePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--details-shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### planner group-planner delete

delete a planner group-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner|groups.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner group-planner get-plan

get-plan a planner group-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner|groups.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-plan|GetPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner list-plan

list-plan a planner group-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner|groups.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-plan|ListPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner update-plan

update-plan a planner group-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner|groups.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-plan|UpdatePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--details-shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### planner group-planner-plan create-bucket

create-bucket a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-bucket|CreateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### planner group-planner-plan create-task

create-task a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner group-planner-plan delete

delete a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteBuckets|
|delete|DeleteTasks|
|delete|DeleteDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner group-planner-plan get-bucket

get-bucket a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket|GetBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan get-detail

get-detail a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan get-task

get-task a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan list-bucket

list-bucket a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-bucket|ListBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan list-task

list-task a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan update-bucket

update-bucket a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket|UpdateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### planner group-planner-plan update-detail

update-detail a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|

### planner group-planner-plan update-task

update-task a planner group-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner group-planner-plan-bucket create-task

create-task a planner group-planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket|groups.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner group-planner-plan-bucket delete

delete a planner group-planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket|groups.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner group-planner-plan-bucket get-task

get-task a planner group-planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket|groups.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan-bucket list-task

list-task a planner group-planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket|groups.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan-bucket update-task

update-task a planner group-planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket|groups.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner group-planner-plan-bucket-task delete

delete a planner group-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket-task|groups.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignedToTaskBoardFormat|
|delete|DeleteBucketTaskBoardFormat|
|delete|DeleteDetails|
|delete|DeleteProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner group-planner-plan-bucket-task get-assigned-to-task-board-format

get-assigned-to-task-board-format a planner group-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket-task|groups.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan-bucket-task get-bucket-task-board-format

get-bucket-task-board-format a planner group-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket-task|groups.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan-bucket-task get-detail

get-detail a planner group-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket-task|groups.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan-bucket-task get-progress-task-board-format

get-progress-task-board-format a planner group-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket-task|groups.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan-bucket-task update-assigned-to-task-board-format

update-assigned-to-task-board-format a planner group-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket-task|groups.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assigned-to-task-board-format|UpdateAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

### planner group-planner-plan-bucket-task update-bucket-task-board-format

update-bucket-task-board-format a planner group-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket-task|groups.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket-task-board-format|UpdateBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner group-planner-plan-bucket-task update-detail

update-detail a planner group-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket-task|groups.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

### planner group-planner-plan-bucket-task update-progress-task-board-format

update-progress-task-board-format a planner group-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-bucket-task|groups.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-progress-task-board-format|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner group-planner-plan-task delete

delete a planner group-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-task|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignedToTaskBoardFormat|
|delete|DeleteBucketTaskBoardFormat|
|delete|DeleteDetails|
|delete|DeleteProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner group-planner-plan-task get-assigned-to-task-board-format

get-assigned-to-task-board-format a planner group-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-task|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan-task get-bucket-task-board-format

get-bucket-task-board-format a planner group-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-task|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan-task get-detail

get-detail a planner group-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-task|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan-task get-progress-task-board-format

get-progress-task-board-format a planner group-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-task|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner group-planner-plan-task update-assigned-to-task-board-format

update-assigned-to-task-board-format a planner group-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-task|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assigned-to-task-board-format|UpdateAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

### planner group-planner-plan-task update-bucket-task-board-format

update-bucket-task-board-format a planner group-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-task|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket-task-board-format|UpdateBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner group-planner-plan-task update-detail

update-detail a planner group-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-task|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

### planner group-planner-plan-task update-progress-task-board-format

update-progress-task-board-format a planner group-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner group-planner-plan-task|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-progress-task-board-format|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner planner create-bucket

create-bucket a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-bucket|CreateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### planner planner create-plan

create-plan a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-plan|CreatePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--details-shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### planner planner create-task

create-task a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner planner delete

delete a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteBuckets|
|delete|DeletePlans|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner planner get

get a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetPlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner get-bucket

get-bucket a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket|GetBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner get-plan

get-plan a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-plan|GetPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner get-task

get-task a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner list-bucket

list-bucket a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-bucket|ListBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner list-plan

list-plan a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-plan|ListPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner list-task

list-task a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner update

update a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--buckets**|array|Read-only. Nullable. Returns a collection of the specified buckets|buckets|buckets|
|**--plans**|array|Read-only. Nullable. Returns a collection of the specified plans|plans|plans|
|**--tasks**|array|Read-only. Nullable. Returns a collection of the specified tasks|tasks|tasks|

### planner planner update-bucket

update-bucket a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket|UpdateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### planner planner update-plan

update-plan a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-plan|UpdatePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--details-shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### planner planner update-task

update-task a planner planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner|planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner planner-bucket create-task

create-task a planner planner-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket|planner.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner planner-bucket delete

delete a planner planner-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket|planner.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner planner-bucket get-task

get-task a planner planner-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket|planner.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-bucket list-task

list-task a planner planner-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket|planner.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-bucket update-task

update-task a planner planner-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket|planner.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner planner-bucket-task delete

delete a planner planner-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket-task|planner.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignedToTaskBoardFormat|
|delete|DeleteBucketTaskBoardFormat|
|delete|DeleteDetails|
|delete|DeleteProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner planner-bucket-task get-assigned-to-task-board-format

get-assigned-to-task-board-format a planner planner-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket-task|planner.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-bucket-task get-bucket-task-board-format

get-bucket-task-board-format a planner planner-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket-task|planner.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-bucket-task get-detail

get-detail a planner planner-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket-task|planner.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-bucket-task get-progress-task-board-format

get-progress-task-board-format a planner planner-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket-task|planner.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-bucket-task update-assigned-to-task-board-format

update-assigned-to-task-board-format a planner planner-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket-task|planner.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assigned-to-task-board-format|UpdateAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

### planner planner-bucket-task update-bucket-task-board-format

update-bucket-task-board-format a planner planner-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket-task|planner.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket-task-board-format|UpdateBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner planner-bucket-task update-detail

update-detail a planner planner-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket-task|planner.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

### planner planner-bucket-task update-progress-task-board-format

update-progress-task-board-format a planner planner-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-bucket-task|planner.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-progress-task-board-format|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner planner-plan create-bucket

create-bucket a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-bucket|CreateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### planner planner-plan create-task

create-task a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner planner-plan delete

delete a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteBuckets|
|delete|DeleteTasks|
|delete|DeleteDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner planner-plan get-bucket

get-bucket a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket|GetBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan get-detail

get-detail a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan get-task

get-task a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan list-bucket

list-bucket a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-bucket|ListBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan list-task

list-task a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan update-bucket

update-bucket a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket|UpdateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### planner planner-plan update-detail

update-detail a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|

### planner planner-plan update-task

update-task a planner planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan|planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner planner-plan-bucket create-task

create-task a planner planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket|planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner planner-plan-bucket delete

delete a planner planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket|planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner planner-plan-bucket get-task

get-task a planner planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket|planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan-bucket list-task

list-task a planner planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket|planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan-bucket update-task

update-task a planner planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket|planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner planner-plan-bucket-task delete

delete a planner planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket-task|planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignedToTaskBoardFormat|
|delete|DeleteBucketTaskBoardFormat|
|delete|DeleteDetails|
|delete|DeleteProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner planner-plan-bucket-task get-assigned-to-task-board-format

get-assigned-to-task-board-format a planner planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket-task|planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan-bucket-task get-bucket-task-board-format

get-bucket-task-board-format a planner planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket-task|planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan-bucket-task get-detail

get-detail a planner planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket-task|planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan-bucket-task get-progress-task-board-format

get-progress-task-board-format a planner planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket-task|planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan-bucket-task update-assigned-to-task-board-format

update-assigned-to-task-board-format a planner planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket-task|planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assigned-to-task-board-format|UpdateAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

### planner planner-plan-bucket-task update-bucket-task-board-format

update-bucket-task-board-format a planner planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket-task|planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket-task-board-format|UpdateBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner planner-plan-bucket-task update-detail

update-detail a planner planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket-task|planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

### planner planner-plan-bucket-task update-progress-task-board-format

update-progress-task-board-format a planner planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-bucket-task|planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-progress-task-board-format|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner planner-plan-task delete

delete a planner planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-task|planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignedToTaskBoardFormat|
|delete|DeleteBucketTaskBoardFormat|
|delete|DeleteDetails|
|delete|DeleteProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner planner-plan-task get-assigned-to-task-board-format

get-assigned-to-task-board-format a planner planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-task|planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan-task get-bucket-task-board-format

get-bucket-task-board-format a planner planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-task|planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan-task get-detail

get-detail a planner planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-task|planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan-task get-progress-task-board-format

get-progress-task-board-format a planner planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-task|planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-plan-task update-assigned-to-task-board-format

update-assigned-to-task-board-format a planner planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-task|planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assigned-to-task-board-format|UpdateAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

### planner planner-plan-task update-bucket-task-board-format

update-bucket-task-board-format a planner planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-task|planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket-task-board-format|UpdateBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner planner-plan-task update-detail

update-detail a planner planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-task|planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

### planner planner-plan-task update-progress-task-board-format

update-progress-task-board-format a planner planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-plan-task|planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-progress-task-board-format|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner planner-task delete

delete a planner planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-task|planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignedToTaskBoardFormat|
|delete|DeleteBucketTaskBoardFormat|
|delete|DeleteDetails|
|delete|DeleteProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner planner-task get-assigned-to-task-board-format

get-assigned-to-task-board-format a planner planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-task|planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-task get-bucket-task-board-format

get-bucket-task-board-format a planner planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-task|planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-task get-detail

get-detail a planner planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-task|planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-task get-progress-task-board-format

get-progress-task-board-format a planner planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-task|planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner planner-task update-assigned-to-task-board-format

update-assigned-to-task-board-format a planner planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-task|planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assigned-to-task-board-format|UpdateAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

### planner planner-task update-bucket-task-board-format

update-bucket-task-board-format a planner planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-task|planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket-task-board-format|UpdateBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner planner-task update-detail

update-detail a planner planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-task|planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

### planner planner-task update-progress-task-board-format

update-progress-task-board-format a planner planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner planner-task|planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-progress-task-board-format|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner user delete

delete a planner user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner user get

get a planner user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetPlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user update

update a planner user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--plans**|array|Read-only. Nullable. Returns the plannerTasks assigned to the user.|plans|plans|
|**--tasks**|array|Read-only. Nullable. Returns the plannerPlans shared with the user.|tasks|tasks|

### planner user-planner create-plan

create-plan a planner user-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-plan|CreatePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--details-shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### planner user-planner create-task

create-task a planner user-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner user-planner delete

delete a planner user-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeletePlans|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner user-planner get-plan

get-plan a planner user-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-plan|GetPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner get-task

get-task a planner user-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner list-plan

list-plan a planner user-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-plan|ListPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner list-task

list-task a planner user-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner update-plan

update-plan a planner user-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-plan|UpdatePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--details-shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### planner user-planner update-task

update-task a planner user-planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner user-planner-plan create-bucket

create-bucket a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-bucket|CreateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### planner user-planner-plan create-task

create-task a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner user-planner-plan delete

delete a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteBuckets|
|delete|DeleteTasks|
|delete|DeleteDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner user-planner-plan get-bucket

get-bucket a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket|GetBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan get-detail

get-detail a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan get-task

get-task a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan list-bucket

list-bucket a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-bucket|ListBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan list-task

list-task a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan update-bucket

update-bucket a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket|UpdateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### planner user-planner-plan update-detail

update-detail a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|

### planner user-planner-plan update-task

update-task a planner user-planner-plan.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner user-planner-plan-bucket create-task

create-task a planner user-planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket|users.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner user-planner-plan-bucket delete

delete a planner user-planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket|users.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner user-planner-plan-bucket get-task

get-task a planner user-planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket|users.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan-bucket list-task

list-task a planner user-planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket|users.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan-bucket update-task

update-task a planner user-planner-plan-bucket.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket|users.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--active-checklist-item-count**|integer|Number of checklist items with value set to false, representing incomplete items.|active_checklist_item_count|activeChecklistItemCount|
|**--applied-categories**|dictionary|plannerAppliedCategories|applied_categories|appliedCategories|
|**--assignee-priority**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|assignee_priority|assigneePriority|
|**--assignments**|dictionary|plannerAssignments|assignments|assignments|
|**--bucket-id**|string|Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.|bucket_id|bucketId|
|**--checklist-item-count**|integer|Number of checklist items that are present on the task.|checklist_item_count|checklistItemCount|
|**--completed-date-time**|date-time|Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|completed_date_time|completedDateTime|
|**--conversation-thread-id**|string|Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.|conversation_thread_id|conversationThreadId|
|**--created-date-time**|date-time|Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--due-date-time**|date-time|Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|due_date_time|dueDateTime|
|**--has-description**|boolean|Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.|has_description|hasDescription|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--percent-complete**|integer|Percentage of task completion. When set to 100, the task is considered completed.|percent_complete|percentComplete|
|**--plan-id**|string|Plan ID to which the task belongs.|plan_id|planId|
|**--preview-type**|choice||preview_type|previewType|
|**--reference-count**|integer|Number of external references that exist on the task.|reference_count|referenceCount|
|**--start-date-time**|date-time|Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--title**|string|Title of the task.|title|title|
|**--bucket-task-board-format**|object|plannerBucketTaskBoardTaskFormat|bucket_task_board_format|bucketTaskBoardFormat|
|**--progress-task-board-format**|object|plannerProgressTaskBoardTaskFormat|progress_task_board_format|progressTaskBoardFormat|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--details-description**|string|Description of the task|description|description|
|**--details-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--details-references**|dictionary|plannerExternalReferences|references|references|
|**--assigned-to-task-board-format-id**|string|Read-only.|id1|id|
|**--assigned-to-task-board-format-order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--assigned-to-task-board-format-unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|
|**--completed-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--completed-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--completed-by-user**|object|identity|microsoft_graph_identity_user|user|

### planner user-planner-plan-bucket-task delete

delete a planner user-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket-task|users.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignedToTaskBoardFormat|
|delete|DeleteBucketTaskBoardFormat|
|delete|DeleteDetails|
|delete|DeleteProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner user-planner-plan-bucket-task get-assigned-to-task-board-format

get-assigned-to-task-board-format a planner user-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket-task|users.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan-bucket-task get-bucket-task-board-format

get-bucket-task-board-format a planner user-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket-task|users.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan-bucket-task get-detail

get-detail a planner user-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket-task|users.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan-bucket-task get-progress-task-board-format

get-progress-task-board-format a planner user-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket-task|users.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan-bucket-task update-assigned-to-task-board-format

update-assigned-to-task-board-format a planner user-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket-task|users.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assigned-to-task-board-format|UpdateAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

### planner user-planner-plan-bucket-task update-bucket-task-board-format

update-bucket-task-board-format a planner user-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket-task|users.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket-task-board-format|UpdateBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner user-planner-plan-bucket-task update-detail

update-detail a planner user-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket-task|users.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

### planner user-planner-plan-bucket-task update-progress-task-board-format

update-progress-task-board-format a planner user-planner-plan-bucket-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-bucket-task|users.planner.plans.buckets.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-progress-task-board-format|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner user-planner-plan-task delete

delete a planner user-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-task|users.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignedToTaskBoardFormat|
|delete|DeleteBucketTaskBoardFormat|
|delete|DeleteDetails|
|delete|DeleteProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner user-planner-plan-task get-assigned-to-task-board-format

get-assigned-to-task-board-format a planner user-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-task|users.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan-task get-bucket-task-board-format

get-bucket-task-board-format a planner user-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-task|users.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan-task get-detail

get-detail a planner user-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-task|users.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan-task get-progress-task-board-format

get-progress-task-board-format a planner user-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-task|users.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-plan-task update-assigned-to-task-board-format

update-assigned-to-task-board-format a planner user-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-task|users.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assigned-to-task-board-format|UpdateAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

### planner user-planner-plan-task update-bucket-task-board-format

update-bucket-task-board-format a planner user-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-task|users.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket-task-board-format|UpdateBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner user-planner-plan-task update-detail

update-detail a planner user-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-task|users.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

### planner user-planner-plan-task update-progress-task-board-format

update-progress-task-board-format a planner user-planner-plan-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-plan-task|users.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-progress-task-board-format|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner user-planner-task delete

delete a planner user-planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-task|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignedToTaskBoardFormat|
|delete|DeleteBucketTaskBoardFormat|
|delete|DeleteDetails|
|delete|DeleteProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### planner user-planner-task get-assigned-to-task-board-format

get-assigned-to-task-board-format a planner user-planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-task|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-task get-bucket-task-board-format

get-bucket-task-board-format a planner user-planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-task|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-task get-detail

get-detail a planner user-planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-task|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-task get-progress-task-board-format

get-progress-task-board-format a planner user-planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-task|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner user-planner-task update-assigned-to-task-board-format

update-assigned-to-task-board-format a planner user-planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-task|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assigned-to-task-board-format|UpdateAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

### planner user-planner-task update-bucket-task-board-format

update-bucket-task-board-format a planner user-planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-task|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket-task-board-format|UpdateBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### planner user-planner-task update-detail

update-detail a planner user-planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-task|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

### planner user-planner-task update-progress-task-board-format

update-progress-task-board-format a planner user-planner-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner user-planner-task|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-progress-task-board-format|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|
