# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az planner_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az planner_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az planner group|groups|[commands](#CommandsIngroups)|
|az planner group-planner|groups.planner|[commands](#CommandsIngroups.planner)|
|az planner group-planner-plan|groups.planner.plans|[commands](#CommandsIngroups.planner.plans)|
|az planner group-planner-plan-bucket|groups.planner.plans.buckets|[commands](#CommandsIngroups.planner.plans.buckets)|
|az planner group-planner-plan-bucket-task|groups.planner.plans.buckets.tasks|[commands](#CommandsIngroups.planner.plans.buckets.tasks)|
|az planner group-planner-plan-task|groups.planner.plans.tasks|[commands](#CommandsIngroups.planner.plans.tasks)|
|az planner planner|planner.planner|[commands](#CommandsInplanner.planner)|
|az planner planner|planner|[commands](#CommandsInplanner)|
|az planner planner-bucket|planner.buckets|[commands](#CommandsInplanner.buckets)|
|az planner planner-bucket-task|planner.buckets.tasks|[commands](#CommandsInplanner.buckets.tasks)|
|az planner planner-plan|planner.plans|[commands](#CommandsInplanner.plans)|
|az planner planner-plan-bucket|planner.plans.buckets|[commands](#CommandsInplanner.plans.buckets)|
|az planner planner-plan-bucket-task|planner.plans.buckets.tasks|[commands](#CommandsInplanner.plans.buckets.tasks)|
|az planner planner-plan-task|planner.plans.tasks|[commands](#CommandsInplanner.plans.tasks)|
|az planner planner-task|planner.tasks|[commands](#CommandsInplanner.tasks)|
|az planner user|users|[commands](#CommandsInusers)|
|az planner user-planner|users.planner|[commands](#CommandsInusers.planner)|
|az planner user-planner-plan|users.planner.plans|[commands](#CommandsInusers.planner.plans)|
|az planner user-planner-plan-bucket|users.planner.plans.buckets|[commands](#CommandsInusers.planner.plans.buckets)|
|az planner user-planner-plan-bucket-task|users.planner.plans.buckets.tasks|[commands](#CommandsInusers.planner.plans.buckets.tasks)|
|az planner user-planner-plan-task|users.planner.plans.tasks|[commands](#CommandsInusers.planner.plans.tasks)|
|az planner user-planner-task|users.planner.tasks|[commands](#CommandsInusers.planner.tasks)|

## COMMANDS
### <a name="CommandsIngroups">Commands in `az planner group` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner group delete-planner](#groupsDeletePlanner)|DeletePlanner|[Parameters](#ParametersgroupsDeletePlanner)|Not Found|
|[az planner group show-planner](#groupsGetPlanner)|GetPlanner|[Parameters](#ParametersgroupsGetPlanner)|Not Found|
|[az planner group update-planner](#groupsUpdatePlanner)|UpdatePlanner|[Parameters](#ParametersgroupsUpdatePlanner)|Not Found|

### <a name="CommandsIngroups.planner">Commands in `az planner group-planner` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner group-planner create-plan](#groups.plannerCreatePlans)|CreatePlans|[Parameters](#Parametersgroups.plannerCreatePlans)|Not Found|
|[az planner group-planner delete-plan](#groups.plannerDeletePlans)|DeletePlans|[Parameters](#Parametersgroups.plannerDeletePlans)|Not Found|
|[az planner group-planner list-plan](#groups.plannerListPlans)|ListPlans|[Parameters](#Parametersgroups.plannerListPlans)|Not Found|
|[az planner group-planner show-plan](#groups.plannerGetPlans)|GetPlans|[Parameters](#Parametersgroups.plannerGetPlans)|Not Found|
|[az planner group-planner update-plan](#groups.plannerUpdatePlans)|UpdatePlans|[Parameters](#Parametersgroups.plannerUpdatePlans)|Not Found|

### <a name="CommandsIngroups.planner.plans">Commands in `az planner group-planner-plan` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner group-planner-plan create-bucket](#groups.planner.plansCreateBuckets)|CreateBuckets|[Parameters](#Parametersgroups.planner.plansCreateBuckets)|Not Found|
|[az planner group-planner-plan create-task](#groups.planner.plansCreateTasks)|CreateTasks|[Parameters](#Parametersgroups.planner.plansCreateTasks)|Not Found|
|[az planner group-planner-plan delete-bucket](#groups.planner.plansDeleteBuckets)|DeleteBuckets|[Parameters](#Parametersgroups.planner.plansDeleteBuckets)|Not Found|
|[az planner group-planner-plan delete-detail](#groups.planner.plansDeleteDetails)|DeleteDetails|[Parameters](#Parametersgroups.planner.plansDeleteDetails)|Not Found|
|[az planner group-planner-plan delete-task](#groups.planner.plansDeleteTasks)|DeleteTasks|[Parameters](#Parametersgroups.planner.plansDeleteTasks)|Not Found|
|[az planner group-planner-plan list-bucket](#groups.planner.plansListBuckets)|ListBuckets|[Parameters](#Parametersgroups.planner.plansListBuckets)|Not Found|
|[az planner group-planner-plan list-task](#groups.planner.plansListTasks)|ListTasks|[Parameters](#Parametersgroups.planner.plansListTasks)|Not Found|
|[az planner group-planner-plan show-bucket](#groups.planner.plansGetBuckets)|GetBuckets|[Parameters](#Parametersgroups.planner.plansGetBuckets)|Not Found|
|[az planner group-planner-plan show-detail](#groups.planner.plansGetDetails)|GetDetails|[Parameters](#Parametersgroups.planner.plansGetDetails)|Not Found|
|[az planner group-planner-plan show-task](#groups.planner.plansGetTasks)|GetTasks|[Parameters](#Parametersgroups.planner.plansGetTasks)|Not Found|
|[az planner group-planner-plan update-bucket](#groups.planner.plansUpdateBuckets)|UpdateBuckets|[Parameters](#Parametersgroups.planner.plansUpdateBuckets)|Not Found|
|[az planner group-planner-plan update-detail](#groups.planner.plansUpdateDetails)|UpdateDetails|[Parameters](#Parametersgroups.planner.plansUpdateDetails)|Not Found|
|[az planner group-planner-plan update-task](#groups.planner.plansUpdateTasks)|UpdateTasks|[Parameters](#Parametersgroups.planner.plansUpdateTasks)|Not Found|

### <a name="CommandsIngroups.planner.plans.buckets">Commands in `az planner group-planner-plan-bucket` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner group-planner-plan-bucket create-task](#groups.planner.plans.bucketsCreateTasks)|CreateTasks|[Parameters](#Parametersgroups.planner.plans.bucketsCreateTasks)|Not Found|
|[az planner group-planner-plan-bucket delete-task](#groups.planner.plans.bucketsDeleteTasks)|DeleteTasks|[Parameters](#Parametersgroups.planner.plans.bucketsDeleteTasks)|Not Found|
|[az planner group-planner-plan-bucket list-task](#groups.planner.plans.bucketsListTasks)|ListTasks|[Parameters](#Parametersgroups.planner.plans.bucketsListTasks)|Not Found|
|[az planner group-planner-plan-bucket show-task](#groups.planner.plans.bucketsGetTasks)|GetTasks|[Parameters](#Parametersgroups.planner.plans.bucketsGetTasks)|Not Found|
|[az planner group-planner-plan-bucket update-task](#groups.planner.plans.bucketsUpdateTasks)|UpdateTasks|[Parameters](#Parametersgroups.planner.plans.bucketsUpdateTasks)|Not Found|

### <a name="CommandsIngroups.planner.plans.buckets.tasks">Commands in `az planner group-planner-plan-bucket-task` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner group-planner-plan-bucket-task delete-assigned-to-task-board-format](#groups.planner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat)|DeleteAssignedToTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-bucket-task delete-bucket-task-board-format](#groups.planner.plans.buckets.tasksDeleteBucketTaskBoardFormat)|DeleteBucketTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.buckets.tasksDeleteBucketTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-bucket-task delete-detail](#groups.planner.plans.buckets.tasksDeleteDetails)|DeleteDetails|[Parameters](#Parametersgroups.planner.plans.buckets.tasksDeleteDetails)|Not Found|
|[az planner group-planner-plan-bucket-task delete-progress-task-board-format](#groups.planner.plans.buckets.tasksDeleteProgressTaskBoardFormat)|DeleteProgressTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.buckets.tasksDeleteProgressTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-bucket-task show-assigned-to-task-board-format](#groups.planner.plans.buckets.tasksGetAssignedToTaskBoardFormat)|GetAssignedToTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.buckets.tasksGetAssignedToTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-bucket-task show-bucket-task-board-format](#groups.planner.plans.buckets.tasksGetBucketTaskBoardFormat)|GetBucketTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.buckets.tasksGetBucketTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-bucket-task show-detail](#groups.planner.plans.buckets.tasksGetDetails)|GetDetails|[Parameters](#Parametersgroups.planner.plans.buckets.tasksGetDetails)|Not Found|
|[az planner group-planner-plan-bucket-task show-progress-task-board-format](#groups.planner.plans.buckets.tasksGetProgressTaskBoardFormat)|GetProgressTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.buckets.tasksGetProgressTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-bucket-task update-assigned-to-task-board-format](#groups.planner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat)|UpdateAssignedToTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-bucket-task update-bucket-task-board-format](#groups.planner.plans.buckets.tasksUpdateBucketTaskBoardFormat)|UpdateBucketTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.buckets.tasksUpdateBucketTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-bucket-task update-detail](#groups.planner.plans.buckets.tasksUpdateDetails)|UpdateDetails|[Parameters](#Parametersgroups.planner.plans.buckets.tasksUpdateDetails)|Not Found|
|[az planner group-planner-plan-bucket-task update-progress-task-board-format](#groups.planner.plans.buckets.tasksUpdateProgressTaskBoardFormat)|UpdateProgressTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.buckets.tasksUpdateProgressTaskBoardFormat)|Not Found|

### <a name="CommandsIngroups.planner.plans.tasks">Commands in `az planner group-planner-plan-task` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner group-planner-plan-task delete-assigned-to-task-board-format](#groups.planner.plans.tasksDeleteAssignedToTaskBoardFormat)|DeleteAssignedToTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.tasksDeleteAssignedToTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-task delete-bucket-task-board-format](#groups.planner.plans.tasksDeleteBucketTaskBoardFormat)|DeleteBucketTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.tasksDeleteBucketTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-task delete-detail](#groups.planner.plans.tasksDeleteDetails)|DeleteDetails|[Parameters](#Parametersgroups.planner.plans.tasksDeleteDetails)|Not Found|
|[az planner group-planner-plan-task delete-progress-task-board-format](#groups.planner.plans.tasksDeleteProgressTaskBoardFormat)|DeleteProgressTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.tasksDeleteProgressTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-task show-assigned-to-task-board-format](#groups.planner.plans.tasksGetAssignedToTaskBoardFormat)|GetAssignedToTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.tasksGetAssignedToTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-task show-bucket-task-board-format](#groups.planner.plans.tasksGetBucketTaskBoardFormat)|GetBucketTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.tasksGetBucketTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-task show-detail](#groups.planner.plans.tasksGetDetails)|GetDetails|[Parameters](#Parametersgroups.planner.plans.tasksGetDetails)|Not Found|
|[az planner group-planner-plan-task show-progress-task-board-format](#groups.planner.plans.tasksGetProgressTaskBoardFormat)|GetProgressTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.tasksGetProgressTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-task update-assigned-to-task-board-format](#groups.planner.plans.tasksUpdateAssignedToTaskBoardFormat)|UpdateAssignedToTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.tasksUpdateAssignedToTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-task update-bucket-task-board-format](#groups.planner.plans.tasksUpdateBucketTaskBoardFormat)|UpdateBucketTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.tasksUpdateBucketTaskBoardFormat)|Not Found|
|[az planner group-planner-plan-task update-detail](#groups.planner.plans.tasksUpdateDetails)|UpdateDetails|[Parameters](#Parametersgroups.planner.plans.tasksUpdateDetails)|Not Found|
|[az planner group-planner-plan-task update-progress-task-board-format](#groups.planner.plans.tasksUpdateProgressTaskBoardFormat)|UpdateProgressTaskBoardFormat|[Parameters](#Parametersgroups.planner.plans.tasksUpdateProgressTaskBoardFormat)|Not Found|

### <a name="CommandsInplanner.planner">Commands in `az planner planner` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner planner create](#planner.plannerUpdatePlanner)|UpdatePlanner|[Parameters](#Parametersplanner.plannerUpdatePlanner)|Not Found|
|[az planner planner show-planner](#planner.plannerGetPlanner)|GetPlanner|[Parameters](#Parametersplanner.plannerGetPlanner)|Not Found|

### <a name="CommandsInplanner">Commands in `az planner planner` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner planner create-bucket](#plannerCreateBuckets)|CreateBuckets|[Parameters](#ParametersplannerCreateBuckets)|Not Found|
|[az planner planner create-plan](#plannerCreatePlans)|CreatePlans|[Parameters](#ParametersplannerCreatePlans)|Not Found|
|[az planner planner create-task](#plannerCreateTasks)|CreateTasks|[Parameters](#ParametersplannerCreateTasks)|Not Found|
|[az planner planner delete-bucket](#plannerDeleteBuckets)|DeleteBuckets|[Parameters](#ParametersplannerDeleteBuckets)|Not Found|
|[az planner planner delete-plan](#plannerDeletePlans)|DeletePlans|[Parameters](#ParametersplannerDeletePlans)|Not Found|
|[az planner planner delete-task](#plannerDeleteTasks)|DeleteTasks|[Parameters](#ParametersplannerDeleteTasks)|Not Found|
|[az planner planner list-bucket](#plannerListBuckets)|ListBuckets|[Parameters](#ParametersplannerListBuckets)|Not Found|
|[az planner planner list-plan](#plannerListPlans)|ListPlans|[Parameters](#ParametersplannerListPlans)|Not Found|
|[az planner planner list-task](#plannerListTasks)|ListTasks|[Parameters](#ParametersplannerListTasks)|Not Found|
|[az planner planner show-bucket](#plannerGetBuckets)|GetBuckets|[Parameters](#ParametersplannerGetBuckets)|Not Found|
|[az planner planner show-plan](#plannerGetPlans)|GetPlans|[Parameters](#ParametersplannerGetPlans)|Not Found|
|[az planner planner show-task](#plannerGetTasks)|GetTasks|[Parameters](#ParametersplannerGetTasks)|Not Found|
|[az planner planner update-bucket](#plannerUpdateBuckets)|UpdateBuckets|[Parameters](#ParametersplannerUpdateBuckets)|Not Found|
|[az planner planner update-plan](#plannerUpdatePlans)|UpdatePlans|[Parameters](#ParametersplannerUpdatePlans)|Not Found|
|[az planner planner update-task](#plannerUpdateTasks)|UpdateTasks|[Parameters](#ParametersplannerUpdateTasks)|Not Found|

### <a name="CommandsInplanner.buckets">Commands in `az planner planner-bucket` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner planner-bucket create-task](#planner.bucketsCreateTasks)|CreateTasks|[Parameters](#Parametersplanner.bucketsCreateTasks)|Not Found|
|[az planner planner-bucket delete-task](#planner.bucketsDeleteTasks)|DeleteTasks|[Parameters](#Parametersplanner.bucketsDeleteTasks)|Not Found|
|[az planner planner-bucket list-task](#planner.bucketsListTasks)|ListTasks|[Parameters](#Parametersplanner.bucketsListTasks)|Not Found|
|[az planner planner-bucket show-task](#planner.bucketsGetTasks)|GetTasks|[Parameters](#Parametersplanner.bucketsGetTasks)|Not Found|
|[az planner planner-bucket update-task](#planner.bucketsUpdateTasks)|UpdateTasks|[Parameters](#Parametersplanner.bucketsUpdateTasks)|Not Found|

### <a name="CommandsInplanner.buckets.tasks">Commands in `az planner planner-bucket-task` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner planner-bucket-task delete-assigned-to-task-board-format](#planner.buckets.tasksDeleteAssignedToTaskBoardFormat)|DeleteAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.buckets.tasksDeleteAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-bucket-task delete-bucket-task-board-format](#planner.buckets.tasksDeleteBucketTaskBoardFormat)|DeleteBucketTaskBoardFormat|[Parameters](#Parametersplanner.buckets.tasksDeleteBucketTaskBoardFormat)|Not Found|
|[az planner planner-bucket-task delete-detail](#planner.buckets.tasksDeleteDetails)|DeleteDetails|[Parameters](#Parametersplanner.buckets.tasksDeleteDetails)|Not Found|
|[az planner planner-bucket-task delete-progress-task-board-format](#planner.buckets.tasksDeleteProgressTaskBoardFormat)|DeleteProgressTaskBoardFormat|[Parameters](#Parametersplanner.buckets.tasksDeleteProgressTaskBoardFormat)|Not Found|
|[az planner planner-bucket-task show-assigned-to-task-board-format](#planner.buckets.tasksGetAssignedToTaskBoardFormat)|GetAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.buckets.tasksGetAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-bucket-task show-bucket-task-board-format](#planner.buckets.tasksGetBucketTaskBoardFormat)|GetBucketTaskBoardFormat|[Parameters](#Parametersplanner.buckets.tasksGetBucketTaskBoardFormat)|Not Found|
|[az planner planner-bucket-task show-detail](#planner.buckets.tasksGetDetails)|GetDetails|[Parameters](#Parametersplanner.buckets.tasksGetDetails)|Not Found|
|[az planner planner-bucket-task show-progress-task-board-format](#planner.buckets.tasksGetProgressTaskBoardFormat)|GetProgressTaskBoardFormat|[Parameters](#Parametersplanner.buckets.tasksGetProgressTaskBoardFormat)|Not Found|
|[az planner planner-bucket-task update-assigned-to-task-board-format](#planner.buckets.tasksUpdateAssignedToTaskBoardFormat)|UpdateAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.buckets.tasksUpdateAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-bucket-task update-bucket-task-board-format](#planner.buckets.tasksUpdateBucketTaskBoardFormat)|UpdateBucketTaskBoardFormat|[Parameters](#Parametersplanner.buckets.tasksUpdateBucketTaskBoardFormat)|Not Found|
|[az planner planner-bucket-task update-detail](#planner.buckets.tasksUpdateDetails)|UpdateDetails|[Parameters](#Parametersplanner.buckets.tasksUpdateDetails)|Not Found|
|[az planner planner-bucket-task update-progress-task-board-format](#planner.buckets.tasksUpdateProgressTaskBoardFormat)|UpdateProgressTaskBoardFormat|[Parameters](#Parametersplanner.buckets.tasksUpdateProgressTaskBoardFormat)|Not Found|

### <a name="CommandsInplanner.plans">Commands in `az planner planner-plan` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner planner-plan create-bucket](#planner.plansCreateBuckets)|CreateBuckets|[Parameters](#Parametersplanner.plansCreateBuckets)|Not Found|
|[az planner planner-plan create-task](#planner.plansCreateTasks)|CreateTasks|[Parameters](#Parametersplanner.plansCreateTasks)|Not Found|
|[az planner planner-plan delete-bucket](#planner.plansDeleteBuckets)|DeleteBuckets|[Parameters](#Parametersplanner.plansDeleteBuckets)|Not Found|
|[az planner planner-plan delete-detail](#planner.plansDeleteDetails)|DeleteDetails|[Parameters](#Parametersplanner.plansDeleteDetails)|Not Found|
|[az planner planner-plan delete-task](#planner.plansDeleteTasks)|DeleteTasks|[Parameters](#Parametersplanner.plansDeleteTasks)|Not Found|
|[az planner planner-plan list-bucket](#planner.plansListBuckets)|ListBuckets|[Parameters](#Parametersplanner.plansListBuckets)|Not Found|
|[az planner planner-plan list-task](#planner.plansListTasks)|ListTasks|[Parameters](#Parametersplanner.plansListTasks)|Not Found|
|[az planner planner-plan show-bucket](#planner.plansGetBuckets)|GetBuckets|[Parameters](#Parametersplanner.plansGetBuckets)|Not Found|
|[az planner planner-plan show-detail](#planner.plansGetDetails)|GetDetails|[Parameters](#Parametersplanner.plansGetDetails)|Not Found|
|[az planner planner-plan show-task](#planner.plansGetTasks)|GetTasks|[Parameters](#Parametersplanner.plansGetTasks)|Not Found|
|[az planner planner-plan update-bucket](#planner.plansUpdateBuckets)|UpdateBuckets|[Parameters](#Parametersplanner.plansUpdateBuckets)|Not Found|
|[az planner planner-plan update-detail](#planner.plansUpdateDetails)|UpdateDetails|[Parameters](#Parametersplanner.plansUpdateDetails)|Not Found|
|[az planner planner-plan update-task](#planner.plansUpdateTasks)|UpdateTasks|[Parameters](#Parametersplanner.plansUpdateTasks)|Not Found|

### <a name="CommandsInplanner.plans.buckets">Commands in `az planner planner-plan-bucket` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner planner-plan-bucket create-task](#planner.plans.bucketsCreateTasks)|CreateTasks|[Parameters](#Parametersplanner.plans.bucketsCreateTasks)|Not Found|
|[az planner planner-plan-bucket delete-task](#planner.plans.bucketsDeleteTasks)|DeleteTasks|[Parameters](#Parametersplanner.plans.bucketsDeleteTasks)|Not Found|
|[az planner planner-plan-bucket list-task](#planner.plans.bucketsListTasks)|ListTasks|[Parameters](#Parametersplanner.plans.bucketsListTasks)|Not Found|
|[az planner planner-plan-bucket show-task](#planner.plans.bucketsGetTasks)|GetTasks|[Parameters](#Parametersplanner.plans.bucketsGetTasks)|Not Found|
|[az planner planner-plan-bucket update-task](#planner.plans.bucketsUpdateTasks)|UpdateTasks|[Parameters](#Parametersplanner.plans.bucketsUpdateTasks)|Not Found|

### <a name="CommandsInplanner.plans.buckets.tasks">Commands in `az planner planner-plan-bucket-task` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner planner-plan-bucket-task delete-assigned-to-task-board-format](#planner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat)|DeleteAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-plan-bucket-task delete-bucket-task-board-format](#planner.plans.buckets.tasksDeleteBucketTaskBoardFormat)|DeleteBucketTaskBoardFormat|[Parameters](#Parametersplanner.plans.buckets.tasksDeleteBucketTaskBoardFormat)|Not Found|
|[az planner planner-plan-bucket-task delete-detail](#planner.plans.buckets.tasksDeleteDetails)|DeleteDetails|[Parameters](#Parametersplanner.plans.buckets.tasksDeleteDetails)|Not Found|
|[az planner planner-plan-bucket-task delete-progress-task-board-format](#planner.plans.buckets.tasksDeleteProgressTaskBoardFormat)|DeleteProgressTaskBoardFormat|[Parameters](#Parametersplanner.plans.buckets.tasksDeleteProgressTaskBoardFormat)|Not Found|
|[az planner planner-plan-bucket-task show-assigned-to-task-board-format](#planner.plans.buckets.tasksGetAssignedToTaskBoardFormat)|GetAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.plans.buckets.tasksGetAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-plan-bucket-task show-bucket-task-board-format](#planner.plans.buckets.tasksGetBucketTaskBoardFormat)|GetBucketTaskBoardFormat|[Parameters](#Parametersplanner.plans.buckets.tasksGetBucketTaskBoardFormat)|Not Found|
|[az planner planner-plan-bucket-task show-detail](#planner.plans.buckets.tasksGetDetails)|GetDetails|[Parameters](#Parametersplanner.plans.buckets.tasksGetDetails)|Not Found|
|[az planner planner-plan-bucket-task show-progress-task-board-format](#planner.plans.buckets.tasksGetProgressTaskBoardFormat)|GetProgressTaskBoardFormat|[Parameters](#Parametersplanner.plans.buckets.tasksGetProgressTaskBoardFormat)|Not Found|
|[az planner planner-plan-bucket-task update-assigned-to-task-board-format](#planner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat)|UpdateAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-plan-bucket-task update-bucket-task-board-format](#planner.plans.buckets.tasksUpdateBucketTaskBoardFormat)|UpdateBucketTaskBoardFormat|[Parameters](#Parametersplanner.plans.buckets.tasksUpdateBucketTaskBoardFormat)|Not Found|
|[az planner planner-plan-bucket-task update-detail](#planner.plans.buckets.tasksUpdateDetails)|UpdateDetails|[Parameters](#Parametersplanner.plans.buckets.tasksUpdateDetails)|Not Found|
|[az planner planner-plan-bucket-task update-progress-task-board-format](#planner.plans.buckets.tasksUpdateProgressTaskBoardFormat)|UpdateProgressTaskBoardFormat|[Parameters](#Parametersplanner.plans.buckets.tasksUpdateProgressTaskBoardFormat)|Not Found|

### <a name="CommandsInplanner.plans.tasks">Commands in `az planner planner-plan-task` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner planner-plan-task delete-assigned-to-task-board-format](#planner.plans.tasksDeleteAssignedToTaskBoardFormat)|DeleteAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.plans.tasksDeleteAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-plan-task delete-bucket-task-board-format](#planner.plans.tasksDeleteBucketTaskBoardFormat)|DeleteBucketTaskBoardFormat|[Parameters](#Parametersplanner.plans.tasksDeleteBucketTaskBoardFormat)|Not Found|
|[az planner planner-plan-task delete-detail](#planner.plans.tasksDeleteDetails)|DeleteDetails|[Parameters](#Parametersplanner.plans.tasksDeleteDetails)|Not Found|
|[az planner planner-plan-task delete-progress-task-board-format](#planner.plans.tasksDeleteProgressTaskBoardFormat)|DeleteProgressTaskBoardFormat|[Parameters](#Parametersplanner.plans.tasksDeleteProgressTaskBoardFormat)|Not Found|
|[az planner planner-plan-task show-assigned-to-task-board-format](#planner.plans.tasksGetAssignedToTaskBoardFormat)|GetAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.plans.tasksGetAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-plan-task show-bucket-task-board-format](#planner.plans.tasksGetBucketTaskBoardFormat)|GetBucketTaskBoardFormat|[Parameters](#Parametersplanner.plans.tasksGetBucketTaskBoardFormat)|Not Found|
|[az planner planner-plan-task show-detail](#planner.plans.tasksGetDetails)|GetDetails|[Parameters](#Parametersplanner.plans.tasksGetDetails)|Not Found|
|[az planner planner-plan-task show-progress-task-board-format](#planner.plans.tasksGetProgressTaskBoardFormat)|GetProgressTaskBoardFormat|[Parameters](#Parametersplanner.plans.tasksGetProgressTaskBoardFormat)|Not Found|
|[az planner planner-plan-task update-assigned-to-task-board-format](#planner.plans.tasksUpdateAssignedToTaskBoardFormat)|UpdateAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.plans.tasksUpdateAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-plan-task update-bucket-task-board-format](#planner.plans.tasksUpdateBucketTaskBoardFormat)|UpdateBucketTaskBoardFormat|[Parameters](#Parametersplanner.plans.tasksUpdateBucketTaskBoardFormat)|Not Found|
|[az planner planner-plan-task update-detail](#planner.plans.tasksUpdateDetails)|UpdateDetails|[Parameters](#Parametersplanner.plans.tasksUpdateDetails)|Not Found|
|[az planner planner-plan-task update-progress-task-board-format](#planner.plans.tasksUpdateProgressTaskBoardFormat)|UpdateProgressTaskBoardFormat|[Parameters](#Parametersplanner.plans.tasksUpdateProgressTaskBoardFormat)|Not Found|

### <a name="CommandsInplanner.tasks">Commands in `az planner planner-task` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner planner-task delete-assigned-to-task-board-format](#planner.tasksDeleteAssignedToTaskBoardFormat)|DeleteAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.tasksDeleteAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-task delete-bucket-task-board-format](#planner.tasksDeleteBucketTaskBoardFormat)|DeleteBucketTaskBoardFormat|[Parameters](#Parametersplanner.tasksDeleteBucketTaskBoardFormat)|Not Found|
|[az planner planner-task delete-detail](#planner.tasksDeleteDetails)|DeleteDetails|[Parameters](#Parametersplanner.tasksDeleteDetails)|Not Found|
|[az planner planner-task delete-progress-task-board-format](#planner.tasksDeleteProgressTaskBoardFormat)|DeleteProgressTaskBoardFormat|[Parameters](#Parametersplanner.tasksDeleteProgressTaskBoardFormat)|Not Found|
|[az planner planner-task show-assigned-to-task-board-format](#planner.tasksGetAssignedToTaskBoardFormat)|GetAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.tasksGetAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-task show-bucket-task-board-format](#planner.tasksGetBucketTaskBoardFormat)|GetBucketTaskBoardFormat|[Parameters](#Parametersplanner.tasksGetBucketTaskBoardFormat)|Not Found|
|[az planner planner-task show-detail](#planner.tasksGetDetails)|GetDetails|[Parameters](#Parametersplanner.tasksGetDetails)|Not Found|
|[az planner planner-task show-progress-task-board-format](#planner.tasksGetProgressTaskBoardFormat)|GetProgressTaskBoardFormat|[Parameters](#Parametersplanner.tasksGetProgressTaskBoardFormat)|Not Found|
|[az planner planner-task update-assigned-to-task-board-format](#planner.tasksUpdateAssignedToTaskBoardFormat)|UpdateAssignedToTaskBoardFormat|[Parameters](#Parametersplanner.tasksUpdateAssignedToTaskBoardFormat)|Not Found|
|[az planner planner-task update-bucket-task-board-format](#planner.tasksUpdateBucketTaskBoardFormat)|UpdateBucketTaskBoardFormat|[Parameters](#Parametersplanner.tasksUpdateBucketTaskBoardFormat)|Not Found|
|[az planner planner-task update-detail](#planner.tasksUpdateDetails)|UpdateDetails|[Parameters](#Parametersplanner.tasksUpdateDetails)|Not Found|
|[az planner planner-task update-progress-task-board-format](#planner.tasksUpdateProgressTaskBoardFormat)|UpdateProgressTaskBoardFormat|[Parameters](#Parametersplanner.tasksUpdateProgressTaskBoardFormat)|Not Found|

### <a name="CommandsInusers">Commands in `az planner user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner user delete-planner](#usersDeletePlanner)|DeletePlanner|[Parameters](#ParametersusersDeletePlanner)|Not Found|
|[az planner user show-planner](#usersGetPlanner)|GetPlanner|[Parameters](#ParametersusersGetPlanner)|Not Found|
|[az planner user update-planner](#usersUpdatePlanner)|UpdatePlanner|[Parameters](#ParametersusersUpdatePlanner)|Not Found|

### <a name="CommandsInusers.planner">Commands in `az planner user-planner` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner user-planner create-plan](#users.plannerCreatePlans)|CreatePlans|[Parameters](#Parametersusers.plannerCreatePlans)|Not Found|
|[az planner user-planner create-task](#users.plannerCreateTasks)|CreateTasks|[Parameters](#Parametersusers.plannerCreateTasks)|Not Found|
|[az planner user-planner delete-plan](#users.plannerDeletePlans)|DeletePlans|[Parameters](#Parametersusers.plannerDeletePlans)|Not Found|
|[az planner user-planner delete-task](#users.plannerDeleteTasks)|DeleteTasks|[Parameters](#Parametersusers.plannerDeleteTasks)|Not Found|
|[az planner user-planner list-plan](#users.plannerListPlans)|ListPlans|[Parameters](#Parametersusers.plannerListPlans)|Not Found|
|[az planner user-planner list-task](#users.plannerListTasks)|ListTasks|[Parameters](#Parametersusers.plannerListTasks)|Not Found|
|[az planner user-planner show-plan](#users.plannerGetPlans)|GetPlans|[Parameters](#Parametersusers.plannerGetPlans)|Not Found|
|[az planner user-planner show-task](#users.plannerGetTasks)|GetTasks|[Parameters](#Parametersusers.plannerGetTasks)|Not Found|
|[az planner user-planner update-plan](#users.plannerUpdatePlans)|UpdatePlans|[Parameters](#Parametersusers.plannerUpdatePlans)|Not Found|
|[az planner user-planner update-task](#users.plannerUpdateTasks)|UpdateTasks|[Parameters](#Parametersusers.plannerUpdateTasks)|Not Found|

### <a name="CommandsInusers.planner.plans">Commands in `az planner user-planner-plan` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner user-planner-plan create-bucket](#users.planner.plansCreateBuckets)|CreateBuckets|[Parameters](#Parametersusers.planner.plansCreateBuckets)|Not Found|
|[az planner user-planner-plan create-task](#users.planner.plansCreateTasks)|CreateTasks|[Parameters](#Parametersusers.planner.plansCreateTasks)|Not Found|
|[az planner user-planner-plan delete-bucket](#users.planner.plansDeleteBuckets)|DeleteBuckets|[Parameters](#Parametersusers.planner.plansDeleteBuckets)|Not Found|
|[az planner user-planner-plan delete-detail](#users.planner.plansDeleteDetails)|DeleteDetails|[Parameters](#Parametersusers.planner.plansDeleteDetails)|Not Found|
|[az planner user-planner-plan delete-task](#users.planner.plansDeleteTasks)|DeleteTasks|[Parameters](#Parametersusers.planner.plansDeleteTasks)|Not Found|
|[az planner user-planner-plan list-bucket](#users.planner.plansListBuckets)|ListBuckets|[Parameters](#Parametersusers.planner.plansListBuckets)|Not Found|
|[az planner user-planner-plan list-task](#users.planner.plansListTasks)|ListTasks|[Parameters](#Parametersusers.planner.plansListTasks)|Not Found|
|[az planner user-planner-plan show-bucket](#users.planner.plansGetBuckets)|GetBuckets|[Parameters](#Parametersusers.planner.plansGetBuckets)|Not Found|
|[az planner user-planner-plan show-detail](#users.planner.plansGetDetails)|GetDetails|[Parameters](#Parametersusers.planner.plansGetDetails)|Not Found|
|[az planner user-planner-plan show-task](#users.planner.plansGetTasks)|GetTasks|[Parameters](#Parametersusers.planner.plansGetTasks)|Not Found|
|[az planner user-planner-plan update-bucket](#users.planner.plansUpdateBuckets)|UpdateBuckets|[Parameters](#Parametersusers.planner.plansUpdateBuckets)|Not Found|
|[az planner user-planner-plan update-detail](#users.planner.plansUpdateDetails)|UpdateDetails|[Parameters](#Parametersusers.planner.plansUpdateDetails)|Not Found|
|[az planner user-planner-plan update-task](#users.planner.plansUpdateTasks)|UpdateTasks|[Parameters](#Parametersusers.planner.plansUpdateTasks)|Not Found|

### <a name="CommandsInusers.planner.plans.buckets">Commands in `az planner user-planner-plan-bucket` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner user-planner-plan-bucket create-task](#users.planner.plans.bucketsCreateTasks)|CreateTasks|[Parameters](#Parametersusers.planner.plans.bucketsCreateTasks)|Not Found|
|[az planner user-planner-plan-bucket delete-task](#users.planner.plans.bucketsDeleteTasks)|DeleteTasks|[Parameters](#Parametersusers.planner.plans.bucketsDeleteTasks)|Not Found|
|[az planner user-planner-plan-bucket list-task](#users.planner.plans.bucketsListTasks)|ListTasks|[Parameters](#Parametersusers.planner.plans.bucketsListTasks)|Not Found|
|[az planner user-planner-plan-bucket show-task](#users.planner.plans.bucketsGetTasks)|GetTasks|[Parameters](#Parametersusers.planner.plans.bucketsGetTasks)|Not Found|
|[az planner user-planner-plan-bucket update-task](#users.planner.plans.bucketsUpdateTasks)|UpdateTasks|[Parameters](#Parametersusers.planner.plans.bucketsUpdateTasks)|Not Found|

### <a name="CommandsInusers.planner.plans.buckets.tasks">Commands in `az planner user-planner-plan-bucket-task` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner user-planner-plan-bucket-task delete-assigned-to-task-board-format](#users.planner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat)|DeleteAssignedToTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-bucket-task delete-bucket-task-board-format](#users.planner.plans.buckets.tasksDeleteBucketTaskBoardFormat)|DeleteBucketTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.buckets.tasksDeleteBucketTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-bucket-task delete-detail](#users.planner.plans.buckets.tasksDeleteDetails)|DeleteDetails|[Parameters](#Parametersusers.planner.plans.buckets.tasksDeleteDetails)|Not Found|
|[az planner user-planner-plan-bucket-task delete-progress-task-board-format](#users.planner.plans.buckets.tasksDeleteProgressTaskBoardFormat)|DeleteProgressTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.buckets.tasksDeleteProgressTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-bucket-task show-assigned-to-task-board-format](#users.planner.plans.buckets.tasksGetAssignedToTaskBoardFormat)|GetAssignedToTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.buckets.tasksGetAssignedToTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-bucket-task show-bucket-task-board-format](#users.planner.plans.buckets.tasksGetBucketTaskBoardFormat)|GetBucketTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.buckets.tasksGetBucketTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-bucket-task show-detail](#users.planner.plans.buckets.tasksGetDetails)|GetDetails|[Parameters](#Parametersusers.planner.plans.buckets.tasksGetDetails)|Not Found|
|[az planner user-planner-plan-bucket-task show-progress-task-board-format](#users.planner.plans.buckets.tasksGetProgressTaskBoardFormat)|GetProgressTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.buckets.tasksGetProgressTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-bucket-task update-assigned-to-task-board-format](#users.planner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat)|UpdateAssignedToTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-bucket-task update-bucket-task-board-format](#users.planner.plans.buckets.tasksUpdateBucketTaskBoardFormat)|UpdateBucketTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.buckets.tasksUpdateBucketTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-bucket-task update-detail](#users.planner.plans.buckets.tasksUpdateDetails)|UpdateDetails|[Parameters](#Parametersusers.planner.plans.buckets.tasksUpdateDetails)|Not Found|
|[az planner user-planner-plan-bucket-task update-progress-task-board-format](#users.planner.plans.buckets.tasksUpdateProgressTaskBoardFormat)|UpdateProgressTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.buckets.tasksUpdateProgressTaskBoardFormat)|Not Found|

### <a name="CommandsInusers.planner.plans.tasks">Commands in `az planner user-planner-plan-task` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner user-planner-plan-task delete-assigned-to-task-board-format](#users.planner.plans.tasksDeleteAssignedToTaskBoardFormat)|DeleteAssignedToTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.tasksDeleteAssignedToTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-task delete-bucket-task-board-format](#users.planner.plans.tasksDeleteBucketTaskBoardFormat)|DeleteBucketTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.tasksDeleteBucketTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-task delete-detail](#users.planner.plans.tasksDeleteDetails)|DeleteDetails|[Parameters](#Parametersusers.planner.plans.tasksDeleteDetails)|Not Found|
|[az planner user-planner-plan-task delete-progress-task-board-format](#users.planner.plans.tasksDeleteProgressTaskBoardFormat)|DeleteProgressTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.tasksDeleteProgressTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-task show-assigned-to-task-board-format](#users.planner.plans.tasksGetAssignedToTaskBoardFormat)|GetAssignedToTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.tasksGetAssignedToTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-task show-bucket-task-board-format](#users.planner.plans.tasksGetBucketTaskBoardFormat)|GetBucketTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.tasksGetBucketTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-task show-detail](#users.planner.plans.tasksGetDetails)|GetDetails|[Parameters](#Parametersusers.planner.plans.tasksGetDetails)|Not Found|
|[az planner user-planner-plan-task show-progress-task-board-format](#users.planner.plans.tasksGetProgressTaskBoardFormat)|GetProgressTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.tasksGetProgressTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-task update-assigned-to-task-board-format](#users.planner.plans.tasksUpdateAssignedToTaskBoardFormat)|UpdateAssignedToTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.tasksUpdateAssignedToTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-task update-bucket-task-board-format](#users.planner.plans.tasksUpdateBucketTaskBoardFormat)|UpdateBucketTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.tasksUpdateBucketTaskBoardFormat)|Not Found|
|[az planner user-planner-plan-task update-detail](#users.planner.plans.tasksUpdateDetails)|UpdateDetails|[Parameters](#Parametersusers.planner.plans.tasksUpdateDetails)|Not Found|
|[az planner user-planner-plan-task update-progress-task-board-format](#users.planner.plans.tasksUpdateProgressTaskBoardFormat)|UpdateProgressTaskBoardFormat|[Parameters](#Parametersusers.planner.plans.tasksUpdateProgressTaskBoardFormat)|Not Found|

### <a name="CommandsInusers.planner.tasks">Commands in `az planner user-planner-task` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az planner user-planner-task delete-assigned-to-task-board-format](#users.planner.tasksDeleteAssignedToTaskBoardFormat)|DeleteAssignedToTaskBoardFormat|[Parameters](#Parametersusers.planner.tasksDeleteAssignedToTaskBoardFormat)|Not Found|
|[az planner user-planner-task delete-bucket-task-board-format](#users.planner.tasksDeleteBucketTaskBoardFormat)|DeleteBucketTaskBoardFormat|[Parameters](#Parametersusers.planner.tasksDeleteBucketTaskBoardFormat)|Not Found|
|[az planner user-planner-task delete-detail](#users.planner.tasksDeleteDetails)|DeleteDetails|[Parameters](#Parametersusers.planner.tasksDeleteDetails)|Not Found|
|[az planner user-planner-task delete-progress-task-board-format](#users.planner.tasksDeleteProgressTaskBoardFormat)|DeleteProgressTaskBoardFormat|[Parameters](#Parametersusers.planner.tasksDeleteProgressTaskBoardFormat)|Not Found|
|[az planner user-planner-task show-assigned-to-task-board-format](#users.planner.tasksGetAssignedToTaskBoardFormat)|GetAssignedToTaskBoardFormat|[Parameters](#Parametersusers.planner.tasksGetAssignedToTaskBoardFormat)|Not Found|
|[az planner user-planner-task show-bucket-task-board-format](#users.planner.tasksGetBucketTaskBoardFormat)|GetBucketTaskBoardFormat|[Parameters](#Parametersusers.planner.tasksGetBucketTaskBoardFormat)|Not Found|
|[az planner user-planner-task show-detail](#users.planner.tasksGetDetails)|GetDetails|[Parameters](#Parametersusers.planner.tasksGetDetails)|Not Found|
|[az planner user-planner-task show-progress-task-board-format](#users.planner.tasksGetProgressTaskBoardFormat)|GetProgressTaskBoardFormat|[Parameters](#Parametersusers.planner.tasksGetProgressTaskBoardFormat)|Not Found|
|[az planner user-planner-task update-assigned-to-task-board-format](#users.planner.tasksUpdateAssignedToTaskBoardFormat)|UpdateAssignedToTaskBoardFormat|[Parameters](#Parametersusers.planner.tasksUpdateAssignedToTaskBoardFormat)|Not Found|
|[az planner user-planner-task update-bucket-task-board-format](#users.planner.tasksUpdateBucketTaskBoardFormat)|UpdateBucketTaskBoardFormat|[Parameters](#Parametersusers.planner.tasksUpdateBucketTaskBoardFormat)|Not Found|
|[az planner user-planner-task update-detail](#users.planner.tasksUpdateDetails)|UpdateDetails|[Parameters](#Parametersusers.planner.tasksUpdateDetails)|Not Found|
|[az planner user-planner-task update-progress-task-board-format](#users.planner.tasksUpdateProgressTaskBoardFormat)|UpdateProgressTaskBoardFormat|[Parameters](#Parametersusers.planner.tasksUpdateProgressTaskBoardFormat)|Not Found|


## COMMAND DETAILS

### group `az planner group`
#### <a name="groupsDeletePlanner">Command `az planner group delete-planner`</a>

##### <a name="ParametersgroupsDeletePlanner">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsGetPlanner">Command `az planner group show-planner`</a>

##### <a name="ParametersgroupsGetPlanner">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsUpdatePlanner">Command `az planner group update-planner`</a>

##### <a name="ParametersgroupsUpdatePlanner">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--plans**|array|Read-only. Nullable. Returns the plannerPlans owned by the group.|plans|plans|

### group `az planner group-planner`
#### <a name="groups.plannerCreatePlans">Command `az planner group-planner create-plan`</a>

##### <a name="Parametersgroups.plannerCreatePlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="groups.plannerDeletePlans">Command `az planner group-planner delete-plan`</a>

##### <a name="Parametersgroups.plannerDeletePlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.plannerListPlans">Command `az planner group-planner list-plan`</a>

##### <a name="Parametersgroups.plannerListPlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.plannerGetPlans">Command `az planner group-planner show-plan`</a>

##### <a name="Parametersgroups.plannerGetPlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.plannerUpdatePlans">Command `az planner group-planner update-plan`</a>

##### <a name="Parametersgroups.plannerUpdatePlans">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

### group `az planner group-planner-plan`
#### <a name="groups.planner.plansCreateBuckets">Command `az planner group-planner-plan create-bucket`</a>

##### <a name="Parametersgroups.planner.plansCreateBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

#### <a name="groups.planner.plansCreateTasks">Command `az planner group-planner-plan create-task`</a>

##### <a name="Parametersgroups.planner.plansCreateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="groups.planner.plansDeleteBuckets">Command `az planner group-planner-plan delete-bucket`</a>

##### <a name="Parametersgroups.planner.plansDeleteBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plansDeleteDetails">Command `az planner group-planner-plan delete-detail`</a>

##### <a name="Parametersgroups.planner.plansDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plansDeleteTasks">Command `az planner group-planner-plan delete-task`</a>

##### <a name="Parametersgroups.planner.plansDeleteTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plansListBuckets">Command `az planner group-planner-plan list-bucket`</a>

##### <a name="Parametersgroups.planner.plansListBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plansListTasks">Command `az planner group-planner-plan list-task`</a>

##### <a name="Parametersgroups.planner.plansListTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plansGetBuckets">Command `az planner group-planner-plan show-bucket`</a>

##### <a name="Parametersgroups.planner.plansGetBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plansGetDetails">Command `az planner group-planner-plan show-detail`</a>

##### <a name="Parametersgroups.planner.plansGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plansGetTasks">Command `az planner group-planner-plan show-task`</a>

##### <a name="Parametersgroups.planner.plansGetTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plansUpdateBuckets">Command `az planner group-planner-plan update-bucket`</a>

##### <a name="Parametersgroups.planner.plansUpdateBuckets">Parameters</a> 
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

#### <a name="groups.planner.plansUpdateDetails">Command `az planner group-planner-plan update-detail`</a>

##### <a name="Parametersgroups.planner.plansUpdateDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|

#### <a name="groups.planner.plansUpdateTasks">Command `az planner group-planner-plan update-task`</a>

##### <a name="Parametersgroups.planner.plansUpdateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az planner group-planner-plan-bucket`
#### <a name="groups.planner.plans.bucketsCreateTasks">Command `az planner group-planner-plan-bucket create-task`</a>

##### <a name="Parametersgroups.planner.plans.bucketsCreateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="groups.planner.plans.bucketsDeleteTasks">Command `az planner group-planner-plan-bucket delete-task`</a>

##### <a name="Parametersgroups.planner.plans.bucketsDeleteTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plans.bucketsListTasks">Command `az planner group-planner-plan-bucket list-task`</a>

##### <a name="Parametersgroups.planner.plans.bucketsListTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plans.bucketsGetTasks">Command `az planner group-planner-plan-bucket show-task`</a>

##### <a name="Parametersgroups.planner.plans.bucketsGetTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plans.bucketsUpdateTasks">Command `az planner group-planner-plan-bucket update-task`</a>

##### <a name="Parametersgroups.planner.plans.bucketsUpdateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az planner group-planner-plan-bucket-task`
#### <a name="groups.planner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat">Command `az planner group-planner-plan-bucket-task delete-assigned-to-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plans.buckets.tasksDeleteBucketTaskBoardFormat">Command `az planner group-planner-plan-bucket-task delete-bucket-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksDeleteBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plans.buckets.tasksDeleteDetails">Command `az planner group-planner-plan-bucket-task delete-detail`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plans.buckets.tasksDeleteProgressTaskBoardFormat">Command `az planner group-planner-plan-bucket-task delete-progress-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksDeleteProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plans.buckets.tasksGetAssignedToTaskBoardFormat">Command `az planner group-planner-plan-bucket-task show-assigned-to-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksGetAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plans.buckets.tasksGetBucketTaskBoardFormat">Command `az planner group-planner-plan-bucket-task show-bucket-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksGetBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plans.buckets.tasksGetDetails">Command `az planner group-planner-plan-bucket-task show-detail`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plans.buckets.tasksGetProgressTaskBoardFormat">Command `az planner group-planner-plan-bucket-task show-progress-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksGetProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat">Command `az planner group-planner-plan-bucket-task update-assigned-to-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

#### <a name="groups.planner.plans.buckets.tasksUpdateBucketTaskBoardFormat">Command `az planner group-planner-plan-bucket-task update-bucket-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksUpdateBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

#### <a name="groups.planner.plans.buckets.tasksUpdateDetails">Command `az planner group-planner-plan-bucket-task update-detail`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksUpdateDetails">Parameters</a> 
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

#### <a name="groups.planner.plans.buckets.tasksUpdateProgressTaskBoardFormat">Command `az planner group-planner-plan-bucket-task update-progress-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.buckets.tasksUpdateProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### group `az planner group-planner-plan-task`
#### <a name="groups.planner.plans.tasksDeleteAssignedToTaskBoardFormat">Command `az planner group-planner-plan-task delete-assigned-to-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.tasksDeleteAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plans.tasksDeleteBucketTaskBoardFormat">Command `az planner group-planner-plan-task delete-bucket-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.tasksDeleteBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plans.tasksDeleteDetails">Command `az planner group-planner-plan-task delete-detail`</a>

##### <a name="Parametersgroups.planner.plans.tasksDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plans.tasksDeleteProgressTaskBoardFormat">Command `az planner group-planner-plan-task delete-progress-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.tasksDeleteProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.planner.plans.tasksGetAssignedToTaskBoardFormat">Command `az planner group-planner-plan-task show-assigned-to-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.tasksGetAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plans.tasksGetBucketTaskBoardFormat">Command `az planner group-planner-plan-task show-bucket-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.tasksGetBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plans.tasksGetDetails">Command `az planner group-planner-plan-task show-detail`</a>

##### <a name="Parametersgroups.planner.plans.tasksGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plans.tasksGetProgressTaskBoardFormat">Command `az planner group-planner-plan-task show-progress-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.tasksGetProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.planner.plans.tasksUpdateAssignedToTaskBoardFormat">Command `az planner group-planner-plan-task update-assigned-to-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.tasksUpdateAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

#### <a name="groups.planner.plans.tasksUpdateBucketTaskBoardFormat">Command `az planner group-planner-plan-task update-bucket-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.tasksUpdateBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

#### <a name="groups.planner.plans.tasksUpdateDetails">Command `az planner group-planner-plan-task update-detail`</a>

##### <a name="Parametersgroups.planner.plans.tasksUpdateDetails">Parameters</a> 
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

#### <a name="groups.planner.plans.tasksUpdateProgressTaskBoardFormat">Command `az planner group-planner-plan-task update-progress-task-board-format`</a>

##### <a name="Parametersgroups.planner.plans.tasksUpdateProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### group `az planner planner`
#### <a name="planner.plannerUpdatePlanner">Command `az planner planner create`</a>

##### <a name="Parametersplanner.plannerUpdatePlanner">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--buckets**|array|Read-only. Nullable. Returns a collection of the specified buckets|buckets|buckets|
|**--plans**|array|Read-only. Nullable. Returns a collection of the specified plans|plans|plans|
|**--tasks**|array|Read-only. Nullable. Returns a collection of the specified tasks|tasks|tasks|

#### <a name="planner.plannerGetPlanner">Command `az planner planner show-planner`</a>

##### <a name="Parametersplanner.plannerGetPlanner">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az planner planner`
#### <a name="plannerCreateBuckets">Command `az planner planner create-bucket`</a>

##### <a name="ParametersplannerCreateBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

#### <a name="plannerCreatePlans">Command `az planner planner create-plan`</a>

##### <a name="ParametersplannerCreatePlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="plannerCreateTasks">Command `az planner planner create-task`</a>

##### <a name="ParametersplannerCreateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="plannerDeleteBuckets">Command `az planner planner delete-bucket`</a>

##### <a name="ParametersplannerDeleteBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="plannerDeletePlans">Command `az planner planner delete-plan`</a>

##### <a name="ParametersplannerDeletePlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="plannerDeleteTasks">Command `az planner planner delete-task`</a>

##### <a name="ParametersplannerDeleteTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="plannerListBuckets">Command `az planner planner list-bucket`</a>

##### <a name="ParametersplannerListBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="plannerListPlans">Command `az planner planner list-plan`</a>

##### <a name="ParametersplannerListPlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="plannerListTasks">Command `az planner planner list-task`</a>

##### <a name="ParametersplannerListTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="plannerGetBuckets">Command `az planner planner show-bucket`</a>

##### <a name="ParametersplannerGetBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="plannerGetPlans">Command `az planner planner show-plan`</a>

##### <a name="ParametersplannerGetPlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="plannerGetTasks">Command `az planner planner show-task`</a>

##### <a name="ParametersplannerGetTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="plannerUpdateBuckets">Command `az planner planner update-bucket`</a>

##### <a name="ParametersplannerUpdateBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

#### <a name="plannerUpdatePlans">Command `az planner planner update-plan`</a>

##### <a name="ParametersplannerUpdatePlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="plannerUpdateTasks">Command `az planner planner update-task`</a>

##### <a name="ParametersplannerUpdateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az planner planner-bucket`
#### <a name="planner.bucketsCreateTasks">Command `az planner planner-bucket create-task`</a>

##### <a name="Parametersplanner.bucketsCreateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="planner.bucketsDeleteTasks">Command `az planner planner-bucket delete-task`</a>

##### <a name="Parametersplanner.bucketsDeleteTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.bucketsListTasks">Command `az planner planner-bucket list-task`</a>

##### <a name="Parametersplanner.bucketsListTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.bucketsGetTasks">Command `az planner planner-bucket show-task`</a>

##### <a name="Parametersplanner.bucketsGetTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.bucketsUpdateTasks">Command `az planner planner-bucket update-task`</a>

##### <a name="Parametersplanner.bucketsUpdateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az planner planner-bucket-task`
#### <a name="planner.buckets.tasksDeleteAssignedToTaskBoardFormat">Command `az planner planner-bucket-task delete-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.buckets.tasksDeleteAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.buckets.tasksDeleteBucketTaskBoardFormat">Command `az planner planner-bucket-task delete-bucket-task-board-format`</a>

##### <a name="Parametersplanner.buckets.tasksDeleteBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.buckets.tasksDeleteDetails">Command `az planner planner-bucket-task delete-detail`</a>

##### <a name="Parametersplanner.buckets.tasksDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.buckets.tasksDeleteProgressTaskBoardFormat">Command `az planner planner-bucket-task delete-progress-task-board-format`</a>

##### <a name="Parametersplanner.buckets.tasksDeleteProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.buckets.tasksGetAssignedToTaskBoardFormat">Command `az planner planner-bucket-task show-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.buckets.tasksGetAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.buckets.tasksGetBucketTaskBoardFormat">Command `az planner planner-bucket-task show-bucket-task-board-format`</a>

##### <a name="Parametersplanner.buckets.tasksGetBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.buckets.tasksGetDetails">Command `az planner planner-bucket-task show-detail`</a>

##### <a name="Parametersplanner.buckets.tasksGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.buckets.tasksGetProgressTaskBoardFormat">Command `az planner planner-bucket-task show-progress-task-board-format`</a>

##### <a name="Parametersplanner.buckets.tasksGetProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.buckets.tasksUpdateAssignedToTaskBoardFormat">Command `az planner planner-bucket-task update-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.buckets.tasksUpdateAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

#### <a name="planner.buckets.tasksUpdateBucketTaskBoardFormat">Command `az planner planner-bucket-task update-bucket-task-board-format`</a>

##### <a name="Parametersplanner.buckets.tasksUpdateBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

#### <a name="planner.buckets.tasksUpdateDetails">Command `az planner planner-bucket-task update-detail`</a>

##### <a name="Parametersplanner.buckets.tasksUpdateDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

#### <a name="planner.buckets.tasksUpdateProgressTaskBoardFormat">Command `az planner planner-bucket-task update-progress-task-board-format`</a>

##### <a name="Parametersplanner.buckets.tasksUpdateProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### group `az planner planner-plan`
#### <a name="planner.plansCreateBuckets">Command `az planner planner-plan create-bucket`</a>

##### <a name="Parametersplanner.plansCreateBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

#### <a name="planner.plansCreateTasks">Command `az planner planner-plan create-task`</a>

##### <a name="Parametersplanner.plansCreateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="planner.plansDeleteBuckets">Command `az planner planner-plan delete-bucket`</a>

##### <a name="Parametersplanner.plansDeleteBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plansDeleteDetails">Command `az planner planner-plan delete-detail`</a>

##### <a name="Parametersplanner.plansDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plansDeleteTasks">Command `az planner planner-plan delete-task`</a>

##### <a name="Parametersplanner.plansDeleteTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plansListBuckets">Command `az planner planner-plan list-bucket`</a>

##### <a name="Parametersplanner.plansListBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plansListTasks">Command `az planner planner-plan list-task`</a>

##### <a name="Parametersplanner.plansListTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plansGetBuckets">Command `az planner planner-plan show-bucket`</a>

##### <a name="Parametersplanner.plansGetBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plansGetDetails">Command `az planner planner-plan show-detail`</a>

##### <a name="Parametersplanner.plansGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plansGetTasks">Command `az planner planner-plan show-task`</a>

##### <a name="Parametersplanner.plansGetTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plansUpdateBuckets">Command `az planner planner-plan update-bucket`</a>

##### <a name="Parametersplanner.plansUpdateBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

#### <a name="planner.plansUpdateDetails">Command `az planner planner-plan update-detail`</a>

##### <a name="Parametersplanner.plansUpdateDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|

#### <a name="planner.plansUpdateTasks">Command `az planner planner-plan update-task`</a>

##### <a name="Parametersplanner.plansUpdateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az planner planner-plan-bucket`
#### <a name="planner.plans.bucketsCreateTasks">Command `az planner planner-plan-bucket create-task`</a>

##### <a name="Parametersplanner.plans.bucketsCreateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="planner.plans.bucketsDeleteTasks">Command `az planner planner-plan-bucket delete-task`</a>

##### <a name="Parametersplanner.plans.bucketsDeleteTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plans.bucketsListTasks">Command `az planner planner-plan-bucket list-task`</a>

##### <a name="Parametersplanner.plans.bucketsListTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plans.bucketsGetTasks">Command `az planner planner-plan-bucket show-task`</a>

##### <a name="Parametersplanner.plans.bucketsGetTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plans.bucketsUpdateTasks">Command `az planner planner-plan-bucket update-task`</a>

##### <a name="Parametersplanner.plans.bucketsUpdateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az planner planner-plan-bucket-task`
#### <a name="planner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat">Command `az planner planner-plan-bucket-task delete-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plans.buckets.tasksDeleteBucketTaskBoardFormat">Command `az planner planner-plan-bucket-task delete-bucket-task-board-format`</a>

##### <a name="Parametersplanner.plans.buckets.tasksDeleteBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plans.buckets.tasksDeleteDetails">Command `az planner planner-plan-bucket-task delete-detail`</a>

##### <a name="Parametersplanner.plans.buckets.tasksDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plans.buckets.tasksDeleteProgressTaskBoardFormat">Command `az planner planner-plan-bucket-task delete-progress-task-board-format`</a>

##### <a name="Parametersplanner.plans.buckets.tasksDeleteProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plans.buckets.tasksGetAssignedToTaskBoardFormat">Command `az planner planner-plan-bucket-task show-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.plans.buckets.tasksGetAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plans.buckets.tasksGetBucketTaskBoardFormat">Command `az planner planner-plan-bucket-task show-bucket-task-board-format`</a>

##### <a name="Parametersplanner.plans.buckets.tasksGetBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plans.buckets.tasksGetDetails">Command `az planner planner-plan-bucket-task show-detail`</a>

##### <a name="Parametersplanner.plans.buckets.tasksGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plans.buckets.tasksGetProgressTaskBoardFormat">Command `az planner planner-plan-bucket-task show-progress-task-board-format`</a>

##### <a name="Parametersplanner.plans.buckets.tasksGetProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat">Command `az planner planner-plan-bucket-task update-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

#### <a name="planner.plans.buckets.tasksUpdateBucketTaskBoardFormat">Command `az planner planner-plan-bucket-task update-bucket-task-board-format`</a>

##### <a name="Parametersplanner.plans.buckets.tasksUpdateBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

#### <a name="planner.plans.buckets.tasksUpdateDetails">Command `az planner planner-plan-bucket-task update-detail`</a>

##### <a name="Parametersplanner.plans.buckets.tasksUpdateDetails">Parameters</a> 
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

#### <a name="planner.plans.buckets.tasksUpdateProgressTaskBoardFormat">Command `az planner planner-plan-bucket-task update-progress-task-board-format`</a>

##### <a name="Parametersplanner.plans.buckets.tasksUpdateProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### group `az planner planner-plan-task`
#### <a name="planner.plans.tasksDeleteAssignedToTaskBoardFormat">Command `az planner planner-plan-task delete-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.plans.tasksDeleteAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plans.tasksDeleteBucketTaskBoardFormat">Command `az planner planner-plan-task delete-bucket-task-board-format`</a>

##### <a name="Parametersplanner.plans.tasksDeleteBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plans.tasksDeleteDetails">Command `az planner planner-plan-task delete-detail`</a>

##### <a name="Parametersplanner.plans.tasksDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plans.tasksDeleteProgressTaskBoardFormat">Command `az planner planner-plan-task delete-progress-task-board-format`</a>

##### <a name="Parametersplanner.plans.tasksDeleteProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.plans.tasksGetAssignedToTaskBoardFormat">Command `az planner planner-plan-task show-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.plans.tasksGetAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plans.tasksGetBucketTaskBoardFormat">Command `az planner planner-plan-task show-bucket-task-board-format`</a>

##### <a name="Parametersplanner.plans.tasksGetBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plans.tasksGetDetails">Command `az planner planner-plan-task show-detail`</a>

##### <a name="Parametersplanner.plans.tasksGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plans.tasksGetProgressTaskBoardFormat">Command `az planner planner-plan-task show-progress-task-board-format`</a>

##### <a name="Parametersplanner.plans.tasksGetProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.plans.tasksUpdateAssignedToTaskBoardFormat">Command `az planner planner-plan-task update-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.plans.tasksUpdateAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

#### <a name="planner.plans.tasksUpdateBucketTaskBoardFormat">Command `az planner planner-plan-task update-bucket-task-board-format`</a>

##### <a name="Parametersplanner.plans.tasksUpdateBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

#### <a name="planner.plans.tasksUpdateDetails">Command `az planner planner-plan-task update-detail`</a>

##### <a name="Parametersplanner.plans.tasksUpdateDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

#### <a name="planner.plans.tasksUpdateProgressTaskBoardFormat">Command `az planner planner-plan-task update-progress-task-board-format`</a>

##### <a name="Parametersplanner.plans.tasksUpdateProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### group `az planner planner-task`
#### <a name="planner.tasksDeleteAssignedToTaskBoardFormat">Command `az planner planner-task delete-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.tasksDeleteAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.tasksDeleteBucketTaskBoardFormat">Command `az planner planner-task delete-bucket-task-board-format`</a>

##### <a name="Parametersplanner.tasksDeleteBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.tasksDeleteDetails">Command `az planner planner-task delete-detail`</a>

##### <a name="Parametersplanner.tasksDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.tasksDeleteProgressTaskBoardFormat">Command `az planner planner-task delete-progress-task-board-format`</a>

##### <a name="Parametersplanner.tasksDeleteProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="planner.tasksGetAssignedToTaskBoardFormat">Command `az planner planner-task show-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.tasksGetAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.tasksGetBucketTaskBoardFormat">Command `az planner planner-task show-bucket-task-board-format`</a>

##### <a name="Parametersplanner.tasksGetBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.tasksGetDetails">Command `az planner planner-task show-detail`</a>

##### <a name="Parametersplanner.tasksGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.tasksGetProgressTaskBoardFormat">Command `az planner planner-task show-progress-task-board-format`</a>

##### <a name="Parametersplanner.tasksGetProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="planner.tasksUpdateAssignedToTaskBoardFormat">Command `az planner planner-task update-assigned-to-task-board-format`</a>

##### <a name="Parametersplanner.tasksUpdateAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

#### <a name="planner.tasksUpdateBucketTaskBoardFormat">Command `az planner planner-task update-bucket-task-board-format`</a>

##### <a name="Parametersplanner.tasksUpdateBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

#### <a name="planner.tasksUpdateDetails">Command `az planner planner-task update-detail`</a>

##### <a name="Parametersplanner.tasksUpdateDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

#### <a name="planner.tasksUpdateProgressTaskBoardFormat">Command `az planner planner-task update-progress-task-board-format`</a>

##### <a name="Parametersplanner.tasksUpdateProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### group `az planner user`
#### <a name="usersDeletePlanner">Command `az planner user delete-planner`</a>

##### <a name="ParametersusersDeletePlanner">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersGetPlanner">Command `az planner user show-planner`</a>

##### <a name="ParametersusersGetPlanner">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdatePlanner">Command `az planner user update-planner`</a>

##### <a name="ParametersusersUpdatePlanner">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--plans**|array|Read-only. Nullable. Returns the plannerTasks assigned to the user.|plans|plans|
|**--tasks**|array|Read-only. Nullable. Returns the plannerPlans shared with the user.|tasks|tasks|

### group `az planner user-planner`
#### <a name="users.plannerCreatePlans">Command `az planner user-planner create-plan`</a>

##### <a name="Parametersusers.plannerCreatePlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--owner**|string|ID of the Group that owns the plan. A valid group must exist before this field can be set. After it is set, this property can’t be updated.|owner|owner|
|**--title**|string|Required. Title of the plan.|title|title|
|**--buckets**|array|Read-only. Nullable. Collection of buckets in the plan.|buckets|buckets|
|**--tasks**|array|Read-only. Nullable. Collection of tasks in the plan.|tasks|tasks|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="users.plannerCreateTasks">Command `az planner user-planner create-task`</a>

##### <a name="Parametersusers.plannerCreateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="users.plannerDeletePlans">Command `az planner user-planner delete-plan`</a>

##### <a name="Parametersusers.plannerDeletePlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.plannerDeleteTasks">Command `az planner user-planner delete-task`</a>

##### <a name="Parametersusers.plannerDeleteTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.plannerListPlans">Command `az planner user-planner list-plan`</a>

##### <a name="Parametersusers.plannerListPlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.plannerListTasks">Command `az planner user-planner list-task`</a>

##### <a name="Parametersusers.plannerListTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.plannerGetPlans">Command `az planner user-planner show-plan`</a>

##### <a name="Parametersusers.plannerGetPlans">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.plannerGetTasks">Command `az planner user-planner show-task`</a>

##### <a name="Parametersusers.plannerGetTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.plannerUpdatePlans">Command `az planner user-planner update-plan`</a>

##### <a name="Parametersusers.plannerUpdatePlans">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="users.plannerUpdateTasks">Command `az planner user-planner update-task`</a>

##### <a name="Parametersusers.plannerUpdateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az planner user-planner-plan`
#### <a name="users.planner.plansCreateBuckets">Command `az planner user-planner-plan create-bucket`</a>

##### <a name="Parametersusers.planner.plansCreateBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|Name of the bucket.|name|name|
|**--order-hint**|string|Hint used to order items of this type in a list view. The format is defined as outlined here.|order_hint|orderHint|
|**--plan-id**|string|Plan ID to which the bucket belongs.|plan_id|planId|
|**--tasks**|array|Read-only. Nullable. The collection of tasks in the bucket.|tasks|tasks|

#### <a name="users.planner.plansCreateTasks">Command `az planner user-planner-plan create-task`</a>

##### <a name="Parametersusers.planner.plansCreateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="users.planner.plansDeleteBuckets">Command `az planner user-planner-plan delete-bucket`</a>

##### <a name="Parametersusers.planner.plansDeleteBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plansDeleteDetails">Command `az planner user-planner-plan delete-detail`</a>

##### <a name="Parametersusers.planner.plansDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plansDeleteTasks">Command `az planner user-planner-plan delete-task`</a>

##### <a name="Parametersusers.planner.plansDeleteTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plansListBuckets">Command `az planner user-planner-plan list-bucket`</a>

##### <a name="Parametersusers.planner.plansListBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plansListTasks">Command `az planner user-planner-plan list-task`</a>

##### <a name="Parametersusers.planner.plansListTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plansGetBuckets">Command `az planner user-planner-plan show-bucket`</a>

##### <a name="Parametersusers.planner.plansGetBuckets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plansGetDetails">Command `az planner user-planner-plan show-detail`</a>

##### <a name="Parametersusers.planner.plansGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plansGetTasks">Command `az planner user-planner-plan show-task`</a>

##### <a name="Parametersusers.planner.plansGetTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plansUpdateBuckets">Command `az planner user-planner-plan update-bucket`</a>

##### <a name="Parametersusers.planner.plansUpdateBuckets">Parameters</a> 
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

#### <a name="users.planner.plansUpdateDetails">Command `az planner user-planner-plan update-detail`</a>

##### <a name="Parametersusers.planner.plansUpdateDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--id**|string|Read-only.|id|id|
|**--category-descriptions**|object|plannerCategoryDescriptions|category_descriptions|categoryDescriptions|
|**--shared-with**|dictionary|plannerUserIds|shared_with|sharedWith|

#### <a name="users.planner.plansUpdateTasks">Command `az planner user-planner-plan update-task`</a>

##### <a name="Parametersusers.planner.plansUpdateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az planner user-planner-plan-bucket`
#### <a name="users.planner.plans.bucketsCreateTasks">Command `az planner user-planner-plan-bucket create-task`</a>

##### <a name="Parametersusers.planner.plans.bucketsCreateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="users.planner.plans.bucketsDeleteTasks">Command `az planner user-planner-plan-bucket delete-task`</a>

##### <a name="Parametersusers.planner.plans.bucketsDeleteTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plans.bucketsListTasks">Command `az planner user-planner-plan-bucket list-task`</a>

##### <a name="Parametersusers.planner.plans.bucketsListTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plans.bucketsGetTasks">Command `az planner user-planner-plan-bucket show-task`</a>

##### <a name="Parametersusers.planner.plans.bucketsGetTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plans.bucketsUpdateTasks">Command `az planner user-planner-plan-bucket update-task`</a>

##### <a name="Parametersusers.planner.plans.bucketsUpdateTasks">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--microsoft-graph-planner-preview-type**|choice||microsoft_graph_planner_preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|
|**--id1**|string|Read-only.|id1|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az planner user-planner-plan-bucket-task`
#### <a name="users.planner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat">Command `az planner user-planner-plan-bucket-task delete-assigned-to-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksDeleteAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plans.buckets.tasksDeleteBucketTaskBoardFormat">Command `az planner user-planner-plan-bucket-task delete-bucket-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksDeleteBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plans.buckets.tasksDeleteDetails">Command `az planner user-planner-plan-bucket-task delete-detail`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plans.buckets.tasksDeleteProgressTaskBoardFormat">Command `az planner user-planner-plan-bucket-task delete-progress-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksDeleteProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plans.buckets.tasksGetAssignedToTaskBoardFormat">Command `az planner user-planner-plan-bucket-task show-assigned-to-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksGetAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plans.buckets.tasksGetBucketTaskBoardFormat">Command `az planner user-planner-plan-bucket-task show-bucket-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksGetBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plans.buckets.tasksGetDetails">Command `az planner user-planner-plan-bucket-task show-detail`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plans.buckets.tasksGetProgressTaskBoardFormat">Command `az planner user-planner-plan-bucket-task show-progress-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksGetProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat">Command `az planner user-planner-plan-bucket-task update-assigned-to-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksUpdateAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

#### <a name="users.planner.plans.buckets.tasksUpdateBucketTaskBoardFormat">Command `az planner user-planner-plan-bucket-task update-bucket-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksUpdateBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

#### <a name="users.planner.plans.buckets.tasksUpdateDetails">Command `az planner user-planner-plan-bucket-task update-detail`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksUpdateDetails">Parameters</a> 
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

#### <a name="users.planner.plans.buckets.tasksUpdateProgressTaskBoardFormat">Command `az planner user-planner-plan-bucket-task update-progress-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.buckets.tasksUpdateProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-bucket-id**|string|key: id of plannerBucket|planner_bucket_id|plannerBucket-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### group `az planner user-planner-plan-task`
#### <a name="users.planner.plans.tasksDeleteAssignedToTaskBoardFormat">Command `az planner user-planner-plan-task delete-assigned-to-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.tasksDeleteAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plans.tasksDeleteBucketTaskBoardFormat">Command `az planner user-planner-plan-task delete-bucket-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.tasksDeleteBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plans.tasksDeleteDetails">Command `az planner user-planner-plan-task delete-detail`</a>

##### <a name="Parametersusers.planner.plans.tasksDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plans.tasksDeleteProgressTaskBoardFormat">Command `az planner user-planner-plan-task delete-progress-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.tasksDeleteProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.plans.tasksGetAssignedToTaskBoardFormat">Command `az planner user-planner-plan-task show-assigned-to-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.tasksGetAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plans.tasksGetBucketTaskBoardFormat">Command `az planner user-planner-plan-task show-bucket-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.tasksGetBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plans.tasksGetDetails">Command `az planner user-planner-plan-task show-detail`</a>

##### <a name="Parametersusers.planner.plans.tasksGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plans.tasksGetProgressTaskBoardFormat">Command `az planner user-planner-plan-task show-progress-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.tasksGetProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.plans.tasksUpdateAssignedToTaskBoardFormat">Command `az planner user-planner-plan-task update-assigned-to-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.tasksUpdateAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

#### <a name="users.planner.plans.tasksUpdateBucketTaskBoardFormat">Command `az planner user-planner-plan-task update-bucket-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.tasksUpdateBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

#### <a name="users.planner.plans.tasksUpdateDetails">Command `az planner user-planner-plan-task update-detail`</a>

##### <a name="Parametersusers.planner.plans.tasksUpdateDetails">Parameters</a> 
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

#### <a name="users.planner.plans.tasksUpdateProgressTaskBoardFormat">Command `az planner user-planner-plan-task update-progress-task-board-format`</a>

##### <a name="Parametersusers.planner.plans.tasksUpdateProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-plan-id**|string|key: id of plannerPlan|planner_plan_id|plannerPlan-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

### group `az planner user-planner-task`
#### <a name="users.planner.tasksDeleteAssignedToTaskBoardFormat">Command `az planner user-planner-task delete-assigned-to-task-board-format`</a>

##### <a name="Parametersusers.planner.tasksDeleteAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.tasksDeleteBucketTaskBoardFormat">Command `az planner user-planner-task delete-bucket-task-board-format`</a>

##### <a name="Parametersusers.planner.tasksDeleteBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.tasksDeleteDetails">Command `az planner user-planner-task delete-detail`</a>

##### <a name="Parametersusers.planner.tasksDeleteDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.tasksDeleteProgressTaskBoardFormat">Command `az planner user-planner-task delete-progress-task-board-format`</a>

##### <a name="Parametersusers.planner.tasksDeleteProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.planner.tasksGetAssignedToTaskBoardFormat">Command `az planner user-planner-task show-assigned-to-task-board-format`</a>

##### <a name="Parametersusers.planner.tasksGetAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.tasksGetBucketTaskBoardFormat">Command `az planner user-planner-task show-bucket-task-board-format`</a>

##### <a name="Parametersusers.planner.tasksGetBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.tasksGetDetails">Command `az planner user-planner-task show-detail`</a>

##### <a name="Parametersusers.planner.tasksGetDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.tasksGetProgressTaskBoardFormat">Command `az planner user-planner-task show-progress-task-board-format`</a>

##### <a name="Parametersusers.planner.tasksGetProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.planner.tasksUpdateAssignedToTaskBoardFormat">Command `az planner user-planner-task update-assigned-to-task-board-format`</a>

##### <a name="Parametersusers.planner.tasksUpdateAssignedToTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hints-by-assignee**|dictionary|plannerOrderHintsByAssignee|order_hints_by_assignee|orderHintsByAssignee|
|**--unassigned-order-hint**|string|Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.|unassigned_order_hint|unassignedOrderHint|

#### <a name="users.planner.tasksUpdateBucketTaskBoardFormat">Command `az planner user-planner-task update-bucket-task-board-format`</a>

##### <a name="Parametersusers.planner.tasksUpdateBucketTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint used to order tasks in the Bucket view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|

#### <a name="users.planner.tasksUpdateDetails">Command `az planner user-planner-task update-detail`</a>

##### <a name="Parametersusers.planner.tasksUpdateDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--checklist**|dictionary|plannerChecklistItems|checklist|checklist|
|**--description**|string|Description of the task|description|description|
|**--preview-type**|choice||preview_type|previewType|
|**--references**|dictionary|plannerExternalReferences|references|references|

#### <a name="users.planner.tasksUpdateProgressTaskBoardFormat">Command `az planner user-planner-task update-progress-task-board-format`</a>

##### <a name="Parametersusers.planner.tasksUpdateProgressTaskBoardFormat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--planner-task-id**|string|key: id of plannerTask|planner_task_id|plannerTask-id|
|**--id**|string|Read-only.|id|id|
|**--order-hint**|string|Hint value used to order the task on the Progress view of the Task Board. The format is defined as outlined here.|order_hint|orderHint|
