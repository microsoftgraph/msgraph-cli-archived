# Azure CLI Module Creation Report

### groupsplanner create-bucket

create-bucket a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-bucket|CreateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### groupsplanner create-plan

create-plan a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-plan|CreatePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--contexts**|any|Any object|contexts|contexts|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--details-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--details-shared-with**|any|Any object|shared_with|sharedWith|
|**--details-category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--details-context-details**|any|Any object|context_details|contextDetails|
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

### groupsplanner create-task

create-task a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: plannerBucket-id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--body**|object|New navigation property|body|body|

### groupsplanner get-assigned-to-task-board-format

get-assigned-to-task-board-format a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner get-bucket

get-bucket a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket|GetBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: plannerBucket-id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner get-bucket-task-board-format

get-bucket-task-board-format a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner get-detail

get-detail a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner get-plan

get-plan a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-plan|GetPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner get-planner

get-planner a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-planner|GetPlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner get-progress-task-board-format

get-progress-task-board-format a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner get-task

get-task a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: plannerBucket-id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner list-bucket

list-bucket a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-bucket|ListBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner list-plan

list-plan a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-plan|ListPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner list-task

list-task a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: plannerBucket-id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### groupsplanner update

update a groupsplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|groupsplanner|groups.planner.plans.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAssignedToTaskBoardFormat|
|update|UpdateBucketTaskBoardFormat|
|update|UpdateDetails|
|update|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: group-id of group|group_id|group-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--order-hints-by-assignee**|any|Any object|order_hints_by_assignee|orderHintsByAssignee|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|any|Any object|references|references|
|**--checklist**|any|Any object|checklist|checklist|
