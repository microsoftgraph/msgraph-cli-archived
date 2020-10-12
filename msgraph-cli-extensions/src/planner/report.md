# Azure CLI Module Creation Report

### planner create-bucket

create-bucket a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.plans|

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

### planner create-plan

create-plan a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner|

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

### planner create-task

create-task a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.plans.buckets|

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
|**--body**|object|New navigation property|body|body|

### planner delete

delete a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.tasks|

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

### planner get-assigned-to-task-board-format

get-assigned-to-task-board-format a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.tasks|

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

### planner get-bucket

get-bucket a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.plans|

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

### planner get-bucket-task-board-format

get-bucket-task-board-format a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.tasks|

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

### planner get-detail

get-detail a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.tasks|

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

### planner get-plan

get-plan a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner|

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

### planner get-planner

get-planner a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-planner|GetPlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### planner get-progress-task-board-format

get-progress-task-board-format a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.tasks|

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

### planner get-task

get-task a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.plans.buckets|

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

### planner list-bucket

list-bucket a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.plans|

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

### planner list-plan

list-plan a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner|

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

### planner list-task

list-task a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.plans.buckets|

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

### planner update-assigned-to-task-board-format

update-assigned-to-task-board-format a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.tasks|

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

### planner update-bucket

update-bucket a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.plans|

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

### planner update-bucket-task-board-format

update-bucket-task-board-format a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.tasks|

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

### planner update-detail

update-detail a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.tasks|

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

### planner update-plan

update-plan a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner|

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

### planner update-planner

update-planner a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-planner|UpdatePlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--plans**|array|Read-only. Nullable. Returns the plannerTasks assigned to the user.|plans|plans|
|**--tasks**|array|Read-only. Nullable. Returns the plannerPlans shared with the user.|tasks|tasks|

### planner update-progress-task-board-format

update-progress-task-board-format a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.tasks|

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

### planner update-task

update-task a planner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|planner|users.planner.plans.buckets|

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
|**--body**|object|New navigation property values|body|body|
