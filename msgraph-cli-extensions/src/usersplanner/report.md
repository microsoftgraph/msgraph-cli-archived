# Azure CLI Module Creation Report

### usersplanner create-all

create-all a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-all|CreateAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

### usersplanner create-bucket

create-bucket a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-bucket|CreateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### usersplanner create-plan

create-plan a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-plan|CreatePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
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

### usersplanner create-task

create-task a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: plannerBucket-id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--body**|object|New navigation property|body|body|

### usersplanner get-all

get-all a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-all|GetAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-delta-id**|string|key: plannerDelta-id of plannerDelta|planner_delta_id|plannerDelta-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner get-assigned-to-task-board-format

get-assigned-to-task-board-format a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assigned-to-task-board-format|GetAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner get-bucket

get-bucket a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket|GetBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: plannerBucket-id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner get-bucket-task-board-format

get-bucket-task-board-format a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-bucket-task-board-format|GetBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner get-detail

get-detail a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-detail|GetDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner get-favorite-plan

get-favorite-plan a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-favorite-plan|GetFavoritePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner get-plan

get-plan a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-plan|GetPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner get-planner

get-planner a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-planner|GetPlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner get-progress-task-board-format

get-progress-task-board-format a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-progress-task-board-format|GetProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner get-recent-plan

get-recent-plan a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-recent-plan|GetRecentPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner get-task

get-task a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: plannerBucket-id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner list-all

list-all a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-all|ListAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner list-bucket

list-bucket a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-bucket|ListBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner list-favorite-plan

list-favorite-plan a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-favorite-plan|ListFavoritePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner list-plan

list-plan a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-plan|ListPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner list-recent-plan

list-recent-plan a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-recent-plan|ListRecentPlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner list-task

list-task a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: plannerBucket-id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### usersplanner update-all

update-all a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-all|UpdateAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-delta-id**|string|key: plannerDelta-id of plannerDelta|planner_delta_id|plannerDelta-id|
|**--id**|string|Read-only.|id|id|

### usersplanner update-assigned-to-task-board-format

update-assigned-to-task-board-format a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assigned-to-task-board-format|UpdateAssignedToTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--order-hints-by-assignee**|any|Any object|order_hints_by_assignee|orderHintsByAssignee|

### usersplanner update-bucket

update-bucket a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.plans|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket|UpdateBuckets|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: plannerBucket-id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

### usersplanner update-bucket-task-board-format

update-bucket-task-board-format a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-bucket-task-board-format|UpdateBucketTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### usersplanner update-detail

update-detail a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-detail|UpdateDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|any|Any object|references|references|
|**--checklist**|any|Any object|checklist|checklist|

### usersplanner update-plan

update-plan a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-plan|UpdatePlans|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
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

### usersplanner update-planner

update-planner a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-planner|UpdatePlanner|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--favorite-plan-references**|any|Any object|favorite_plan_references|favoritePlanReferences|
|**--recent-plan-references**|any|Any object|recent_plan_references|recentPlanReferences|
|**--tasks**|array|Read-only. Nullable. Returns the plannerPlans shared with the user.|tasks|tasks|
|**--plans**|array|Read-only. Nullable. Returns the plannerTasks assigned to the user.|plans|plans|
|**--favorite-plans**|array||favorite_plans|favoritePlans|
|**--recent-plans**|array||recent_plans|recentPlans|
|**--all**|array||all|all|

### usersplanner update-progress-task-board-format

update-progress-task-board-format a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-progress-task-board-format|UpdateProgressTaskBoardFormat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### usersplanner update-task

update-task a usersplanner.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersplanner|users.planner.plans.buckets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--planner-plan-id**|string|key: plannerPlan-id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: plannerBucket-id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: plannerTask-id of plannerTask|planner_task_id|plannerTask-id|
|**--body**|object|New navigation property values|body|body|
