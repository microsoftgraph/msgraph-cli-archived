# Azure CLI Module Creation Report

### education create-assignment

create-assignment a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-assignment|CreateAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--id**|string|Read-only.|id|id|
|**--allow-late-submissions**|boolean||allow_late_submissions|allowLateSubmissions|
|**--allow-students-to-add-resources-to-submission**|boolean||allow_students_to_add_resources_to_submission|allowStudentsToAddResourcesToSubmission|
|**--assign-date-time**|date-time||assign_date_time|assignDateTime|
|**--assigned-date-time**|date-time||assigned_date_time|assignedDateTime|
|**--assign-to**|dictionary|educationAssignmentRecipient|assign_to|assignTo|
|**--class-id**|string||class_id|classId|
|**--close-date-time**|date-time||close_date_time|closeDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--due-date-time**|date-time||due_date_time|dueDateTime|
|**--grading**|dictionary|educationAssignmentGradeType|grading|grading|
|**--instructions**|object|educationItemBody|instructions|instructions|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--status**|choice||status|status|
|**--categories**|array||categories|categories|
|**--resources**|array||resources|resources|
|**--submissions**|array||submissions|submissions|
|**--rubric-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--rubric-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--rubric-description**|object|educationItemBody|description|description|
|**--rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--rubric-grading**|dictionary|educationAssignmentGradeType|microsoft_graph_education_assignment_grade_type_grading|grading|
|**--rubric-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--rubric-levels**|array||levels|levels|
|**--rubric-qualities**|array||qualities|qualities|
|**--rubric-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--rubric-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--rubric-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--rubric-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--rubric-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--rubric-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--rubric-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--rubric-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--rubric-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--rubric-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--rubric-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--rubric-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name11|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id11|id|

### education create-assignment-category

create-assignment-category a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-assignment-category|CreateAssignmentCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### education create-category

create-category a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-category|CreateCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### education create-class

create-class a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-class|CreateClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--class-code**|string|Class code used by the school to identify the class.|class_code|classCode|
|**--course**|object|educationCourse|course|course|
|**--description**|string|Description of the class.|description|description|
|**--display-name**|string|Name of the class.|display_name|displayName|
|**--external-id**|string|ID of the class from the syncing system.|external_id|externalId|
|**--external-name**|string|Name of the class in the syncing system.|external_name|externalName|
|**--external-source**|choice||external_source|externalSource|
|**--external-source-detail**|string||external_source_detail|externalSourceDetail|
|**--grade**|string||grade|grade|
|**--mail-nickname**|string|Mail name for sending email to all members, if this is enabled.|mail_nickname|mailNickname|
|**--term**|object|educationTerm|term|term|
|**--assignment-categories**|array||assignment_categories|assignmentCategories|
|**--assignments**|array||assignments|assignments|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|
|**--members**|array|All users in the class. Nullable.|members|members|
|**--schools**|array|All schools that this class is associated with. Nullable.|schools|schools|
|**--teachers**|array|All teachers in the class. Nullable.|teachers|teachers|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id2|id|

### education create-error

create-error a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-error|CreateErrors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--id**|string|Read-only.|id|id|
|**--entry-type**|string||entry_type|entryType|
|**--error-code**|string||error_code|errorCode|
|**--error-message**|string||error_message|errorMessage|
|**--joining-value**|string||joining_value|joiningValue|
|**--recorded-date-time**|date-time||recorded_date_time|recordedDateTime|
|**--reportable-identifier**|string||reportable_identifier|reportableIdentifier|

### education create-outcome

create-outcome a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-outcome|CreateOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|

### education create-ref-class

create-ref-class a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-class|CreateRefClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education create-ref-member

create-ref-member a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member|CreateRefMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education create-ref-school

create-ref-school a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-school|CreateRefSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education create-ref-taught-class

create-ref-taught-class a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-taught-class|CreateRefTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education create-ref-teacher

create-ref-teacher a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-teacher|CreateRefTeachers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education create-ref-user

create-ref-user a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-user|CreateRefUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education create-resource

create-resource a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-resource|CreateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|

### education create-rubric

create-rubric a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-rubric|CreateRubrics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--display-name**|string||display_name|displayName|
|**--grading**|dictionary|educationAssignmentGradeType|grading|grading|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id5|id|

### education create-school

create-school a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-school|CreateSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Organization description.|description|description|
|**--display-name**|string|Organization display name.|display_name|displayName|
|**--external-source**|choice||external_source|externalSource|
|**--external-source-detail**|string||external_source_detail|externalSourceDetail|
|**--address**|object|physicalAddress|address|address|
|**--external-id**|string|ID of school in syncing system.|external_id|externalId|
|**--external-principal-id**|string|ID of principal in syncing system.|external_principal_id|externalPrincipalId|
|**--fax**|string||fax|fax|
|**--highest-grade**|string|Highest grade taught.|highest_grade|highestGrade|
|**--lowest-grade**|string|Lowest grade taught.|lowest_grade|lowestGrade|
|**--phone**|string|Phone number of school.|phone|phone|
|**--principal-email**|string|Email address of the principal.|principal_email|principalEmail|
|**--principal-name**|string|Name of the principal.|principal_name|principalName|
|**--school-number**|string|School Number.|school_number|schoolNumber|
|**--classes**|array|Classes taught at the school. Nullable.|classes|classes|
|**--users**|array|Users in the school. Nullable.|users|users|
|**--administrative-unit-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--administrative-unit-deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--administrative-unit-description**|string|An optional description for the administrative unit.|microsoft_graph_administrative_unit_description|description|
|**--administrative-unit-display-name**|string|Display name for the administrative unit.|microsoft_graph_administrative_unit_display_name|displayName|
|**--administrative-unit-visibility**|string|Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the adminstrative unit.|visibility|visibility|
|**--administrative-unit-members**|array|Users and groups that are members of this Adminsitrative Unit. HTTP Methods: GET (list members), POST (add members), DELETE (remove members).|members|members|
|**--administrative-unit-scoped-role-members**|array|Scoped-role members of this Administrative Unit.  HTTP Methods: GET (list scopedRoleMemberships), POST (add scopedRoleMembership), DELETE (remove scopedRoleMembership).|scoped_role_members|scopedRoleMembers|
|**--administrative-unit-extensions**|array||extensions|extensions|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id2|id|

### education create-submission

create-submission a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-submission|CreateSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--recipient**|dictionary|educationSubmissionRecipient|recipient|recipient|
|**--released-date-time**|date-time||released_date_time|releasedDateTime|
|**--resources-folder-url**|string||resources_folder_url|resourcesFolderUrl|
|**--returned-date-time**|date-time||returned_date_time|returnedDateTime|
|**--status**|choice||status|status|
|**--submitted-date-time**|date-time||submitted_date_time|submittedDateTime|
|**--unsubmitted-date-time**|date-time||unsubmitted_date_time|unsubmittedDateTime|
|**--outcomes**|array||outcomes|outcomes|
|**--resources**|array||resources|resources|
|**--submitted-resources**|array||submitted_resources|submittedResources|
|**--unsubmitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--unsubmitted-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--unsubmitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--unsubmitted-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--unsubmitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--unsubmitted-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--submitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--submitted-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--submitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--submitted-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--submitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--submitted-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--returned-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--returned-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--returned-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--returned-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--returned-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--returned-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--released-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--released-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--released-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--released-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--released-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--released-by-application-id**|string|Unique identifier for the identity.|id11|id|

### education create-submitted-resource

create-submitted-resource a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-submitted-resource|CreateSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|

### education create-synchronization-profile

create-synchronization-profile a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-synchronization-profile|CreateSynchronizationProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--data-provider**|dictionary|educationSynchronizationDataProvider|data_provider|dataProvider|
|**--display-name**|string||display_name|displayName|
|**--expiration-date**|date||expiration_date|expirationDate|
|**--handle-special-character-constraint**|boolean||handle_special_character_constraint|handleSpecialCharacterConstraint|
|**--identity-synchronization-configuration**|dictionary|educationIdentitySynchronizationConfiguration|identity_synchronization_configuration|identitySynchronizationConfiguration|
|**--licenses-to-assign**|array||licenses_to_assign|licensesToAssign|
|**--state**|choice||state|state|
|**--errors**|array||errors|errors|
|**--profile-status**|object|educationSynchronizationProfileStatus|profile_status|profileStatus|

### education create-user

create-user a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user|CreateUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

### education delete

delete a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteOutcomes|
|delete|DeleteResources|
|delete|DeleteSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

### education delta

delta a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.taughtClasses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|

### education get-administrative-unit

get-administrative-unit a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-administrative-unit|GetAdministrativeUnit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-assignment

get-assignment a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assignment|GetAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-assignment-category

get-assignment-category a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assignment-category|GetAssignmentCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-category

get-category a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-category|GetCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-class

get-class a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-class|GetClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-education-root

get-education-root a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.educationRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-education-root|GetEducationRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-error

get-error a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-error|GetErrors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--education-synchronization-error-id**|string|key: id of educationSynchronizationError|education_synchronization_error_id|educationSynchronizationError-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-group

get-group a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-group|GetGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-me

get-me a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-me|GetMe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-outcome

get-outcome a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-outcome|GetOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-profile-status

get-profile-status a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-profile-status|GetProfileStatus|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-ref-administrative-unit

get-ref-administrative-unit a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-administrative-unit|GetRefAdministrativeUnit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|

### education get-ref-group

get-ref-group a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-group|GetRefGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|

### education get-ref-user

get-ref-user a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-user|GetRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|

### education get-resource

get-resource a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-resource-folder-url

get-resource-folder-url a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource-folder-url|getResourcesFolderUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

### education get-rubric

get-rubric a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-rubric|GetRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-school

get-school a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-school|GetSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-submission

get-submission a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-submission|GetSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-submitted-resource

get-submitted-resource a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-submitted-resource|GetSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-synchronization-profile

get-synchronization-profile a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-synchronization-profile|GetSynchronizationProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education get-user

get-user a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user|GetUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-assignment

list-assignment a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-assignment|ListAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-assignment-category

list-assignment-category a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-assignment-category|ListAssignmentCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-category

list-category a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-category|ListCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-class

list-class a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-class|ListClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-error

list-error a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-error|ListErrors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-member

list-member a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member|ListMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-outcome

list-outcome a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-outcome|ListOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-ref-class

list-ref-class a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-class|ListRefClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education list-ref-member

list-ref-member a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member|ListRefMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education list-ref-school

list-ref-school a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-school|ListRefSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education list-ref-taught-class

list-ref-taught-class a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-taught-class|ListRefTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education list-ref-teacher

list-ref-teacher a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-teacher|ListRefTeachers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education list-ref-user

list-ref-user a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-user|ListRefUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education list-resource

list-resource a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-resource|ListResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-rubric

list-rubric a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-rubric|ListRubrics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-school

list-school a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-school|ListSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-submission

list-submission a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-submission|ListSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-submitted-resource

list-submitted-resource a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-submitted-resource|ListSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-synchronization-profile

list-synchronization-profile a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-synchronization-profile|ListSynchronizationProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-taught-class

list-taught-class a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-taught-class|ListTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-teacher

list-teacher a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-teacher|ListTeachers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education list-user

list-user a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user|ListUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education pause

pause a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|pause|pause|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### education publish

publish a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|publish|publish|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

### education reset

reset a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reset|reset|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### education resume

resume a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|resume|resume|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### education return

return a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|return|return|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

### education set-ref-administrative-unit

set-ref-administrative-unit a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-administrative-unit|SetRefAdministrativeUnit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### education set-ref-group

set-ref-group a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-group|SetRefGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### education set-ref-user

set-ref-user a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-user|SetRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### education start

start a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|start|start|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### education submit

submit a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|submit|submit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

### education unsubmit

unsubmit a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unsubmit|unsubmit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

### education update-assignment

update-assignment a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assignment|UpdateAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--allow-late-submissions**|boolean||allow_late_submissions|allowLateSubmissions|
|**--allow-students-to-add-resources-to-submission**|boolean||allow_students_to_add_resources_to_submission|allowStudentsToAddResourcesToSubmission|
|**--assign-date-time**|date-time||assign_date_time|assignDateTime|
|**--assigned-date-time**|date-time||assigned_date_time|assignedDateTime|
|**--assign-to**|dictionary|educationAssignmentRecipient|assign_to|assignTo|
|**--class-id**|string||class_id|classId|
|**--close-date-time**|date-time||close_date_time|closeDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--due-date-time**|date-time||due_date_time|dueDateTime|
|**--grading**|dictionary|educationAssignmentGradeType|grading|grading|
|**--instructions**|object|educationItemBody|instructions|instructions|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--status**|choice||status|status|
|**--categories**|array||categories|categories|
|**--resources**|array||resources|resources|
|**--submissions**|array||submissions|submissions|
|**--rubric-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--rubric-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--rubric-description**|object|educationItemBody|description|description|
|**--rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--rubric-grading**|dictionary|educationAssignmentGradeType|microsoft_graph_education_assignment_grade_type_grading|grading|
|**--rubric-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--rubric-levels**|array||levels|levels|
|**--rubric-qualities**|array||qualities|qualities|
|**--rubric-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--rubric-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--rubric-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--rubric-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--rubric-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--rubric-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--rubric-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--rubric-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--rubric-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--rubric-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--rubric-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--rubric-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name11|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id11|id|

### education update-assignment-category

update-assignment-category a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assignment-category|UpdateAssignmentCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### education update-category

update-category a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-category|UpdateCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### education update-class

update-class a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-class|UpdateClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--id**|string|Read-only.|id|id|
|**--class-code**|string|Class code used by the school to identify the class.|class_code|classCode|
|**--course**|object|educationCourse|course|course|
|**--description**|string|Description of the class.|description|description|
|**--display-name**|string|Name of the class.|display_name|displayName|
|**--external-id**|string|ID of the class from the syncing system.|external_id|externalId|
|**--external-name**|string|Name of the class in the syncing system.|external_name|externalName|
|**--external-source**|choice||external_source|externalSource|
|**--external-source-detail**|string||external_source_detail|externalSourceDetail|
|**--grade**|string||grade|grade|
|**--mail-nickname**|string|Mail name for sending email to all members, if this is enabled.|mail_nickname|mailNickname|
|**--term**|object|educationTerm|term|term|
|**--assignment-categories**|array||assignment_categories|assignmentCategories|
|**--assignments**|array||assignments|assignments|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|
|**--members**|array|All users in the class. Nullable.|members|members|
|**--schools**|array|All schools that this class is associated with. Nullable.|schools|schools|
|**--teachers**|array|All teachers in the class. Nullable.|teachers|teachers|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id2|id|

### education update-education-root

update-education-root a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.educationRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-education-root|UpdateEducationRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--synchronization-profiles**|array||synchronization_profiles|synchronizationProfiles|
|**--classes**|array|Read-only. Nullable.|classes|classes|
|**--me**|object|educationUser|me|me|
|**--schools**|array|Read-only. Nullable.|schools|schools|
|**--users**|array|Read-only. Nullable.|users|users|

### education update-error

update-error a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-error|UpdateErrors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--education-synchronization-error-id**|string|key: id of educationSynchronizationError|education_synchronization_error_id|educationSynchronizationError-id|
|**--id**|string|Read-only.|id|id|
|**--entry-type**|string||entry_type|entryType|
|**--error-code**|string||error_code|errorCode|
|**--error-message**|string||error_message|errorMessage|
|**--joining-value**|string||joining_value|joiningValue|
|**--recorded-date-time**|date-time||recorded_date_time|recordedDateTime|
|**--reportable-identifier**|string||reportable_identifier|reportableIdentifier|

### education update-me

update-me a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-me|UpdateMe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property values|body|body|

### education update-outcome

update-outcome a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-outcome|UpdateOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|

### education update-profile-status

update-profile-status a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-profile-status|UpdateProfileStatus|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--id**|string|Read-only.|id|id|
|**--last-synchronization-date-time**|date-time||last_synchronization_date_time|lastSynchronizationDateTime|
|**--status**|choice||status|status|

### education update-resource

update-resource a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-resource|UpdateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|

### education update-rubric

update-rubric a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-rubric|UpdateRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--display-name**|string||display_name|displayName|
|**--grading**|dictionary|educationAssignmentGradeType|grading|grading|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id5|id|

### education update-school

update-school a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-school|UpdateSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Organization description.|description|description|
|**--display-name**|string|Organization display name.|display_name|displayName|
|**--external-source**|choice||external_source|externalSource|
|**--external-source-detail**|string||external_source_detail|externalSourceDetail|
|**--address**|object|physicalAddress|address|address|
|**--external-id**|string|ID of school in syncing system.|external_id|externalId|
|**--external-principal-id**|string|ID of principal in syncing system.|external_principal_id|externalPrincipalId|
|**--fax**|string||fax|fax|
|**--highest-grade**|string|Highest grade taught.|highest_grade|highestGrade|
|**--lowest-grade**|string|Lowest grade taught.|lowest_grade|lowestGrade|
|**--phone**|string|Phone number of school.|phone|phone|
|**--principal-email**|string|Email address of the principal.|principal_email|principalEmail|
|**--principal-name**|string|Name of the principal.|principal_name|principalName|
|**--school-number**|string|School Number.|school_number|schoolNumber|
|**--classes**|array|Classes taught at the school. Nullable.|classes|classes|
|**--users**|array|Users in the school. Nullable.|users|users|
|**--administrative-unit-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--administrative-unit-deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--administrative-unit-description**|string|An optional description for the administrative unit.|microsoft_graph_administrative_unit_description|description|
|**--administrative-unit-display-name**|string|Display name for the administrative unit.|microsoft_graph_administrative_unit_display_name|displayName|
|**--administrative-unit-visibility**|string|Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the adminstrative unit.|visibility|visibility|
|**--administrative-unit-members**|array|Users and groups that are members of this Adminsitrative Unit. HTTP Methods: GET (list members), POST (add members), DELETE (remove members).|members|members|
|**--administrative-unit-scoped-role-members**|array|Scoped-role members of this Administrative Unit.  HTTP Methods: GET (list scopedRoleMemberships), POST (add scopedRoleMembership), DELETE (remove scopedRoleMembership).|scoped_role_members|scopedRoleMembers|
|**--administrative-unit-extensions**|array||extensions|extensions|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id2|id|

### education update-submission

update-submission a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-submission|UpdateSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--recipient**|dictionary|educationSubmissionRecipient|recipient|recipient|
|**--released-date-time**|date-time||released_date_time|releasedDateTime|
|**--resources-folder-url**|string||resources_folder_url|resourcesFolderUrl|
|**--returned-date-time**|date-time||returned_date_time|returnedDateTime|
|**--status**|choice||status|status|
|**--submitted-date-time**|date-time||submitted_date_time|submittedDateTime|
|**--unsubmitted-date-time**|date-time||unsubmitted_date_time|unsubmittedDateTime|
|**--outcomes**|array||outcomes|outcomes|
|**--resources**|array||resources|resources|
|**--submitted-resources**|array||submitted_resources|submittedResources|
|**--unsubmitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--unsubmitted-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--unsubmitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--unsubmitted-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--unsubmitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--unsubmitted-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--submitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--submitted-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--submitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--submitted-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--submitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--submitted-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--returned-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--returned-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--returned-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--returned-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--returned-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--returned-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--released-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--released-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--released-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--released-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--released-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--released-by-application-id**|string|Unique identifier for the identity.|id11|id|

### education update-submitted-resource

update-submitted-resource a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-submitted-resource|UpdateSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|

### education update-synchronization-profile

update-synchronization-profile a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-synchronization-profile|UpdateSynchronizationProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--id**|string|Read-only.|id|id|
|**--data-provider**|dictionary|educationSynchronizationDataProvider|data_provider|dataProvider|
|**--display-name**|string||display_name|displayName|
|**--expiration-date**|date||expiration_date|expirationDate|
|**--handle-special-character-constraint**|boolean||handle_special_character_constraint|handleSpecialCharacterConstraint|
|**--identity-synchronization-configuration**|dictionary|educationIdentitySynchronizationConfiguration|identity_synchronization_configuration|identitySynchronizationConfiguration|
|**--licenses-to-assign**|array||licenses_to_assign|licensesToAssign|
|**--state**|choice||state|state|
|**--errors**|array||errors|errors|
|**--profile-status**|object|educationSynchronizationProfileStatus|profile_status|profileStatus|

### education update-user

update-user a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user|UpdateUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|object|New navigation property values|body|body|

### education upload-url

upload-url a education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|upload-url|uploadUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
