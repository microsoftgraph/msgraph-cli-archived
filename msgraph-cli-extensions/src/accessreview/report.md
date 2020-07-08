# Azure CLI Module Creation Report

### accessreview access-review apply-decision

apply-decision a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|apply-decision|applyDecisions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|

### accessreview access-review create-decision

create-decision a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-decision|CreateDecisions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-access-review-decision-access-review-id-access-review-id**|string||microsoft_graph_access_review_decision_access_review_id_access_review_id|accessReviewId|
|**--reviewed-by**|object|userIdentity|reviewed_by|reviewedBy|
|**--reviewed-date-time**|date-time||reviewed_date_time|reviewedDateTime|
|**--review-result**|string||review_result|reviewResult|
|**--justification**|string||justification|justification|
|**--applied-by**|object|userIdentity|applied_by|appliedBy|
|**--applied-date-time**|date-time||applied_date_time|appliedDateTime|
|**--apply-result**|string||apply_result|applyResult|
|**--access-recommendation**|string||access_recommendation|accessRecommendation|

### accessreview access-review create-instance

create-instance a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-instance|CreateInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--status**|string||status|status|
|**--created-by**|object|userIdentity|created_by|createdBy|
|**--business-flow-template-id**|string||business_flow_template_id|businessFlowTemplateId|
|**--reviewer-type**|string||reviewer_type|reviewerType|
|**--description**|string||description|description|
|**--reviewed-entity**|object|identity|reviewed_entity|reviewedEntity|
|**--reviewers**|array||reviewers|reviewers|
|**--decisions**|array||decisions|decisions|
|**--my-decisions**|array||my_decisions|myDecisions|
|**--instances**|array||instances|instances|
|**--settings-mail-notifications-enabled**|boolean||mail_notifications_enabled|mailNotificationsEnabled|
|**--settings-reminders-enabled**|boolean||reminders_enabled|remindersEnabled|
|**--settings-justification-required-on-approval**|boolean||justification_required_on_approval|justificationRequiredOnApproval|
|**--settings-recurrence-settings**|object|accessReviewRecurrenceSettings|recurrence_settings|recurrenceSettings|
|**--settings-auto-review-enabled**|boolean||auto_review_enabled|autoReviewEnabled|
|**--settings-activity-duration-in-days**|integer||activity_duration_in_days|activityDurationInDays|
|**--settings-auto-review-settings**|object|autoReviewSettings|auto_review_settings|autoReviewSettings|
|**--settings-auto-apply-review-results-enabled**|boolean||auto_apply_review_results_enabled|autoApplyReviewResultsEnabled|
|**--settings-access-recommendations-enabled**|boolean||access_recommendations_enabled|accessRecommendationsEnabled|

### accessreview access-review create-my-decision

create-my-decision a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-my-decision|CreateMyDecisions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-access-review-decision-access-review-id-access-review-id**|string||microsoft_graph_access_review_decision_access_review_id_access_review_id|accessReviewId|
|**--reviewed-by**|object|userIdentity|reviewed_by|reviewedBy|
|**--reviewed-date-time**|date-time||reviewed_date_time|reviewedDateTime|
|**--review-result**|string||review_result|reviewResult|
|**--justification**|string||justification|justification|
|**--applied-by**|object|userIdentity|applied_by|appliedBy|
|**--applied-date-time**|date-time||applied_date_time|appliedDateTime|
|**--apply-result**|string||apply_result|applyResult|
|**--access-recommendation**|string||access_recommendation|accessRecommendation|

### accessreview access-review create-reviewer

create-reviewer a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-reviewer|CreateReviewers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### accessreview access-review get-decision

get-decision a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-decision|GetDecisions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--access-review-decision-id**|string|key: accessReviewDecision-id of accessReviewDecision|access_review_decision_id|accessReviewDecision-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review get-instance

get-instance a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-instance|GetInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--access-review-id1**|string|key: accessReview-id of accessReview|access_review_id1|accessReview-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review get-my-decision

get-my-decision a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-my-decision|GetMyDecisions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--access-review-decision-id**|string|key: accessReviewDecision-id of accessReviewDecision|access_review_decision_id|accessReviewDecision-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review get-reviewer

get-reviewer a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-reviewer|GetReviewers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--access-review-reviewer-id**|string|key: accessReviewReviewer-id of accessReviewReviewer|access_review_reviewer_id|accessReviewReviewer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review list-decision

list-decision a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-decision|ListDecisions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review list-instance

list-instance a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-instance|ListInstances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review list-my-decision

list-my-decision a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-my-decision|ListMyDecisions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review list-reviewer

list-reviewer a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-reviewer|ListReviewers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review reset-decision

reset-decision a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reset-decision|resetDecisions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|

### accessreview access-review send-reminder

send-reminder a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send-reminder|sendReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|

### accessreview access-review stop

stop a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|stop|stop|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|

### accessreview access-review update

update a accessreview access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review|accessReviews|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateDecisions|
|update|UpdateInstances|
|update|UpdateMyDecisions|
|update|UpdateReviewers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--access-review-decision-id**|string|key: accessReviewDecision-id of accessReviewDecision|access_review_decision_id|accessReviewDecision-id|
|**--access-review-id1**|string|key: accessReview-id of accessReview|access_review_id1|accessReview-id1|
|**--access-review-reviewer-id**|string|key: accessReviewReviewer-id of accessReviewReviewer|access_review_reviewer_id|accessReviewReviewer-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-access-review-decision-access-review-id-access-review-id**|string||microsoft_graph_access_review_decision_access_review_id_access_review_id|accessReviewId|
|**--reviewed-by**|object|userIdentity|reviewed_by|reviewedBy|
|**--reviewed-date-time**|date-time||reviewed_date_time|reviewedDateTime|
|**--review-result**|string||review_result|reviewResult|
|**--justification**|string||justification|justification|
|**--applied-by**|object|userIdentity|applied_by|appliedBy|
|**--applied-date-time**|date-time||applied_date_time|appliedDateTime|
|**--apply-result**|string||apply_result|applyResult|
|**--access-recommendation**|string||access_recommendation|accessRecommendation|
|**--display-name**|string||display_name|displayName|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--status**|string||status|status|
|**--created-by**|object|userIdentity|created_by|createdBy|
|**--business-flow-template-id**|string||business_flow_template_id|businessFlowTemplateId|
|**--reviewer-type**|string||reviewer_type|reviewerType|
|**--description**|string||description|description|
|**--reviewed-entity**|object|identity|reviewed_entity|reviewedEntity|
|**--reviewers**|array||reviewers|reviewers|
|**--decisions**|array||decisions|decisions|
|**--my-decisions**|array||my_decisions|myDecisions|
|**--instances**|array||instances|instances|
|**--settings-mail-notifications-enabled**|boolean||mail_notifications_enabled|mailNotificationsEnabled|
|**--settings-reminders-enabled**|boolean||reminders_enabled|remindersEnabled|
|**--settings-justification-required-on-approval**|boolean||justification_required_on_approval|justificationRequiredOnApproval|
|**--settings-recurrence-settings**|object|accessReviewRecurrenceSettings|recurrence_settings|recurrenceSettings|
|**--settings-auto-review-enabled**|boolean||auto_review_enabled|autoReviewEnabled|
|**--settings-activity-duration-in-days**|integer||activity_duration_in_days|activityDurationInDays|
|**--settings-auto-review-settings**|object|autoReviewSettings|auto_review_settings|autoReviewSettings|
|**--settings-auto-apply-review-results-enabled**|boolean||auto_apply_review_results_enabled|autoApplyReviewResultsEnabled|
|**--settings-access-recommendations-enabled**|boolean||access_recommendations_enabled|accessRecommendationsEnabled|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### accessreview access-review-access-review create-access-review

create-access-review a accessreview access-review-access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review-access-review|accessReviews.accessReview|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-access-review|CreateAccessReview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--status**|string||status|status|
|**--created-by**|object|userIdentity|created_by|createdBy|
|**--business-flow-template-id**|string||business_flow_template_id|businessFlowTemplateId|
|**--reviewer-type**|string||reviewer_type|reviewerType|
|**--description**|string||description|description|
|**--reviewed-entity**|object|identity|reviewed_entity|reviewedEntity|
|**--reviewers**|array||reviewers|reviewers|
|**--decisions**|array||decisions|decisions|
|**--my-decisions**|array||my_decisions|myDecisions|
|**--instances**|array||instances|instances|
|**--settings-mail-notifications-enabled**|boolean||mail_notifications_enabled|mailNotificationsEnabled|
|**--settings-reminders-enabled**|boolean||reminders_enabled|remindersEnabled|
|**--settings-justification-required-on-approval**|boolean||justification_required_on_approval|justificationRequiredOnApproval|
|**--settings-recurrence-settings**|object|accessReviewRecurrenceSettings|recurrence_settings|recurrenceSettings|
|**--settings-auto-review-enabled**|boolean||auto_review_enabled|autoReviewEnabled|
|**--settings-activity-duration-in-days**|integer||activity_duration_in_days|activityDurationInDays|
|**--settings-auto-review-settings**|object|autoReviewSettings|auto_review_settings|autoReviewSettings|
|**--settings-auto-apply-review-results-enabled**|boolean||auto_apply_review_results_enabled|autoApplyReviewResultsEnabled|
|**--settings-access-recommendations-enabled**|boolean||access_recommendations_enabled|accessRecommendationsEnabled|

### accessreview access-review-access-review delete

delete a accessreview access-review-access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review-access-review|accessReviews.accessReview|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccessReview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--if-match**|string|ETag|if_match|If-Match|

### accessreview access-review-access-review get-access-review

get-access-review a accessreview access-review-access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review-access-review|accessReviews.accessReview|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-access-review|GetAccessReview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review-access-review list-access-review

list-access-review a accessreview access-review-access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review-access-review|accessReviews.accessReview|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-access-review|ListAccessReview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review-access-review update

update a accessreview access-review-access-review.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review-access-review|accessReviews.accessReview|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAccessReview|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-id**|string|key: accessReview-id of accessReview|access_review_id|accessReview-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--status**|string||status|status|
|**--created-by**|object|userIdentity|created_by|createdBy|
|**--business-flow-template-id**|string||business_flow_template_id|businessFlowTemplateId|
|**--reviewer-type**|string||reviewer_type|reviewerType|
|**--description**|string||description|description|
|**--reviewed-entity**|object|identity|reviewed_entity|reviewedEntity|
|**--reviewers**|array||reviewers|reviewers|
|**--decisions**|array||decisions|decisions|
|**--my-decisions**|array||my_decisions|myDecisions|
|**--instances**|array||instances|instances|
|**--settings-mail-notifications-enabled**|boolean||mail_notifications_enabled|mailNotificationsEnabled|
|**--settings-reminders-enabled**|boolean||reminders_enabled|remindersEnabled|
|**--settings-justification-required-on-approval**|boolean||justification_required_on_approval|justificationRequiredOnApproval|
|**--settings-recurrence-settings**|object|accessReviewRecurrenceSettings|recurrence_settings|recurrenceSettings|
|**--settings-auto-review-enabled**|boolean||auto_review_enabled|autoReviewEnabled|
|**--settings-activity-duration-in-days**|integer||activity_duration_in_days|activityDurationInDays|
|**--settings-auto-review-settings**|object|autoReviewSettings|auto_review_settings|autoReviewSettings|
|**--settings-auto-apply-review-results-enabled**|boolean||auto_apply_review_results_enabled|autoApplyReviewResultsEnabled|
|**--settings-access-recommendations-enabled**|boolean||access_recommendations_enabled|accessRecommendationsEnabled|

### accessreview access-review-decision-access-review-decision create-access-review-decision

create-access-review-decision a accessreview access-review-decision-access-review-decision.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review-decision-access-review-decision|accessReviewDecisions.accessReviewDecision|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-access-review-decision|CreateAccessReviewDecision|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--access-review-id**|string||access_review_id|accessReviewId|
|**--reviewed-by**|object|userIdentity|reviewed_by|reviewedBy|
|**--reviewed-date-time**|date-time||reviewed_date_time|reviewedDateTime|
|**--review-result**|string||review_result|reviewResult|
|**--justification**|string||justification|justification|
|**--applied-by**|object|userIdentity|applied_by|appliedBy|
|**--applied-date-time**|date-time||applied_date_time|appliedDateTime|
|**--apply-result**|string||apply_result|applyResult|
|**--access-recommendation**|string||access_recommendation|accessRecommendation|

### accessreview access-review-decision-access-review-decision delete

delete a accessreview access-review-decision-access-review-decision.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review-decision-access-review-decision|accessReviewDecisions.accessReviewDecision|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAccessReviewDecision|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-decision-id**|string|key: accessReviewDecision-id of accessReviewDecision|access_review_decision_id|accessReviewDecision-id|
|**--if-match**|string|ETag|if_match|If-Match|

### accessreview access-review-decision-access-review-decision get-access-review-decision

get-access-review-decision a accessreview access-review-decision-access-review-decision.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review-decision-access-review-decision|accessReviewDecisions.accessReviewDecision|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-access-review-decision|GetAccessReviewDecision|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-decision-id**|string|key: accessReviewDecision-id of accessReviewDecision|access_review_decision_id|accessReviewDecision-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review-decision-access-review-decision list-access-review-decision

list-access-review-decision a accessreview access-review-decision-access-review-decision.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review-decision-access-review-decision|accessReviewDecisions.accessReviewDecision|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-access-review-decision|ListAccessReviewDecision|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview access-review-decision-access-review-decision update

update a accessreview access-review-decision-access-review-decision.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview access-review-decision-access-review-decision|accessReviewDecisions.accessReviewDecision|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAccessReviewDecision|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--access-review-decision-id**|string|key: accessReviewDecision-id of accessReviewDecision|access_review_decision_id|accessReviewDecision-id|
|**--id**|string|Read-only.|id|id|
|**--access-review-id**|string||access_review_id|accessReviewId|
|**--reviewed-by**|object|userIdentity|reviewed_by|reviewedBy|
|**--reviewed-date-time**|date-time||reviewed_date_time|reviewedDateTime|
|**--review-result**|string||review_result|reviewResult|
|**--justification**|string||justification|justification|
|**--applied-by**|object|userIdentity|applied_by|appliedBy|
|**--applied-date-time**|date-time||applied_date_time|appliedDateTime|
|**--apply-result**|string||apply_result|applyResult|
|**--access-recommendation**|string||access_recommendation|accessRecommendation|

### accessreview business-flow-template-business-flow-template create-business-flow-template

create-business-flow-template a accessreview business-flow-template-business-flow-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview business-flow-template-business-flow-template|businessFlowTemplates.businessFlowTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-business-flow-template|CreateBusinessFlowTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### accessreview business-flow-template-business-flow-template delete

delete a accessreview business-flow-template-business-flow-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview business-flow-template-business-flow-template|businessFlowTemplates.businessFlowTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteBusinessFlowTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--business-flow-template-id**|string|key: businessFlowTemplate-id of businessFlowTemplate|business_flow_template_id|businessFlowTemplate-id|
|**--if-match**|string|ETag|if_match|If-Match|

### accessreview business-flow-template-business-flow-template get-business-flow-template

get-business-flow-template a accessreview business-flow-template-business-flow-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview business-flow-template-business-flow-template|businessFlowTemplates.businessFlowTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-business-flow-template|GetBusinessFlowTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--business-flow-template-id**|string|key: businessFlowTemplate-id of businessFlowTemplate|business_flow_template_id|businessFlowTemplate-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview business-flow-template-business-flow-template list-business-flow-template

list-business-flow-template a accessreview business-flow-template-business-flow-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview business-flow-template-business-flow-template|businessFlowTemplates.businessFlowTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-business-flow-template|ListBusinessFlowTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview business-flow-template-business-flow-template update

update a accessreview business-flow-template-business-flow-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview business-flow-template-business-flow-template|businessFlowTemplates.businessFlowTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateBusinessFlowTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--business-flow-template-id**|string|key: businessFlowTemplate-id of businessFlowTemplate|business_flow_template_id|businessFlowTemplate-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### accessreview program create-control

create-control a accessreview program.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program|programs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-control|CreateControls|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-id**|string|key: program-id of program|program_id|program-id|
|**--id**|string|Read-only.|id|id|
|**--control-id**|string||control_id|controlId|
|**--microsoft-graph-program-control-program-id**|string||microsoft_graph_program_control_program_id|programId|
|**--control-type-id**|string||control_type_id|controlTypeId|
|**--display-name**|string||display_name|displayName|
|**--status**|string||status|status|
|**--owner**|object|userIdentity|owner|owner|
|**--resource**|object|programResource|resource|resource|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--program**|object|program|program|program|

### accessreview program get-control

get-control a accessreview program.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program|programs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-control|GetControls|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-id**|string|key: program-id of program|program_id|program-id|
|**--program-control-id**|string|key: programControl-id of programControl|program_control_id|programControl-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview program list-control

list-control a accessreview program.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program|programs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-control|ListControls|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-id**|string|key: program-id of program|program_id|program-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview program update

update a accessreview program.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program|programs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateControls|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-id**|string|key: program-id of program|program_id|program-id|
|**--program-control-id**|string|key: programControl-id of programControl|program_control_id|programControl-id|
|**--id**|string|Read-only.|id|id|
|**--control-id**|string||control_id|controlId|
|**--microsoft-graph-program-control-program-id**|string||microsoft_graph_program_control_program_id|programId|
|**--control-type-id**|string||control_type_id|controlTypeId|
|**--display-name**|string||display_name|displayName|
|**--status**|string||status|status|
|**--owner**|object|userIdentity|owner|owner|
|**--resource**|object|programResource|resource|resource|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--program**|object|program|program|program|

### accessreview program-control get-program

get-program a accessreview program-control.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control|programControls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-program|GetProgram|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-control-id**|string|key: programControl-id of programControl|program_control_id|programControl-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview program-control update

update a accessreview program-control.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control|programControls|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateProgram|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-control-id**|string|key: programControl-id of programControl|program_control_id|programControl-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--description**|string||description|description|
|**--controls**|array||controls|controls|

### accessreview program-control-program-control create-program-control

create-program-control a accessreview program-control-program-control.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control-program-control|programControls.programControl|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-program-control|CreateProgramControl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--control-id**|string||control_id|controlId|
|**--program-id**|string||program_id|programId|
|**--control-type-id**|string||control_type_id|controlTypeId|
|**--display-name**|string||display_name|displayName|
|**--status**|string||status|status|
|**--owner**|object|userIdentity|owner|owner|
|**--resource**|object|programResource|resource|resource|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--program**|object|program|program|program|

### accessreview program-control-program-control delete

delete a accessreview program-control-program-control.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control-program-control|programControls.programControl|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteProgramControl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-control-id**|string|key: programControl-id of programControl|program_control_id|programControl-id|
|**--if-match**|string|ETag|if_match|If-Match|

### accessreview program-control-program-control get-program-control

get-program-control a accessreview program-control-program-control.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control-program-control|programControls.programControl|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-program-control|GetProgramControl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-control-id**|string|key: programControl-id of programControl|program_control_id|programControl-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview program-control-program-control list-program-control

list-program-control a accessreview program-control-program-control.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control-program-control|programControls.programControl|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-program-control|ListProgramControl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview program-control-program-control update

update a accessreview program-control-program-control.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control-program-control|programControls.programControl|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateProgramControl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-control-id**|string|key: programControl-id of programControl|program_control_id|programControl-id|
|**--id**|string|Read-only.|id|id|
|**--control-id**|string||control_id|controlId|
|**--program-id**|string||program_id|programId|
|**--control-type-id**|string||control_type_id|controlTypeId|
|**--display-name**|string||display_name|displayName|
|**--status**|string||status|status|
|**--owner**|object|userIdentity|owner|owner|
|**--resource**|object|programResource|resource|resource|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--program**|object|program|program|program|

### accessreview program-control-type-program-control-type create-program-control-type

create-program-control-type a accessreview program-control-type-program-control-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control-type-program-control-type|programControlTypes.programControlType|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-program-control-type|CreateProgramControlType|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--control-type-group-id**|string||control_type_group_id|controlTypeGroupId|
|**--display-name**|string||display_name|displayName|

### accessreview program-control-type-program-control-type delete

delete a accessreview program-control-type-program-control-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control-type-program-control-type|programControlTypes.programControlType|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteProgramControlType|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-control-type-id**|string|key: programControlType-id of programControlType|program_control_type_id|programControlType-id|
|**--if-match**|string|ETag|if_match|If-Match|

### accessreview program-control-type-program-control-type get-program-control-type

get-program-control-type a accessreview program-control-type-program-control-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control-type-program-control-type|programControlTypes.programControlType|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-program-control-type|GetProgramControlType|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-control-type-id**|string|key: programControlType-id of programControlType|program_control_type_id|programControlType-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview program-control-type-program-control-type list-program-control-type

list-program-control-type a accessreview program-control-type-program-control-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control-type-program-control-type|programControlTypes.programControlType|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-program-control-type|ListProgramControlType|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview program-control-type-program-control-type update

update a accessreview program-control-type-program-control-type.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-control-type-program-control-type|programControlTypes.programControlType|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateProgramControlType|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-control-type-id**|string|key: programControlType-id of programControlType|program_control_type_id|programControlType-id|
|**--id**|string|Read-only.|id|id|
|**--control-type-group-id**|string||control_type_group_id|controlTypeGroupId|
|**--display-name**|string||display_name|displayName|

### accessreview program-program create-program

create-program a accessreview program-program.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-program|programs.program|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-program|CreateProgram|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--description**|string||description|description|
|**--controls**|array||controls|controls|

### accessreview program-program delete

delete a accessreview program-program.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-program|programs.program|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteProgram|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-id**|string|key: program-id of program|program_id|program-id|
|**--if-match**|string|ETag|if_match|If-Match|

### accessreview program-program get-program

get-program a accessreview program-program.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-program|programs.program|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-program|GetProgram|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-id**|string|key: program-id of program|program_id|program-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview program-program list-program

list-program a accessreview program-program.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-program|programs.program|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-program|ListProgram|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### accessreview program-program update

update a accessreview program-program.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|accessreview program-program|programs.program|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateProgram|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--program-id**|string|key: program-id of program|program_id|program-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--description**|string||description|description|
|**--controls**|array||controls|controls|
